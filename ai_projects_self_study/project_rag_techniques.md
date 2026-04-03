# Project Guide: RAG Techniques

原项目：

- https://github.com/NirDiamant/rag_techniques

---

## 这个项目最适合你学什么

这个仓库更像一套 RAG 技术实验库。

它非常适合你在已经懂基础 RAG 后，继续回答这类问题：

- 除了最基础 pipeline，还有哪些常见变体
- 各种技术点分别在优化哪一层
- 我应该在什么场景下选哪种方法

---

## 为什么应该在这个阶段做它

你做完基础 RAG 后，最容易出现的假象是：

- 以为 RAG 已经学完了

但其实后面还有很多技术变化：

- retrieval strategy
- reranking
- chunking variations
- query transformation
- hybrid ideas

这个仓库适合帮你建立“技术地图”。

---

## 前置知识

- 已跑过一个最小 RAG demo
- 最好已看过 [rag-from-scratch](./project_rag_from_scratch.md)
- 最好已接触过 [complex-RAG-guide](./project_complex_rag_guide.md)

---

## 先看什么

不要打算一次性看完整仓库。

推荐做法：

1. 先看目录，按主题分类
2. 只挑 3 个你最关心的 technique
3. 每个 technique 都回答“它在优化哪一层”

---

## 第一周最小任务

第一周建议你只选三类：

1. chunking 类
2. retrieval enhancement 类
3. evaluation / reranking 类

每类只看一个代表性 notebook 或文档。

---

## 开做指南

### 环境要求

- Notebook 环境
- 基础 RAG 运行经验

### 最小启动动作

1. 克隆仓库
2. 浏览整体结构
3. 选 3 个 technique
4. 对每个 technique 做一页笔记

### 第一遍不要改什么

- 不要想“全部学完”
- 不要每个 notebook 都跑
- 不要在没分类的情况下碎片化吸收

### 第二遍建议你改什么

- 选择一个 technique 拿自己的数据做实验
- 和基础 RAG 做一次对照

---

## 你做完后应该掌握什么

- 知道 RAG 不是单一技术，而是一组可组合策略
- 知道什么是“问题在哪一层，就改哪一层”
- 知道如何系统比较不同 technique

---

## 常见卡点

- 把仓库当成百科全书，结果什么都没真正做
- 看了很多 technique，但没有对照实验
- 不区分“值得学”和“适合当前阶段”

---

## 最小完成标准

- 你能说出 3 到 5 种 RAG enhancement technique
- 你能解释它们分别在解决什么问题
- 你能选出 1 到 2 个最值得自己复现的技巧

---

## 下一站

做完后建议去：

- [DeepSearcher](./project_deep_searcher.md)

这样你会更容易把 techniques 映射到真实系统里。
