#!/bin/bash
#SBATCH --mail-user=miao.hu@soton.ac.uk
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mem=80G
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --partition=a100
#SBATCH --gres=gpu:1
#SBATCH --time=60:00:00
#SBATCH --job-name=odrl_ner_train
#SBATCH --output=./result_out/main_odrl_ner_train-%j.out

set -euo pipefail

# Avoid inherited cluster locale warnings and tokenizer/fork warnings.
unset LC_ALL
export LANG=C.UTF-8
export TOKENIZERS_PARALLELISM=false

PROJECT_DIR="${SLURM_SUBMIT_DIR:-$(pwd)}"
VENV_PATH="${VENV_PATH:-/home/mh1f25/.conda/envs/odrl_extraction}"

# =============================================================================
# MODEL SELECTION
# =============================================================================
# Default profile. Change only this value, or override it without editing:
#   sbatch --export=ALL,MODEL_PROFILE=deberta-v3-large gpu_run_funetuning.sh
#
# Supported values:
#   modernbert-large   ModernBERT-large + CRF
#   deberta-v3-large   DeBERTa-v3-large + CRF
#   deberta-v3-large-lstm
#                      DeBERTa-v3-large + BiLSTM + CRF
#   bert               Contract BERT-base + CRF
MODEL_PROFILE="${MODEL_PROFILE:-modernbert-large}"

# Shared dataset/training settings. Every value can also be overridden through
# `sbatch --export=ALL,NAME=value,...`.
DATA_PATH="${DATA_PATH:-./data/}"
TRAIN_FILE="${TRAIN_FILE:-train_correct_with_agent_gpt-5.6-luna_flat.txt}"
VALID_FILE="${VALID_FILE:-valid_correct_with_agent_gpt-5.6-luna_flat.txt}"
TEST_FILE="${TEST_FILE:-test_correct_with_agent_gpt-5.6-luna_flat.txt}"
DATA_TAG="${DATA_TAG:-correct_data_with_agent_gpt-5.6-luna-v2}"
SAVE_DIR="${SAVE_DIR:-./save_model}"
NUM_EPOCHS="${NUM_EPOCHS:-20}"
METRICS_TYPE="${METRICS_TYPE:-entity}"
PROJ_DROPOUT="${PROJ_DROPOUT:-0.1}"

# Each profile defines only the settings that differ by encoder.
case "$MODEL_PROFILE" in
    modernbert-large)
        MODEL_NAME="modernbert-large-crf"
        DEFAULT_MODEL_PATH="/iridisfs/scratch/mh1f25/llms_model/ModernBERT-large"
        DEFAULT_BATCH_SIZE=8
        DEFAULT_MAX_LENGTH=400
        DEFAULT_LEARNING_RATE=2e-5
        DEFAULT_LABEL_TYPE=BIO
        DEFAULT_AMP_DTYPE=float32
        DEFAULT_USING_LSTM=0
        ;;
    deberta-v3-large)
        MODEL_NAME="deberta-v3-large-crf"
        DEFAULT_MODEL_PATH="/iridisfs/scratch/mh1f25/llms_model/deberta-v3-large"
        DEFAULT_BATCH_SIZE=8
        DEFAULT_MAX_LENGTH=400
        DEFAULT_LEARNING_RATE=2e-5
        DEFAULT_LABEL_TYPE=BIO
        DEFAULT_AMP_DTYPE=auto
        DEFAULT_USING_LSTM=0
        ;;
    deberta-v3-large-lstm)
        MODEL_NAME="deberta-v3-large-lstm-crf"
        DEFAULT_MODEL_PATH="/iridisfs/scratch/mh1f25/llms_model/deberta-v3-large"
        DEFAULT_BATCH_SIZE=8
        DEFAULT_MAX_LENGTH=512
        DEFAULT_LEARNING_RATE=2e-5
        DEFAULT_LABEL_TYPE=BIOES
        DEFAULT_AMP_DTYPE=auto
        DEFAULT_USING_LSTM=1
        ;;
    bert)
        MODEL_NAME="contract-bert-crf"
        DEFAULT_MODEL_PATH="/iridisfs/scratch/mh1f25/llms_model/bert-base-uncased-contracts"
        DEFAULT_BATCH_SIZE=16
        DEFAULT_MAX_LENGTH=400
        DEFAULT_LEARNING_RATE=5e-5
        DEFAULT_LABEL_TYPE=BIO
        DEFAULT_AMP_DTYPE=auto
        DEFAULT_USING_LSTM=0
        ;;
    *)
        echo "ERROR: unsupported MODEL_PROFILE='$MODEL_PROFILE'." >&2
        echo "Choose: modernbert-large, deberta-v3-large, deberta-v3-large-lstm, or bert." >&2
        exit 2
        ;;
