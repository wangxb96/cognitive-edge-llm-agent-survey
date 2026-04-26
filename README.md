# Cognitive Edge LLM-Agent Survey

Professional taxonomy and reading map for Cognitive Edge Computing research on Large Language Models (LLMs) and AI Agents.

认知边缘计算（LLM 与 AI Agent）综述的专业分类、阅读地图与引用索引。

## Table of Contents | 目录

1. [Overview | 项目概述](#overview--项目概述)
2. [Survey Scope | 综述范围](#survey-scope--综述范围)
3. [Taxonomy at a Glance | 分类总览](#taxonomy-at-a-glance--分类总览)
4. [Detailed Taxonomy and References | 分类详情与参考文献](#detailed-taxonomy-and-references--分类详情与参考文献)
5. [Recommended Evaluation Metrics | 推荐评测指标](#recommended-evaluation-metrics--推荐评测指标)
6. [Paper Citation | 论文引用](#paper-citation--论文引用)
7. [How to Maintain This README | README 维护规范](#how-to-maintain-this-readme--readme-维护规范)
8. [License | 许可证](#license--许可证)

## Overview | 项目概述

This repository provides a single-file, academically structured survey layout for edge-side LLM and agent systems.
It is designed for researchers and practitioners who need:

- a clean taxonomy of cognitive edge computing,
- representative references under each category,
- reproducibility-oriented reporting guidance,
- and citation-ready paper information.

本仓库采用单 README 学术化布局，面向边缘侧大模型与智能体研究，提供：

- 清晰的分类体系，
- 每个分类下的代表文献，
- 面向复现的评测建议，
- 可直接使用的论文引用信息。

## Survey Scope | 综述范围

### EN

The survey focuses on capability preservation under constrained budgets:

- compute and memory limits,
- tail latency and service stability,
- energy and thermal envelopes,
- privacy, safety, and governance constraints,
- device-edge-cloud collaborative deployment.

### 中文

综述重点关注“预算约束下的能力保持”，包括：

- 算力与内存限制，
- 尾时延与服务稳定性，
- 能耗与热约束，
- 隐私、安全与治理要求，
- 端-边-云协同部署。

## Taxonomy at a Glance | 分类总览

| Category | Focus (EN) | 中文要点 |
|---|---|---|
| A. Foundations | Edge intelligence + LLM basics | 边缘智能基础与大模型基础 |
| B. Deployment Challenges | Resource, latency, reliability, security constraints | 资源、时延、稳定性与安全挑战 |
| C. Optimization Strategies | Data/model/runtime/system co-optimization | 数据、模型、运行时、系统协同优化 |
| D. Agentic Systems | Tool-use loops, multi-agent coordination | 工具调用回路与多智能体协同 |
| E. Applications | Mobility, healthcare, industrial and consumer scenarios | 车联网、医疗、工业与消费场景 |
| F. Evaluation and Trust | Multi-metric evaluation, reproducibility, governance | 多指标评测、复现与治理可信 |

## Detailed Taxonomy and References | 分类详情与参考文献

### A. Foundations | 基础概念

Scope:
- EN: Core concepts of edge computing and LLM capability formation.
- 中文: 边缘计算与大模型能力形成机制的基础知识。

Representative references:
1. Shi et al., Edge Computing: Vision and Challenges, IEEE IoTJ, 2016. https://doi.org/10.1109/JIOT.2016.2579198
2. Zhou et al., Edge Intelligence, Proceedings of the IEEE, 2019. https://doi.org/10.1109/JPROC.2019.2918951
3. Vaswani et al., Attention Is All You Need, NeurIPS, 2017. https://arxiv.org/abs/1706.03762
4. Brown et al., Language Models are Few-Shot Learners, NeurIPS, 2020. https://arxiv.org/abs/2005.14165
5. Wei et al., Emergent Abilities of LLMs, TMLR, 2022. https://arxiv.org/abs/2206.07682

### B. Deployment Challenges | 部署挑战

Scope:
- EN: Hard constraints in real deployment: memory bandwidth, tail latency, reliability, and safety.
- 中文: 真实部署中的硬约束：内存带宽、尾时延、稳定性与安全。

Representative references:
1. Gholami et al., Quantization Methods Survey, 2022. https://arxiv.org/abs/2103.13630
2. Nagel et al., Neural Network Quantization White Paper, 2021. https://arxiv.org/abs/2106.08295
3. Kwon et al., PagedAttention for LLM Serving, SOSP, 2023. https://doi.org/10.1145/3600006.3613165
4. Murthy et al., MobileAIBench, 2024. https://arxiv.org/abs/2406.10290
5. Han et al., LLM Multi-Agent Systems: Challenges and Open Problems, 2024. https://arxiv.org/abs/2402.03578

### C. Optimization Strategies | 优化策略

Scope:
- EN: Budget-first co-design across data, model, runtime, and system routing.
- 中文: 以预算为中心的数据、模型、运行时与系统协同设计。

Representative references:
1. Qin et al., On-device LLM Personalization with Data Selection and Synthesis, DAC, 2024.
2. Jacob et al., Quantization and Training for Integer-Only Inference, CVPR, 2018. https://doi.org/10.1109/CVPR.2018.00287
3. Frantar et al., GPTQ, ICLR, 2023. https://arxiv.org/abs/2210.17323
4. Hinton et al., Distilling the Knowledge in a Neural Network, 2015. https://arxiv.org/abs/1503.02531
5. Dao, FlashAttention-2, ICLR, 2024. https://arxiv.org/abs/2307.08691
6. Li et al., EAGLE-2, EMNLP, 2024. https://aclanthology.org/2024.emnlp-main.422/
7. Zhao et al., QSpec, 2024. https://arxiv.org/abs/2410.11305
8. Tian et al., Edge-Cloud Collaborative Inference Survey, 2024. https://arxiv.org/abs/2407.04482

### D. Agentic Systems | 智能体系统

Scope:
- EN: Agent loop control, tool invocation policies, and multi-agent collaboration at the edge.
- 中文: 边缘侧智能体回路控制、工具调用策略与多智能体协同。

Representative references:
1. Dorri et al., Multi-agent Systems: A Survey, IEEE Access, 2018. https://doi.org/10.1109/ACCESS.2018.2831228
2. Shen et al., HuggingGPT, 2023. https://arxiv.org/abs/2303.17580
3. Han et al., LLM Multi-Agent Systems, 2024. https://arxiv.org/abs/2402.03578
4. Yan et al., Communication-centric Survey of LLM-based MAS, 2025. https://arxiv.org/abs/2502.14321
5. Belcak et al., Small Language Models are the Future of Agentic AI, 2025. https://arxiv.org/abs/2506.02153
6. Gao et al., Survey of Self-evolving Agents, 2025. https://arxiv.org/abs/2507.21046

### E. Applications | 应用场景

Scope:
- EN: Domain deployment patterns in mobility, healthcare, and industrial/consumer edge AI.
- 中文: 车联网、医疗、工业/消费端的边缘部署模式。

Representative references:
1. Deng et al., Edge intelligence confluence survey, 2020. https://doi.org/10.1109/JIOT.2020.3007838
2. Ali et al., Federated Learning for Smart Healthcare, IEEE JBHI, 2022.
3. Abdin et al., Phi-4 Technical Report, 2024.
4. Team Gemma et al., Gemma Technical Report, 2024. https://arxiv.org/abs/2403.08295
5. Mehta et al., OpenELM, 2024.
6. Marone et al., mmBERT, 2025. https://arxiv.org/abs/2509.06888

### F. Evaluation and Trust | 评估与可信

Scope:
- EN: Reproducibility-first evaluation and governance-aware risk reporting.
- 中文: 以可复现为优先、兼顾治理约束的风险与评估框架。

Representative references:
1. Murthy et al., MobileAIBench, 2024. https://arxiv.org/abs/2406.10290
2. Laskaridis et al., Mobile and Edge Evaluation of LLMs, 2024.
3. Strubell et al., Energy and Policy Considerations, AAAI, 2020. https://doi.org/10.1609/aaai.v34i09.7123
4. Dwork and Roth, Differential Privacy Foundations, 2014. https://doi.org/10.1561/0400000042

## Recommended Evaluation Metrics | 推荐评测指标

To avoid single-number claims, report at least:

- Task quality (accuracy, task success, reasoning fidelity)
- Throughput (tokens/s)
- Startup latency (TTFT)
- Tail latency (p95/p99)
- Energy per token (J/token)
- Offload ratio (device vs edge/cloud)

为避免单指标结论，建议至少报告：

- 任务质量（准确率、任务成功率、推理保持度）
- 吞吐（tokens/s）
- 启动时延（TTFT）
- 尾时延（p95/p99）
- 单位 token 能耗（J/token）
- 卸载比例（端侧与边/云占比）

## Paper Citation | 论文引用

If this repository supports your research, please cite the survey paper:

如果本仓库对你的研究有帮助，请引用以下综述论文：

```bibtex
@article{wang2026cognitiveedge,
	title   = {Cognitive Edge Computing: A Survey on Optimizing Large Language Models and Autonomous Agents for the Edge},
	author  = {Wang, Xubin and Li, Qing and Jia, Weijia},
	journal = {Under review / manuscript repository},
	year    = {2026},
	note    = {Please replace with final publication venue and DOI when available}
}
```

## How to Maintain This README | README 维护规范

1. Add new papers under one primary category first.
2. Keep bilingual EN/ZH descriptions synchronized.
3. Include linkable identifiers when possible (DOI/arXiv/ACL/OpenReview).
4. Mark unresolved metadata with a clear note instead of leaving ambiguity.

1. 新文献先归入一个主分类。
2. 保持中英文说明同步更新。
3. 优先补全可点击标识（DOI/arXiv/ACL/OpenReview）。
4. 元数据不确定时请明确标注，不要留含糊描述。

## License | 许可证

This project is released under the repository's LICENSE.

本项目遵循仓库中的 LICENSE。
