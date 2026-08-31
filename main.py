
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
                        help="Checkpoint/model identifier, e.g. 'contract-bert-crf' or 'deberta-v3-crf'.")
    parser.add_argument("--data_path", required=True, default="./data/")
    parser.add_argument("--save_dir", required=True, default="./save_models/")
    parser.add_argument("--word_embedding_model_path", required=True)  # e.g., "/home/.../bert-base-cased"
    parser.add_argument(
        "--train_file", "--train_path", dest="train_path",
        help="Training JSONL filename under --data_path, or an explicit path.",
    )
    parser.add_argument(
        "--valid_file", "--dev_path", dest="dev_path",
        help="Validation JSONL filename under --data_path, or an explicit path.",
    )
    parser.add_argument(
        "--test_file", "--test_path", dest="test_path",
        help="Test JSONL filename under --data_path, or an explicit path.",
    )
    parser.add_argument(
        "--data_tag",
        default="",
        help=(
            "Dataset provenance tag appended to checkpoint/result filenames, "
            "for example correct_data_with_agent_gpt-5.6-luna."
        ),
    )
    parser.add_argument("--label_type", choices=["BIO", "BIOES"], default="BIO",
                        help="Tagging scheme to use for labels and metrics.")
    parser.add_argument(
        "--metrics_type", "--metrics-type",
        choices=["entity", "token"],
        default="entity",
        help="Metric used for validation checkpoint selection and overall test results.",
    )
    parser.add_argument("--trust_remote_code", action="store_true",
                        help="Pass to HuggingFace loaders when using custom community checkpoints.")

    # Training settings
    parser.add_argument("--num_epochs", type=int, default=10)
    parser.add_argument("--batch_size", type=int, default=16)

    parser.add_argument("--learning_rate", type=float, default=5e-5)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--use_scheduler", type=bool, default=True)
    parser.add_argument(
        "--amp_dtype", "--amp-dtype",
        choices=["auto", "float16", "bfloat16", "float32"],
        default="auto",
        help=(
            "CUDA training precision. 'auto' uses BF16 for ModernBERT and FP16 "
            "for other encoders; float32 disables AMP."
        ),
    )


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
    parser.add_argument(
        "--using-lstm", "--using_lstm",
        dest="using_lstm",
        action="store_true",
        help="Insert a BiLSTM between the pretrained encoder and CRF. Omit for encoder + CRF.",
    )

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
    print(f"Training data:   {cfg.train_path}")
    print(f"Validation data: {cfg.dev_path}")
    print(f"Test data:       {cfg.test_path}")
    print(f"Checkpoint prefix: {cfg.save_path}")

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


    main()

#     train:
# nohup python -u main.py  \
#   --model contract-bert-lstm-crf  \
#   --data_path ./data/   \
#   --train_file train_correct_with_agent_gpt-5.6-luna.txt  \
#   --valid_file valid_correct_with_agent_gpt-5.6-luna.txt   \
#   --test_file test_correct_with_agent_gpt-5.6-luna.txt  \
#   --data_tag correct_data_with_agent_gpt-5.6-luna-v2  \
#   --save_dir ./save_model  \
#   --word_embedding_model_path /home/mh1f25/scratch/llms_model/bert-base-uncased-contracts  \
#   --num_epochs 20  \
#   --batch_size 16  \
#   --max_length 400 \
#   --learning_rate 5e-5  \
#   --label_type BIO  \
#   --rnn_layers 1  \
#   --device cuda  \
#   --do_train \
#   --do_test > main_contract_bert_epoches20_rnnlays1_mq400_adv_BIO_bs16_with_correct_datasetgpt5.6-v2.log 2>&1 &



# using legal-bert-base-uncased


# nohup python -u main.py  \
#   --model legal-bert-base-uncased-lstm-crf  \
#   --data_path ./data/   \
#   --train_file train_correct_with_agent_gpt-5.6-luna.txt  \
#   --valid_file valid_correct_with_agent_gpt-5.6-luna.txt   \
#   --test_file test_correct_with_agent_gpt-5.6-luna.txt  \
#   --data_tag correct_data_with_agent_gpt-5.6-luna  \
#   --save_dir ./save_model  \
#   --word_embedding_model_path /home/mh1f25/scratch/llms_model/legal-bert-base-uncased  \
#   --num_epochs 20  \
#   --batch_size 16  \
#   --max_length 400 \
#   --learning_rate 5e-5  \
#   --label_type BIO  \
#   --rnn_layers 1  \
#   --device cuda  \
#   --do_train \
#   --do_test > main_legal-bert-base-uncased_epoches20_rnnlays1_mq400_adv_BIO_bs16_with_correct_datasetgpt5.6.log 2>&1 &
#






# ### Run the tagged model API
#
# nohup .venv/bin/python -u app_rule_bias.py \
#     --model contract-bert-lstm-crf \
#     --data_path ./data/ \
#     --save_dir ./save_model \
#     --word_embedding_model_path /home/mh1f25/scratch/llms_model/bert-base-uncased-contracts \
#     --num_epochs 20 \
#     --batch_size 16 \
#     --max_length 400 \
#     --learning_rate 5e-5 \
#     --label_type BIO \
#     --rnn_layers 1 \
#     --rule_bias_alpha 3.0 \
#     --correct_data_model correct_data_with_agent_gpt-5.6-luna-v2 \
#     --device cpu \
#     --host 0.0.0.0 \
#     --port 5002 \
#     > fastapi_rule_bias_correct_data_gpt-5.6-luna-v2.log 2>&1 &



# new dataset:
# nohup python -u main.py \
# --model contract-bert-lstm-crf \
# --data_path ./data/ \
# --train_file train_correct_with_agent_gpt-5.6-luna_flat.txt \
# --valid_file valid_correct_with_agent_gpt-5.6-luna_flat.txt \
# --test_file test_correct_with_agent_gpt-5.6-luna_flat.txt \
# --data_tag correct_data_with_agent_gpt-5.6-luna-v2 \
# --save_dir ./save_model \
# --word_embedding_model_path /home/mh1f25/scratch/llms_model/bert-base-uncased-contracts \
# --num_epochs 20 \
# --batch_size 16 \
# --max_length 400 \
# --learning_rate 5e-5 \
# --label_type BIO \
# --rnn_layers 1 \
# --device cuda \
# --do_train \
# --do_test \
# > main_contract_bert_correct_data_with_agent_gpt-5.6-luna-v2.log 2>&1 &
#
# echo $! > main_contract_bert_correct_data_with_agent_gpt-5.6-luna-v2.pid


