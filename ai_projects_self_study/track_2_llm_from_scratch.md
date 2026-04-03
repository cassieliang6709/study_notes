# Track 2: LLM From Scratch

这条线解决的是：

- 语言模型到底是怎么训练出来的
- tokenizer、embedding、attention、loss、sampling 到底怎么串起来
- 为什么很多“会调 API”的人，其实并不真的理解模型本体

---

## 这条线的正确顺序

1. [MiniMind](./project_minimind.md)
2. [Stanford CS336](./project_cs336.md)

---

## 为什么先 MiniMind 再 CS336

因为：

- `MiniMind` 更像低门槛实战入口
- `CS336` 更像系统课程 + 工程作业路线

如果一上来就直接啃 CS336，容易被系统深度和工作量压住。

---

## 每一站分别学什么

### 1. MiniMind

你在这里学：

- 小模型从零训练的完整感
- 训练脚本、tokenizer、模型结构、推理脚本怎么配合
- 在个人机器资源有限的情况下，如何理解 LLM 训练流程

做完应该能做到：

- 你能讲清楚一个超小语言模型是怎么被训练和使用的

### 2. CS336

你在这里学：

- language modeling 的系统知识
- 从 tokenizer 到 transformer 再到优化与系统层设计
- 真正课程级别的从零实现路径

做完应该能做到：

- 你不只是“知道 attention”，而是知道整条训练链路

---

## 这条线的重点

学这条线时，不要只看模型公式。

你要同时看三层：

1. 数学和概念
2. 代码实现
3. 训练系统与工程代价

---

## 正确的学习顺序

建议按下面顺序啃：

1. tokenizer
2. embedding
3. self-attention
4. transformer block
5. language modeling loss
6. training loop
7. inference / generation
8. scaling 和系统问题

---

## 这条线的完成标准

做到下面这些，才算真的入门：

- 你能自己讲一遍 decoder-only LM 的主链路
- 你知道 pretraining 的输入输出到底是什么
- 你能读懂一个小模型训练脚本，不只会运行
- 你能指出 tokenizer、context length、batch、optimizer 在训练中的作用

---

## 建议产出

学完这条线，建议你自己做一个最小项目：

- 手写一个极小 decoder-only transformer
- 在小语料上训练
- 跑一个最简单的文本生成 demo

重点不是效果多强，而是你真的自己走过一遍。
