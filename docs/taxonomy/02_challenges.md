# Taxonomy B: Deployment Challenges | 分类B：部署挑战

## B1. Resource Bottlenecks | 资源瓶颈

- EN: Compute mismatch, memory bandwidth pressure, KV-cache growth, thermal throttling.
- 中文: 算力失配、带宽压力、KV 缓存增长与热节流。

### References

- Gholami et al. A Survey of Quantization Methods for Efficient Neural Network Inference. 2022.
- Nagel et al. A White Paper on Neural Network Quantization. 2021.
- Kwon et al. Efficient Memory Management for LLM Serving with PagedAttention. SOSP, 2023.

## B2. Performance and Stability | 性能与稳定性

- EN: Throughput/latency tradeoff, startup delay, p95/p99 tail latency under bursty load.
- 中文: 吞吐-时延权衡、首 token 延迟、突发负载下 p95/p99 尾时延。

### References

- Murthy et al. MobileAIBench: Benchmarking LLMs and LMMs for On-Device Use Cases. 2024.
- Sheng et al. FlexGen: High-throughput Generative Inference of LLMs with a Single GPU. ICML, 2023.

## B3. Security and Privacy Risks | 安全与隐私风险

- EN: Prompt injection, unsafe tool use, privacy leakage, weak policy control.
- 中文: 提示词注入、工具滥用、隐私泄露与策略控制不足。

### References

- Dwork and Roth. The Algorithmic Foundations of Differential Privacy. 2014.
- Han et al. LLM Multi-Agent Systems: Challenges and Open Problems. 2024.
