
import logging
import os
import argparse

from model.config import Config
import torch
from src.utils import print_and_save_params, get_data
from src.train import run_train
from src.predict import run_test as run_plain_test
from src.predict_hybrid_bias import run_test as run_hybrid_test
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.ERROR)  # Only show errors, not warnings


def main():
    parser = argparse.ArgumentParser()

    # Required
    parser.add_argument("--model", required=True,
                        help="Model identifier, e.g. 'bert-lstm-crf', 'deberta-crf', or 'deberta-lstm-crf'.")
    parser.add_argument("--data_path", required=True, default="./data/")
    parser.add_argument("--save_dir", required=True, default="./save_models/")
    parser.add_argument("--word_embedding_model_path", required=True)  # e.g., "/home/.../bert-base-cased"
    parser.add_argument("--label_type", choices=["BIO", "BIOES"], default="BIO",
                        help="Tagging scheme to use for labels and metrics.")
    parser.add_argument("--trust_remote_code", action="store_true",
                        help="Pass to HuggingFace loaders when using custom community checkpoints.")

    # Training settings
    parser.add_argument("--num_epochs", type=int, default=10)
    parser.add_argument("--batch_size", type=int, default=16)

    parser.add_argument("--learning_rate", type=float, default=5e-5)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--use_scheduler", type=bool, default=True)


    # IDCNN hyperparams
    parser.add_argument("--num_filters", type=int, default=64)
    parser.add_argument("--cnn_dropout", type=float, default=0.4)
    parser.add_argument("--kernel_size", type=int, default=3)
    parser.add_argument("--num_block", type=int, default=4)

    # LSTM hyperparams
    parser.add_argument("--hidden_dim", type=int, default=768)
    parser.add_argument("--rnn_layers", type=int, default=1)
    parser.add_argument("--rnn_dropout", type=float, default=0.1)
    parser.add_argument("--proj_dropout", type=float, default=0.4)

    parser.add_argument("--max_length", type=int, default=400)

    # Labels handling
    parser.add_argument("--include_special_labels", action="store_true", default=True)


    parser.add_argument("--do_train",
                        action='store_true',
                        help="Whether to run training.")

    parser.add_argument("--do_test",
                        action='store_true',
                        help="Whether to run eval on the test set.")
    parser.add_argument(
        "--prediction_strategy",
        choices=["plain", "rule_bias"],
        default="plain",
        help="Test with ordinary CRF decoding or rule-biased decoding plus post-rules.",
    )
    parser.add_argument(
        "--rule_bias_alpha",
        type=float,
        default=3.0,
        help="Positive emission bias used when --prediction_strategy rule_bias.",
    )
    parser.add_argument(
        "--no_rule_postprocess",
        action="store_true",
        help="With rule_bias, use emission bias without deterministic post-rules.",
    )


    args = parser.parse_args()

    cfg = Config(args)
    cfg.rule_bias_alpha = args.rule_bias_alpha
    cfg.apply_rule_postprocess = not args.no_rule_postprocess

    # Preserve the metadata associated with an existing checkpoint during
    # test-only runs. Training runs create/update the parameter record.
    if args.do_train:
        print_and_save_params(cfg, args.save_dir)

    model = cfg.build_model()


    # will be making changes
    train_dataloader, dev_dataloader, test_dataloader, dev_features, test_features = get_data(cfg)

    # Train
    if args.do_train:
        run_train(model, cfg, train_dataloader, dev_dataloader, dev_features)  #to call run_train in train.py

    # # Test
    if args.do_test:

        logger.info('do testing ...')


        best_model_path = cfg.save_path + '_best_f1.pth'
        last_model_path = cfg.save_path + '_last_model.pth'

        # Check if best_f1.pth exists, otherwise load last_model.pth
        if os.path.isfile(best_model_path):
            print   (f"Loading best model from {best_model_path}")
            logger.info(f"Loading best model from {best_model_path}")
            model.load_state_dict(torch.load(best_model_path, map_location=cfg.device, weights_only=True))
        elif os.path.isfile(last_model_path):
            print  (f"Loading last model from {last_model_path}")
            logger.info(f"Loading last model from {last_model_path}")
            model.load_state_dict(torch.load(last_model_path, map_location=cfg.device, weights_only=True))
        else:
            raise FileNotFoundError(f"Neither {best_model_path} nor {last_model_path} exists.")

        # 模型训练
        test_runner = run_hybrid_test if args.prediction_strategy == "rule_bias" else run_plain_test
        metrics_df = test_runner(
            model,
            cfg,
            test_dataloader,
            test_features=test_features,
        )
        print(metrics_df)
        # Save where you like (your snippet used config.trained_model_path; if not set, use cfg.save_dir)

        logger.info('------------------test result------------------')
        logger.info(metrics_df)

        strategy_suffix = (
            f"_hybrid_rule_bias_alpha{format(args.rule_bias_alpha, 'g').replace('.', 'p')}"
            if args.prediction_strategy == "rule_bias"
            else "_plain"
        )
        metrics_df.to_csv(
            cfg.save_path + strategy_suffix + '_test_result.csv',
            index=False,
        )



if __name__ == "__main__":

    #  python main.py --model bert-lstm-crf  --data_path ./data/ --save_dir ./save_model --word_embedding_model_path /home/mh1f25/scratch/llms_model/bert-base-cased  --do_train --do_test  --num_epochs 3
    #  python main.py --model deberta-crf  --data_path ./data/ --save_dir ./save_model --word_embedding_model_path /home/mh1f25/scratch/llms_model/deberta-base  --do_train --do_test  --num_epochs 3

    # nohup python main.py --model bert-lstm-crf  --data_path ./data/ --save_dir ./save_model --word_embedding_model_path /home/mh1f25/scratch/llms_model/bert-base-cased  --do_train --do_test  --num_epochs 3  > main.log  2>&1 &

    # Test the trained Contract-BERT checkpoint with rule-biased decoding and post-rules:
    # python main.py --model contract-bert-lstm-crf --data_path ./data/ --save_dir ./save_model --word_embedding_model_path /home/mh1f25/scratch/llms_model/bert-base-uncased-contracts --num_epochs 20 --batch_size 16 --max_length 400 --learning_rate 5e-5 --label_type BIO --rnn_layers 1 --device cpu --do_test --prediction_strategy rule_bias --rule_bias_alpha 3.0


    main()

# one model:
# BERT + LSTM + CRF
# BERT is used to embeddings each token
# LSTM + CRF sequence labeling

# Could be adding rule-based model, create a ACTREE to identify ODRL Entity

 # For English NER, transformer encoders fine‑tuned on tagging datasets tend to dominate. In practice I’d shortlist:
 #
 #  - deberta-v3-large or deberta-v3-base: strong contextual representations, great out of the box for NER with modest compute.
 #  - roberta-large or bert-large-cased: still very competitive, tons of community recipes and checkpoints.
 #  - xlm-roberta-large: multilingual if you need cross-language coverage.
 #  - modernBERT-base (or “Longformer”-style models) when sentences get very long; they handle context that vanilla BERT truncates.
 #  - Instruction-tuned encoder-decoders (FLAN-T5 large/xxl) can be repurposed, but they’re heavier. Decoder-only LLMs (Llama/Mistral) work via the new wrapper, yet they usually need more finetuning
 #    effort to match the dedicated encoders.
 #
