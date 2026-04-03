# Project Guide: rag-from-scratch

原项目：

- https://github.com/langchain-ai/rag-from-scratch

---

## 这个项目最适合你学什么

这是你做 RAG 的最好第一站之一。

它最适合帮你建立：

- 什么是最小 RAG 主链路
- 检索、上下文、生成之间的关系
- notebook 驱动的实验节奏

---

## 为什么应该最先做它

因为它足够轻，足够清楚。

它不会一开始就把你丢进巨大的系统设计里，而是先帮你把最关键的问题弄清楚：

- 文档怎么被检索出来
- 检索出来的内容怎么参与回答
- 哪些环节最值得先理解

---

## 前置知识

- Python
- 基础 LLM API 使用
- 最基本的 embedding / vector store 概念

---

## 先看什么

建议顺序：

1. 仓库 README
2. 最早期、最基础的 notebooks
3. 每个 notebook 之间新增了什么能力

第一遍不要贪多。

你的目标不是“一口气看完所有 notebook”，而是先建立主线。

---

## 第一周最小任务

第一周只做下面四件事：

1. 跑通一个最小 notebook
2. 画出 retrieval -> context -> answer 主链路
3. 改一个 prompt 或 retrieval 参数
4. 写下你观察到的变化

---

## 开做指南

### 环境要求

- Python
- Notebook 环境
- 一个可用的模型 API key

### 最小启动动作

1. 克隆仓库
2. 安装依赖
3. 打开最基础 notebook
4. 跑完整个 notebook
5. 修改一个小参数再跑一遍

### 第一遍不要改什么

- 不要急着加入自己的复杂数据
- 不要急着跳到后面的高级 notebook
- 不要先做 UI

### 第二遍建议你改什么

- 换一份自己的小文档
- 比较 chunk 大小
- 比较 top-k retrieval 数量

---

## 你做完后应该掌握什么

- 知道最小 RAG 是怎么搭起来的
- 知道什么叫 context grounding
- 知道为什么检索质量会直接影响回答

---

## 常见卡点

- 一开始就想追求复杂 agent RAG
- 只盯最终回答，不看检索结果
- 没做对照实验，学不到东西

---

## 最小完成标准

- 你能自己从头复述最小 RAG 流程
- 你能改一个参数并解释结果变化
- 你能把这个仓库里的最基础版本，用自己的话讲给别人听

---

## 下一站

下一步直接去：

- [Complex RAG Guide](./project_complex_rag_guide.md)

这样你会明显看出“复杂 RAG 比基础 RAG 多了哪些层”。
