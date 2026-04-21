---
title: MemoryOS
permalink: /projects/memoryos/
---

# MemoryOS

Retrieval-focused product system with FastAPI, React, PostgreSQL, and pgvector.

## Overview

MemoryOS is a personal memory management system: users store notes, experiences, and knowledge fragments, and retrieve them via semantic search. The backend handles ingestion, embedding, vector storage, and ranked retrieval. The frontend provides a simple interface for capture and search. The core design goal was retrieval quality — not just returning results, but returning the right results with explainable relevance.

## Stack

- **Backend**: Python, FastAPI, SQLAlchemy
- **Database**: PostgreSQL + pgvector extension
- **Embeddings**: OpenAI `text-embedding-3-small` (swappable interface)
- **Frontend**: React, TypeScript
- **Search**: hybrid — vector similarity + keyword filter
- **Deployment**: Docker Compose

## Key Design Decisions

**pgvector over a dedicated vector DB** — Keeping embeddings in PostgreSQL alongside relational metadata avoids the operational complexity of a separate vector database. The `ivfflat` index handles search at this scale. If the dataset grows past a few million records, migrating to a dedicated store is straightforward because the embedding interface is abstracted.

**Hybrid retrieval** — Pure vector search returns semantically similar results but can miss exact-match keyword queries. Pure keyword search misses paraphrase and concept overlap. The system runs both in parallel and merges results by a weighted score, with the keyword filter acting as a hard gate for time-based or tag-based constraints.

**Chunking strategy** — Long notes are chunked by paragraph with 10% overlap. Each chunk stores a back-reference to the source document. Retrieval returns chunks, but the UI always surfaces the full document context so users aren't shown fragments without origin.

**Embedding model as a dependency** — The embedding client is injected at startup. Swapping from OpenAI to a local model (e.g., `sentence-transformers`) requires changing one config value, not refactoring call sites.

## Challenges

The hardest retrieval problem was temporal relevance: a semantically close result from 3 years ago is often less useful than a moderately relevant result from last week. Adding a recency decay factor to the ranking score helped, but the right decay coefficient required tuning against real user feedback rather than a principled formula.

The second issue was chunking granularity. Chunks too small lost context; chunks too large diluted the embedding signal. Paragraph-level chunking with overlap was a reasonable default but the system exposes chunk size as a configurable parameter.

## Results

- Semantic search latency: <100ms p95 for collections up to ~50k chunks (pgvector ivfflat, single-node Postgres)
- Retrieval precision: qualitatively improved with hybrid search vs. vector-only on a test set of 200 queries
- Full stack running in Docker Compose with one `docker compose up`

---

[← Projects](../)
