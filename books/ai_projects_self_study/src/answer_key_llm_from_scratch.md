title: "参考答案：LLM From Scratch"
---

# 参考答案：LLM From Scratch

对应题目：

- [LLM From Scratch 自测题](./self_test_llm_from_scratch.md)

---

## 1.

最粗的主链路是：

- 文本先被 tokenizer 切成 token
- token 变成 embedding
- embedding 经过多层 transformer block
- 输出每个位置对应的 logits
- 根据 logits 预测下一个 token

---

## 2.

tokenizer 负责把原始文本变成模型可处理的离散 token 序列。

它本质上定义了：

- 模型看世界的最小单位是什么

---

## 3.

因为 tokenizer 会影响：

- 序列长度
- 词片切分方式
- 稀有词处理
- 训练和推理效率

它不是边角料，而是输入表示的一部分。

---

## 4.

embedding 层负责把离散 token id 映射到连续向量空间。

这样模型才能在向量空间里学习模式。

---

## 5.

self-attention 的核心价值是：

- 每个 token 在计算表示时，可以动态参考其他 token

这让模型能建模长距离依赖。

---

## 6.

训练目标通常是：

- 根据前面的 token，预测下一个 token

---

## 7.

因为 language model 的训练数据天然可以转成：

- 输入前缀
- 目标下一个 token

这使得预训练能在海量文本上自监督进行。

---

## 8.

核心部件通常包括：

- 数据加载
- tokenizer
- model
- loss
- optimizer
- training loop
- checkpoint / logging

---

## 9.

因为这些超参会影响：

- 梯度估计稳定性
- 有效上下文长度
- 收敛速度
- 显存消耗

---

## 10.

训练入口更关注：

- 前向
- loss
- 反向传播
- 参数更新

推理入口更关注：

- 给定 prompt
- 逐步采样生成 token

---

## 11.

`MiniMind` 最适合帮你建立：

- 小模型完整链路的直觉

---

## 12.

`CS336` 和普通教程的区别是：

- 它更系统
- 更接近课程和作业驱动
- 不只讲概念，也强调实现和工程视角

---

## 13.

因为你先有了一个小模型的整体感，再去看系统课程时，不会只剩抽象名词。

---

## 14.

合格图里至少要包括：

- tokenizer
- embeddings
- transformer blocks
- logits
- sampling

---

## 15.

一个合理实现顺序可以是：

1. tokenizer
2. dataset / dataloader
3. embeddings
4. transformer block
5. LM head
6. loss
7. training loop
8. generation

---

## 16.

训练不收敛时，优先怀疑：

- 数据 / tokenizer 问题
- 学习率 / optimizer / batch 问题
- 实现 bug

---

## 17.

pretraining 学到的是：

- 语言模式
- 统计共现
- 一般性的文本建模能力

它没有直接解决：

- 指令服从
- 人类偏好
- 多步 agent 行为稳定性
