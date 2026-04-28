# Artifact Reproducibility Guide

This document provides the minimal reproducibility path for the manuscript artifacts in this folder.

## Scope

The public artifact subset includes:

- Benchmark runner scripts for Ollama-based model evaluation.
- Post-processing scripts for clean summary generation.
- Plot scripts for the main benchmark figures.
- Raw/summary data examples and aggregated outputs.

## Environment

- Python: 3.10+
- OS: Linux/macOS
- Optional for power metrics: NVIDIA GPU + `nvidia-smi`
- Optional for model serving: Ollama

Install dependencies from the project root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r assets/reproducibility/requirements.txt
```

## Reproduce Main Benchmark Figures

From repository root:

```bash
cd assets/reproducibility
python3 scripts/rebuild_clean_server_artifacts.py \
  --root . \
  --device kindlab_R203 \
  --required-contexts 512,1024,2048,4096
```

Expected outputs:

- `analysis/server_suite_summary_clean_latest_valid.json`
- `analysis/server_suite_aggregated.csv`
- `figures/kindlab_R203_latency_vs_quality.{png,pdf}`
- `figures/kindlab_R203_throughput_by_model.{png,pdf}`
- `figures/kindlab_R203_ttft_p95.{png,pdf}`
- `figures/kindlab_R203_quality_heatmap.{png,pdf}`
- `figures/kindlab_R203_energy_profile.{png,pdf}`

## Run a New Server Suite (Optional)

If Ollama and models are available locally:

```bash
cd assets/reproducibility
python3 scripts/run_ollama_server_suite.py \
  --models qwen3:8b,llama2:7b,gemma3:4b,gpt-oss:20b,deepseek-r1:14b \
  --contexts 512,1024,2048,4096 \
  --repeats 1 \
  --max-tokens 128 \
  --device kindlab_R203
```

This produces:

- `data/server_suite_raw_<timestamp>.csv`
- `data/server_suite_summary_<timestamp>.json`
- Appended rows in `experiments/experiment_matrix.csv`

Then regenerate clean artifacts and figures with `rebuild_clean_server_artifacts.py`.

## Notes

- Plot generation automatically avoids unusable summary snapshots and prefers valid benchmark batches.
- This subfolder focuses on benchmark reproduction. Packaging scripts are intentionally excluded from this public subset.
