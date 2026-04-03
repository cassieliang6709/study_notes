---
title: "Project Guide: Complex RAG Guide"
---

# Project Guide: Complex RAG Guide

原项目：

- https://github.com/FareedKhan-dev/complex-RAG-guide

---

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
