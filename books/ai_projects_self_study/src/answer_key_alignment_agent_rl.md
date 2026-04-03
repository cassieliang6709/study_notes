title: "参考答案：Alignment / Agent RL"
---

# 参考答案：Alignment / Agent RL

对应题目：

- [Alignment / Agent RL 自测题](./self_test_alignment_agent_rl.md)

---

## 1.

因为 pretraining 主要学的是：

- 语言模式
- 下一个 token 预测

但这不自动等于：

- 听话
- 符合偏好
- 稳定完成多步任务

---

## 2.

SFT 主要解决：

- 让模型学会按示例格式和目标行为输出

---

## 3.

SFT 没完全解决：

- 长期偏好优化
- 多候选之间的相对优劣
- 多步行为稳定性

---

## 4.

因为 alignment 不只是“更像人类说话”。

它更关心：

- 是否符合任务目标
- 是否更符合偏好
- 是否减少不想要的行为

---

## 5.

Expert Iteration 的核心想法是：

- 先生成候选
- 筛掉高质量样本
- 再用这些更好的样本继续训练

---

## 6.

GRPO 和 SFT 的区别在于：

- SFT 直接在给定 target 上监督学习
- GRPO 更强调基于奖励或相对优劣来优化策略

---

## 7.

reward 负责把“什么更好”变成可优化的训练信号。

---

## 8.

因为训练要基于采样到的响应来估计好坏。

如果采样分布变了：

- 奖励分布会变
- 更新方向也会变

---

## 9.

多步 agent 更难，因为它涉及：

- 长轨迹
- 中间步骤误差累积
- 奖励分配更复杂

---

## 10.

trajectory 重要，因为 agent 的质量不只在最后一句话，而在整段交互过程。

---

## 11.

`ModelAlignmentFromScratch` 最值得学的是：

- 把 SFT、EI、GRPO 具体落到实现层

---

## 12.

因为 SFT 是最基础 baseline。

先看它，才能看懂后面的高级方法到底多了什么。

---

## 13.

`OpenPipe ART` 更强调：

- agent task
- 多步 interaction
- rollout / reward / training 的结合

---

## 14.

合格表至少能区分：

- pretraining：学语言模式
- SFT：学示例行为
- EI：筛高质量样本后迭代提升
- GRPO：基于相对奖励优化策略
- agent RL：优化多步任务行为

---

## 15.

优先怀疑：

- reward 设计不合理
- 任务定义不清
- rollout 质量差
- credit assignment 难

---

## 16.

一个最小 agent RL 任务可以这样定义：

- task：完成一个简单多步查询或工具调用
- reward：任务是否成功、步骤是否合理
- success criterion：成功率是否提升、轨迹是否更稳定
