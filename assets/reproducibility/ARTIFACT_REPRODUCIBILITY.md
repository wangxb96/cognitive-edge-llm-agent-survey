# Benchmark script provenance and supported recalculation

This folder retains original runner, selector and plotting sources from the focused survey project. These files assume that project's earlier directory layout. The repository does not include the historical request CSVs, summary JSONs or experiment matrix needed by the old figure-rebuild command.

## Current public record

Use the [integrated server archive](https://github.com/wangxb96/Awesome-EdgeAI/tree/supplement-2026-11-13-v4/survey/server) for the recovered empirical requests, summaries, task definitions, campaign/failure ledger and descriptive reanalysis. The [supplement](https://github.com/wangxb96/Awesome-EdgeAI/tree/supplement-2026-11-13-v4/survey/supplement) defines the interpretation boundaries. The [figure catalogue](https://github.com/wangxb96/Awesome-EdgeAI/tree/supplement-2026-11-13-v4/survey/figures) provides supported redraw sources and inputs.

```sh
git clone --branch supplement-2026-11-13-v4 https://github.com/wangxb96/Awesome-EdgeAI.git
cd Awesome-EdgeAI
python3 survey/server/analyze_archived.py
```

The analysis uses Python 3.9+ and the standard library. It invokes no model and makes no network calls after the clone. Figure redrawing and supplement compilation require the dependencies documented in their respective directories.

## What the older scripts establish

| Snapshot | Inspectable behavior |
|---|---|
| [Runner](scripts/run_ollama_server_suite.py) | Ten task prompts/answers, normalized answer-containment scoring, request timing and two-endpoint GPU-power proxy |
| [Selector](scripts/rebuild_clean_server_artifacts.py) | Earlier latest-complete-per-model summary selection, including why campaigns can be mixed |
| [Plotter](scripts/plot_benchmark_results.py) | Earlier aggregate-table and figure construction |

The runner and selector match the copies in the integrated server archive. Their defaults are source-level information, not a record of the exact options used in historical execution. Running them with new models would produce a new experiment rather than reproduce the old execution.

## Measurement limits

The historical score is answer containment rather than strict exact match. The field named TTFT is prompt-evaluation duration, and energy is an unvalidated endpoint GPU-power proxy. Actual prompt length differs from configured context ceilings. Campaigns, empty response fields and failures must be inspected before interpreting the results.

Exact historical checkpoint/template, precision, runtime/driver/placement, command-line settings and complete power/response traces were not retained. Recalculation is supported; identical model execution, causal capability rankings and transfer to mobile devices are not established.

[Back to the focused guide](../../README.md)
