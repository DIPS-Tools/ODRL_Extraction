FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install the CPU-only PyTorch wheel separately so the service image does not
# contain CUDA runtime libraries that are unnecessary for --device cpu.
RUN python -m pip install \
      --index-url https://download.pytorch.org/whl/cpu \
      torch==2.4.0

COPY requirements.docker.txt ./requirements.docker.txt
RUN python -m pip install -r requirements.docker.txt

COPY app_rule_bias.py odrl_output.py ./
COPY model ./model
COPY src ./src
COPY templates ./templates

# Config creates these paths during startup. The checkpoint itself is supplied
# as a read-only bind mount by docker-compose.yml.
RUN mkdir -p /app/save_model/quantized /app/data \
    && useradd --create-home --uid 10001 appuser \
    && chown -R appuser:appuser /app

USER appuser

EXPOSE 5001

CMD ["python", "-u", "app_rule_bias.py", "--help"]
