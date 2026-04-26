# Taxonomy C: Optimization Strategies | 分类C：优化策略

## C1. Data and Context Optimization | 数据与上下文优化

- EN: Data selection/synthesis, token budgeting, context compression, retrieval quality control.
- 中文: 数据选择/合成、Token 预算、上下文压缩与检索质量控制。

### References

- Qin et al. Enabling On-device LLM Personalization with Self-supervised Data Selection and Synthesis. DAC, 2024.
- Tirumala et al. D4: Improving LLM Pretraining via Document De-duplication and Diversification. NeurIPS, 2023.

## C2. Model Compression and Adaptation | 模型压缩与适配

- EN: Quantization, pruning, distillation, low-rank adaptation, compact SLM design.
- 中文: 量化、剪枝、蒸馏、低秩适配与小模型结构设计。

### References

- Jacob et al. Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference. CVPR, 2018.
- Frantar et al. GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers. ICLR, 2023.
- Hinton et al. Distilling the Knowledge in a Neural Network. 2015.
- Gou et al. Knowledge Distillation: A Survey. IJCV, 2021.
- Tan et al. MobileQuant: Mobile-friendly Quantization for On-device Language Models. EMNLP Findings, 2024.

## C3. Runtime and Serving Optimization | 运行时与服务优化

- EN: KV management, scheduling, speculative decoding, memory-aware serving.
- 中文: KV 管理、调度、投机解码与内存感知服务。

### References

- Kwon et al. PagedAttention for LLM Serving. SOSP, 2023.
- Dao. FlashAttention-2. ICLR, 2024.
- Li et al. EAGLE-2: Faster Inference with Dynamic Draft Trees. EMNLP, 2024.
- Zhao et al. QSpec: Speculative Decoding with Complementary Quantization Schemes. 2024.

## C4. Edge-Cloud Collaboration | 端边云协同

- EN: Dynamic routing and selective offloading between local and cloud inference.
- 中文: 本地与云端推理之间的动态路由与选择性卸载。

### References

- Tian et al. Edge-Cloud Collaborative Inference: A Contemporary Survey. 2024.
- Jin et al. Collm: Integrating Collaborative and Lightweight LLMs. NeurIPS, 2025.
- Yuan et al. Local-Cloud Inference Offloading for LLMs. 2025.
