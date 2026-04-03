---
title: "Track 3: Alignment And Agent RL"
---

# Track 3: Alignment And Agent RL

这条线解决的是：

- 预训练后的模型为什么还不够好用
- 怎么通过 SFT、偏好优化、RL 让模型更符合目标
- 多步 agent 为什么需要专门训练，而不是只靠 prompt

---

## 这条线的正确顺序

1. [ModelAlignmentFromScratch](./project_model_alignment_from_scratch.md)
2. [OpenPipe ART](./project_openpipe_art.md)

---

## 为什么这样排

因为：

- `ModelAlignmentFromScratch` 更像教学型、手写型 alignment 项目
- `ART` 更像更现代、更框架化、面向 agent tasks 的训练工具

先理解单模型 alignment，再看 agent reinforcement，会稳很多。

---

## 每一站分别学什么

### 1. ModelAlignmentFromScratch

你在这里学：

- SFT 在做什么
- EI 在做什么
- GRPO 在做什么
- reward、sampling、training loop 怎么结合

做完应该能做到：

- 你知道“对齐”不是一句空话，而是一组具体训练方法

### 2. OpenPipe ART

你在这里学：

- agent reinforcement training 的任务形式
- 多步任务、轨迹、奖励、优化之间的关系
- 为什么 agent RL 的难点和普通 SFT 不一样

做完应该能做到：

- 你能理解 agent 训练为什么要强调 interaction 和 trajectory

---

## 学这条线前你最好已经会

- PyTorch 基础
- transformer 基础
- language model training loop 基础
- 最好已经做过一点小模型训练或至少认真看过 [Track 2](./track_2_llm_from_scratch.md)

---

## 这条线最容易误解的地方

### 误解 1

“SFT 就等于 alignment”

不对。

SFT 只是 alignment 里最基础的一层。

### 误解 2

“RLHF / GRPO 只是多一个 reward model”

也不对。

真正难的是：

- 样本怎么来
- 奖励怎么定义
- 训练稳定性怎么保证
- 多步任务怎么 credit assignment

### 误解 3

“agent 只要 prompt 写好就行”

不对。

多步 agent 在很多场景下确实会受训练方式影响。

---

## 这条线的完成标准

做到下面这些，才算真正入门：

- 你能说清 SFT、EI、GRPO 各自在优化什么
- 你知道 alignment 的目标不只是“让输出更像人”
- 你知道 agent RL 比普通 instruction tuning 多了什么难点
- 你能读懂一个最小的 alignment 训练脚本

---

## 建议产出

学完这条线，建议你写一篇自己的短总结：

- pretraining 解决什么问题
- SFT 解决什么问题
- preference / policy optimization 解决什么问题
- agent RL 为什么又是下一层

这篇总结会强迫你真的把概念区分开。
