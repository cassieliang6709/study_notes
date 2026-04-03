# 自测题：LLM From Scratch

这份题是检查你有没有真正开始理解“模型本体”。

---

## Part 1: 主链路理解

### 1.

一个 decoder-only language model，从输入文本到输出下一个 token，中间大致发生了什么？

### 2.

tokenizer 在整个系统里到底负责什么？

### 3.

为什么 tokenizer 不是“可有可无的小细节”？

### 4.

embedding 层在做什么？

### 5.

self-attention 为什么是 transformer 的核心？

---

## Part 2: 训练理解

### 6.

language model training 里的训练目标是什么？

### 7.

为什么 pretraining 本质上是一个“预测下一个 token”的问题？

### 8.

训练脚本里通常至少会有哪几个核心部件？

### 9.

为什么 batch size、sequence length、learning rate 都会影响训练？

### 10.

训练和推理的代码入口，通常有什么不同？

---

## Part 3: 项目对应题

### 11.

`MiniMind` 最适合帮你建立什么直觉？

### 12.

`CS336` 和一个普通教程最大的区别是什么？

### 13.

如果你已经跑通 `MiniMind`，为什么接着看 `CS336` 会更稳？

---

## Part 4: 动手题

### 14.

请你画一个最小 decoder-only LM 的结构图。

至少要有：

- tokenizer
- embeddings
- transformer blocks
- logits
- sampling / generation

### 15.

如果让你自己写一个极小语言模型实验，你会按什么顺序实现？

### 16.

如果模型训练不收敛，你会优先检查哪三类问题？

### 17.

请你解释：

- pretraining 学到了什么
- 它没有解决什么

---

## 自评分标准

每题：

- `2 分`：能自己解释，还能连接到代码
- `1 分`：知道概念，但和代码连不起来
- `0 分`：不会

总分：

- `14 分以上`：说明你已经有模型主链路意识
- `9 到 13 分`：说明概念有了，但实现层还不够稳
- `8 分以下`：建议回到 `MiniMind` 和 `CS336` 的基础部分
