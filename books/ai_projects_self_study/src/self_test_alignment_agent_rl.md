title: "自测题：Alignment / Agent RL"
---

# 自测题：Alignment / Agent RL

这份题主要检查你有没有把：

- pretraining
- SFT
- preference optimization
- agent RL

区分开。

---

## Part 1: 基础区分

### 1.

为什么模型完成 pretraining 后，通常还不够“好用”？

### 2.

SFT 在解决什么问题？

### 3.

SFT 没有解决什么问题？

### 4.

为什么 alignment 不能简单理解成“让模型更像人说话”？

---

## Part 2: 方法理解

### 5.

`Expert Iteration` 的核心想法是什么？

### 6.

`GRPO` 和普通 supervised fine-tuning 的区别是什么？

### 7.

reward 在 alignment 里扮演什么角色？

### 8.

为什么 sampling 会影响 alignment 的训练结果？

### 9.

为什么多步 agent 任务会比单步问答更难训练？

### 10.

trajectory 在 agent RL 里为什么重要？

---

## Part 3: 项目对应题

### 11.

`ModelAlignmentFromScratch` 最值得你学的是什么？

### 12.

这个项目里为什么建议先读 `sft.py`，不要一开始就冲 `GRPO.py`？

### 13.

`OpenPipe ART` 和普通对齐项目相比，更强调什么？

---

## Part 4: 动手题

### 14.

请你自己写一张表，对比：

- pretraining
- SFT
- EI
- GRPO
- agent RL

字段至少包含：

- 输入数据
- 优化目标
- 输出能力

### 15.

如果一个 agent 在多步任务里表现不稳定，你会怀疑哪几类问题？

### 16.

如果让你自己设计一个最小 agent RL 任务，你会怎么定义：

- task
- reward
- success criterion

---

## 自评分标准

每题：

- `2 分`：能说清楚，还能和项目代码联系起来
- `1 分`：概念知道，但边界模糊
- `0 分`：不会

总分：

- `13 分以上`：说明你已经开始真正理解 alignment
- `8 到 12 分`：说明概念初步建立，但还需要再看实现
- `7 分以下`：建议先回到 `ModelAlignmentFromScratch`
