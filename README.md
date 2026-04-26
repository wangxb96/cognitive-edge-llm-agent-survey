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
10. [Curated Paper Index (Normalized Format) | 统一格式论文索引](#curated-paper-index-normalized-format--统一格式论文索引)
11. [Extended Coverage: Additional 52 Manuscript References | 扩展覆盖：来自主稿的 52 条补充文献](#extended-coverage-additional-52-manuscript-references--扩展覆盖来自主稿的-52-条补充文献)
12. [New Literature Batch-II (2024-2025): 30 Additional Papers | 新文献批次II（2024-2025）：新增30篇](#new-literature-batch-ii-2024-2025-30-additional-papers--新文献批次ii2024-2025新增30篇)
13. [New Literature Batch-III (Curated, Edge-First): 27 Additional Papers | 新文献批次III（精选，边缘优先）：新增27篇](#new-literature-batch-iii-curated-edge-first-27-additional-papers--新文献批次iii精选边缘优先新增27篇)
14. [Authenticity Ledger for Batch-II/III | 批次II/III真实性台账](#authenticity-ledger-for-batch-iiiii--批次iiiii真实性台账)
15. [Timeline by Year | 按年份时间线](#timeline-by-year--按年份时间线)
16. [Task-Oriented Retrieval Matrix | 按任务维度检索矩阵](#task-oriented-retrieval-matrix--按任务维度检索矩阵)
17. [Journal/Conference Target Mapping | 投稿方向映射](#journalconference-target-mapping--投稿方向映射)
18. [Survey Delta vs Related Repositories and Surveys | 与相关综述的差异化](#survey-delta-vs-related-repositories-and-surveys--与相关综述的差异化)
19. [Recommended Reporting Template | 推荐报告模板](#recommended-reporting-template--推荐报告模板)
20. [Citation | 引用信息](#citation--引用信息)
21. [Maintenance Rules | 维护规范](#maintenance-rules--维护规范)
22. [License | 许可证](#license--许可证)

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

## Curated Paper Index (Normalized Format) | 统一格式论文索引

Format:
- `[ID] [BibKey] Author (Year). Title. Venue. Link. One-line contribution.`
- 统一格式: `[编号] [BibKey] 作者(年份). 标题. 会议/期刊. 链接. 一句话贡献.`

### A. Foundations

- [A-01] `shi2016edge` Shi et al. (2016). Edge Computing: Vision and Challenges. IEEE IoTJ. https://doi.org/10.1109/JIOT.2016.2579198. Early edge-computing problem formulation.
- [A-02] `zhou2019edge` Zhou et al. (2019). Edge Intelligence. Proceedings of the IEEE. https://doi.org/10.1109/JPROC.2019.2918951. Defines edge intelligence architecture and trade-offs.
- [A-03] `deng2020edge` Deng et al. (2020). Edge Intelligence Confluence Survey. IEEE IoTJ. https://doi.org/10.1109/JIOT.2020.3007838. Consolidates edge+AI system evolution.
- [A-04] `vaswani2017attention` Vaswani et al. (2017). Attention Is All You Need. NeurIPS. https://arxiv.org/abs/1706.03762. Transformer foundation.
- [A-05] `brown2020language` Brown et al. (2020). Language Models are Few-Shot Learners. NeurIPS. https://arxiv.org/abs/2005.14165. In-context learning at scale.
- [A-06] `wei2022emergent` Wei et al. (2022). Emergent Abilities of LLMs. TMLR. https://arxiv.org/abs/2206.07682. Emergence behavior under scale.

### B. Challenges

- [B-01] `gholami2022survey` Gholami et al. (2022). Quantization Survey. Low-power Computer Vision. https://arxiv.org/abs/2103.13630. Efficiency bottlenecks and quantization taxonomy.
- [B-02] `nagel2021white` Nagel et al. (2021). White Paper on Neural Network Quantization. arXiv. https://arxiv.org/abs/2106.08295. Practical quantization caveats.
- [B-03] `kwon2023efficient` Kwon et al. (2023). PagedAttention. SOSP. https://doi.org/10.1145/3600006.3613165. Memory management for serving stability.
- [B-04] `murthy2024mobileaibench` Murthy et al. (2024). MobileAIBench. arXiv. https://arxiv.org/abs/2406.10290. On-device benchmarking baseline.
- [B-05] `han2024llm` Han et al. (2024). LLM Multi-Agent Systems. arXiv. https://arxiv.org/abs/2402.03578. Agent risks and open problems.

### C. Optimization

- [C-01] `qin2024enabling` Qin et al. (2024). On-device Personalization with Data Selection/Synthesis. DAC. Data-centric personalization pipeline.
- [C-02] `jacob2018quantization` Jacob et al. (2018). Integer-Arithmetic-Only Inference. CVPR. https://doi.org/10.1109/CVPR.2018.00287. Foundational quantization method.
- [C-03] `frantar2023gptq` Frantar et al. (2023). GPTQ. ICLR. https://arxiv.org/abs/2210.17323. Post-training quantization for LLMs.
- [C-04] `qlora2023` Dettmers et al. (2023). QLoRA. NeurIPS. Adapter tuning over quantized models.
- [C-05] `tan2024mobilequant` Tan et al. (2024). MobileQuant. EMNLP Findings. Mobile-friendly quantization strategy.
- [C-06] `dao2024flashattention` Dao (2024). FlashAttention-2. ICLR. https://arxiv.org/abs/2307.08691. Faster attention kernels.
- [C-07] `li2024eagle` Li et al. (2024). EAGLE-2. EMNLP. https://aclanthology.org/2024.emnlp-main.422/. Dynamic draft-tree acceleration.
- [C-08] `zhao2024qspec` Zhao et al. (2024). QSpec. arXiv. https://arxiv.org/abs/2410.11305. Quantization + speculative decoding.
- [C-09] `tian2024edge` Tian et al. (2024). Edge-Cloud Collaborative Inference Survey. arXiv. Systematic routing and collaboration synthesis.

### D. Agentic Intelligence

- [D-01] `shen2023hugginggpt` Shen et al. (2023). HuggingGPT. arXiv. https://arxiv.org/abs/2303.17580. Tool-augmented agent architecture.
- [D-02] `yan2025beyond` Yan et al. (2025). Beyond Self-Talk. arXiv. https://arxiv.org/abs/2502.14321. Communication-centric MAS analysis.
- [D-03] `belcak2025small` Belcak et al. (2025). SLMs are the Future of Agentic AI. arXiv. https://arxiv.org/abs/2506.02153. Small-model-first agent argument.
- [D-04] `gao2025survey` Gao et al. (2025). Self-evolving Agents Survey. arXiv. https://arxiv.org/abs/2507.21046. Evolutionary agent mechanisms.

### E/F. Applications, Evaluation, Security

- [E-01] `abdin2024phi` Abdin et al. (2024). Phi-4 Technical Report. arXiv. Compact high-capability model family.
- [E-02] `team2024gemma` Team Gemma (2024). Gemma Technical Report. arXiv. https://arxiv.org/abs/2403.08295. Open model stack for practical deployment.
- [E-03] `mehtaopenelm` Mehta et al. (2024). OpenELM. ICML Workshop. Efficient open model design.
- [E-04] `marone2025mmbert` Marone et al. (2025). mmBERT. arXiv. https://arxiv.org/abs/2509.06888. Efficient multilingual encoder for retrieval.
- [F-01] `strubell2020energy` Strubell et al. (2020). Energy and Policy Considerations. AAAI. https://doi.org/10.1609/aaai.v34i09.7123. Energy-aware reporting perspective.
- [F-02] `dwork2014algorithmic` Dwork and Roth (2014). Differential Privacy Foundations. FnT TCS. https://doi.org/10.1561/0400000042. Formal privacy baseline.

## Extended Coverage: Additional 52 Manuscript References | 扩展覆盖：来自主稿的 52 条补充文献

This section expands coverage using bibkey-verified entries from the manuscript bibliography.

本节基于主稿 `references.bib` 自动抽取并人工校核的条目，进一步提升覆盖度。

| ID | Theme | BibKey | Year | Title | Venue |
|---|---|---|---|---|---|
| X-01 | Runtime & Serving | `alizadeh2024llm` | 2024 | Llm in a flash: Efficient large language model inference with limited memory | Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) |
| X-02 | Model Optimization | `jeon2023frustratingly` | 2023 | A frustratingly easy post-training quantization scheme for llms | Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing |
| X-03 | Model Optimization | `edalati2022kronecker` | 2022 | Kronecker Decomposition for GPT Compression | Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers) |
| X-04 | Model Optimization | `bai2022towards` | 2022 | Towards efficient post-training quantization of pre-trained language models | Advances in neural information processing systems |
| X-05 | Model Optimization | `guan2024aptq` | 2024 | Aptq: Attention-aware post-training mixed-precision quantization for large language models | Proceedings of the 61st ACM/IEEE Design Automation Conference |
| X-06 | Model Optimization | `lin2024awq` | 2024 | Awq: Activation-aware weight quantization for on-device llm compression and acceleration | Proceedings of machine learning and systems |
| X-07 | Model Optimization | `frantar2023sparsegpt` | 2023 | Sparsegpt: Massive language models can be accurately pruned in one-shot | International conference on machine learning |
| X-08 | Model Optimization | `qlora2023` | 2023 | Qlora: Efficient finetuning of quantized llms | Advances in neural information processing systems |
| X-09 | Applications & Benchmarks | `gloeckle2024better` | 2024 | Better \& Faster Large Language Models via Multi-token Prediction | International Conference on Machine Learning |
| X-10 | Runtime & Serving | `zhao2025fr` | 2025 | Fr-spec: Accelerating large-vocabulary language models via frequency-ranked speculative sampling | arXiv preprint arXiv:2502.14856 |
| X-11 | Model Optimization | `zhao2024qspec` | 2024 | Qspec: Speculative decoding with complementary quantization schemes | arXiv preprint arXiv:2410.11305 |
| X-12 | Model Optimization | `zhang2025speculative` | 2025 | Speculative decoding meets quantization: Compatibility evaluation and hierarchical framework design | arXiv preprint arXiv:2505.22179 |
| X-13 | Runtime & Serving | `sheng2023flexgen` | 2023 | Flexgen: High-throughput generative inference of large language models with a single gpu | International Conference on Machine Learning |
| X-14 | Runtime & Serving | `zheng2024sglang` | 2024 | Sglang: Efficient execution of structured language model programs | Advances in neural information processing systems |
| X-15 | Runtime & Serving | `cai2024llmaas` | 2024 | LLMaaS: Serving Large Language Models on Trusted Serverless Computing Platforms | IEEE Transactions on Artificial Intelligence |
| X-16 | Runtime & Serving | `li2025sled` | 2025 | SLED: A Speculative LLM Decoding Framework for Efficient Edge Serving | arXiv preprint arXiv:2506.09397 |
| X-17 | Applications & Benchmarks | `kim2025slim` | 2025 | Slim-Llama: A 4.69 mW Large-Language-Model Processor with Binary/Ternary Weights for Billion-Parameter Llama Model | 2025 IEEE International Solid-State Circuits Conference (ISSCC) |
| X-18 | Model Optimization | `wang2019haq` | 2019 | Haq: Hardware-aware automated quantization with mixed precision | Proceedings of the IEEE/CVF conference on computer vision and pattern recognition |
| X-19 | Applications & Benchmarks | `capodieci2018deadline` | 2018 | Deadline-based scheduling for GPU with preemption support | 2018 IEEE Real-Time Systems Symposium (RTSS) |
| X-20 | Runtime & Serving | `kouris2022fluid` | 2022 | Fluid batching: Exit-aware preemptive serving of early-exit neural networks on edge npus | arXiv preprint arXiv:2209.13443 |
| X-21 | Model Optimization | `ignatov2021real` | 2021 | Real-time quantized image super-resolution on mobile npus, mobile ai 2021 challenge: Report | Proceedings of the IEEE/CVF conference on computer vision and pattern recognition |
| X-22 | Applications & Benchmarks | `cho2021farnn` | 2021 | FARNN: FPGA-GPU hybrid acceleration platform for recurrent neural networks | IEEE Transactions on Parallel and Distributed Systems |
| X-23 | Runtime & Serving | `choudhury2022fpga` | 2022 | An FPGA overlay for CNN inference with fine-grained flexible parallelism | ACM Transactions on Architecture and Code Optimization (TACO) |
| X-24 | Applications & Benchmarks | `yang2023processing` | 2023 | Processing-in-memory using optically-addressed phase change memory | 2023 IEEE/ACM International Symposium on Low Power Electronics and Design (ISLPED) |
| X-25 | Runtime & Serving | `yi2023edgemoe` | 2023 | Edgemoe: Fast on-device inference of moe-based large language models | arXiv preprint arXiv:2308.14352 |
| X-26 | Collaboration & Deployment | `yi2025edgemoe` | 2025 | Edgemoe: Empowering sparse large language models on mobile devices | IEEE Transactions on Mobile Computing |
| X-27 | Applications & Benchmarks | `li2024locmoe` | 2024 | LocMoE: a low-overhead MoE for large language model training | Proceedings of the Thirty-Third International Joint Conference on Artificial Intelligence |
| X-28 | Applications & Benchmarks | `shen2024jetmoe` | 2024 | Jetmoe: Reaching llama2 performance with 0.1 m dollars | arXiv preprint arXiv:2404.07413 |
| X-29 | Applications & Benchmarks | `shazeer2017sparsely` | 2017 | The sparsely-gated mixture-of-experts layer | Outrageously large neural networks |
| X-30 | Collaboration & Deployment | `qin2024enabling` | 2024 | Enabling on-device large language model personalization with self-supervised data selection and synthesis | Proceedings of the 61st ACM/IEEE Design Automation Conference |
| X-31 | Applications & Benchmarks | `tirumala2023d4` | 2023 | D4: Improving llm pretraining via document de-duplication and diversification | Advances in Neural Information Processing Systems |
| X-32 | Applications & Benchmarks | `marone2025mmbert` | 2025 | mmBERT: A Modern Multilingual Encoder with Annealed Language Learning | arXiv preprint arXiv:2509.06888 |
| X-33 | Applications & Benchmarks | `wu2025livelongbench` | 2025 | LiveLongBench: Tackling Long-Context Understanding for Spoken Texts from Live Streams | arXiv preprint arXiv:2504.17366 |
| X-34 | Collaboration & Deployment | `xiao2024understanding` | 2024 | Understanding Large Language Models in Your Pockets: Performance Study on COTS Mobile Devices | arXiv preprint arXiv:2410.03613 |
| X-35 | Collaboration & Deployment | `laskaridismobile` |  | Mobile and edge evaluation of large language models | Workshop on Efficient Systems for Foundation Models II |
| X-36 | Collaboration & Deployment | `murthy2024mobileaibench` | 2024 | Mobileaibench: Benchmarking llms and lmms for on-device use cases | arXiv preprint arXiv:2406.10290 |
| X-37 | Collaboration & Deployment | `xu2024device` | 2024 | On-device language models: A comprehensive review | arXiv preprint arXiv:2409.00088 |
| X-38 | Collaboration & Deployment | `zheng2025review` | 2025 | A review on edge large language models: Design, execution, and applications | ACM Computing Surveys |
| X-39 | Survey & Foundations | `lu2024small` | 2024 | Small language models: Survey, measurements, and insights | arXiv preprint arXiv:2409.15790 |
| X-40 | Survey & Foundations | `van2024survey` | 2024 | A survey of small language models | arXiv preprint arXiv:2410.20011 |
| X-41 | Collaboration & Deployment | `team2025minicpm4` | 2025 | Minicpm4: Ultra-efficient llms on end devices | arXiv preprint arXiv:2506.07900 |
| X-42 | Model Optimization | `abouelenin2025phi` | 2025 | Phi-4-mini technical report: Compact yet powerful multimodal language models via mixture-of-loras | arXiv preprint arXiv:2503.01743 |
| X-43 | Agent Systems | `han2024llm` | 2024 | LLM multi-agent systems: Challenges and open problems | arXiv preprint arXiv:2402.03578 |
| X-44 | Agent Systems | `yan2025beyond` | 2025 | Beyond self-talk: A communication-centric survey of llm-based multi-agent systems | arXiv preprint arXiv:2502.14321 |
| X-45 | Agent Systems | `gao2025survey` | 2025 | A survey of self-evolving agents: On path to artificial super intelligence | arXiv preprint arXiv:2507.21046 |
| X-46 | Agent Systems | `shen2023hugginggpt` | 2023 | Hugginggpt: Solving ai tasks with chatgpt and its friends in hugging face | Advances in Neural Information Processing Systems |
| X-47 | Security & Trust | `carlini2021extracting` | 2021 | Extracting training data from large language models | 30th USENIX security symposium (USENIX Security 21) |
| X-48 | Survey & Foundations | `dwork2014algorithmic` | 2014 | The algorithmic foundations of differential privacy | Foundations and trends{\textregistered} in theoretical computer science |
| X-49 | Collaboration & Deployment | `ali2022federated` | 2022 | Federated learning for privacy preservation in smart healthcare systems: A comprehensive survey | IEEE journal of biomedical and health informatics |
| X-50 | Applications & Benchmarks | `strubell2020energy` | 2020 | Energy and policy considerations for modern deep learning research | Proceedings of the AAAI conference on artificial intelligence |
| X-51 | Runtime & Serving | `yuan2025local` | 2025 | Local-Cloud Inference Offloading for LLMs in Multi-Modal, Multi-Task, Multi-Dialogue Settings | arXiv preprint arXiv:2502.11007 |
| X-52 | Collaboration & Deployment | `tian2024edge` | 2024 | An edge-cloud collaboration framework for generative ai service provision with synergetic big cloud model and small edge models | IEEE Network |

## New Literature Batch-II (2024-2025): 30 Additional Papers | 新文献批次II（2024-2025）：新增30篇

| ID | BibKey | Year | Title | Venue |
|---|---|---|---|---|
| N-01 | `amp4ec` | 2025 | AMP4EC: Adaptive Model Partitioning Framework for Efficient Deep Learning Inference in Edge Computing Environments | arXiv preprint arXiv:2504.00407 |
| N-02 | `andong2025federated` | 2025 | Federated Multi-Agent Reinforcement Learning for Privacy-Preserving and Energy-Aware Resource Management in 6G Edge Networks | arXiv preprint arXiv:2509.10163 |
| N-03 | `bohdal2025efficient` | 2025 | Efficient Compositional Multi-tasking for On-device Large Language Models | arXiv preprint arXiv:2507.16083 |
| N-04 | `chen2025inference` | 2025 | Inference performance evaluation for LLMs on edge devices with a novel benchmarking framework and metric | arXiv preprint arXiv:2508.11269 |
| N-05 | `chiu2025v2v` | 2025 | V2v-llm: Vehicle-to-vehicle cooperative autonomous driving with multi-modal large language models | arXiv preprint arXiv:2502.09980 |
| N-06 | `faghri2025mobileclip2` | 2025 | MobileCLIP2: Improving Multi-Modal Reinforced Training | arXiv preprint arXiv:2508.20691 |
| N-07 | `fan2025parallel` | 2025 | Parallel CPU-GPU Execution for LLM Inference on Constrained GPUs | arXiv preprint arXiv:2506.03296 |
| N-08 | `fang2025federated` | 2025 | Federated sketching lora: On-device collaborative fine-tuning of large language models | arXiv preprint arXiv:2501.19389 |
| N-09 | `frantar2025marlin` | 2025 | Marlin: Mixed-precision auto-regressive parallel inference on large language models | Proceedings of the 30th ACM SIGPLAN Annual Symposium on Principles and Practice of Parallel Programming |
| N-10 | `guo2025deepseek` | 2025 | DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning | Nature |
| N-11 | `hu2025llm` | 2025 | Llm-based misbehavior detection architecture for enhanced traffic safety in connected autonomous vehicles | IEEE Transactions on Vehicular Technology |
| N-12 | `huang2025vinci` | 2025 | Vinci: A Real-time Smart Assistant Based on Egocentric Vision-language Model for Portable Devices | Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies |
| N-13 | `jin2025innovative` | 2025 | An Innovative Brain-Computer Interface Interaction System Based on the Large Language Model | arXiv preprint arXiv:2502.11659 |
| N-14 | `joshi2025neuro` | 2025 | Neuro-LIFT: A neuromorphic, LLM-based interactive framework for autonomous drone flight at the edge | arXiv preprint arXiv:2501.19259 |
| N-15 | `kong2025quantum` | 2025 | Quantum-enhanced llm efficient fine tuning | arXiv preprint arXiv:2503.12790 |
| N-16 | `lee2025paise` | 2025 | PAISE: PIM-Accelerated Inference Scheduling Engine for Transformer-based LLM | 2025 IEEE International Symposium on High Performance Computer Architecture (HPCA) |
| N-17 | `li2025cusmer` | 2025 | CuSMer: Multimodal Intent Recognition in Customer Service via Data Augment and LLM Merge | Companion Proceedings of the ACM on Web Conference 2025 |
| N-18 | `li2025next` | 2025 | What Is Next for LLMs? Next-Generation AI Computing Hardware Using Photonic Chips | arXiv preprint arXiv:2505.05794 |
| N-19 | `li2025pushing` | 2025 | Pushing up to the limit of memory bandwidth and capacity utilization for efficient llm decoding on embedded fpga | 2025 Design, Automation \& Test in Europe Conference (DATE) |
| N-20 | `li2025qpart` | 2025 | QPART: Adaptive Model Quantization and Dynamic Workload Balancing for Accuracy-aware Edge Inference | arXiv preprint arXiv:2506.23934 |
| N-21 | `li2025urban` | 2025 | Urban Computing in the Era of Large Language Models | ACM Transactions on Intelligent Systems and Technology |
| N-22 | `liu2025ops` | 2025 | OPS: Outlier-Aware Precision-Slice Framework for LLM Acceleration | 2025 Design, Automation \& Test in Europe Conference (DATE) |
| N-23 | `lu2025bluelm` | 2025 | Bluelm-v-3b: Algorithm and system co-design for multimodal large language models on mobile devices | Proceedings of the Computer Vision and Pattern Recognition Conference |
| N-24 | `mao2025deepwriter` | 2025 | DeepWriter: A Fact-Grounded Multimodal Writing Assistant Based On Offline Knowledge Base | arXiv preprint arXiv:2507.14189 |
| N-25 | `pan2025instattention` | 2025 | InstAttention: In-Storage Attention Offloading for Cost-Effective Long-Context LLM Inference | 2025 IEEE International Symposium on High Performance Computer Architecture (HPCA) |
| N-26 | `qu2025mobile` | 2025 | Mobile edge intelligence for large language models: A contemporary survey | IEEE Communications Surveys \& Tutorials |
| N-27 | `ravichandran2025distilling` | 2025 | Distilling On-device Language Models for Robot Planning with Minimal Human Intervention | arXiv preprint arXiv:2506.17486 |
| N-28 | `sakib2025small` | 2025 | Small Language Models: Architectures, Techniques, Evaluation, Problems and Future Adaptation | arXiv preprint arXiv:2505.19529 |
| N-29 | `seo2025facil` | 2025 | FACIL: Flexible DRAM Address Mapping for SoC-PIM Cooperative On-device LLM Inference | 2025 IEEE International Symposium on High Performance Computer Architecture (HPCA) |
| N-30 | `sun2025disco` | 2025 | DiSCo: Device-Server Collaborative LLM-Based Text Streaming Services | arXiv preprint arXiv:2502.11417 |

## New Literature Batch-III (Curated, Edge-First): 27 Additional Papers | 新文献批次III（精选，边缘优先）：新增27篇

| ID | BibKey | Year | Title | Venue |
|---|---|---|---|---|
| M-01 | `cheng2024autoiot` | 2024 | Autoiot: Automated iot platform using large language models | IEEE Internet of Things Journal |
| M-02 | `xue2024powerinfer` | 2024 | Powerinfer-2: Fast large language model inference on a smartphone | arXiv preprint arXiv:2406.06282 |
| M-03 | `xu2024edgellm` | 2024 | Edgellm: Fast on-device llm inference with speculative decoding | IEEE Transactions on Mobile Computing |
| M-04 | `li2024federated` | 2024 | Federated black-box prompt tuning system for large language models on the edge | Proceedings of the 30th Annual International Conference on Mobile Computing and Networking |
| M-05 | `cai2024self` | 2024 | Self-adapting large visual-language models to edge devices across visual modalities | European Conference on Computer Vision |
| M-06 | `ma2024one` | 2024 | From one thousand pages of specification to unveiling hidden bugs: Large language model assisted fuzzing of matter $\{IoT\}$ devices | 33rd USENIX Security Symposium (USENIX Security 24) |
| M-07 | `oliinyk2024fuzzing` | 2024 | Fuzzing $\{BusyBox\}$: Leveraging $\{LLM\}$ and Crash Reuse for Embedded Bug Unearthing | 33rd USENIX Security Symposium (USENIX Security 24) |
| M-08 | `wei2025t` | 2025 | T-mac: Cpu renaissance via table lookup for low-bit llm deployment on edge | Proceedings of the Twentieth European Conference on Computer Systems |
| M-09 | `kong2024swapmoe` | 2024 | SwapMoE: Serving Off-the-shelf MoE-based Large Language Models with Tunable Memory Budget | Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) |
| M-10 | `chen2024understanding` | 2024 | Understanding the potential of fpga-based spatial acceleration for large language model inference | ACM Transactions on Reconfigurable Technology and Systems |
| M-11 | `hu2024realizing` | 2024 | Realizing Efficient On-Device Language-Based Image Retrieval | ACM Transactions on Multimedia Computing, Communications and Applications |
| M-12 | `xu2024towards` | 2024 | Towards energy-efficient llama2 architecture on embedded fpgas | Proceedings of the 33rd ACM International Conference on Information and Knowledge Management |
| M-13 | `zhang2024edgeshard` | 2024 | Edgeshard: Efficient llm inference via collaborative edge computing | IEEE Internet of Things Journal |
| M-14 | `xu2025fast` | 2025 | Fast on-device LLM inference with npus | Proceedings of the 30th ACM International Conference on Architectural Support for Programming Languages and Operating Systems, Volume 1 |
| M-15 | `yu2024cambricon` | 2024 | Cambricon-llm: A chiplet-based hybrid architecture for on-device inference of 70b llm | 2024 57th IEEE/ACM International Symposium on Microarchitecture (MICRO) |
| M-16 | `ren2024industrial` | 2024 | Industrial internet of things with large language models (LLMs): an intelligence-based reinforcement learning approach | IEEE Transactions on Mobile Computing |
| M-17 | `zhang2025vavlm` | 2025 | VaVLM: Toward Efficient Edge-Cloud Video Analytics With Vision-Language Models | IEEE Transactions on Broadcasting |
| M-18 | `rivkin2024aiot` | 2024 | Aiot smart home via autonomous llm agents | IEEE Internet of Things Journal |
| M-19 | `yang2025quality` | 2025 | Quality-of-Service Aware LLM Routing for Edge Computing with Multiple Experts | IEEE Transactions on Mobile Computing |
| M-20 | `chen2024autoos` | 2024 | Autoos: make your os more powerful by exploiting large language models | Forty-first International Conference on Machine Learning |
| M-21 | `cai2025prompt` | 2025 | Prompt-Ladder: Memory-efficient prompt tuning for vision-language models on edge devices | Pattern Recognition |
| M-22 | `minicpm-v4` | 2024 | MiniCPM-V: A GPT-4V Level MLLM on Your Phone | arXiv preprint arXiv:2408.01800 |
| M-23 | `sun2025lincoln` | 2025 | Lincoln: Real-Time 50\~{} 100B LLM Inference on Consumer Devices with LPDDR-Interfaced, Compute-Enabled Flash Memory | 2025 IEEE International Symposium on High Performance Computer Architecture (HPCA) |
| M-24 | `tian2025clone` | 2025 | CLONE: Customizing LLMs for Efficient Latency-Aware Inference at the Edge | arXiv preprint arXiv:2506.02847 |
| M-25 | `wang2025empowering` | 2025 | Empowering edge intelligence: A comprehensive survey on on-device ai models | ACM Computing Surveys |
| M-26 | `zhao2025mobilellm` | 2025 | MobileLLM-R1: Exploring the Limits of Sub-Billion Language Model Reasoners with Open Training Recipes | arXiv preprint arXiv:2509.24945 |
| M-27 | `yang2025mobileviclip` | 2025 | MobileViCLIP: An Efficient Video-Text Model for Mobile Devices | arXiv preprint arXiv:2508.07312 |

## Authenticity Ledger for Batch-II/III | 批次II/III真实性台账

All items below are mapped to the manuscript bibliography source.

下表逐条映射到主稿参考文献来源，便于审稿和复核。

| BibKey | Year | Link | Source | Status |
|---|---|---|---|---|
| `amp4ec` | 2025 | https://arxiv.org/abs/2504.00407 | `references.bib` | matched |
| `andong2025federated` | 2025 | https://arxiv.org/abs/2509.10163 | `references.bib` | matched |
| `bohdal2025efficient` | 2025 | https://arxiv.org/abs/2507.16083 | `references.bib` | matched |
| `chen2025inference` | 2025 | https://arxiv.org/abs/2508.11269 | `references.bib` | matched |
| `chiu2025v2v` | 2025 | https://arxiv.org/abs/2502.09980 | `references.bib` | matched |
| `faghri2025mobileclip2` | 2025 | https://arxiv.org/abs/2508.20691 | `references.bib` | matched |
| `fan2025parallel` | 2025 | https://arxiv.org/abs/2506.03296 | `references.bib` | matched |
| `fang2025federated` | 2025 | https://arxiv.org/abs/2501.19389 | `references.bib` | matched |
| `frantar2025marlin` | 2025 | N/A | `references.bib` | matched |
| `guo2025deepseek` | 2025 | https://doi.org/10.1038/s41586-025-09422-z | `references.bib` | matched |
| `hu2025llm` | 2025 | N/A | `references.bib` | matched |
| `huang2025vinci` | 2025 | N/A | `references.bib` | matched |
| `jin2025innovative` | 2025 | https://arxiv.org/abs/2502.11659 | `references.bib` | matched |
| `joshi2025neuro` | 2025 | https://arxiv.org/abs/2501.19259 | `references.bib` | matched |
| `kong2025quantum` | 2025 | https://arxiv.org/abs/2503.12790 | `references.bib` | matched |
| `lee2025paise` | 2025 | N/A | `references.bib` | matched |
| `li2025cusmer` | 2025 | N/A | `references.bib` | matched |
| `li2025next` | 2025 | https://arxiv.org/abs/2505.05794 | `references.bib` | matched |
| `li2025pushing` | 2025 | N/A | `references.bib` | matched |
| `li2025qpart` | 2025 | https://arxiv.org/abs/2506.23934 | `references.bib` | matched |
| `li2025urban` | 2025 | N/A | `references.bib` | matched |
| `liu2025ops` | 2025 | N/A | `references.bib` | matched |
| `lu2025bluelm` | 2025 | N/A | `references.bib` | matched |
| `mao2025deepwriter` | 2025 | https://arxiv.org/abs/2507.14189 | `references.bib` | matched |
| `pan2025instattention` | 2025 | N/A | `references.bib` | matched |
| `qu2025mobile` | 2025 | N/A | `references.bib` | matched |
| `ravichandran2025distilling` | 2025 | https://arxiv.org/abs/2506.17486 | `references.bib` | matched |
| `sakib2025small` | 2025 | https://arxiv.org/abs/2505.19529 | `references.bib` | matched |
| `seo2025facil` | 2025 | N/A | `references.bib` | matched |
| `sun2025disco` | 2025 | https://arxiv.org/abs/2502.11417 | `references.bib` | matched |
| `cheng2024autoiot` | 2024 | N/A | `references.bib` | matched |
| `xue2024powerinfer` | 2024 | https://arxiv.org/abs/2406.06282 | `references.bib` | matched |
| `xu2024edgellm` | 2024 | N/A | `references.bib` | matched |
| `li2024federated` | 2024 | N/A | `references.bib` | matched |
| `cai2024self` | 2024 | N/A | `references.bib` | matched |
| `ma2024one` | 2024 | N/A | `references.bib` | matched |
| `oliinyk2024fuzzing` | 2024 | N/A | `references.bib` | matched |
| `wei2025t` | 2025 | N/A | `references.bib` | matched |
| `kong2024swapmoe` | 2024 | N/A | `references.bib` | matched |
| `chen2024understanding` | 2024 | N/A | `references.bib` | matched |
| `hu2024realizing` | 2024 | N/A | `references.bib` | matched |
| `xu2024towards` | 2024 | N/A | `references.bib` | matched |
| `zhang2024edgeshard` | 2024 | N/A | `references.bib` | matched |
| `xu2025fast` | 2025 | N/A | `references.bib` | matched |
| `yu2024cambricon` | 2024 | N/A | `references.bib` | matched |
| `ren2024industrial` | 2024 | N/A | `references.bib` | matched |
| `zhang2025vavlm` | 2025 | N/A | `references.bib` | matched |
| `rivkin2024aiot` | 2024 | N/A | `references.bib` | matched |
| `yang2025quality` | 2025 | N/A | `references.bib` | matched |
| `chen2024autoos` | 2024 | N/A | `references.bib` | matched |
| `cai2025prompt` | 2025 | N/A | `references.bib` | matched |
| `minicpm-v4` | 2024 | https://arxiv.org/abs/2408.01800 | `references.bib` | matched |
| `sun2025lincoln` | 2025 | N/A | `references.bib` | matched |
| `tian2025clone` | 2025 | https://arxiv.org/abs/2506.02847 | `references.bib` | matched |
| `wang2025empowering` | 2025 | N/A | `references.bib` | matched |
| `zhao2025mobilellm` | 2025 | https://arxiv.org/abs/2509.24945 | `references.bib` | matched |
| `yang2025mobileviclip` | 2025 | https://arxiv.org/abs/2508.07312 | `references.bib` | matched |

## Timeline by Year | 按年份时间线

| Year | Milestone Papers | Why It Matters |
|---|---|---|
| 2014-2017 | `dwork2014algorithmic`, `vaswani2017attention` | Privacy foundations + Transformer paradigm |
| 2018-2020 | `jacob2018quantization`, `zhou2019edge`, `brown2020language` | Efficient inference + edge intelligence + few-shot LLM shift |
| 2021-2022 | `nagel2021white`, `wei2022emergent`, `gholami2022survey` | Quantization practices + capability emergence + efficiency synthesis |
| 2023 | `kwon2023efficient`, `frantar2023gptq`, `shen2023hugginggpt` | Serving memory breakthroughs + PTQ for LLM + tool-using agents |
| 2024 | `murthy2024mobileaibench`, `tan2024mobilequant`, `li2024eagle`, `team2024gemma` | On-device benchmarks + mobile quantization + decode acceleration + open deployable models |
| 2025 | `belcak2025small`, `gao2025survey`, `marone2025mmbert` | SLM-first agent direction + self-evolving agents + multilingual retrieval efficiency |

## Task-Oriented Retrieval Matrix | 按任务维度检索矩阵

| Task/Problem | Recommended Entry Papers | Category |
|---|---|---|
| Edge AI fundamentals | `shi2016edge`, `zhou2019edge`, `deng2020edge` | A |
| LLM capability baseline | `vaswani2017attention`, `brown2020language`, `wei2022emergent` | A |
| On-device benchmarking | `murthy2024mobileaibench`, `laskaridismobile`, `xiao2024understanding` | B/F |
| Quantization for deployment | `jacob2018quantization`, `frantar2023gptq`, `tan2024mobilequant`, `qlora2023` | C |
| Serving/runtime optimization | `kwon2023efficient`, `dao2024flashattention`, `li2024eagle`, `zhao2024qspec` | C |
| Edge-cloud offloading | `tian2024edge`, `jin2024collm`, `yuan2025local` | C |
| Agent tool-use and control | `shen2023hugginggpt`, `han2024llm`, `gao2025survey` | D |
| SLM for agentic deployment | `belcak2025small`, `lu2024small`, `van2024survey` | A/D |
| Privacy and governance | `dwork2014algorithmic`, `carlini2021extracting`, `han2024llm` | B/F |

## Journal/Conference Target Mapping | 投稿方向映射

| Research Emphasis | Suggested Targets |
|---|---|
| Data/knowledge management, retrieval pipelines, reproducible protocol synthesis | TKDE, TOIS, ACM CSUR |
| Edge systems architecture, offloading, serving orchestration | IEEE TMC, IEEE IoTJ, IEEE TPDS |
| Efficient model compression and deployment algorithms | TNNLS, ML Systems workshops, ICML/NeurIPS systems tracks |
| Agent safety, tool governance, and applied trustworthy deployment | IEEE TAI, AI ethics/governance tracks, domain-focused venues |

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
