---
title: 简历
permalink: /resume/
---

# 梁玥（Cassie Liang）

**后端方向 AI 研究生** — Java、Python、分布式系统、检索基础设施。  
求职方向：Amazon 及同等公司 SDE 岗位。

📧 liang.yue@northeastern.edu · [GitHub](https://github.com/cassieliang6709) · [个人主页](https://cassieliang6709.github.io/personal_website/)

---

## 教育背景

**东北大学（Northeastern University）** — 人工智能硕士  
预计 2027 年 5 月毕业

**上海财经大学** — 会计学学士

---

## 工作经历

### YouDescribe — 软件工程实习生
*2025 年 11 月 – 至今*

为服务视障用户的无障碍平台开发并上线两个功能。

- **播放速度模拟器**：发现质量衡量漏洞（志愿者按 1x 审听，用户实际以 2x–3x 收听）。用 React + TypeScript 开发模拟器并接入 Google Cloud TTS；要求志愿者提交前必须以 3x 试听。描述质量分上升，用户侧反馈改善，无需人工审核介入。
- **AI 辅助创作**：将 LLM 草稿生成集成进创作流程，降低志愿者冷启动门槛，同时保留志愿者的编辑主导权。

### 德勤（Deloitte）— 审计数据分析师
*2023 年 7 月 – 2024 年 6 月*

- 用 Python/pandas 构建自动化 ETL 流水线，用于审计 engagement 中财务分录数据的规范化和科目映射。每个 engagement 的数据准备时间从 1–2 天缩短至约 3 小时。
- 设计基于规则的映射引擎（hash map 精确匹配 + 正则 fuzzy matching），配显式异常路由——系统不会对低置信度映射静默通过。

---

## 项目

| 项目 | 技术栈 | 简介 |
|---|---|---|
| [OrderFlow](../projects/orderflow/) | Java、Spring Boot、PostgreSQL | 带 saga 回滚和幂等支付的订单生命周期后端 |
| [FinancialReport](../projects/financial-report/) | Python、pandas、PostgreSQL | 多格式接入 + 规则映射 + 异常路由的财务数据平台 |
| [MemoryOS](../projects/memoryos/) | FastAPI、React、pgvector | 用于个人知识管理的语义 + 关键词混合检索系统 |
| [YouDescribe](../projects/youdescribe/) | React、TypeScript、GCP TTS | 生产无障碍工具；播放速度模拟器提升了描述质量 |
| VisoCode | Python、LangGraph | 自然语言转教学动画的 multi-agent 系统；AdventureX 2025 最佳技术奖 |
| AlgoMentor | Python、LLM | 带三层提示系统的 AI 编程辅导工具，防止过度依赖答案 |

---

## 技术能力

**语言**：Java、Python、TypeScript、SQL  
**后端**：Spring Boot、FastAPI、Node.js、REST API  
**数据**：PostgreSQL、pgvector、pandas、SQLAlchemy  
**AI/ML**：LangGraph、RAG 系统、向量搜索、OpenAI API  
**工具**：Docker、Git、Google Cloud、Testcontainers

---

## Amazon 面试定位

最强故事对应关系：

- **Learn and Be Curious / Dive Deep**：VisoCode LangGraph 重构（文档不够用时直接看源码）
- **Invent and Simplify / Deliver Results**：德勤 ETL 流水线（2 天 → 3 小时，显式异常路由）
- **Customer Obsession / Ownership**：YouDescribe 播放速度模拟器（自己发现问题、开发、上线，不在 sprint 里）
- **Invent and Simplify / Customer Obsession**：AlgoMentor 提示系统（行为设计，不只是功能设计）

完整故事库：[行为面试准备](../bq_prep/)

---

[← 返回首页](../)
