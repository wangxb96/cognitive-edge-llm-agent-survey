# Cognitive Edge Computing Survey: LLMs and AI Agents for Edge Deployment

A concise, professional survey map for deploying large models and AI agents under real edge constraints.

认知边缘计算综述导航：聚焦大模型与智能体在边缘场景中的可部署优化。

## Table of Contents | 目录

1. [Overview | 概述](#overview--概述)
2. [Scope | 范围](#scope--范围)
3. [Visual Snapshot | 图示概览](#visual-snapshot--图示概览)
4. [Taxonomy | 分类框架](#taxonomy--分类框架)
5. [Key Literature by Category | 分类别核心文献](#key-literature-by-category--分类别核心文献)
6. [Recent Highlights (2024-2025) | 近两年重点文献](#recent-highlights-2024-2025--近两年重点文献)
7. [Evaluation Checklist | 评测清单](#evaluation-checklist--评测清单)
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

## Visual Snapshot | 图示概览

The figure below illustrates a central message of the survey: edge deployment is a multi-objective problem, and no single model dominates quality and latency simultaneously.

下图体现了本文综述的一个核心判断：边缘部署本质上是多目标权衡问题，不存在在质量与时延上同时绝对占优的统一模型。

![Latency-quality frontier on edge hardware](assets/latency-quality-frontier.png)

Figure note:
- EN: A synchronized benchmark on a 4x RTX 4090 D server shows that GPT-OSS 20B leads on quality, Llama2 7B remains attractive on latency/efficiency, and Gemma3 4B occupies a balanced region. This is exactly why edge deployment must be analyzed as a trade-off surface rather than a single ranking.
- 中文：在 4x RTX 4090 D 平台上的同步实验表明，GPT-OSS 20B 在质量上更强，Llama2 7B 在时延/效率上仍具吸引力，Gemma3 4B 则处于相对平衡的位置。这说明边缘部署必须以“权衡前沿”而不是“单一排名”来分析。

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

- Shi et al., Edge Computing: Vision and Challenges, IEEE IoT Journal, 2016. Establishes the classic edge-computing problem setting and resource bottlenecks.
- Zhou et al., Edge Intelligence, Proceedings of the IEEE, 2019. Connects AI workloads with edge-side orchestration and service constraints.
- Deng et al., Edge intelligence: The confluence of edge computing and AI, IEEE IoT Journal, 2020. A broader systems survey that helps situate edge AI before the LLM era.
- Vaswani et al., Attention Is All You Need, NeurIPS, 2017. The architectural origin of the transformer family used by modern LLMs.
- Brown et al., Language Models are Few-Shot Learners, NeurIPS, 2020. Marks the scale-driven jump toward general-purpose prompting and in-context learning.
- Wei et al., Emergent Abilities of Large Language Models, TMLR, 2022. Explains why scaling introduces new reasoning behaviors relevant to edge capability preservation.
- Lu et al., Small Language Models: Survey, Measurements, and Insights, 2024. Useful entry point for compact-model design space.
- Zheng et al., A Review on Edge Large Language Models: Design, Execution, and Applications, ACM CSUR, 2025. Closest neighboring review on edge-side LLM deployment.

### B. Deployment Challenges

- Gholami et al., A Survey of Quantization Methods for Efficient Neural Network Inference, 2022. Summarizes the compression toolbox that underpins most edge deployment work.
- Nagel et al., A White Paper on Neural Network Quantization, 2021. Practical reference for quantization failure modes and calibration issues.
- Kwon et al., Efficient Memory Management for LLM Serving with PagedAttention, SOSP, 2023. Shows why serving memory, not just FLOPs, is a first-order deployment bottleneck.
- Murthy et al., MobileAIBench: Benchmarking LLMs/LMMs for On-Device Use Cases, 2024. Provides a modern empirical basis for phone-scale and device-scale evaluation.
- Xiao et al., Understanding Large Language Models in Your Pockets, 2024. Characterizes real on-device performance behavior on commodity mobile hardware.
- Han et al., LLM Multi-Agent Systems: Challenges and Open Problems, 2024. Important for edge deployments where tool-use amplifies cost, latency, and safety risks.
- Carlini et al., Extracting Training Data from Large Language Models, USENIX Security, 2021. Canonical reminder that privacy leakage remains a concrete deployment risk.
- Dwork and Roth, The Algorithmic Foundations of Differential Privacy, 2014. Foundational lens for privacy-preserving edge AI.

### C. Optimization Strategies

- Qin et al., On-device Personalization with Data Selection and Synthesis, DAC, 2024. Represents data-centric optimization rather than model-only optimization.
- Jacob et al., Quantization and Training for Integer-Arithmetic-Only Inference, CVPR, 2018. Early but still influential efficient-inference baseline.
- Frantar et al., GPTQ, ICLR, 2023. One of the most widely adopted post-training quantization methods for LLMs.
- Dettmers et al., QLoRA, NeurIPS, 2023. Key method for efficient adaptation over quantized models.
- Tan et al., MobileQuant, EMNLP Findings, 2024. Explicitly targets mobile/on-device constraints for language models.
- Jeon et al., A Frustratingly Easy Post-Training Quantization Scheme for LLMs, EMNLP, 2023. Strong lightweight baseline for practical PTQ comparisons.
- Lin et al., AWQ, ML Systems, 2024. Activation-aware quantization with strong relevance for deployment.
- Dao, FlashAttention-2, ICLR, 2024. Kernel-level acceleration for attention-dominated inference.
- Li et al., EAGLE-2, EMNLP, 2024. Representative decoding-side acceleration work.
- Zhao et al., QSpec, 2024. Illustrates the interaction between speculative decoding and quantization.
- Tian et al., Edge-Cloud Collaborative Inference (Survey), 2024. Useful when deployment includes selective cloud assistance.
- Zhang et al., EdgeShard, IEEE IoTJ, 2024. A practical example of collaborative edge-side inference.

### D. Agentic Intelligence

- Dorri et al., Multi-agent Systems: A Survey, IEEE Access, 2018. Classical conceptual grounding for agent interaction and coordination.
- Shen et al., HuggingGPT, 2023. Early influential example of tool-augmented agent orchestration.
- Han et al., LLM Multi-Agent Systems, 2024. Surveys key system risks, communication issues, and coordination overheads.
- Yan et al., Communication-Centric Survey of LLM-based Multi-Agent Systems, 2025. Valuable when analyzing communication cost and role design.
- Belcak et al., Small Language Models are the Future of Agentic AI, 2025. Strong argument for SLM-first deployment under practical cost constraints.
- Gao et al., A Survey of Self-Evolving Agents, 2025. Covers adaptive and self-improving agent pipelines.
- Rivkin et al., AIoT Smart Home via Autonomous LLM Agents, 2024. Concrete edge-side agent application case.

### E. Applications

- Abdin et al., Phi-4 Technical Report, 2024. Compact, high-capability model family useful for edge-oriented comparison.
- Team Gemma, Gemma Technical Report, 2024. Widely referenced open-family baseline for deployable inference.
- Mehta et al., OpenELM, 2024. Efficient language model family with explicit design-for-efficiency flavor.
- Marone et al., mmBERT, 2025. Strong multilingual encoder reference for retrieval-heavy edge pipelines.
- Chiu et al., V2V-LLM for Cooperative Autonomous Driving, 2025. Illustrates edge reasoning in vehicular collaboration.
- Hu et al., LLM-based Misbehavior Detection for Connected Autonomous Vehicles, 2025. Shows safety-oriented transport applications.
- Ren et al., Industrial IoT with LLMs, 2024. Example of industrial intelligence under edge and RL constraints.
- Hu et al., Realizing Efficient On-Device Language-Based Image Retrieval, 2024. Demonstrates practical retrieval deployment on constrained devices.

### F. Evaluation and Trust

- Strubell et al., Energy and Policy Considerations for Modern Deep Learning Research, AAAI, 2020. Remains the standard reminder that efficiency must be reported, not assumed.
- Dwork and Roth, The Algorithmic Foundations of Differential Privacy, 2014. Core privacy baseline for any sensitive edge workload.
- Laskaridis et al., Mobile and Edge Evaluation of LLMs, 2024. Useful for benchmarking methodology and realistic deployment framing.
- Murthy et al., MobileAIBench, 2024. Important for cross-model comparative evaluation on device-relevant tasks.
- Oliinyk et al., Fuzzing BusyBox with LLM support, USENIX Security, 2024. Shows that LLM-assisted security tooling is now relevant to embedded environments.
- Ma et al., LLM-assisted fuzzing of IoT device stacks, USENIX Security, 2024. Connects LLM reasoning to IoT vulnerability discovery.
- Gilbert et al., Large Language Model AI Chatbots Require Approval as Medical Devices, Nature Medicine, 2023. Highlights governance implications in regulated domains.

## Recent Highlights (2024-2025) | 近两年重点文献

### Systems and Serving

- PowerInfer-2: fast smartphone LLM inference with stronger practical device orientation (2024).
- EdgeLLM: speculative decoding targeted at fast on-device inference (2024).
- SwapMoE: tunable-memory serving for off-the-shelf MoE models (2024).
- Fast on-device LLM inference with NPUs: highlights the growing importance of mobile accelerator backends (2025).
- Lincoln: pushes very large-model inference closer to consumer-device feasibility (2025).
- Marlin: mixed-precision autoregressive inference optimization for high-throughput serving (2025).

### Collaboration and Routing

- EdgeShard: collaborative edge inference as a systems-level solution to memory and load limits (2024).
- QoS-aware LLM routing with multiple experts: explicit service-quality optimization for edge routing (2025).
- CLONE: latency-aware model customization for edge environments (2025).
- Device-server collaborative text streaming: practical collaborative service design (2025).
- Federated black-box prompt tuning on the edge: collaboration without centralized raw-data exposure (2024).

### Hardware-Aware Acceleration

- Cambricon-LLM: chiplet-based architecture for very large on-device inference (2024).
- PAISE: PIM-accelerated transformer scheduling engine (2025).
- FACIL: SoC-PIM cooperative mapping for on-device LLM inference (2025).
- T-MAC: low-bit CPU-oriented deployment path for edge inference (2025).
- FPGA-based spatial acceleration studies: important for specialized embedded deployments (2024-2025).

### Multimodal and Domain Deployment

- Self-adapting VLMs for edge modalities (2024).
- MiniCPM-V on-phone multimodal model (2024).
- MobileLLM-R1 sub-billion reasoning models (2025).
- VaVLM for edge-cloud video analytics (2025).
- Industrial IoT with LLM-based intelligence (2024).
- AIoT smart home via autonomous LLM agents (2024).
- V2V-LLM and related vehicle-cooperative reasoning systems (2025).

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
