---
title: Resume
permalink: /resume/
---

# Yue (Cassie) Liang

**Backend-oriented AI graduate student** — Java, Python, distributed systems, retrieval infrastructure.  
Targeting SDE roles at Amazon and comparable companies.

📧 liang.yue@northeastern.edu · [GitHub](https://github.com/cassieliang6709) · [Portfolio](https://cassieliang6709.github.io/personal_website/)

---

## Education

**Northeastern University** — M.S. in Artificial Intelligence  
Expected May 2027

**Shanghai University of Finance and Economics** — B.S. in Accounting

---

## Experience

### YouDescribe — Software Engineering Intern
*Nov 2025 – Present*

Built and shipped two features to production for an accessibility platform serving visually impaired users.

- **Playback Speed Simulator**: Identified a quality measurement gap (volunteers reviewed at 1x, users listen at 2x–3x). Built a React + TypeScript simulator wired into Google Cloud TTS; required volunteers to preview at 3x before submitting. Description quality scores improved, user-side feedback improved, without manual review.
- **AI-assisted authoring**: Integrated LLM drafting into the authoring flow to reduce cold-start friction for volunteers while preserving volunteer editorial control.

### Deloitte — Audit Data Analyst
*Jul 2023 – Jun 2024*

- Built a Python/pandas ETL pipeline to automate financial journal entry normalization and account mapping for audit engagements. Reduced data preparation time from 1–2 days to ~3 hours per engagement.
- Designed a rule-based mapping engine (hash map for exact match + regex fuzzy matching) with explicit exception routing — the system never silently passes low-confidence mappings.

---

## Projects

| Project | Stack | Summary |
|---|---|---|
| [OrderFlow](../projects/orderflow/) | Java, Spring Boot, PostgreSQL | Order lifecycle backend with saga-pattern rollback and idempotent payment handling |
| [FinancialReport](../projects/financial-report/) | Python, pandas, PostgreSQL | Financial data platform with multi-format ingestion, rule-based mapping, and exception routing |
| [MemoryOS](../projects/memoryos/) | FastAPI, React, pgvector | Semantic + keyword hybrid retrieval system for personal knowledge management |
| [YouDescribe](../projects/youdescribe/) | React, TypeScript, GCP TTS | Production accessibility tooling; playback simulator improved volunteer description quality |
| VisoCode | Python, LangGraph | Multi-agent system for natural language → animated video; won Most Technically Outstanding at AdventureX 2025 |
| AlgoMentor | Python, LLM | AI coding tutor with 3-level hint system designed to preserve learning without over-scaffolding |

---

## Skills

**Languages**: Java, Python, TypeScript, SQL  
**Backend**: Spring Boot, FastAPI, Node.js, REST APIs  
**Data**: PostgreSQL, pgvector, pandas, SQLAlchemy  
**AI/ML**: LangGraph, RAG systems, vector search, OpenAI API  
**Tools**: Docker, Git, Google Cloud, Testcontainers

---

## Positioning Notes

For Amazon SDE interviews, the strongest stories are:

- **Learn and Be Curious / Dive Deep**: VisoCode LangGraph refactor (read the source code when docs ran out)
- **Invent and Simplify / Deliver Results**: Deloitte ETL pipeline (2 days → 3 hours, explicit exception routing)
- **Customer Obsession / Ownership**: YouDescribe playback simulator (found the problem, built it, shipped it unprompted)
- **Invent and Simplify / Customer Obsession**: AlgoMentor hint system (behavior design, not just feature design)

Full BQ story bank: [Bilingual BQ Prep](../bq_prep/bilingual/)

---

[← Back to Home](../)
