# Project Guide: OpenPipe ART

原项目：

- https://github.com/OpenPipe/ART

---

## 这页为什么重要

`ART` 不是普通微调框架，而是一个更接近 agent reinforcement training 的入口。

如果前面那些项目教你的是：

- 最小 RAG
- 小模型训练
- 单模型 alignment

那么这个项目开始逼你面对另外一种复杂度：

- 多步任务
- trajectory
- reward over interaction
- rollout-driven training

这就是它真正值得学的地方。

---

## 你应该从它学到什么

不是“又一个训练仓库怎么跑”。

你真正应该学到的是：

1. agent RL 和单轮回答训练的本质差别
2. rollout / trajectory 为什么会让训练复杂很多
3. reward 设计为什么直接决定 agent 行为
4. 一个框架到底在帮你管理哪些复杂度

---

## 最小 agent 训练链路

第一遍你至少要能自己复述这条链路：

```text
task
-> agent interacts over multiple steps
-> collect trajectory / rollout
-> compute reward or success signal
-> optimize policy based on that signal
```

和 SFT 最大的不同，不是“loss 名字变了”，而是训练对象从单次回答变成了多步行为。

---

## 为什么它必须放在后面

这个项目不适合当第一站。

因为你至少需要先理解这些东西：

- 一个标准语言模型训练 loop
- alignment 的基本训练信号
- reward / rollout / policy update 的基本直觉

否则你一看 agent RL，只会觉得“多了很多流程”，但抓不到本质。

---

## 第一遍最该观察的四件事

### 1. 任务是怎么定义的

先不要急着看训练结果。

你要先看：

- agent 在解决什么类型的任务
- 一次 episode 包含几步
- 成功或失败是怎么定义的

### 2. trajectory 是什么样子

这一步很关键。

你要知道：

- 每一步记录了什么
- 什么时候结束 rollout
- 哪些中间行为会影响最终 reward

### 3. reward 是怎么来的

agent 系统里，reward 不是装饰，它直接塑造行为。

你至少要定位到：

- reward 定义在哪里
- reward 是 sparse 还是 dense
- reward 和目标行为之间有什么映射

### 4. 框架帮你省掉了哪些事

这一类框架最值得学的，不只是 API，而是 abstraction。

你要看懂：

- 哪些是 task 层
- 哪些是 rollout 层
- 哪些是 optimization 层

---

## 第一周不要做什么

这类项目很容易让人误判复杂度。

第一周不要做这些：

- 一上来就追 benchmark
- 一上来就魔改 reward
- 一上来就扩大任务规模
- 还没看懂 trajectory，就开始调超参

第一周重点不是训出强 agent，而是把多步训练结构讲清楚。

---

## 第一周真正该做什么

### Day 1

- 跑通最小环境
- 确认最小 example 能工作

### Day 2

- 看任务定义
- 写出 agent 一次 episode 的开始、过程、结束

### Day 3

- 看 rollout / trajectory 结构
- 画出 agent 交互路径

### Day 4

- 找 reward 定义
- 写出 reward 在什么时刻产生、如何反馈

### Day 5

- 看 optimization 主流程
- 明确训练更新用到了哪些 rollout 信息

### Day 6

- 用自己的话比较：
  - agent RL 和 SFT 有什么不同
  - agent RL 和单模型 alignment 有什么不同

### Day 7

- 设计一个非常小的实验：
  - 一个简单任务
  - 一个朴素 reward
  - 一个你预期 agent 会改进的行为

---

## 你最该产出的东西

### 1. 一张 agent 训练流程图

```text
task -> rollout -> trajectory -> reward -> update
```

### 2. 一份抽象层说明

你至少要能分清：

- task abstraction
- rollout abstraction
- optimization abstraction

### 3. 一个小 reward 设计草稿

不一定要马上训练，但你要能写出：

- 目标行为是什么
- 什么信号说明它做对了
- reward 如何编码这个信号

---

## 常见误区

### 误区 1：把它当普通微调框架

多步行为训练的单位不是单条样本，而是 trajectory。

### 误区 2：只看结果，不看 reward

agent 学成什么样，通常先看 reward 定义，再看模型本身。

### 误区 3：任务结构都没讲清，就开始调参

这会让你永远不知道问题出在任务、reward 还是优化。

---

## 最小完成标准

你至少要做到下面三条中的两条：

- 能说清 agent RL 和单步 alignment 的区别
- 能解释 rollout / trajectory / reward 的关系
- 能指出这个框架最核心的两个到三个抽象层

---

## 做完它以后该做什么

这个项目更像这条线的高阶实践点。

做完它以后，最值得做的不是继续看更大框架，而是自己做一个极小实验：

- 设计一个简单多步任务
- 定义一个很朴素的 reward
- 看 agent 是否能学到更稳定的行为

到这一步，你才算真正开始把 agent RL 变成自己的东西。
