#!/usr/bin/env python3
import csv
import json
import pathlib
import statistics
import time
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "experiments" / "ollama_mve_config.json"
OUT_DIR = ROOT / "data"
OUT_DIR.mkdir(parents=True, exist_ok=True)
RAW_CSV = OUT_DIR / f"ollama_mve_raw_{int(time.time())}.csv"
SUMMARY_JSON = OUT_DIR / "ollama_mve_summary.json"
MATRIX_CSV = ROOT / "experiments" / "experiment_matrix.csv"


def post_json(url: str, payload: dict) -> dict:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as resp:
        return json.loads(resp.read().decode("utf-8"))


def normalized_answer(text: str) -> str:
    return " ".join(text.strip().split()).lower()


def make_padding_prompt(target_words: int) -> str:
    seed = "edge model latency benchmark token "
    words = seed.split()
    out = []
    while len(out) < target_words:
        out.extend(words)
    return " ".join(out[:target_words])


def run_once(base_url: str, model: str, num_ctx: int, prompt: str, max_tokens: int, temperature: float, seed: int) -> dict:
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_ctx": num_ctx,
            "num_predict": max_tokens,
            "temperature": temperature,
            "seed": seed,
        },
    }
    t0 = time.time()
    resp = post_json(base_url, payload)
    t1 = time.time()

    eval_count = resp.get("eval_count", 0)
    eval_duration = resp.get("eval_duration", 0)  # ns
    prompt_eval_count = resp.get("prompt_eval_count", 0)
    prompt_eval_duration = resp.get("prompt_eval_duration", 0)  # ns

    decode_tps = 0.0
    if eval_duration > 0 and eval_count > 0:
        decode_tps = eval_count / (eval_duration / 1e9)

    ttft_ms = 0.0
    if prompt_eval_duration > 0:
        ttft_ms = (prompt_eval_duration / 1e6)

    return {
        "response": resp.get("response", ""),
        "wall_latency_ms": (t1 - t0) * 1000.0,
        "ttft_ms": ttft_ms,
        "decode_tokens": eval_count,
        "decode_tps": decode_tps,
        "prompt_tokens": prompt_eval_count,
    }


def append_matrix_rows(rows):
    with MATRIX_CSV.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for r in rows:
            writer.writerow([
                r["run_id"],
                r["date"],
                "kindlab_r203_sim_local",
                r["model"],
                r["quantization"],
                r["context_len"],
                r["prompt_tokens"],
                r["gen_tokens"],
                "default",
                "single-session",
                "local-only",
                f"{r['ttft_ms']:.2f}",
                f"{r['p50_latency_ms']:.2f}",
                f"{r['p95_latency_ms']:.2f}",
                f"{r['tokens_per_sec']:.2f}",
                "NA",
                "NA",
                "exact_match",
                f"{r['quality_value']:.3f}",
                "0",
                r["notes"],
            ])


def main():
    cfg = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    all_raw = []
    summary_rows = []

    for model in cfg["models"]:
        quant = "int4/int8-runtime"
        for num_ctx in cfg["contexts"]:
            latencies = []
            ttfts = []
            tps_list = []
            gen_tokens = []
            quality_hits = 0
            quality_total = 0

            # warmup with padding prompt to stabilize cache/runtime path
            warm_prompt = make_padding_prompt(160)
            _ = run_once(
                cfg["base_url"],
                model,
                num_ctx,
                warm_prompt,
                cfg["max_tokens"],
                cfg["temperature"],
                cfg["seed"],
            )

            for task in cfg["quality_tasks"]:
                for rep in range(cfg["repeats"]):
                    result = run_once(
                        cfg["base_url"],
                        model,
                        num_ctx,
                        task["prompt"],
                        cfg["max_tokens"],
                        cfg["temperature"],
                        cfg["seed"] + rep,
                    )
                    pred = normalized_answer(result["response"])
                    ans = normalized_answer(task["answer"])
                    hit = 1 if ans in pred else 0
                    quality_hits += hit
                    quality_total += 1

                    latencies.append(result["wall_latency_ms"])
                    ttfts.append(result["ttft_ms"])
                    tps_list.append(result["decode_tps"])
                    gen_tokens.append(result["decode_tokens"])

                    all_raw.append({
                        "model": model,
                        "context_len": num_ctx,
                        "task_id": task["id"],
                        "repeat": rep,
                        "wall_latency_ms": result["wall_latency_ms"],
                        "ttft_ms": result["ttft_ms"],
                        "decode_tokens": result["decode_tokens"],
                        "decode_tps": result["decode_tps"],
                        "prompt_tokens": result["prompt_tokens"],
                        "quality_hit": hit,
                        "prediction": result["response"].strip().replace("\n", " "),
                        "answer": task["answer"],
                    })

            p50 = statistics.median(latencies) if latencies else 0.0
            p95 = statistics.quantiles(latencies, n=20)[18] if len(latencies) >= 20 else max(latencies) if latencies else 0.0
            mean_ttft = statistics.mean(ttfts) if ttfts else 0.0
            mean_tps = statistics.mean(tps_list) if tps_list else 0.0
            mean_gen = statistics.mean(gen_tokens) if gen_tokens else 0.0
            q = (quality_hits / quality_total) if quality_total else 0.0

            summary_rows.append({
                "run_id": f"ollama_mve_{int(time.time())}_{model.replace(':','_')}_{num_ctx}",
                "date": time.strftime("%Y-%m-%d"),
                "model": model,
                "quantization": quant,
                "context_len": num_ctx,
                "prompt_tokens": int(statistics.mean([r["prompt_tokens"] for r in all_raw if r["model"] == model and r["context_len"] == num_ctx]) if any(r["model"] == model and r["context_len"] == num_ctx for r in all_raw) else 0),
                "gen_tokens": int(mean_gen),
                "ttft_ms": mean_ttft,
                "p50_latency_ms": p50,
                "p95_latency_ms": p95,
                "tokens_per_sec": mean_tps,
                "quality_value": q,
                "notes": "MVE via Ollama API; no privileged power metrics",
            })

    with RAW_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(all_raw[0].keys()) if all_raw else ["model"])
        writer.writeheader()
        if all_raw:
            writer.writerows(all_raw)

    SUMMARY_JSON.write_text(json.dumps(summary_rows, indent=2), encoding="utf-8")
    append_matrix_rows(summary_rows)

    print(f"Wrote raw results: {RAW_CSV}")
    print(f"Wrote summary: {SUMMARY_JSON}")
    print(f"Appended matrix: {MATRIX_CSV}")


if __name__ == "__main__":
    main()
