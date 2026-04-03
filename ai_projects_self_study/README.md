# AI Projects Self-Study Hub

这套文档是给你自己自学用的，不是课程官网，也不是仓库翻译。

目标只有一个：

- 让你知道这些项目分别在教什么
- 让你知道先做哪个、后做哪个
- 让你每次打开一个仓库时，知道第一步该干什么

---

## 怎么用这套文档

建议不要同时开 8 个仓库乱看。

正确方式是：

1. 先选一条学习主线
2. 在这条线里按顺序做项目
3. 每个项目先完成“最小复现”
4. 第二遍再改代码、换数据、做自己的版本

---

## 三条主线

### 1. RAG / Retrieval Systems

适合你如果现在最想做：

- 企业知识库问答
- 检索增强生成
- 多步搜索与 deep research

入口：

- [RAG Systems Track](./track_1_rag_systems.md)

### 2. LLM From Scratch

适合你如果现在最想搞懂：

- tokenizer
- transformer
- pretraining
- 小模型从零训练

入口：

- [LLM From Scratch Track](./track_2_llm_from_scratch.md)

### 3. Alignment / Agent RL

适合你如果已经有一点 LLM 基础，想继续学：

- SFT
- preference optimization
- GRPO
- agent reinforcement training

入口：

- [Alignment And Agent RL Track](./track_3_alignment_and_agent_rl.md)

---

## 推荐顺序

如果你是第一次系统做这类项目，建议按这个顺序：

1. [LangChain rag-from-scratch](./project_rag_from_scratch.md)
2. [Complex RAG Guide](./project_complex_rag_guide.md)
3. [RAG Techniques](./project_rag_techniques.md)
4. [DeepSearcher](./project_deep_searcher.md)
5. [MiniMind](./project_minimind.md)
6. [Stanford CS336](./project_cs336.md)
7. [ModelAlignmentFromScratch](./project_model_alignment_from_scratch.md)
8. [OpenPipe ART](./project_openpipe_art.md)

为什么这样排：

- 前 4 个先把 RAG 做实
- 中间 2 个补齐“模型本体”理解
- 最后 2 个进入 alignment 和 agent RL

---

## 项目一句话定位

| 项目 | 一句话定位 | 难度 |
| --- | --- | --- |
| [rag-from-scratch](./project_rag_from_scratch.md) | 最适合入门 RAG 主链路的实践仓库 | 低 |
| [complex-RAG-guide](./project_complex_rag_guide.md) | 把 RAG 从 demo 拉到更复杂流程 | 中 |
| [rag_techniques](./project_rag_techniques.md) | RAG 技术手册和实验集 | 中 |
| [deep-searcher](./project_deep_searcher.md) | 更接近产品化 deep research / private data search | 中高 |
| [minimind](./project_minimind.md) | 小模型从零训练的低门槛入口 | 中 |
| [CS336](./project_cs336.md) | 系统学习 language modeling from scratch | 高 |
| [ModelAlignmentFromScratch](./project_model_alignment_from_scratch.md) | 从 SFT 到 EI / GRPO 的手写实现 | 高 |
| [OpenPipe ART](./project_openpipe_art.md) | 面向多步 agent 的强化训练框架 | 高 |

---

## 如果你不知道从哪条线开始

### 你想先做应用

先走 RAG：

- [RAG Systems Track](./track_1_rag_systems.md)

### 你想先打基础

先走 LLM from scratch：

- [LLM From Scratch Track](./track_2_llm_from_scratch.md)

### 你已经做过一些 RAG 或小模型训练

再走 alignment：

- [Alignment And Agent RL Track](./track_3_alignment_and_agent_rl.md)

---

## 推荐学习节奏

### 轻量版

- 每周 3 天
- 每次 60 到 90 分钟
- 适合稳步推进

### 冲刺版

- 每周 5 到 6 天
- 每次 2 到 3 小时
- 适合想在 1 到 2 个月打出一条完整主线

---

## 每个项目怎么做

不要一上来就“看懂全部代码”。

统一按下面流程：

1. 看这份导学页
2. 打开原项目 README
3. 跑通最小 demo
4. 只改一个局部模块
5. 写你自己的总结

建议每做完一个项目，都回答这 4 个问题：

- 这个项目核心解决什么问题
- 它的最小可运行链路是什么
- 它和上一个项目相比多了什么
- 如果让我自己重写，我先重写哪一层

---

## 项目索引

- [DeepSearcher](./project_deep_searcher.md)
- [DeepSearcher 7-Day Plan](./week_plan_deep_searcher.md)
- [MiniMind](./project_minimind.md)
- [MiniMind 7-Day Plan](./week_plan_minimind.md)
- [Complex RAG Guide](./project_complex_rag_guide.md)
- [Complex RAG Guide 7-Day Plan](./week_plan_complex_rag_guide.md)
- [rag-from-scratch](./project_rag_from_scratch.md)
- [rag-from-scratch 7-Day Plan](./week_plan_rag_from_scratch.md)
- [RAG Techniques](./project_rag_techniques.md)
- [RAG Techniques 7-Day Plan](./week_plan_rag_techniques.md)
- [OpenPipe ART](./project_openpipe_art.md)
- [OpenPipe ART 7-Day Plan](./week_plan_openpipe_art.md)
- [ModelAlignmentFromScratch](./project_model_alignment_from_scratch.md)
- [ModelAlignmentFromScratch 7-Day Plan](./week_plan_model_alignment_from_scratch.md)
- [Stanford CS336](./project_cs336.md)
- [Stanford CS336 7-Day Plan](./week_plan_cs336.md)

---

## 第二层内容

如果你已经确定要开始做，不只是浏览导学页，那就直接进入每个项目的 `7-Day Plan`。

这些计划的目标是：

- 每天只做一小块
- 不让你陷入“今天又不知道该干什么”
- 每天结束都有明确产出

推荐进入方式：

1. 先读对应项目导学页
2. 再打开对应 `7-Day Plan`
3. 照着每天任务推进

---

## 第三层内容

如果你已经学完一轮，想检查自己到底有没有真的掌握，再做这一层：

- [RAG 自测题](./self_test_rag.md)
- [LLM From Scratch 自测题](./self_test_llm_from_scratch.md)
- [Alignment / Agent RL 自测题](./self_test_alignment_agent_rl.md)
- [综合项目自测](./self_test_capstone.md)

使用方式：

1. 不看原文档，先自己答
2. 能口头解释的题，不要只写关键词
3. 做完后再回去查漏补缺

---

## 第四层内容

如果你做完自测后想核对思路，再看这一层：

- [RAG 自测参考答案](./answer_key_rag.md)
- [LLM From Scratch 自测参考答案](./answer_key_llm_from_scratch.md)
- [Alignment / Agent RL 自测参考答案](./answer_key_alignment_agent_rl.md)
- [综合项目自测参考答案](./answer_key_capstone.md)

建议顺序：

1. 先独立做题
2. 再对照答案
3. 把不会的点写回自己的笔记

---

## 你真正的目标

不是“收藏这些 repo”。

而是做到这三件事：

- 你能独立复现一个最小 RAG 系统
- 你能讲清楚一个小语言模型从 tokenizer 到训练的主流程
- 你能区分 pretraining、SFT、GRPO、agent RL 分别在解决什么问题
