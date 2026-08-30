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
#SBATCH --job-name=odrl_roberta_large
#SBATCH --output=./result_out/main_roberta-large_crf_correct_data_gpt-5.6-luna-v2-%j.out

set -euo pipefail

PROJECT_DIR="${SLURM_SUBMIT_DIR:-$(pwd)}"
VENV_PATH="${VENV_PATH:-/home/mh1f25/.conda/envs/odrl_extraction}"
MODEL_PATH="${ROBERTA_MODEL_PATH:-/iridisfs/scratch/mh1f25/llms_model/roberta-large}"

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
    echo "ERROR: RoBERTa model directory not found: $MODEL_PATH" >&2
    echo "Copy/download it first, or submit with ROBERTA_MODEL_PATH=/path/to/model." >&2
    exit 1
fi

for DATA_FILE in \
    data/train_correct_with_agent_gpt-5.6-luna_flat.txt \
    data/valid_correct_with_agent_gpt-5.6-luna_flat.txt \
    data/test_correct_with_agent_gpt-5.6-luna_flat.txt
do
    if [[ ! -f "$DATA_FILE" ]]; then
        echo "ERROR: dataset file not found: $DATA_FILE" >&2
        exit 1
    fi
done

mkdir -p save_model

echo "Job started: $(date --iso-8601=seconds)"
echo "Host: $(hostname)"
echo "Project: $PROJECT_DIR"
echo "Environment: ${CONDA_PREFIX:-${VIRTUAL_ENV:-$VENV_PATH}}"
echo "Python: $PYTHON_BIN"
echo "Model: $MODEL_PATH"

nvidia-smi

"$PYTHON_BIN" -c 'import torch, transformers; print(f"torch={torch.__version__}"); print(f"transformers={transformers.__version__}"); print(f"cuda_available={torch.cuda.is_available()}"); print(f"cuda_runtime={torch.version.cuda}"); assert torch.cuda.is_available(), "PyTorch cannot access the allocated GPU"'

# Previous DeBERTa-v3-large + CRF experiment:
# "$PYTHON_BIN" -u main.py \
#     --model deberta-v3-large-crf \
#     --data_path ./data/ \
#     --train_file train_correct_with_agent_gpt-5.6-luna_flat.txt \
#     --valid_file valid_correct_with_agent_gpt-5.6-luna_flat.txt \
#     --test_file test_correct_with_agent_gpt-5.6-luna_flat.txt \
#     --data_tag correct_data_with_agent_gpt-5.6-luna-v2 \
#     --save_dir ./save_model \
#     --word_embedding_model_path /iridisfs/scratch/mh1f25/llms_model/deberta-v3-large \
#     --num_epochs 20 \
#     --batch_size 8 \
#     --max_length 512 \
#     --learning_rate 2e-5 \
#     --label_type BIOES \
#     --metrics_type entity \
#     --proj_dropout 0.1 \
#     --device cuda \
#     --do_train \
#     --do_test

"$PYTHON_BIN" -u main.py \
    --model roberta-large-crf \
    --data_path ./data/ \
    --train_file train_correct_with_agent_gpt-5.6-luna_flat.txt \
    --valid_file valid_correct_with_agent_gpt-5.6-luna_flat.txt \
    --test_file test_correct_with_agent_gpt-5.6-luna_flat.txt \
    --data_tag correct_data_with_agent_gpt-5.6-luna-v2 \
    --save_dir ./save_model \
    --word_embedding_model_path "$MODEL_PATH" \
    --num_epochs 20 \
    --batch_size 8 \
    --max_length 400 \
    --learning_rate 2e-5 \
    --label_type BIO \
    --metrics_type entity \
    --proj_dropout 0.1 \
    --device cuda \
    --do_train \
    --do_test

echo "Job finished: $(date --iso-8601=seconds)"




# mkdir -p result_out save_model
 #  sbatch gpu_run_funetuning.sh
 #
 #  Although each node has two GPUs, request only one. The current training code is single-GPU and does
 #  not use distributed training; requesting two would waste the second GPU.
 #
 #  An A100 80GB should comfortably handle:
 #
 #  DeBERTa-v3-large + CRF
 #  max_length=400
 #  batch_size=8
 #  mixed-precision training
 #
 #  You could potentially increase batch size to 16, but start with 8 to establish a reliable baseline.
 #  Check memory during training with:
 #
 #  watch -n 2 nvidia-smi
 #
 #  My partition ranking for this experiment is:
 #
 #  1. a100 — recommended, non-preemptible, up to 60 hours.
 #  2. dual_h200 or quad_h200 — potentially faster, but unnecessary for this dataset.
 #  3. scavenger_4a100 — only for short experiments; 12-hour limit and preemption risk.
 #  4. scavenger_8h100 — fast but also preemptible and limited to 12 hours.
 #  5. Private swarm_a100/swarm_h100 — only if you are eligible.
#  ST = PD
  #
  #  PD means Slurm has not allocated an A100 yet. (None) means no specific blocking reason
  #  is currently reported; it may simply be waiting for the scheduler’s next allocation
  #  cycle.
  #
  #  Check full details:
  #
  #  scontrol show job 1477910
  #
  #  Show the pending reason more clearly:
  #
  #  squeue -j 1477910 -o "%.18i %.9P %.20j %.8u %.2t %.10M %.6D %R"
  #
  #  Check priority:
  #
  #  sprio -j 1477910
  #
  #  Monitor it:
  #
  #  watch -n 10 'squeue -j 1477910'
  #
  #  When it starts, ST changes from PD to R, and a node such as rose02 will appear. Then
  #  monitor the output:
  #
  #  tail -f result_out/main_deberta-v3-large_crf_correct_data_gpt-5.6-luna-v2-1477910.out
  #
  #  There is no need to resubmit or cancel it at this point.
