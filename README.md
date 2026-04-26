# Cognitive Edge LLM-Agent Survey Taxonomy | 认知边缘大模型与智能体综述分类

This repository organizes the survey content of cognitive edge computing into a bilingual taxonomy (English + 中文), with representative references under each category.

本仓库将认知边缘计算综述内容整理为中英文双语分类体系，并在每个分类下提供代表性参考文献，便于持续维护与扩展。

## Table of Contents | 目录

1. [Scope and Positioning | 范围与定位](#1-scope-and-positioning--范围与定位)
2. [Taxonomy A: Foundations | 分类A基础概念](#2-taxonomy-a-foundations--分类a基础概念)
3. [Taxonomy B: Deployment Challenges | 分类B部署挑战](#3-taxonomy-b-deployment-challenges--分类b部署挑战)
4. [Taxonomy C: Optimization Strategies | 分类C优化策略](#4-taxonomy-c-optimization-strategies--分类c优化策略)
5. [Taxonomy D: Agentic Systems and Collaboration | 分类D智能体系统与协同](#5-taxonomy-d-agentic-systems-and-collaboration--分类d智能体系统与协同)
6. [Taxonomy E: Applications | 分类E应用场景](#6-taxonomy-e-applications--分类e应用场景)
7. [Taxonomy F: Evaluation, Security, and Trust | 分类F评估安全与可信](#7-taxonomy-f-evaluation-security-and-trust--分类f评估安全与可信)
8. [Maintenance Rules | 维护规则](#8-maintenance-rules--维护规则)

## 1. Scope and Positioning | 范围与定位

- EN: Focus on edge/on-device LLMs and AI agents under constrained compute, memory, energy, and latency budgets.
- 中文: 聚焦资源受限条件下的端侧/边缘侧大模型与 AI 智能体，强调算力、内存、能耗与时延预算约束。

- EN: Core objective is capability preservation under budget, not single-metric optimization.
- 中文: 核心目标是“预算约束下能力保持”，而不是单指标最优。

## 2. Taxonomy A: Foundations | 分类A：基础概念

### A1. Edge Computing and Edge Intelligence | 边缘计算与边缘智能
- EN: Architecture hierarchy (device-edge-cloud), data proximity, and low-latency execution.
- 中文: 端-边-云分层架构、数据近源处理与低时延执行。

Representative References | 代表文献
- Shi et al., "Edge Computing: Vision and Challenges," IEEE IoT Journal, 2016.
- Zhou et al., "Edge Intelligence: Paving the Last Mile of Artificial Intelligence with Edge Computing," Proceedings of the IEEE, 2019.
- Deng et al., "Edge intelligence: The confluence of edge computing and artificial intelligence," IEEE IoT Journal, 2020.
- Li et al., "Edge AI: On-demand accelerating deep neural network inference via edge computing," IEEE TWC, 2019.

### A2. LLM Fundamentals for Edge Context | 面向边缘场景的大模型基础
- EN: Transformer paradigm, scaling behavior, and emergent reasoning capabilities.
- 中文: Transformer 范式、规模化规律与涌现推理能力。

Representative References | 代表文献
- Vaswani et al., "Attention is All You Need," NeurIPS, 2017.
- Brown et al., "Language Models are Few-Shot Learners," NeurIPS, 2020.
- Wei et al., "Emergent Abilities of Large Language Models," TMLR, 2022.
- Xu et al., "EdgeLLM: A Comprehensive Survey of Large Language Models for Edge Computing," ACM CSUR, 2024.

## 3. Taxonomy B: Deployment Challenges | 分类B：部署挑战

### B1. Resource Bottlenecks | 资源瓶颈
- EN: Compute mismatch, memory bandwidth pressure, KV-cache growth, and thermal constraints.
- 中文: 算力失配、内存带宽压力、KV 缓存增长与热设计约束。

Representative References | 代表文献
- Gholami et al., "A Survey of Quantization Methods for Efficient Neural Network Inference," 2022.
- Nagel et al., "A White Paper on Neural Network Quantization," 2021.
- Kwon et al., "Efficient Memory Management for LLM Serving with PagedAttention," SOSP, 2023.

### B2. Performance and System Stability | 性能与系统稳定性
- EN: Throughput vs. latency, startup delay, p95/p99 tail latency, bursty workloads.
- 中文: 吞吐与时延权衡、首 token 启动时延、p95/p99 尾时延与突发负载稳定性。

Representative References | 代表文献
- Murthy et al., "MobileAIBench: Benchmarking LLMs and LMMs for On-Device Use Cases," 2024.
- Sheng et al., "FlexGen: High-throughput Generative Inference of LLMs with a Single GPU," ICML, 2023.

### B3. Security and Privacy Risks | 安全与隐私风险
- EN: Prompt injection, unsafe tool use, data leakage, and weak governance.
- 中文: 提示词注入、工具滥用、数据泄露与治理薄弱。

Representative References | 代表文献
- Dwork and Roth, "The Algorithmic Foundations of Differential Privacy," 2014.
- Han et al., "LLM Multi-Agent Systems: Challenges and Open Problems," 2024.

## 4. Taxonomy C: Optimization Strategies | 分类C：优化策略

### C1. Data and Context Optimization | 数据与上下文优化
- EN: Data selection/synthesis, token budgeting, context compression, retrieval quality control.
- 中文: 数据选择与合成、Token 预算、上下文压缩与检索质量控制。

Representative References | 代表文献
- Qin et al., "Enabling On-device LLM Personalization with Self-supervised Data Selection and Synthesis," DAC, 2024.
- Tirumala et al., "D4: Improving LLM Pretraining via Document De-duplication and Diversification," NeurIPS, 2023.

### C2. Model Compression and Adaptation | 模型压缩与适配
- EN: Quantization, pruning, distillation, low-rank adaptation, compact SLM design.
- 中文: 量化、剪枝、知识蒸馏、低秩适配与小模型结构设计。

Representative References | 代表文献
- Jacob et al., "Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference," CVPR, 2018.
- Frantar et al., "GPTQ: Accurate Post-Training Quantization for GPTs," ICLR, 2023.
- Hinton et al., "Distilling the Knowledge in a Neural Network," 2015.
- Gou et al., "Knowledge Distillation: A Survey," IJCV, 2021.
- Tan et al., "MobileQuant: Mobile-friendly Quantization for On-device Language Models," EMNLP Findings, 2024.

### C3. Runtime and Serving Optimization | 运行时与服务优化
- EN: KV-cache management, scheduling, speculative decoding, memory-aware serving.
- 中文: KV 缓存管理、调度策略、投机解码与内存感知服务。

Representative References | 代表文献
- Kwon et al., "PagedAttention for LLM Serving," SOSP, 2023.
- Dao, "FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning," ICLR, 2024.
- Li et al., "EAGLE-2: Faster Inference with Dynamic Draft Trees," EMNLP, 2024.
- Zhao et al., "QSpec: Speculative Decoding with Complementary Quantization Schemes," 2024.

### C4. Edge-Cloud Collaboration | 端边云协同
- EN: Dynamic routing and selective offloading between local and cloud execution.
- 中文: 本地与云端执行之间的动态路由与选择性卸载。

Representative References | 代表文献
- Tian et al., "Edge-Cloud Collaborative Inference: A Contemporary Survey," 2024.
- Jin et al., "Collm: Integrating Collaborative and Lightweight LLMs," NeurIPS, 2025.
- Yuan et al., "Local-Cloud Inference Offloading for LLMs," 2025.

## 5. Taxonomy D: Agentic Systems and Collaboration | 分类D：智能体系统与协同

### D1. Agent Capability Model | 智能体能力模型
- EN: Perception-reasoning-action loop with tool-use and planning constraints.
- 中文: 感知-推理-行动闭环，并受工具调用与规划预算约束。

Representative References | 代表文献
- Dorri et al., "Multi-agent Systems: A Survey," IEEE Access, 2018.
- Shen et al., "HuggingGPT: Solving AI Tasks with ChatGPT and Its Friends in Hugging Face," NeurIPS, 2023.

### D2. Multi-Agent and Small-Model Trends | 多智能体与小模型趋势
- EN: Multi-agent collaboration and SLM-oriented agent deployment for edge practicality.
- 中文: 多智能体协作与面向边缘可部署性的小模型智能体方向。

Representative References | 代表文献
- Han et al., "LLM Multi-Agent Systems: Challenges and Open Problems," 2024.
- Yan et al., "Beyond Self-Talk: A Communication-centric Survey of LLM-based MAS," 2025.
- Belcak et al., "Small Language Models are the Future of Agentic AI," 2025.
- Gao et al., "A Survey of Self-evolving Agents," 2025.

## 6. Taxonomy E: Applications | 分类E：应用场景

### E1. Mobility and Autonomous Systems | 移动与自动系统
- EN: Autonomous driving, vehicle-edge coordination, and real-time decision support.
- 中文: 自动驾驶、车端-路侧协同与实时决策支持。

Representative References | 代表文献
- Zhou et al., "Edge Intelligence," 2019.
- Deng et al., "Edge Intelligence Confluence Survey," 2020.

### E2. Healthcare and Privacy-Sensitive Domains | 医疗与隐私敏感领域
- EN: Personalized and secure inference with privacy-preserving learning.
- 中文: 以隐私保护为约束的个性化推理与学习。

Representative References | 代表文献
- Ali et al., "Federated Learning for Privacy Preservation in Smart Healthcare Systems," JBHI, 2022.
- Dwork and Roth, "Differential Privacy," 2014.

### E3. On-Device Consumer and Industrial AI | 端侧消费与工业 AI
- EN: Mobile assistants, industrial quality inspection, multilingual edge retrieval.
- 中文: 移动智能助手、工业质检与多语检索等端侧能力。

Representative References | 代表文献
- Abdin et al., "Phi-4 Technical Report," 2024.
- Team Gemma, "Gemma: Open Models Based on Gemini Research and Technology," 2024.
- Mehta et al., "OpenELM," ICML ES-FM Workshop, 2024.
- Marone et al., "mmBERT: A Modern Multilingual Encoder," 2025.

## 7. Taxonomy F: Evaluation, Security, and Trust | 分类F：评估、安全与可信

### F1. Reproducibility-oriented Evaluation | 面向复现的评估
- EN: Multi-metric reporting should include quality, throughput, startup latency, tail latency, and energy/token.
- 中文: 多指标报告应覆盖质量、吞吐、启动时延、尾时延与单位 token 能耗。

Representative References | 代表文献
- Murthy et al., "MobileAIBench," 2024.
- Laskaridis et al., "Mobile and Edge Evaluation of Large Language Models," 2024.
- Strubell et al., "Energy and Policy Considerations for Modern Deep Learning Research," AAAI, 2020.

### F2. Governance and Security Baseline | 治理与安全基线
- EN: Standardized risk management for model/data/tool chain in edge deployment.
- 中文: 端侧部署需对模型、数据与工具链进行标准化风险治理。

Representative References | 代表文献
- Dwork and Roth, "Differential Privacy," 2014.
- Han et al., "LLM Multi-Agent Systems: Challenges and Open Problems," 2024.
- Gao et al., "Self-evolving Agents Survey," 2025.

## 8. Maintenance Rules | 维护规则

- EN: Add new papers by category first, then update cross-category links.
- 中文: 新增文献先归类，再更新跨分类关联。

- EN: Keep hardware and evaluation settings explicit for each empirical claim.
- 中文: 每条实验结论必须注明硬件与评测设置。

- EN: Prefer Pareto-style reporting (quality-latency-energy) over single headline numbers.
- 中文: 优先使用质量-时延-能耗的 Pareto 报告，而非单一指标。