esac

# Optional per-run overrides, applied after the selected profile.
MODEL_PATH="${MODEL_PATH:-$DEFAULT_MODEL_PATH}"
BATCH_SIZE="${BATCH_SIZE:-$DEFAULT_BATCH_SIZE}"
MAX_LENGTH="${MAX_LENGTH:-$DEFAULT_MAX_LENGTH}"
LEARNING_RATE="${LEARNING_RATE:-$DEFAULT_LEARNING_RATE}"
LABEL_TYPE="${LABEL_TYPE:-$DEFAULT_LABEL_TYPE}"
AMP_DTYPE="${AMP_DTYPE:-$DEFAULT_AMP_DTYPE}"
USING_LSTM="${USING_LSTM:-$DEFAULT_USING_LSTM}"
HIDDEN_DIM="${HIDDEN_DIM:-768}"
RNN_LAYERS="${RNN_LAYERS:-1}"
RNN_DROPOUT="${RNN_DROPOUT:-0.1}"

MODEL_EXTRA_ARGS=()
if [[ "$USING_LSTM" == "1" ]]; then
    MODEL_EXTRA_ARGS+=(
        --using-lstm
        --hidden_dim "$HIDDEN_DIM"
        --rnn_layers "$RNN_LAYERS"
        --rnn_dropout "$RNN_DROPOUT"
    )
elif [[ "$USING_LSTM" != "0" ]]; then
    echo "ERROR: USING_LSTM must be 0 or 1; received '$USING_LSTM'." >&2
    exit 2
fi

# ModernBERT uses the conservative eager backend unless explicitly overridden.
export ODRL_MODERNBERT_ATTN_IMPLEMENTATION="${ODRL_MODERNBERT_ATTN_IMPLEMENTATION:-eager}"

cd "$PROJECT_DIR"

if [[ -f "$VENV_PATH/conda-meta/history" ]]; then
    CONDA_SH="/iridisfs/ixsoftware/conda/miniconda-py3/etc/profile.d/conda.sh"
    if [[ ! -f "$CONDA_SH" ]]; then
        echo "ERROR: Conda initialization script not found: $CONDA_SH" >&2
        exit 1
    fi
    # shellcheck disable=SC1090
    source "$CONDA_SH"
    conda activate "$VENV_PATH"
elif [[ -f "$VENV_PATH/bin/activate" ]]; then
    # shellcheck disable=SC1090
    source "$VENV_PATH/bin/activate"
else
    echo "ERROR: no Conda or Python virtual environment found at: $VENV_PATH" >&2
    echo "Create it first, or submit with VENV_PATH=/path/to/environment." >&2
    exit 1
fi

PYTHON_BIN="$VENV_PATH/bin/python"
ACTIVE_PYTHON="$(command -v python || true)"
if [[ ! -x "$PYTHON_BIN" ]]; then
    echo "ERROR: virtual-environment Python is not executable on $(hostname): $PYTHON_BIN" >&2
    echo "The environment may contain a broken Python symlink." >&2
    echo "On Iridis, use a Conda environment that is accessible from A100 compute nodes." >&2
    exit 1
fi

if [[ "$ACTIVE_PYTHON" != "$PYTHON_BIN" ]]; then
    echo "ERROR: activating $VENV_PATH selected the wrong Python interpreter." >&2
    echo "Expected: $PYTHON_BIN" >&2
    echo "Actual:   ${ACTIVE_PYTHON:-not found}" >&2
    echo "The virtual environment was probably moved or copied after it was created." >&2
    echo "Recreate .venv at its current project path." >&2
    exit 1
fi

if [[ ! -d "$MODEL_PATH" ]]; then
    echo "ERROR: model directory not found: $MODEL_PATH" >&2
    echo "Copy/download it first, or submit with MODEL_PATH=/path/to/model." >&2
    exit 1
fi

for DATA_FILE in \
    "$DATA_PATH/$TRAIN_FILE" \
    "$DATA_PATH/$VALID_FILE" \
    "$DATA_PATH/$TEST_FILE"
do
    if [[ ! -f "$DATA_FILE" ]]; then
        echo "ERROR: dataset file not found: $DATA_FILE" >&2
        exit 1
    fi
done

mkdir -p "$SAVE_DIR"

