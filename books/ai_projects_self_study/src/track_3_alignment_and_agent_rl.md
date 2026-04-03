title: "Track 3: Alignment And Agent RL"
---

# Track 3: Alignment And Agent RL

这条线解决的是：

- 预训练后的模型为什么还不够好用
- 怎么通过 SFT、偏好优化、RL 让模型更符合目标
- 多步 agent 为什么需要专门训练，而不是只靠 prompt

---

## 这个学习主线的总结

这条主线解决的是“模型为什么在预训练后还不够可用”。它会带你从单模型对齐走到多步 agent 强化训练，让你看到稳定性和奖励设计为什么会变成核心问题。

## 本页在教什么

这页在教你为什么要先理解 SFT / 偏好优化，再去理解 agent RL，而不是一上来直接看最复杂的 rollout 框架。

## Python 代码

```python
preferences = {"response_a": 1, "response_b": 0}
chosen = max(preferences, key=preferences.get)
print(chosen)
```

## 时间复杂度

本页重点是训练思路，不以复杂度为重点。

## 空间复杂度

本页重点是训练思路，不以复杂度为重点。

## 怎么想到

alignment 最容易让人困惑的地方，是一堆训练名词并排出现。更稳的方法是按问题难度排序：先理解单步偏好，再理解多步奖励，这样 agent RL 的复杂度才不会显得跳跃。

## 示例 case

例子：如果两个回答里一个更符合偏好标注，系统会更倾向保留高分回答。再往后，agent RL 只是把这个选择问题扩展到多步轨迹上。

## 常见 Follow-up

- SFT、偏好优化、GRPO 的差别怎么用一句话讲清？
- 为什么 agent 任务训练更不稳定？
- reward model 和 grader 在实践里分别扮演什么角色？

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
