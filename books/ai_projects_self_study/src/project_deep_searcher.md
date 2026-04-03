# Project Guide: DeepSearcher

原项目：

- https://github.com/zilliztech/deep-searcher

---

## 这页为什么重要

`DeepSearcher` 不是最小教学 demo，而是更接近“可以拿来搭系统”的那类项目。

如果 `rag-from-scratch` 教你的是最小主链路，那么 `DeepSearcher` 教你的就是：

- 一个 RAG 系统怎么开始有工程分层
- provider、数据加载、查询流程怎么拆开
- 为什么 deep research / private data search 不只是“再接一个向量库”

这页的重点不是让你一下子全看懂，而是让你知道第一遍到底该盯哪里。

---

## 你应该从它学到什么

不是“我会跑一个更复杂的 RAG”。

你真正应该学到的是：

1. 数据加载和查询不是同一阶段
2. 可配置 provider 层为什么重要
3. 从 demo 走向系统时，会多出哪些工程层
4. 为什么 private data search 更像产品问题，而不只是模型问题

---

## 最小系统链路

第一遍你至少要能自己复述这条链路：

```text
collect documents
-> ingest / parse / chunk
-> embed and index
-> receive user query
-> retrieve relevant context
-> generate answer or report
```

如果连“加载阶段”和“查询阶段”都没分清，你其实还没开始理解这个项目。

---

## 它和基础 RAG 的关键差别

你做完 `rag-from-scratch` 再来看这个项目，应该主动比较：

### 1. 入口更多了

最小 RAG 一般只有 notebook 或单脚本。

这里你会开始遇到：

- Python API
- CLI
- 多种配置方式

### 2. 配置面更宽了

最小 demo 往往默认很多东西。

这里你要开始面对：

- LLM provider
- embedding provider
- vector store
- data source

### 3. 工程边界更清楚了

你要学会把系统拆成：

- 数据准备
- 索引构建
- 查询执行
- 结果组织

这一步很重要，因为从这里开始，你学的不是“RAG 例子”，而是“RAG 系统”。

---

## 第一遍最该观察的三件事

### 1. 文档是怎么进入系统的

不要先盯最终回答。

先看：

- 输入文档格式是什么
- ingestion 的入口在哪里
- 索引建立发生在什么阶段

### 2. query 执行路径是什么

你要知道一个 query 进入后经历了哪些层：

- query 输入
- 检索
- 上下文组织
- 回答或报告生成

### 3. 配置如何影响行为

第一轮不要换一堆 provider。

但你至少要看懂：

- 哪些参数决定模型侧行为
- 哪些参数决定检索侧行为
- 哪些参数只是工程接入层

---

## 第一周不要做什么

这类项目最容易把人带偏，因为它“看起来很完整”。

第一周不要做这些事：

- 一上来就换三种 provider 对比
- 一上来就想部署成服务
- 一上来就抓网页、接私有知识库、做报告自动化
- ingestion 还没跑通，就开始讨论 answer quality

第一周你只需要先跑通最小系统路径。

---

## 第一周真正该做什么

### Day 1

- 按 README 跑通最小环境
- 确认依赖、provider、配置项都能工作

### Day 2

- 只看最小 ingestion 流程
- 记录一份文档是怎么被加载进去的

### Day 3

- 跑一个最小 query
- 画出 query 的执行路径

### Day 4

- 换一小份自己的本地文档
- 确认不是只会跑示例数据

### Day 5

- 看一个 provider 配置点
- 解释这个配置改的是“模型层”还是“系统层”

### Day 6

- 比较它和基础 RAG demo 的结构差别
- 写出多出来的 3 个工程层

### Day 7

- 用自己的话复盘：
  - 这个项目到底在系统上比最小 RAG 多了什么
  - 如果你自己重写，先保留哪些层
  - 哪些层先不要做

---

## 你最该产出的东西

### 1. 系统分层图

```text
data source -> ingestion -> indexing -> query -> retrieval -> answer/report
```

### 2. 一份最小配置说明

你至少要能写清：

- LLM 用什么
- embedding 用什么
- 数据从哪里来
- query 从哪里发起

### 3. 一个对比结论

你要能讲清：

“这个项目和最小 RAG demo 的差别，不是只是功能更多，而是开始出现系统边界和配置边界。”

---

## 常见误区

### 误区 1：把复杂度误当成学习价值

复杂不等于更适合第一轮。

### 误区 2：provider 没配通就开始讨论架构

基础环境没跑通时，所有分析都很虚。

### 误区 3：只看回答，不看 ingestion

很多质量问题其实在数据进入系统的时候就已经决定了。

---

## 最小完成标准

你至少要做到下面三条中的两条：

- 能解释数据加载阶段和查询阶段的分工
- 能对自己的本地文档跑一条 query
- 能说清这个项目比基础 RAG demo 多出来的工程层

---

## 做完它以后该去哪

如果你想补模型本体理解，下一站去：

- [MiniMind](./project_minimind.md)

如果你想继续往更复杂的训练和 agent 方向走，后面再去：

- [OpenPipe ART](./project_openpipe_art.md)
