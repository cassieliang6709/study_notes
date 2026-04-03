# Project Guide: ModelAlignmentFromScratch

原项目：

- https://github.com/Sherlock1956/ModelAlignmentFromScratch

---

## 这页为什么重要

这个项目的价值不在“又一个训练仓库”，而在于它让你第一次真正面对这个问题：

预训练之后，模型为什么还需要对齐？

如果你已经学过一点模型训练，但对下面这些词还是有点飘，这页就很重要：

- SFT
- Expert Iteration
- GRPO

它把这些东西从概念拉回到实现层。

---

## 你应该从它学到什么

不是“我知道几种 alignment 方法名字”。

你真正应该学到的是：

1. SFT、EI、GRPO 各自在优化什么
2. alignment 比 pretraining 多出来哪些部件
3. reward / grading / sampling 在训练里分别扮演什么角色
4. 为什么越往 agent 或 RL 方向走，系统越不稳定

---

## 最小认知链路

第一遍你应该能自己复述这条链路：

```text
prompt
-> model response
-> reward / grading / preference signal
-> objective based on that signal
-> parameter update
```

和普通预训练相比，多出来的关键不是“换了个 loss 名字”，而是训练信号来源变了。

---

## 为什么它值得在这个阶段做

这类项目最适合放在你已经有模型基础之后。

因为你必须先知道：

- 普通语言模型训练在干什么
- logits 和 loss 是怎么来的
- 一个标准 training loop 长什么样

否则你一看 alignment，只会觉得“它又多了一堆脚本”，但不知道本质差异是什么。

---

## 第一遍最该观察的四件事

### 1. 先看 SFT，不要先啃 GRPO

顺序很重要。

第一遍建议：

1. `sft.py`
2. `expert_iteration.py`
3. `GRPO.py`
4. reward / grader 相关文件

如果你一开始直接看 `GRPO.py`，大概率只会被流程复杂度淹没。

### 2. 每种方法的训练信号来自哪里

你至少要分清：

- SFT 是监督信号
- EI 是专家迭代式改进
- GRPO 更接近基于组内比较或奖励的优化

### 3. response sampling 在哪里发生

alignment 项目里，一个关键新增复杂度就是：

- 不是只算一次 forward 就结束
- 可能需要采样多个 response
- 然后再打分或比较

### 4. reward / grading 逻辑在哪里

第一遍必须定位到：

- reward 是怎么来的
- grader 在哪里
- 它如何反馈回训练目标

---

## 第一周不要做什么

这类项目最容易被“高级名词”带偏。

第一周不要做这些：

- 一上来就改 reward 设计
- 一上来就追训练效果
- 一上来就把 GRPO 当黑盒神技
- SFT 还没看懂，就硬看 RL 部分

第一周重点是建立对比框架，不是做优化。

---

## 第一周真正该做什么

### Day 1

- 跑通环境
- 看 README 和目录结构

### Day 2

- 精读 `sft.py`
- 写出 SFT 的输入、输出、loss

### Day 3

- 看 `expert_iteration.py`
- 记录它比 SFT 多了哪一层流程

### Day 4

- 看 `GRPO.py`
- 先画流程，不急着逐行深挖

### Day 5

- 找 reward / grader 相关逻辑
- 确认训练信号是怎么回到更新目标里的

### Day 6

- 写一张对比表：
  - SFT 优化什么
  - EI 优化什么
  - GRPO 优化什么

### Day 7

- 用自己的话复盘：
  - alignment 比 pretraining 多了什么
  - 为什么 response sampling 会让系统更复杂
  - 为什么 agent RL 往往更不稳定

---

## 你最该产出的东西

### 1. 一张方法对比表

最少包含三列：

- 训练信号来源
- 目标函数直觉
- 比 SFT 多出来的复杂度

### 2. 一条训练信号链路

```text
prompt -> sampled response -> reward / grading -> optimization objective -> update
```

### 3. 一段自己的解释

你要能说清：

“alignment 的核心不是把模型再训一遍，而是改变模型收到的训练信号，让它朝更符合任务目标或偏好的方向更新。”

---

## 常见误区

### 误区 1：把 GRPO 当成高级版 SFT

它们的训练信号和优化逻辑不是一回事。

### 误区 2：只看结果，不看 reward 来源

对齐训练里，reward 来源就是系统灵魂。

### 误区 3：没理解 baseline 就看高级方法

如果 SFT 都没讲清，后面的比较基本都不稳。

---

## 最小完成标准

你至少要做到下面三条中的两条：

- 能解释 SFT、EI、GRPO 各自在优化什么
- 能指出 reward / grader 相关逻辑的位置
- 能说清 alignment 相比 pretraining 多出来的关键部件

---

## 做完它以后该去哪

下一站建议去：

- [OpenPipe ART](./project_openpipe_art.md)

因为这时你已经有单模型 alignment 的基本框架，再去看更偏 agent RL 的训练系统，思路会顺很多。
