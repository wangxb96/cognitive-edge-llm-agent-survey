# Artifact Release Notes Template

## Title

Cognitive Edge Computing Survey: Reproducibility Artifacts

## Suggested Tag

v1.0-artifacts

## Summary

This release provides reproducibility artifacts for the manuscript:

**Cognitive Edge Computing: A Survey on Optimizing Large Language Models and Autonomous Agents for the Edge**.

It includes benchmark runners, cleaned aggregation pipelines, and plotting scripts used to produce the main benchmark tables and figures.

## Included Components

- Benchmark runners:
  - `scripts/run_ollama_server_suite.py`
  - `scripts/run_ollama_mve.py`
- Artifact rebuilding:
  - `scripts/rebuild_clean_server_artifacts.py`
- Plot generation:
  - `scripts/plot_benchmark_results.py`
- Reproducibility docs:
  - `ARTIFACT_REPRODUCIBILITY.md`

## Quick Reproduction

From repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r assets/reproducibility/requirements.txt

cd assets/reproducibility
python3 scripts/rebuild_clean_server_artifacts.py \
  --root . \
  --device kindlab_R203 \
  --required-contexts 512,1024,2048,4096
```

Expected regenerated outputs include:

- `analysis/server_suite_aggregated.csv`
- `figures/kindlab_R203_latency_vs_quality.{png,pdf}`
- `figures/kindlab_R203_throughput_by_model.{png,pdf}`
- `figures/kindlab_R203_ttft_p95.{png,pdf}`
- `figures/kindlab_R203_quality_heatmap.{png,pdf}`
- `figures/kindlab_R203_energy_profile.{png,pdf}`

## Notes for Reviewers

- The pipeline excludes failed benchmark rows (`oom_or_fail=1`) when producing final clean artifacts.
- The plotting pipeline validates summary usability and falls back to valid matrix-derived batches when needed.
- The public subset focuses on benchmark reproduction scripts and figure/table regeneration.

## Citation

If this artifact is useful, please cite the associated manuscript and repository release/tag.
