title: "Track 1: RAG Systems"
---

# Track 1: RAG Systems

这条线解决的是：

- 怎么把外部知识接进 LLM
- 怎么让回答更 grounded
- 怎么从“简单问答”走到“复杂检索 + 推理 + 报告”

---

## 这个学习主线的总结

这条主线的核心不是把所有 RAG 仓库都看一遍，而是按难度和抽象层次逐步升级：先学最小链路，再看复杂组件，再建技术地图，最后接近系统形态。这样 beginner 才不会一开始就被复杂度淹没。

## 本页在教什么

这页在教你为什么 RAG 相关项目不能乱序看，以及每一站分别在补哪一层能力。

## Python 代码

```python
steps = ["retrieve", "build context", "generate answer"]
for step in steps:
    print(step)
```

## 时间复杂度

本页重点是学习路径设计，不以复杂度为重点。

## 空间复杂度

本页重点是学习路径设计，不以复杂度为重点。

## 怎么想到

RAG 相关资源太多时，最容易犯的错是按 star 数或热度乱看。更有效的顺序应该由“学习阻力”决定，而不是由“功能多少”决定。

## 示例 case

例子：先做 `rag-from-scratch`，你会先看懂主链路；再做 `complex-RAG-guide`，你才知道 rewriting、filtering 这些层为什么出现。

## 常见 Follow-up

- 为什么不建议 beginner 第一站就上 deep research 系统？
- 基础 RAG 和复杂 RAG 的分水岭是什么？
- 什么时候说明你已经可以从 demo 进入系统级项目？

## 这条线的正确顺序

1. [rag-from-scratch](./project_rag_from_scratch.md)
2. [complex-RAG-guide](./project_complex_rag_guide.md)
3. [rag_techniques](./project_rag_techniques.md)
4. [deep-searcher](./project_deep_searcher.md)

这不是按 star 排的，是按学习阻力排的。

---

## 每一站分别学什么

### 1. rag-from-scratch

你在这里学：

- 最基础的 RAG 主链路
- retrieval 和 generation 怎么连起来
- 最小 notebook 级实验方式

做完应该能做到：

- 自己写一个最小检索问答 demo

### 2. complex-RAG-guide

你在这里学：

- 更复杂的 chunking
- query rewriting
- filtering
- planning / execution
- evaluation

做完应该能做到：

- 不再把 RAG 理解成“向量库 + prompt”这么简单

### 3. rag_techniques

你在这里学：

- 不同 RAG 技术点的横向比较
- 什么技术适合什么场景
- 怎么做实验而不是只会抄 pipeline

做完应该能做到：

- 你知道可以优化哪一层，而不是只会换模型

### 4. deep-searcher

你在这里学：

- 更产品化的 deep research 结构
- private data search
- 更完整的配置、provider、vector DB 组合

做完应该能做到：

- 把 RAG 往“系统”而不是“demo”推进

---

## 这条线的核心知识图

从简单到复杂，可以理解成：

1. 检索到上下文
2. 把上下文喂给模型
3. 判断上下文够不够
4. 不够就改 query 或换 retrieval
5. 对结果做过滤、校验、评估
6. 最后做多步规划和报告生成

---

## 先别急着学的东西

如果你还没跑通第一个最小 RAG，不要急着碰这些：

- agentic RAG
- graph-based planning
- 很复杂的 reranking 组合
- 大而全的评估框架

先把主链路跑通。

---

## 这条线的完成标准

做到下面这些，才算真的学到：

- 你能解释 chunking 为什么会影响效果
- 你知道 retrieval quality 和 generation quality 不是一回事
- 你能比较简单 RAG 和复杂 RAG 的结构差别
- 你能自己做一个带引用或带 source attribution 的回答系统

---

## 建议产出

学这条线时，建议你最终自己做一个项目：

- 一个本地文档问答工具
- 一个课程笔记检索助手
- 一个 PDF / 网页混合检索问答器

要求不要大，但必须自己配数据、自己跑检索、自己看效果。
