# Cognitive Edge Computing Literature Hub: A Comprehensive Taxonomy and Professional Survey Map for Optimizing Large Language Models and AI Agents for Pervasive Device-Edge-Cloud Deployment

A bilingual, high-density survey README for Cognitive Edge Computing research.

面向认知边缘计算研究的中英双语高信息密度综述主页。

## Table of Contents | 目录

1. [Executive Summary | 执行摘要](#executive-summary--执行摘要)
2. [Scope and Positioning | 研究范围与定位](#scope-and-positioning--研究范围与定位)
3. [Taxonomy Framework | 分类框架](#taxonomy-framework--分类框架)
4. [Category A: Foundations and System Context | 类别A基础与系统背景](#category-a-foundations-and-system-context--类别a基础与系统背景)
5. [Category B: Deployment Challenges | 类别B部署挑战](#category-b-deployment-challenges--类别b部署挑战)
6. [Category C: Optimization Strategies | 类别C优化策略](#category-c-optimization-strategies--类别c优化策略)
7. [Category D: Agentic Intelligence and Collaboration | 类别D智能体与协同](#category-d-agentic-intelligence-and-collaboration--类别d智能体与协同)
8. [Category E: Application Domains | 类别E应用场景](#category-e-application-domains--类别e应用场景)
9. [Category F: Evaluation, Security, and Governance | 类别F评测安全与治理](#category-f-evaluation-security-and-governance--类别f评测安全与治理)
10. [Survey Delta vs Related Repositories and Surveys | 与相关综述的差异化](#survey-delta-vs-related-repositories-and-surveys--与相关综述的差异化)
11. [Recommended Reporting Template | 推荐报告模板](#recommended-reporting-template--推荐报告模板)
12. [Citation | 引用信息](#citation--引用信息)
13. [Maintenance Rules | 维护规范](#maintenance-rules--维护规范)
14. [License | 许可证](#license--许可证)

## Executive Summary | 执行摘要

### EN

This repository is built as a professional literature map for Cognitive Edge Computing, where LLMs and AI agents are deployed under strict constraints of memory, latency, energy, safety, and privacy. The core viewpoint is budget-first capability preservation: retain reasoning and autonomous behavior under realistic device-edge-cloud conditions rather than chasing single benchmark numbers.

### 中文

本仓库以专业综述导航的形式组织认知边缘计算文献，关注大模型与智能体在内存、时延、能耗、安全和隐私约束下的实际部署。核心观点是“预算优先的能力保持”：在真实端-边-云条件下保持推理与自治能力，而不是追求单一基准分数。

## Scope and Positioning | 研究范围与定位

- Focus models: LLM, SLM, multimodal LLM, MoE-based edge models
- Focus systems: on-device inference, edge serving, edge-cloud collaboration, agent tool loops
- Focus objectives: reasoning fidelity, cost/energy efficiency, latency stability, reproducibility, governance
- Time span: representative works from classical edge computing foundations to recent 2024-2025 edge LLM/agent literature

## Taxonomy Framework | 分类框架

```text
A. Foundations and Context
  A1. Edge computing and edge intelligence fundamentals
  A2. LLM architecture and capability foundations
  A3. On-device model families and SLM trends

B. Deployment Challenges
  B1. Compute-memory-bandwidth bottlenecks
  B2. Tail-latency and serving stability
  B3. Privacy, safety, and trust risks

C. Optimization Strategies
  C1. Data/context optimization
  C2. Model compression and adaptation
  C3. Runtime and serving optimization
  C4. Edge-cloud collaborative routing
  C5. Hardware-aware and system co-design

D. Agentic Intelligence
  D1. Tool-augmented agent loop design
  D2. Multi-agent coordination patterns
  D3. Small-model-first agent deployment

E. Applications
  E1. Mobility and autonomous systems
  E2. Healthcare and privacy-sensitive deployment
  E3. Industrial and enterprise edge intelligence

F. Evaluation, Security, Governance
  F1. Reproducible multi-metric evaluation
  F2. Security/privacy controls and policy alignment
  F3. Open challenges and future directions
```

## Category A: Foundations and System Context | 类别A：基础与系统背景

### A1. Edge Computing and Edge Intelligence Fundamentals | 边缘计算与边缘智能基础

- Shi et al. (2016), Edge Computing: Vision and Challenges, IEEE IoT Journal
  Contribution: Early edge vision and system-level challenge framing.
- Zhou et al. (2019), Edge Intelligence, Proceedings of the IEEE
  Contribution: Integrates AI with edge architecture and service constraints.
- Deng et al. (2020), Edge Intelligence Confluence Survey, IEEE IoT Journal
  Contribution: Comprehensive survey on edge-AI integration trends.
- Li et al. (2019), Edge AI On-demand DNN Inference, IEEE TWC
  Contribution: Latency-aware inference acceleration via edge offloading.
- Chen and Ran (2019), Deep Learning with Edge Computing, Proceedings of the IEEE
  Contribution: Systematic review of edge deep learning pipelines.

### A2. LLM Foundations for Edge Adaptation | 面向边缘适配的大模型基础

- Vaswani et al. (2017), Attention Is All You Need
- Brown et al. (2020), Language Models are Few-Shot Learners
- Wei et al. (2022), Emergent Abilities of LLMs
- Touvron et al. (2023), Llama 2 Technical Report
- Dubey et al. (2024), The Llama 3 Herd of Models
- Team Gemma (2024), Gemma Technical Report

### A3. On-device and Small Language Model Direction | 端侧与小模型方向

- Lu et al. (2024), Small Language Models Survey
- Van Nguyen et al. (2024), Survey of Small Language Models
- Belcak et al. (2025), Small Language Models are the Future of Agentic AI
- Mehta et al. (2024), OpenELM
- Abdin et al. (2024), Phi-4 Technical Report
- Liu et al. (2024), MobileLLM

## Category B: Deployment Challenges | 类别B：部署挑战

### B1. Compute, Memory, and Bandwidth Pressure | 算力内存带宽压力

- Gholami et al. (2022), Quantization Survey
- Nagel et al. (2021), Neural Network Quantization White Paper
- Xu et al. (2024), EdgeLLM Survey
- Xiao et al. (2024), Understanding LLMs in Your Pockets
- Yi et al. (2025), EdgeMoE for Mobile Devices

### B2. Latency, Throughput, and Stability | 时延吞吐与稳定性

- Kwon et al. (2023), PagedAttention
- Sheng et al. (2023), FlexGen
- Murthy et al. (2024), MobileAIBench
- Laskaridis et al. (2024), Mobile and Edge Evaluation of LLMs
- Frantar et al. (2025), Marlin Mixed-Precision Inference

### B3. Security, Privacy, and Safety Risks | 安全隐私与安全性风险

- Dwork and Roth (2014), Differential Privacy Foundations
- Carlini et al. (2021), Extracting Training Data from LLMs
- Han et al. (2024), LLM Multi-Agent Systems: Challenges
- Andong et al. (2025), Federated Learning and Privacy Directions

## Category C: Optimization Strategies | 类别C：优化策略

### C1. Data and Context Optimization | 数据与上下文优化

- Qin et al. (2024), On-device Personalization via Data Selection and Synthesis
- Tirumala et al. (2023), Document De-duplication and Diversification (D4)
- Wu et al. (2025), LiveLongBench for Long-context Understanding
- Marone et al. (2025), mmBERT for Efficient Multilingual Retrieval

### C2. Model Compression and Adaptation | 模型压缩与适配

- Jacob et al. (2018), Integer-only Quantization Training
- Hinton et al. (2015), Knowledge Distillation
- Gou et al. (2021), Distillation Survey
- Frantar et al. (2023), GPTQ
- Dettmers et al. (2023), QLoRA
- Tan et al. (2024), MobileQuant
- Frantar and Alistarh (2023), SparseGPT
- Han et al. (2016), Deep Compression

### C3. Runtime and Serving Optimization | 运行时与服务优化

- Kwon et al. (2023), PagedAttention
- Zheng et al. (2024), SGLang
- Dao (2024), FlashAttention-2
- Li et al. (2024), EAGLE-2
- Zhao et al. (2024), QSpec
- Zhao et al. (2025), FR-Spec
- Zhang et al. (2025), Speculative Decoding meets Quantization

### C4. Edge-Cloud Collaboration and Offloading | 端边云协同与卸载

- Tian et al. (2024), Edge-Cloud Collaborative Inference Survey
- Jin et al. (2025), CoLLM
- Yuan et al. (2025), Local-Cloud Inference Offloading
- Dai et al. (2020), Edge Intelligence for Resource Allocation and Offloading

### C5. Hardware-aware Co-design | 硬件感知协同设计

- Wang et al. (2019), HAQ Hardware-aware Quantization
- Kim et al. (2025), Slim-Llama Low-power LLM Processor
- Yang et al. (2023), PIM-based acceleration pathways
- Cho et al. (2021), FPGA-GPU hybrid acceleration
- Kouris et al. (2022), Fluid batching on edge NPUs

## Category D: Agentic Intelligence and Collaboration | 类别D：智能体与协同

### D1. Tool-use Agent Loop | 工具调用智能体回路

- Shen et al. (2023), HuggingGPT
- Han et al. (2024), LLM Multi-agent Challenges
- Gao et al. (2025), Self-evolving Agents Survey

### D2. Multi-agent Communication and Planning | 多智能体通信与规划

- Dorri et al. (2018), Multi-agent Systems Survey
- Yan et al. (2025), Communication-centric MAS Survey
- Belcak et al. (2025), SLM-first agentic deployment

### D3. Practical Edge Agent Patterns | 边缘智能体落地模式

- Planner-Executor role split
- Tool-step budget caps
- Cached tool outputs with freshness checks
- Adaptive offload policy by network and battery state

## Category E: Application Domains | 类别E：应用场景

### E1. Mobility and Autonomous Systems | 车联网与自动系统

- Edge intelligence for low-latency control and perception
- Representative basis: Zhou 2019, Deng 2020, Xu 2024

### E2. Healthcare and Privacy-sensitive AI | 医疗与隐私敏感AI

- Federated adaptation and privacy-preserving local inference
- Representative basis: Ali 2022, Dwork 2014, Andong 2025

### E3. Industrial and Enterprise Edge AI | 工业与企业边缘智能

- On-device assistants, quality control pipelines, multilingual retrieval, domain-specialized SLMs
- Representative basis: OpenELM 2024, Gemma 2024, Phi-4 2024, mmBERT 2025

## Category F: Evaluation, Security, and Governance | 类别F：评测安全与治理

### F1. Reproducible Multi-metric Evaluation | 可复现多指标评测

Minimum report set:

- Task quality: accuracy, task success, reasoning fidelity
- Serving performance: throughput, TTFT, p95/p99
- Cost metrics: J/token, memory footprint, offload ratio
- Stability: failure/retry rate, long-run thermal behavior

### F2. Security and Governance Controls | 安全与治理控制

Recommended checklist:

- Prompt injection resistance and tool safety policy
- Data leakage risk tests and privacy mechanism disclosure
- Trust boundaries for local-edge-cloud data movement
- Reproducibility level tag (artifact availability and protocol completeness)

### F3. Key References | 关键文献

- Strubell et al. (2020), Energy and Policy Considerations
- Murthy et al. (2024), MobileAIBench
- Laskaridis et al. (2024), Mobile and Edge Evaluation
- Dwork and Roth (2014), Differential Privacy

## Survey Delta vs Related Repositories and Surveys | 与相关综述的差异化

| Dimension | Common survey pattern | This repository |
|---|---|---|
| Structure | Topic list only | Full taxonomy + operational deployment map |
| Metrics | Accuracy-centric | Multi-objective (quality, latency, energy, stability) |
| Agent perspective | Often optional | Agent loop and multi-agent collaboration as first-class axis |
| Edge realism | Partial | Explicit device-edge-cloud constraints and offloading trade-offs |
| Reproducibility | Limited protocol guidance | Reporting template and governance checklist |

## Recommended Reporting Template | 推荐报告模板

Use this compact template in paper notes:

- Work:
- Category tag: A/B/C/D/E/F
- Deployment target: device / edge / cloud-hybrid
- Model scale and precision:
- Hardware and runtime stack:
- Metrics reported: quality / throughput / TTFT / p95-p99 / J-token / offload ratio
- Security and privacy controls:
- Reproducibility level: E1 / E2 / E3
- Practical takeaway:

建议每篇论文按以上模板记录，便于横向对比与后续复现实验。

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

## Maintenance Rules | 维护规范

1. Add each new paper to one primary category, then cross-link to secondary categories if needed.
2. Keep EN and 中文 content synchronized.
3. Include DOI/arXiv/ACL/OpenReview links whenever available.
4. Avoid single-metric claims without deployment conditions.
5. Record hardware, context length, and decoding settings for all performance statements.

## License | 许可证

Released under the repository LICENSE.

遵循仓库 LICENSE。
