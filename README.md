# Cognitive Edge Computing Survey: LLMs and AI Agents for Edge Deployment

A concise, professional survey map for deploying large models and AI agents under real edge constraints.

认知边缘计算综述导航：聚焦大模型与智能体在边缘场景中的可部署优化。

## Table of Contents | 目录

1. [Overview | 概述](#overview--概述)
2. [Scope | 范围](#scope--范围)
3. [Taxonomy | 分类框架](#taxonomy--分类框架)
4. [Key Literature by Category | 分类别核心文献](#key-literature-by-category--分类别核心文献)
5. [Recent Highlights (2024-2025) | 近两年重点文献](#recent-highlights-2024-2025--近两年重点文献)
6. [Evaluation Checklist | 评测清单](#evaluation-checklist--评测清单)
7. [Suggested Venue Mapping | 投稿方向建议](#suggested-venue-mapping--投稿方向建议)
8. [Citation | 引用信息](#citation--引用信息)
9. [License | 许可证](#license--许可证)

## Overview | 概述

### EN

This repository organizes the literature of Cognitive Edge Computing for LLMs and AI Agents into a practical taxonomy.
The focus is deployment realism at the edge: reasoning quality, latency stability, energy efficiency, and security/privacy under resource-constrained environments.

### 中文

本仓库将认知边缘计算相关文献按可部署视角进行结构化整理。
重点不是单一指标提升，而是在边缘资源约束下同时兼顾推理质量、时延稳定、能耗效率与安全隐私。

## Scope | 范围

- Models: LLM, SLM, multimodal language models, MoE variants
- Systems: on-device inference, edge serving, optional cloud collaboration, agent tool-use loops
- Objectives: quality-preserving optimization, efficient serving, trustworthy deployment

## Taxonomy | 分类框架

| Category | Focus (EN) | 中文重点 |
|---|---|---|
| A. Foundations | edge intelligence and LLM fundamentals | 边缘智能与大模型基础 |
| B. Deployment Challenges | compute/memory/latency/security bottlenecks | 算力内存时延与安全瓶颈 |
| C. Optimization Strategies | data/model/runtime/system co-optimization | 数据/模型/运行时/系统协同优化 |
| D. Agentic Intelligence | planning, tool-use, multi-agent collaboration | 规划、工具调用、多智能体协同 |
| E. Applications | mobility, healthcare, industrial edge AI | 车联网、医疗、工业边缘应用 |
| F. Evaluation & Trust | reproducibility, metrics, governance | 可复现评测与可信治理 |

## Key Literature by Category | 分类别核心文献

### A. Foundations

- Shi et al., Edge Computing: Vision and Challenges, IEEE IoT Journal, 2016.
- Zhou et al., Edge Intelligence, Proceedings of the IEEE, 2019.
- Deng et al., Edge intelligence: The confluence of edge computing and AI, IEEE IoT Journal, 2020.
- Vaswani et al., Attention Is All You Need, NeurIPS, 2017.
- Brown et al., Language Models are Few-Shot Learners, NeurIPS, 2020.
- Wei et al., Emergent Abilities of Large Language Models, TMLR, 2022.

### B. Deployment Challenges

- Gholami et al., A Survey of Quantization Methods for Efficient Neural Network Inference, 2022.
- Nagel et al., A White Paper on Neural Network Quantization, 2021.
- Kwon et al., Efficient Memory Management for LLM Serving with PagedAttention, SOSP, 2023.
- Murthy et al., MobileAIBench: Benchmarking LLMs/LMMs for On-Device Use Cases, 2024.
- Han et al., LLM Multi-Agent Systems: Challenges and Open Problems, 2024.
- Carlini et al., Extracting Training Data from Large Language Models, USENIX Security, 2021.

### C. Optimization Strategies

- Qin et al., On-device Personalization with Data Selection and Synthesis, DAC, 2024.
- Jacob et al., Quantization and Training for Integer-Arithmetic-Only Inference, CVPR, 2018.
- Frantar et al., GPTQ, ICLR, 2023.
- Dettmers et al., QLoRA, NeurIPS, 2023.
- Tan et al., MobileQuant, EMNLP Findings, 2024.
- Dao, FlashAttention-2, ICLR, 2024.
- Li et al., EAGLE-2, EMNLP, 2024.
- Tian et al., Edge-Cloud Collaborative Inference (Survey), 2024.

### D. Agentic Intelligence

- Dorri et al., Multi-agent Systems: A Survey, IEEE Access, 2018.
- Shen et al., HuggingGPT, 2023.
- Han et al., LLM Multi-Agent Systems, 2024.
- Yan et al., Communication-Centric Survey of LLM-based Multi-Agent Systems, 2025.
- Belcak et al., Small Language Models are the Future of Agentic AI, 2025.
- Gao et al., A Survey of Self-Evolving Agents, 2025.

### E. Applications

- Abdin et al., Phi-4 Technical Report, 2024.
- Team Gemma, Gemma Technical Report, 2024.
- Mehta et al., OpenELM, 2024.
- Marone et al., mmBERT, 2025.
- Chiu et al., V2V-LLM for Cooperative Autonomous Driving, 2025.
- Rivkin et al., AIoT Smart Home via Autonomous LLM Agents, 2024.

### F. Evaluation and Trust

- Strubell et al., Energy and Policy Considerations for Modern Deep Learning Research, AAAI, 2020.
- Dwork and Roth, The Algorithmic Foundations of Differential Privacy, 2014.
- Laskaridis et al., Mobile and Edge Evaluation of LLMs, 2024.
- Oliinyk et al., Fuzzing BusyBox with LLM support, USENIX Security, 2024.
- Ma et al., LLM-assisted fuzzing of IoT device stacks, USENIX Security, 2024.

## Recent Highlights (2024-2025) | 近两年重点文献

### Systems and Serving

- PowerInfer-2: Fast smartphone LLM inference (2024)
- EdgeLLM: Fast on-device speculative decoding (2024)
- SwapMoE: Memory-budgeted MoE serving (2024)
- Fast on-device LLM inference with NPUs (2025)
- Lincoln: Real-time 50-100B LLM inference on consumer devices (2025)

### Collaboration and Routing

- EdgeShard: collaborative edge inference (2024)
- QoS-aware LLM routing with multiple experts (2025)
- CLONE: latency-aware edge customization (2025)
- Device-server collaborative text streaming (2025)

### Hardware-Aware Acceleration

- Cambricon-LLM chiplet architecture (2024)
- PAISE: PIM-accelerated transformer scheduling (2025)
- FACIL: SoC-PIM cooperative inference mapping (2025)
- T-MAC: low-bit deployment on edge CPUs (2025)

### Multimodal and Domain Deployment

- Self-adapting VLMs for edge modalities (2024)
- MiniCPM-V on-phone multimodal model (2024)
- MobileLLM-R1 sub-billion reasoning models (2025)
- VaVLM edge-cloud video analytics (2025)
- Industrial IoT with LLM-based intelligence (2024)

## Evaluation Checklist | 评测清单

Recommended minimum report for each study:

- Quality: accuracy/task success/reasoning fidelity
- Performance: throughput, TTFT, p95/p99 latency
- Efficiency: memory footprint, energy per token
- Deployment: on-device ratio, optional offload ratio (when cloud collaboration is enabled)
- Reliability: long-run stability, retry/failure rate
- Trust: privacy/security mechanism and threat assumptions

## Suggested Venue Mapping | 投稿方向建议

| Research emphasis | Suggested venues |
|---|---|
| Data/knowledge management + reproducible protocol synthesis | TKDE, TOIS, ACM CSUR |
| Edge systems and serving architecture | IEEE TMC, IEEE IoTJ, IEEE TPDS |
| Efficient inference/compression methods | TNNLS, MLSys tracks, ICML/NeurIPS systems |
| Trustworthy and secure agent deployment | IEEE TAI, security/system venues |

## Citation | 引用信息

If this repository is useful for your research, please cite:

如果本仓库对你的研究有帮助，请引用：

```bibtex
@article{wang2025cognitive,
  title={Cognitive edge computing: A comprehensive survey on optimizing large models and AI agents for pervasive deployment},
  author={Wang, Xubin and Li, Qing and Jia, Weijia},
  journal={arXiv preprint arXiv:2501.03265},
  year={2025}
}
```

## License | 许可证

Released under the repository LICENSE.