echo "Job started: $(date --iso-8601=seconds)"
echo "Host: $(hostname)"
echo "Project: $PROJECT_DIR"
echo "Environment: ${CONDA_PREFIX:-${VIRTUAL_ENV:-$VENV_PATH}}"
echo "Python: $PYTHON_BIN"
echo "Model profile: $MODEL_PROFILE"
echo "Model name: $MODEL_NAME"
echo "Model path: $MODEL_PATH"
echo "Dataset: $DATA_PATH ($TRAIN_FILE, $VALID_FILE, $TEST_FILE)"
echo "Settings: epochs=$NUM_EPOCHS batch_size=$BATCH_SIZE max_length=$MAX_LENGTH learning_rate=$LEARNING_RATE label_type=$LABEL_TYPE amp_dtype=$AMP_DTYPE metrics_type=$METRICS_TYPE using_lstm=$USING_LSTM hidden_dim=$HIDDEN_DIM rnn_layers=$RNN_LAYERS"

nvidia-smi

"$PYTHON_BIN" -c 'import torch, transformers; print(f"torch={torch.__version__}"); print(f"transformers={transformers.__version__}"); print(f"cuda_available={torch.cuda.is_available()}"); print(f"cuda_runtime={torch.version.cuda}"); assert torch.cuda.is_available(), "PyTorch cannot access the allocated GPU"'

"$PYTHON_BIN" -u main.py \
    --model "$MODEL_NAME" \
    --data_path "$DATA_PATH" \
    --train_file "$TRAIN_FILE" \
    --valid_file "$VALID_FILE" \
    --test_file "$TEST_FILE" \
    --data_tag "$DATA_TAG" \
    --save_dir "$SAVE_DIR" \
    --word_embedding_model_path "$MODEL_PATH" \
    --num_epochs "$NUM_EPOCHS" \
    --batch_size "$BATCH_SIZE" \
    --max_length "$MAX_LENGTH" \
    --learning_rate "$LEARNING_RATE" \
    --label_type "$LABEL_TYPE" \
    --metrics_type "$METRICS_TYPE" \
    --amp_dtype "$AMP_DTYPE" \
    --proj_dropout "$PROJ_DROPOUT" \
    --device cuda \
    "${MODEL_EXTRA_ARGS[@]}" \
    --do_train \
    --do_test

echo "Job finished: $(date --iso-8601=seconds)"




#  - modernbert-large
  #  - deberta-v3-large
  #  - bert — contract BERT + CRF
  #
  #  There is now one shared training command. You do not need to comment/uncomment model
  #  blocks.
  #
  #  Run DeBERTa:
  #
#    sbatch \
#      --export=ALL,MODEL_PROFILE=deberta-v3-large,NUM_EPOCHS=30,LABEL_TYPE=BIOES \
#      --job-name=odrl_deberta \
#      --output=result_out/main_deberta_ltBIOSE_epoch30_-%j.out \
#      gpu_run_funetuning.sh
  #
  #  Run DeBERTa + BiLSTM + CRF:
  #
#    sbatch \
#      --export=ALL,MODEL_PROFILE=deberta-v3-large-lstm,NUM_EPOCHS=30 \
#      --job-name=odrl_deberta_lstm \
#      --output=result_out/main_deberta_lstm_ltBIOES_epoch30-%j.out \
#      gpu_run_funetuning.sh
  #
  #  Run ModernBERT:
  #
#    sbatch \
#      --export=ALL,MODEL_PROFILE=modernbert-large \
#      --job-name=odrl_modernbert \
#      --output=result_out/main_modernbert-%j.out \
#      gpu_run_funetuning.sh
  #
  #  Run contract BERT:
  #
  #  sbatch \
  #    --export=ALL,MODEL_PROFILE=bert \
  #    --job-name=odrl_bert \
  #    --output=result_out/main_bert-%j.out \
  #    gpu_run_funetuning.sh
  #
  #  Running without a profile uses ModernBERT:
  #
  #  sbatch gpu_run_funetuning.sh
  #
  #  Each profile sets its own model path, model identifier, batch size, maximum length,
  #  learning rate, label type, architecture, and AMP precision.
  #
  #  You can override individual settings:
  #
  #  sbatch \
  #    --export=ALL,MODEL_PROFILE=deberta-v3-
  #    large,BATCH_SIZE=16,MAX_LENGTH=512,LEARNING_RATE=1e-5 \
  #    gpu_run_funetuning.sh
  #
  #  The script passes Bash syntax validation.
