title: "Project Guide: Complex RAG Guide"
---

# Project Guide: Complex RAG Guide

原项目：

- https://github.com/FareedKhan-dev/complex-RAG-guide

---

## 这个项目 / 学习主题的总结

`complex-RAG-guide` 的价值在于告诉你：真实 RAG 系统为什么会长出 cleaning、rewriting、filtering、planning、evaluation 这些层。它适合用来回答“最小 RAG 跑通以后，下一步复杂度到底从哪里来”。

## 本页在教什么

这页在教你怎么看“复杂 RAG”不是乱堆模块，而是针对不同失败点逐层补结构。

## Python 代码

```python
def rewrite_query(query: str) -> str:
    return query.replace("it", "the retrieved document")


def filter_docs(docs: list[str], keyword: str) -> list[str]:
    return [doc for doc in docs if keyword.lower() in doc.lower()]


query = "How do I use it safely?"
docs = [
    "The retrieved document should be cited in the answer.",
    "FastAPI app startup sequence.",
]

rewritten = rewrite_query(query)
filtered = filter_docs(docs, "document")
print(rewritten)
print(filtered)
```

## 时间复杂度

示例里主要做一次字符串处理和一次线性过滤，所以时间复杂度是 `O(n)`。

## 空间复杂度

过滤后的结果列表最多保留所有文档，所以空间复杂度是 `O(n)`。

## 怎么想到

复杂 RAG 的每一层都不是凭空加出来的，而是某个失败模式逼出来的。比如检索不稳，就会想到 query rewriting 或 filtering；回答不可信，就会想到 citation 和 evaluation。

## 示例 case

例子：用户问题里出现模糊代词 `it`，系统先把 query 改写得更明确，再过滤掉明显不相关文档。这样你就能看到“复杂度”其实是在修正系统失误。

## 常见 Follow-up

- 什么情况下值得加 query rewriting？
- filtering 和 reranking 在职责上有什么区别？
- evaluation 为什么是复杂 RAG 里迟早会补的一层？

## 这个项目最适合你学什么

这个项目适合你在基础 RAG 之后，继续看“复杂 RAG 管线怎么长出来”。

它比最小 demo 多了很多真实系统里常见的部件，比如：

- cleaning
- chunking
- filtering
- query rewriting
- planning / execution
- evaluation

---

## 为什么应该在这个阶段做它

因为很多人学 RAG 会卡在这一步：

- 已经知道向量检索和 prompt 拼接
- 但不知道为什么真实系统会有那么多额外模块

这个仓库正好把这些模块串起来。

---

## 前置知识

- 基础 RAG 主链路
- 向量检索的基本概念
- Notebook 式实验的习惯

---

## 先看什么

建议顺序：

1. README 里的 pipeline overview
2. `RAG_pipeline.ipynb`
3. helper functions
4. planner / re-planner / task handler 相关部分
5. evaluation 相关部分

---

## 第一周最小任务

1. 看懂 pipeline 分成哪几层
2. 跑通最小 notebook
3. 只挑 1 个增强点认真看

推荐第一遍只挑下面三个之一：

- query rewriting
- relevance filtering
- evaluation

不要第一次就想全部吃掉。

---

## 开做指南

### 环境要求

- Jupyter Notebook
- LangChain / LangGraph / 向量检索相关依赖
- LLM API key

### 最小启动动作

1. 安装依赖
2. 打开 notebook
3. 跑通一条最小问答流程
4. 记录每一步输入输出

### 第一遍不要改什么

- 不要先改 planner prompt
- 不要先加自己的全部复杂数据
- 不要一开始就研究所有 sub-graph

### 第二遍建议你改什么

- 自己换一份语料
- 对比不同 chunking
- 只保留你认为最有用的两个增强模块

---

## 你做完后应该掌握什么

- 知道复杂 RAG 为什么会出现 planner / executor
- 知道 retrieval 后还会有过滤、重写、校验
- 知道 evaluation 不是附属品，而是关键环节

---

## 常见卡点

- 过早陷入 LangGraph 结构，而忽略主链路
- 同时改太多模块，不知道效果变化来自哪里
- 只看回答结果，不看中间状态

---

## 最小完成标准

- 你能画出这个 pipeline 的主要节点
- 你能解释 planner 和 retriever 分别负责什么
- 你能拿一个小实验说明某个增强模块是否值得保留

---

## 下一站

建议下一步去：

- [RAG Techniques](./project_rag_techniques.md)
- [DeepSearcher](./project_deep_searcher.md)
