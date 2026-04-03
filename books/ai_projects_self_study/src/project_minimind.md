# Project Guide: MiniMind

原项目：

- https://github.com/jingyaogong/minimind

---

## 这页为什么重要

`MiniMind` 很适合做“模型本体第一站”。

如果你前面做了不少应用层项目，但总觉得自己对模型内部还是模糊的，这个项目的价值就会非常高。

它不是为了追求最强结果，而是为了让你第一次把这些东西连起来：

- tokenizer
- model
- training loop
- generation

这四个环节一旦连起来，你对 LLM 的理解会稳定很多。

---

## 你应该从它学到什么

不是“我也跑过一个小模型”。

你真正应该学到的是：

1. 文本是怎么变成 token 的
2. token 是怎么进模型的
3. logits 和 loss 是怎么来的
4. 训练脚本和推理脚本到底有什么不同

---

## 最小模型链路

第一遍你必须能自己复述这条链路：

```text
raw text
-> tokenizer
-> token ids
-> model forward
-> logits
-> loss
-> backward / optimizer step
```

如果这条链路讲不出来，就说明你还在“看代码”，不是“理解模型”。

---

## 为什么它适合作为第一站

它比完整课程项目更轻，但又不是纯概念材料。

这意味着：

- 你能真的跑起来
- 你能看到训练和推理的真实代码
- 你不会一开始就淹死在大规模系统复杂度里

对第一次学“LLM from scratch”的人来说，这个平衡非常好。

---

## 第一遍最该观察的四件事

### 1. tokenizer 在干什么

很多人只盯 attention，这是不够的。

你要先看：

- 文本怎么被切分
- vocab 在哪里定义
- token ids 是怎么送进模型的

### 2. model forward 输入输出是什么

你应该明确：

- 输入 tensor 的 shape 是什么
- 输出 logits 的 shape 是什么
- 为什么最后能算出 loss

### 3. training loop 由哪些部件组成

你至少要找出来：

- data loader
- optimizer
- loss calculation
- backward
- parameter update

### 4. generation 和 training 的差别

你要分清：

- 训练是在学参数
- generation 是在已有参数上做 token 采样

这是很多初学者一开始最模糊的地方。

---

## 第一周不要做什么

这类项目最常见的偏航方式有这些：

- 一上来就想训更大模型
- 一上来就追求结果好不好看
- 一上来就换复杂数据集
- 没搞清训练 loop，就直接研究 attention 细节

第一周重点不是“训得强”，而是“链路讲得清”。

---

## 第一周真正该做什么

### Day 1

- 跑通环境
- 记录仓库里最小训练或推理入口

### Day 2

- 看 tokenizer 流程
- 画出 text -> token ids 的过程

### Day 3

- 看 model forward
- 记录输入输出 tensor 的含义

### Day 4

- 看 training loop
- 写出 loss、backward、optimizer 的顺序

### Day 5

- 跑一次最小训练或最小推理
- 确认你不是只看代码

### Day 6

- 改一个小超参数
- 比如层数、hidden size、context length 或 batch 相关参数

### Day 7

- 用自己的话复盘：
  - tokenizer、model、loss、generation 的关系
  - 训练脚本和推理脚本的分工
  - 如果自己重写，先保留哪几个核心模块

---

## 你最该产出的东西

### 1. 一张训练链路图

```text
text -> tokenizer -> ids -> model -> logits -> loss -> backward -> optimizer
```

### 2. 一个模块说明表

至少列清：

- tokenizer
- model
- training script
- inference / generation script

### 3. 一个小实验记录

改一个小超参数，然后记：

- 改了什么
- 结果有什么变化
- 你猜为什么

---

## 常见误区

### 误区 1：只盯 attention

attention 很重要，但不是模型链路的全部。

### 误区 2：会运行就以为看懂了

真正的理解标准是你能解释数据怎么流过系统。

### 误区 3：一开始就想做“大训练”

第一次最重要的是可解释性，不是规模。

---

## 最小完成标准

你至少要做到下面三条中的两条：

- 能自己复述 text -> token -> logits -> loss 的主链路
- 能指出训练入口和推理入口分别在哪里
- 能改一个小超参数并解释变化

---

## 做完它以后该去哪

下一站建议去：

- [Stanford CS336](./project_cs336.md)

因为这时你已经有了最小模型训练的直觉，再去看系统课程内容会更稳，不会只剩一堆抽象概念。
