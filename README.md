# Cognitive Edge Computing Survey: LLMs and AI Agents for Edge Deployment

A focused companion to the cognitive-edge version of the survey, covering LLMs and agents under deployment constraints.

**Reading route.** Use the [integrated guide](https://github.com/wangxb96/Awesome-EdgeAI) for the current literature map, figures and public supplement. This repository retains the focused guide and the original benchmark-script snapshots. The [server archive](https://github.com/wangxb96/Awesome-EdgeAI/tree/main/survey/server) provides recovered request data, corrected metric definitions and supported offline recalculation.

认知边缘计算综述导航：聚焦大模型与智能体在边缘场景中的可部署优化。

## Table of Contents | 目录

1. [Overview | 概述](#overview--概述)
2. [Key Takeaways | 核心结论](#key-takeaways--核心结论)
3. [Scope | 范围](#scope--范围)
4. [Visual Snapshot | 图示概览](#visual-snapshot--图示概览)
5. [Taxonomy | 分类框架](#taxonomy--分类框架)
6. [Key Literature by Category | 分类别核心文献](#key-literature-by-category--分类别核心文献)
7. [Recent Highlights (2024-2025) | 近两年重点文献](#recent-highlights-2024-2025--近两年重点文献)
8. [Evaluation Checklist | 评测清单](#evaluation-checklist--评测清单)
9. [Citation | 引用信息](#citation--引用信息)
10. [License | 许可证](#license--许可证)

## Overview | 概述

### EN

This repository organizes the literature of Cognitive Edge Computing for LLMs and AI Agents into a practical taxonomy.
The focus is deployment realism at the edge: reasoning quality, latency stability, energy efficiency, and security/privacy under resource-constrained environments.

### 中文

本仓库将认知边缘计算相关文献按可部署视角进行结构化整理。
重点不是单一指标提升，而是在边缘资源约束下同时兼顾推理质量、时延稳定、能耗效率与安全隐私。

## Key Takeaways | 核心结论

- Deployment should be evaluated on a multi-objective frontier: quality, latency, and energy must be reported together rather than with a single metric.
- Edge success is increasingly decided by system-level co-design: model compression, runtime scheduling, and memory orchestration are tightly coupled.
- Agentic edge AI is feasible but cost-sensitive: communication topology and routing policy often dominate end-to-end latency.
- Hardware-aware optimization is no longer optional: NPUs, PIM, FPGA, and low-bit CPU paths have become first-class deployment strategies.
- Trust and reproducibility are mandatory for deployment claims: privacy/security assumptions and benchmark protocols should be explicit.

- 边缘部署应按多目标前沿评估：质量、时延、能耗需联合报告，而非单一指标排名。
- 边缘性能越来越取决于系统级协同设计：模型压缩、运行时调度与内存管理必须联动优化。
- 智能体化边缘 AI 可行但对成本敏感：通信拓扑与路由策略常决定端到端时延。
- 硬件感知优化已成为刚需：NPU、PIM、FPGA 与低比特 CPU 路径正在成为一线部署方案。
- 可信与可复现是部署结论成立的前提：隐私/安全假设与评测协议需要显式声明。

## Scope | 范围

- Models: LLM, SLM, multimodal language models, MoE variants
- Systems: on-device inference, edge serving, optional cloud collaboration, agent tool-use loops
- Objectives: quality-preserving optimization, efficient serving, trustworthy deployment

## Reproducibility Artifacts | 可复现材料

| Material | Location and use |
|---|---|
| Current supplement | [PDF and source](https://github.com/wangxb96/Awesome-EdgeAI/tree/main/survey/supplement), including the historical server record and its limits |
| Recovered empirical data | [Server archive and offline analysis](https://github.com/wangxb96/Awesome-EdgeAI/tree/main/survey/server), with thirteen campaigns, tasks, failures and descriptive reanalysis |
| Figure sources | [Editable catalogue](https://github.com/wangxb96/Awesome-EdgeAI/tree/main/survey/figures), with source inputs and vector exports |
| Original script snapshots | [Runner](assets/reproducibility/scripts/run_ollama_server_suite.py), [selector](assets/reproducibility/scripts/rebuild_clean_server_artifacts.py), [plotter](assets/reproducibility/scripts/plot_benchmark_results.py); these assume the earlier project layout |

For supported offline recalculation, clone the integrated repository and run:

```sh
git clone --branch supplement-2026-11-13-v4 https://github.com/wangxb96/Awesome-EdgeAI.git
cd Awesome-EdgeAI
python3 survey/server/analyze_archived.py
```

This recalculates the archived records without invoking a model. Exact historical checkpoint/template, precision, runtime/driver/placement and complete power/response traces were not retained. Script defaults do not establish execution-time settings, so this is not identical experimental re-execution.

原始脚本用于追溯评分、请求计时、功耗代理和旧版结果选择逻辑。可离线复算的数据及入口位于上表所列的当前公开归档。四卡 RTX 4090 D 的历史记录不能直接验证移动端性能，回答包含分数也不能解释为模型推理能力排名。

## Visual Snapshot | 图示概览

![Task and resource loops in cognitive edge computing](https://raw.githubusercontent.com/wangxb96/Awesome-EdgeAI/supplement-2026-11-13-v4/survey/figures/cognitive_edge_overview.png)

The conceptual figure connects task acceptance, context/reasoning/action and resource adaptation across device, edge and cloud. It encodes no measured performance. The [source and vector exports](https://github.com/wangxb96/Awesome-EdgeAI/tree/supplement-2026-11-13-v4/survey/figures) are public.

概念图展示任务与资源调整的闭环，图形位置不表示实验性能。历史服务器观测应结合[重分析与测量边界](https://github.com/wangxb96/Awesome-EdgeAI/tree/supplement-2026-11-13-v4/survey/server)阅读，不能据此作跨硬件的能力排名。

## Taxonomy | 分类框架

| Category | Focus (EN) | 中文重点 |
|---|---|---|
| A. Foundations | edge intelligence and LLM fundamentals | 边缘智能与大模型基础 |
| B. Deployment Challenges | compute/memory/latency/security bottlenecks | 算力内存时延与安全瓶颈 |
| C. Optimization Strategies | data/model/runtime/system co-optimization | 数据/模型/运行时/系统协同优化 |
| D. Agentic Intelligence | planning, tool-use, multi-agent collaboration | 规划、工具调用、多智能体协同 |
| E. Applications | mobility, healthcare, industrial edge AI | 车联网、医疗、工业边缘应用 |
| F. Evaluation & Trust | reproducibility, metrics, governance | 可复现评测与可信治理 |

```mermaid
flowchart TD
  A[Foundations<br/>边缘智能与大模型基础] --> B[Deployment Challenges<br/>资源 时延 安全 瓶颈]
  B --> C[Optimization Strategies<br/>数据 模型 运行时 系统协同]
  C --> D[Agentic Intelligence<br/>规划 工具调用 多智能体]
  C --> E[Applications<br/>车联网 医疗 工业边缘]
  D --> E
  E --> F[Evaluation and Trust<br/>质量 时延 能耗 可信治理]
  F --> C
```

Diagram note:
- EN: This condensed framework follows the paper's logic: challenges drive optimization, optimization enables agentic and domain deployment, and evaluation closes the loop.
- 中文：这个简化框架遵循论文主线：挑战驱动优化，优化支撑智能体与应用落地，评测再反向约束设计。

## Key Literature by Category | 分类别核心文献

The list below emphasizes representative papers that help readers quickly understand what each category contributes to edge deployment research.

下列文献优先选择具有代表性的工作，用于帮助读者快速把握各类别对边缘部署研究分别解决了什么问题。

Direct links are added where a stable publisher page or arXiv record is available.

在存在稳定出版社页面或 arXiv 记录时，下面条目补充了直达链接。

### A. Foundations

- Shi et al., [Edge Computing: Vision and Challenges](https://doi.org/10.1109/jiot.2016.2579198), IEEE IoT Journal, 2016. Defines the classical edge-computing setting and the resource bottlenecks inherited by later LLM systems.
- Zhou et al., [Edge Intelligence: Paving the Last Mile of Artificial Intelligence with Edge Computing](https://doi.org/10.1109/jproc.2019.2918951), Proceedings of the IEEE, 2019. Frames AI-at-the-edge as a joint problem of orchestration, service quality, and distributed resource management.
- Deng et al., [Edge intelligence: The confluence of edge computing and artificial intelligence](https://doi.org/10.1109/jiot.2020.2984887), IEEE IoT Journal, 2020. Provides the broader pre-LLM systems context needed to understand why edge intelligence evolved toward cognitive edge computing.
- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), NeurIPS, 2017. Supplies the transformer foundation on which most deployable language models are built.
- Brown et al., [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165), NeurIPS, 2020. Establishes scale-driven in-context learning as the capability target that edge deployment tries to preserve.
- Wei et al., [Emergent Abilities of Large Language Models](https://arxiv.org/abs/2206.07682), TMLR, 2022. Explains why scaling changes model behavior and why compression must protect more than perplexity alone.
- Lu et al., [Small Language Models: Survey, Measurements, and Insights](https://arxiv.org/abs/2409.15790), arXiv, 2024. Maps the compact-model design space that is most relevant to realistic edge deployment.
- Zheng et al., [A Review on Edge Large Language Models: Design, Execution, and Applications](https://doi.org/10.1145/3719664), ACM CSUR, 2025. Serves as the closest neighboring review focused specifically on edge-side LLM execution.

### B. Deployment Challenges

- Gholami et al., [A Survey of Quantization Methods for Efficient Neural Network Inference](https://arxiv.org/abs/2103.13630), arXiv, 2022. Summarizes the compression toolbox that underlies most practical edge-model reduction pipelines.
- Nagel et al., [A White Paper on Neural Network Quantization](https://arxiv.org/abs/2106.08295), arXiv, 2021. Clarifies calibration errors, accuracy collapse, and other quantization failure modes faced in deployment.
- Kwon et al., [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://doi.org/10.1145/3600006.3613165), SOSP, 2023. Demonstrates that serving memory and KV-cache behavior are first-order bottlenecks, not secondary implementation details.
- Murthy et al., [MobileAIBench: Benchmarking LLMs/LMMs for On-Device Use Cases](https://arxiv.org/abs/2406.10290), arXiv, 2024. Provides a device-relevant benchmark basis for assessing realistic mobile and on-device workloads.
- Xiao et al., [Understanding Large Language Models in Your Pockets: Performance Study on COTS Mobile Devices](https://arxiv.org/abs/2410.03613), arXiv, 2024. Characterizes the actual runtime behavior of pocket-scale inference on commodity mobile platforms.
- Han et al., [LLM Multi-Agent Systems: Challenges and Open Problems](https://arxiv.org/abs/2402.03578), arXiv, 2024. Highlights how planning, communication, and tool-use loops amplify latency, cost, and safety pressure at the edge.
- Carlini et al., [Extracting Training Data from Large Language Models](https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-extracting), USENIX Security, 2021. Anchors the privacy-leakage threat model that remains relevant for sensitive edge workloads.
- Dwork and Roth, [The Algorithmic Foundations of Differential Privacy](https://doi.org/10.1561/0400000042), 2014. Provides the formal privacy framework most often used when edge AI must satisfy data minimization requirements.

### C. Optimization Strategies

- Qin et al., [Enabling On-Device Large Language Model Personalization with Self-Supervised Data Selection and Synthesis](https://doi.org/10.1145/3649329.3655665), DAC, 2024. Represents the data-centric path, showing that deployment quality can be improved without relying only on larger models.
- Jacob et al., [Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference](https://doi.org/10.1109/CVPR.2018.00060), CVPR, 2018. Supplies an early efficient-inference baseline that still informs integer-oriented deployment practice.
- Frantar et al., [GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers](https://arxiv.org/abs/2210.17323), ICLR, 2023. Became a standard post-training quantization reference for preserving LLM quality under aggressive compression.
- Dettmers et al., [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314), NeurIPS, 2023. Shows how efficient fine-tuning can be layered on top of quantized models rather than replacing them.
- Tan et al., [MobileQuant: Mobile-friendly Quantization for On-device Language Models](https://doi.org/10.18653/v1/2024.findings-emnlp.570), EMNLP Findings, 2024. Targets mobile-specific constraints and therefore connects compression decisions with actual device behavior.
- Jeon et al., [A Frustratingly Easy Post-Training Quantization Scheme for LLMs](https://doi.org/10.18653/v1/2023.emnlp-main.892), EMNLP, 2023. Provides a strong lightweight PTQ baseline for practical comparisons.
- Lin et al., [AWQ: Activation-aware Weight Quantization for On-device LLM Compression and Acceleration](https://arxiv.org/abs/2306.00978), ML Systems, 2024. Uses activation-aware quantization to improve the quality-efficiency balance relevant to deployment.
- Dao, [FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning](https://arxiv.org/abs/2307.08691), ICLR, 2024. Represents kernel-level acceleration for attention-dominated inference paths.
- Li et al., [EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees](https://doi.org/10.18653/v1/2024.emnlp-main.422), EMNLP, 2024. Illustrates decoding-side acceleration where the latency gains come from generation strategy, not only from compression.
- Zhao et al., [QSpec: Speculative Decoding with Complementary Quantization Schemes](https://arxiv.org/abs/2410.11305), arXiv, 2024. Highlights the interaction between speculative decoding and quantized execution.
- Tian et al., [An Edge-Cloud Collaboration Framework for Generative AI Service Provision with Synergetic Big Cloud Model and Small Edge Models](https://doi.org/10.1109/mnet.2024.3420755), IEEE Network, 2024. Summarizes how selective cloud assistance can be integrated when pure local execution is insufficient.
- Zhang et al., [EdgeShard: Efficient LLM Inference via Collaborative Edge Computing](https://doi.org/10.1109/jiot.2024.3524255), IEEE IoTJ, 2024. Gives a concrete systems example of collaborative inference across edge resources.

### D. Agentic Intelligence

- Dorri et al., [Multi-agent Systems: A Survey](https://doi.org/10.1109/access.2018.2831228), IEEE Access, 2018. Provides the classical coordination vocabulary behind later LLM-agent interaction patterns.
- Shen et al., [HuggingGPT: Solving AI Tasks with ChatGPT and Its Friends in Hugging Face](https://arxiv.org/abs/2303.17580), NeurIPS, 2023. Offers an early influential example of tool-augmented orchestration rather than single-model prompting.
- Han et al., [LLM Multi-Agent Systems: Challenges and Open Problems](https://arxiv.org/abs/2402.03578), arXiv, 2024. Summarizes the major system risks, communication overheads, and coordination costs introduced by multi-agent designs.
- Yan et al., [Beyond Self-Talk: A Communication-Centric Survey of LLM-based Multi-Agent Systems](https://arxiv.org/abs/2502.14321), arXiv, 2025. Is especially useful for edge settings where communication cost and message topology directly affect feasibility.
- Belcak et al., [Small Language Models are the Future of Agentic AI](https://arxiv.org/abs/2506.02153), arXiv, 2025. Makes the practical case that SLM-first agents are often better aligned with deployment constraints.
- Gao et al., [A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence](https://arxiv.org/abs/2507.21046), arXiv, 2025. Covers adaptive agent pipelines where policies and behaviors continue to improve after initial deployment.
- Rivkin et al., [AIoT Smart Home via Autonomous LLM Agents](https://doi.org/10.1109/jiot.2024.3471904), IEEE Internet of Things Journal, 2024. Grounds the agent discussion in a concrete edge-resident smart-home case.

### E. Applications

- Abdin et al., [Phi-4 Technical Report](https://arxiv.org/abs/2412.08905), arXiv, 2024. Represents compact but capable model design that is directly relevant to edge-side comparison.
- Team Gemma, [Gemma: Open Models Based on Gemini Research and Technology](https://arxiv.org/abs/2403.08295), arXiv, 2024. Serves as a widely adopted open baseline for deployable language inference.
- Mehta et al., [OpenELM: An Efficient Language Model Family with Open Training and Inference Framework](https://arxiv.org/abs/2404.14619), ICML ES-FoMo Workshop, 2024. Emphasizes efficiency-aware model design instead of treating compression as an afterthought.
- Marone et al., [mmBERT: A Modern Multilingual Encoder with Annealed Language Learning](https://arxiv.org/abs/2509.06888), arXiv, 2025. Provides a multilingual encoder reference for retrieval-heavy pipelines that may run near the data source.
- Chiu et al., [V2V-LLM: Vehicle-to-Vehicle Cooperative Autonomous Driving with Multi-Modal Large Language Models](https://arxiv.org/abs/2502.09980), arXiv, 2025. Illustrates cooperative vehicular reasoning where edge latency and coordination both matter.
- Hu et al., [LLM-based Misbehavior Detection Architecture for Enhanced Traffic Safety in Connected Autonomous Vehicles](https://doi.org/10.1109/tvt.2025.3551327), IEEE Transactions on Vehicular Technology, 2025. Shows how edge intelligence is used for safety-sensitive transport monitoring.
- Ren et al., [Industrial Internet of Things with Large Language Models (LLMs): an Intelligence-based Reinforcement Learning Approach](https://doi.org/10.1109/tmc.2024.3522130), IEEE Transactions on Mobile Computing, 2024. Extends the discussion into industrial environments with stronger reliability and control constraints.
- Hu et al., [Realizing Efficient On-Device Language-Based Image Retrieval](https://doi.org/10.1145/3649896), ACM TOMM, 2024. Demonstrates a concrete multimodal retrieval workload that fits constrained devices.

### F. Evaluation and Trust

- Strubell et al., [Energy and Policy Considerations for Modern Deep Learning Research](https://doi.org/10.1609/aaai.v34i09.7123), AAAI, 2020. Reminds the field that efficiency and environmental cost must be reported rather than left implicit.
- Dwork and Roth, [The Algorithmic Foundations of Differential Privacy](https://doi.org/10.1561/0400000042), FnT TCS, 2014. Remains the core privacy baseline for sensitive edge workloads.
- Laskaridis et al., [Mobile and Edge Evaluation of Large Language Models](https://doi.org/10.36227/techrxiv.172115025.57884352/v1), TechRxiv / ICML ES-FoMo Workshop, 2024. Helps define realistic benchmarking methodology for edge-oriented model comparison.
- Murthy et al., [MobileAIBench: Benchmarking LLMs/LMMs for On-Device Use Cases](https://arxiv.org/abs/2406.10290), arXiv, 2024. Supports cross-model evaluation on tasks and devices closer to actual deployment practice.
- Oliinyk et al., [Fuzzing BusyBox: Leveraging LLM and Crash Reuse for Embedded Bug Unearthing](https://www.usenix.org/conference/usenixsecurity24/presentation/asmita), USENIX Security, 2024. Shows that LLM-assisted security tooling is now relevant to embedded software stacks.
- Ma et al., [From One Thousand Pages of Specification to Unveiling Hidden Bugs: Large Language Model Assisted Fuzzing of Matter IoT Devices](https://www.usenix.org/conference/usenixsecurity24/presentation/ma-xiaoyue), USENIX Security, 2024. Connects model-assisted reasoning with concrete IoT vulnerability discovery workflows.
- Gilbert et al., [Large Language Model AI Chatbots Require Approval as Medical Devices](https://doi.org/10.1038/s41591-023-02412-6), Nature Medicine, 2023. Highlights the governance and regulatory implications of deploying language systems in sensitive domains.

## Recent Highlights (2024-2025) | 近两年重点文献

Tag legend: `[System]` serving/runtime, `[Routing]` collaboration/policy, `[Hardware]` accelerator/memory mapping, `[Application]` domain deployment.

标签说明：`[System]` 表示服务与运行时，`[Routing]` 表示协同与路由策略，`[Hardware]` 表示硬件/内存映射优化，`[Application]` 表示场景化落地。

### Systems and Serving

This line of work pushes edge deployment from proof-of-concept execution toward practical serving stacks that optimize startup cost, generation latency, memory footprint, and accelerator utilization together.

这一方向的研究正把边缘部署从“能跑起来”推进到“可稳定服务”，重点同时优化启动开销、生成时延、显存占用与硬件利用率。

- [System] [PowerInfer-2: Fast Large Language Model Inference on a Smartphone](https://arxiv.org/abs/2406.06282). arXiv, 2024. A strong reference for phone-class large-model execution.
- [System] [EdgeLLM: Fast On-Device LLM Inference with Speculative Decoding](https://doi.org/10.1109/tmc.2024.3513457). IEEE Transactions on Mobile Computing, 2024. Shows how decoding policy directly changes on-device latency.
- [System] [SwapMoE: Serving Off-the-shelf MoE-based Large Language Models with Tunable Memory Budget](https://doi.org/10.18653/v1/2024.acl-long.363). ACL, 2024. Highlights memory-budget-aware serving for sparse expert models.
- [Hardware] [Fast On-Device LLM Inference with NPUs](https://doi.org/10.1145/3669940.3707239). ASPLOS, 2025. Demonstrates the growing importance of mobile accelerator backends.
- [Hardware] [Lincoln: Real-Time 50-100B LLM Inference on Consumer Devices with LPDDR-Interfaced, Compute-Enabled Flash Memory](https://doi.org/10.1109/hpca61900.2025.00128). HPCA, 2025. Pushes very large-model inference closer to consumer-device feasibility.
- [System] [Marlin: Mixed-precision Auto-regressive Parallel Inference on Large Language Models](https://doi.org/10.1145/3710848.3710871). PPoPP, 2025. Optimizes high-throughput serving through mixed-precision generation.

### Collaboration and Routing

Recent collaboration work treats routing as a first-class control problem: deciding when to stay local, when to shard, and when to escalate to a stronger remote model under latency and quality constraints.

近期协同研究把路由本身视为一类核心控制问题，即在时延与质量约束下，决定何时本地执行、何时边缘分片、何时升级到更强的远端模型。

- [Routing] [EdgeShard: Efficient LLM Inference via Collaborative Edge Computing](https://doi.org/10.1109/jiot.2024.3524255). IEEE Internet of Things Journal, 2024. Frames collaboration as a systems-level response to memory and load limits.
- [Routing] [Quality-of-Service Aware LLM Routing for Edge Computing with Multiple Experts](https://doi.org/10.1109/tmc.2025.3590969). IEEE Transactions on Mobile Computing, 2025. Treats routing as an explicit service-quality optimization problem.
- [Routing] [CLONE: Customizing LLMs for Efficient Latency-Aware Inference at the Edge](https://arxiv.org/abs/2506.02847). arXiv, 2025. Connects edge adaptation with latency-aware customization.
- [Routing] [DiSCo: Device-Server Collaborative LLM-Based Text Streaming Services](https://arxiv.org/abs/2502.11417). arXiv, 2025. Provides a concrete collaborative service architecture for streaming outputs.
- [Routing] [Federated Black-box Prompt Tuning System for Large Language Models on the Edge](https://doi.org/10.1145/3636534.3698856). MobiCom, 2024. Shows how collaboration can happen without centralizing raw private data.

### Hardware-Aware Acceleration

Hardware-aware studies make it clear that edge LLM progress is not only algorithmic; deployment quality increasingly depends on how models are mapped onto NPUs, PIM, FPGA, and low-bit CPU backends.

硬件感知方向说明，边缘大模型进展并不只是算法改进，部署效果越来越取决于模型如何映射到 NPU、PIM、FPGA 与低比特 CPU 后端。

- [Hardware] [Cambricon-LLM: A Chiplet-based Hybrid Architecture for On-Device Inference of 70B LLM](https://doi.org/10.1109/micro61859.2024.00108). MICRO, 2024. Explores hardware architecture support for very large on-device models.
- [Hardware] [PAISE: PIM-Accelerated Inference Scheduling Engine for Transformer-based LLM](https://doi.org/10.1109/hpca61900.2025.00126). HPCA, 2025. Pushes scheduling intelligence into the memory-centric acceleration path.
- [Hardware] [FACIL: Flexible DRAM Address Mapping for SoC-PIM Cooperative On-device LLM Inference](https://doi.org/10.1109/hpca61900.2025.00127). HPCA, 2025. Focuses on memory mapping and SoC-PIM cooperation.
- [Hardware] [T-MAC: CPU Renaissance via Table Lookup for Low-bit LLM Deployment on Edge](https://doi.org/10.1145/3689031.3696099). EuroSys, 2025. Reopens the low-bit CPU deployment path for edge inference.
- [Hardware] [Understanding the Potential of FPGA-based Spatial Acceleration for Large Language Model Inference](https://doi.org/10.1145/3656177). ACM TRETS, 2024, and [Pushing up to the Limit of Memory Bandwidth and Capacity Utilization for Efficient LLM Decoding on Embedded FPGA](https://doi.org/10.23919/date64628.2025.10993087). DATE, 2025. Together they frame FPGA deployment as a specialized but increasingly relevant embedded path.

### Multimodal and Domain Deployment

The most visible application trend is that edge intelligence is moving beyond text-only assistants into multimodal perception, smart-home coordination, industrial control, and cooperative mobility.

最明显的应用趋势是，边缘智能正在从纯文本助手扩展到多模态感知、智能家居协同、工业控制与协同交通等场景。

- [Application] [Self-adapting Large Visual-Language Models to Edge Devices Across Visual Modalities](https://doi.org/10.1007/978-3-031-73390-1_18). ECCV, 2024. Demonstrates modality-aware VLM adaptation for edge conditions.
- [Application] [MiniCPM-V: A GPT-4V Level MLLM on Your Phone](https://arxiv.org/abs/2408.01800). arXiv, 2024. A notable on-phone multimodal deployment reference.
- [Application] [MobileLLM-R1: Exploring the Limits of Sub-Billion Language Model Reasoners with Open Training Recipes](https://arxiv.org/abs/2509.24945). arXiv, 2025. Pushes compact reasoning models into the practical edge range.
- [Application] [VaVLM: Toward Efficient Edge-Cloud Video Analytics With Vision-Language Models](https://doi.org/10.1109/tbc.2025.3549983). IEEE Transactions on Broadcasting, 2025. Extends the survey toward video analytics with edge-cloud cooperation.
- [Application] [Industrial Internet of Things with Large Language Models (LLMs): an Intelligence-based Reinforcement Learning Approach](https://doi.org/10.1109/tmc.2024.3522130). IEEE Transactions on Mobile Computing, 2024. Grounds the industrial edge case with stronger reliability constraints.
- [Application] [AIoT Smart Home via Autonomous LLM Agents](https://doi.org/10.1109/jiot.2024.3471904). IEEE Internet of Things Journal, 2024. Shows autonomous agents embedded in smart-home control loops.
- [Application] [V2V-LLM: Vehicle-to-Vehicle Cooperative Autonomous Driving with Multi-Modal Large Language Models](https://arxiv.org/abs/2502.09980). arXiv, 2025. Represents cooperative mobility and vehicular reasoning at the edge.

## Evaluation Checklist | 评测清单

Recommended minimum report for each study:

- Quality: accuracy/task success/reasoning fidelity
- Performance: throughput, TTFT, p95/p99 latency
- Efficiency: memory footprint, energy per token
- Deployment: on-device ratio, optional offload ratio (when cloud collaboration is enabled)
- Reliability: long-run stability, retry/failure rate
- Trust: privacy/security mechanism and threat assumptions

## Citation | 引用信息

The two records are versions of the same arXiv manuscript. Cite the version used; v1 is the initial data/model/system preprint, and v2 introduces the cognitive-edge framing.

两条记录属于同一篇预印本的不同版本，引用时请注明实际使用的版本。

```bibtex
@article{wang2025optimizing_v1,
  title={Optimizing Edge AI: A Comprehensive Survey on Data, Model, and System Strategies},
  author={Wang, Xubin and Jia, Weijia},
  journal={arXiv preprint arXiv:2501.03265v1},
  year={2025},
  note={Version 1, January 4, 2025},
  url={https://arxiv.org/abs/2501.03265v1}
}

@article{wang2025cognitive_v2,
  title={Cognitive Edge Computing: A Comprehensive Survey on Optimizing Large Models and AI Agents for Pervasive Deployment},
  author={Wang, Xubin and Li, Qing and Jia, Weijia},
  journal={arXiv preprint arXiv:2501.03265v2},
  year={2025},
  note={Version 2, November 7, 2025},
  url={https://arxiv.org/abs/2501.03265v2}
}
```

Version repositories: [data/model/system guide](https://github.com/wangxb96/Awesome-EdgeAI) · [cognitive-edge focused guide](https://github.com/wangxb96/cognitive-edge-llm-agent-survey).

## License | 许可证

Released under the repository LICENSE.
