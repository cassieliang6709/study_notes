---
title: "Project Guide: DeepSearcher"
---

# Project Guide: DeepSearcher

原项目：

- https://github.com/zilliztech/deep-searcher

---

## 这个项目最适合你学什么

`DeepSearcher` 更像一个“可配置的 deep research / private data search 系统”，不是最小教学 demo。

你在这里主要学：

- private data search 的系统结构
- LLM、embedding、vector DB 的模块化配置
- 从本地文件 / 网页加载数据，再做查询和报告生成

---

## 为什么应该在这个阶段做它

它适合放在你已经学过基础 RAG 之后。

原因很直接：

- 它的配置面更宽
- 支持多种 provider
- 更接近真实系统，而不是 notebook 教程

如果你还没做过基础 RAG，先去做：

- [rag-from-scratch](./project_rag_from_scratch.md)
- [complex-RAG-guide](./project_complex_rag_guide.md)

---

## 前置知识

- 基本 RAG 主链路
- embedding 和 vector DB 是什么
- Python 环境管理
- API key / provider 配置

---

## 先看什么

第一遍不要到处翻。

建议顺序：

1. README 的 `Quick Start`
2. README 里的 `Configuration`
3. README 里的 `CLI Mode`
4. 仓库里的 `examples/`
5. 顶层 `main.py`
6. `deepsearcher/` 主包结构

---

## 第一周最小任务

目标不是自定义全部 provider。

第一周只做这几件事：

1. 本地创建虚拟环境
2. 安装项目
3. 配一个最简单的 LLM + embedding
4. 加载一份本地文档
5. 跑一次 query

如果这 5 步没通，不要碰高级配置。

---

## 开做指南

### 环境要求

- Python 3.10 左右
- 一个可用的 LLM provider key
- 一个可用的 embedding 配置

### 最小启动动作

按 README 的 quick start 跑最小版本：

1. 建 `.venv`
2. `pip install deepsearcher` 或开发模式安装
3. 配环境变量
4. 用 `load_from_local_files(...)` 加载数据
5. 用 `query(...)` 提问

### 第一遍不要改什么

- 不要先换 3 种向量库
- 不要先改内部模块
- 不要先部署 web service

### 第二遍建议你改什么

- 换一份自己的文档数据
- 比较不同 embedding / LLM provider
- 试 CLI 和 Python API 两种入口

---

## 你做完后应该掌握什么

- 知道一个可扩展 RAG 系统如何拆 provider 层
- 知道 offline loading 和 online querying 是两步
- 知道 demo 级 RAG 和系统级 RAG 的差别

---

## 常见卡点

- provider key 没配全
- embedding 和 LLM 配置不匹配
- 文档加载阶段还没通，就急着查 query 质量
- 一开始就想支持网页抓取、全部格式、全部后端

---

## 最小完成标准

- 你能对自己的本地文档跑出一条 query
- 你能解释数据加载和查询阶段分别发生了什么
- 你能说清这个系统比基础 RAG demo 多了哪些工程层设计

---

## 下一站

如果你做完这个项目，建议下一步去：

- [MiniMind](./project_minimind.md) 如果你想补模型基础
- [OpenPipe ART](./project_openpipe_art.md) 如果你想看更复杂的训练框架
