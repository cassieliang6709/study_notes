---
title: "Project Guide: ModelAlignmentFromScratch"
---

# Project Guide: ModelAlignmentFromScratch

原项目：

- https://github.com/Sherlock1956/ModelAlignmentFromScratch

---

## 这个项目最适合你学什么

这个项目很适合用来理解“对齐训练到底在做什么”。

它不是泛泛而谈，而是直接落到实现层：

- SFT
- Expert Iteration
- GRPO

而且它把重点放在数学推理任务上。

---

## 为什么应该在这个阶段做它

如果你已经看过一些 LLM from scratch 内容，但对“预训练之后下一步是什么”仍然模糊，这个项目正好能补上。

它特别适合建立这条认知链：

- pretraining 不是终点
- alignment 不是一句话
- 不同 alignment 方法优化目标不同

---

## 前置知识

- transformer 和语言模型训练基础
- PyTorch 训练 loop 基础
- 最好已看过 [CS336](./project_cs336.md) 或 [MiniMind](./project_minimind.md)

---

## 先看什么

建议顺序：

1. README 的项目概述
2. `cs336_alignment/` 目录结构
3. `sft.py`
4. `expert_iteration.py`
5. `GRPO.py`
6. `drgrpo_grader.py`

先从 `sft.py` 开始很重要，不要一上来先啃 `GRPO.py`。

---

## 第一周最小任务

第一周只要完成这几件事：

1. 跑通环境
2. 把三种方法的输入输出关系看清
3. 至少读懂 `sft.py`
4. 写一张对比表：SFT vs EI vs GRPO

---

## 开做指南

### 环境要求

- Python
- PyTorch / transformers 训练环境
- 最好有 GPU

### 最小启动动作

1. 按 README 安装依赖
2. 看下载模型脚本
3. 跑 `sft.py`
4. 再跑 `expert_iteration.py` 或 `GRPO.py`

### 第一遍不要改什么

- 不要先改奖励函数
- 不要先改数据集
- 不要一开始就优化训练效果

### 第二遍建议你改什么

- 改一个 reward 细节
- 观察不同方法训练曲线差异
- 看 vLLM 和训练如何结合

---

## 你做完后应该掌握什么

- 知道 SFT、EI、GRPO 的目标差异
- 知道 response sampling 和 reward 在 alignment 中的作用
- 知道训练脚本里哪些部分是 alignment 特有的

---

## 常见卡点

- 没读懂 baseline，就直接跳高级方法
- 把 GRPO 当成“黑盒高级版 SFT”
- 只看结果，不看 loss / sampling / reward 过程

---

## 最小完成标准

- 你能解释三种方法各自在优化什么
- 你能指出这个仓库里 reward 相关逻辑的位置
- 你能说清 alignment 相比 pretraining 多了哪些部件

---

## 下一站

建议下一步去：

- [OpenPipe ART](./project_openpipe_art.md)

因为这时你已经有了单模型 alignment 的感觉，再去看 agent RL 会更顺。
