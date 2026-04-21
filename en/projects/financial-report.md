---
title: FinancialReport
permalink: /projects/financial-report/
---

# FinancialReport

Financial data platform with ingestion, retrieval, validation, and report assembly.

## Overview

FinancialReport is a data pipeline and reporting backend that ingests heterogeneous financial data (CSV, Excel, JSON feeds), validates and normalizes it into a common schema, and assembles structured reports for downstream analysis. The core challenge is that source data is never clean: account names differ between clients, encoding is inconsistent, and column schemas vary by data source.

## Stack

- **Language**: Python 3.11
- **Data layer**: pandas, SQLAlchemy, PostgreSQL
- **Validation**: Pydantic schemas, custom rule engine
- **Ingestion**: multi-format parser (CSV, Excel, JSON)
- **Reporting**: Jinja2 templates, PDF export

## Key Design Decisions

**Three-layer ingestion pipeline** — Data flows through normalization → mapping → validation before reaching the report layer. Each layer has a clean interface so failures are isolated and retryable without reprocessing upstream steps.

**Rule-based account mapping with exception routing** — A hash map handles exact matches against a master taxonomy dictionary (O(1), covers ~75% of accounts). Regex-based fuzzy matching handles naming variations. Entries below a confidence threshold are routed to an exception log instead of silently passing — the system never guesses.

**Pydantic validation at the boundary** — All ingested records are validated against strict schemas before writing to the database. Invalid records are rejected with structured error messages, not silently coerced.

**Report assembly as a separate concern** — The report layer reads from the validated, normalized store. It never touches raw ingestion artifacts. This keeps the data model stable and makes report templates easy to test independently.

## Challenges

The trickiest part was the mapping engine's confidence threshold. Setting it too high sent too many records to exceptions (slow to review); too low let bad mappings through silently. The solution was a calibration pass against a labeled holdout set — we tuned the threshold to maximize F1 on the exception routing decision rather than just picking a round number.

The second challenge was encoding. Financial data from older accounting systems often arrives in Latin-1 or CP1252, not UTF-8. The normalization layer now detects encoding via `chardet` before parsing and logs the detected encoding as metadata.

## Results

- Mapping accuracy: ~94% of accounts auto-mapped correctly at the tuned threshold
- Data preparation time: reduced from ~2 days (manual) to ~3 hours per engagement
- Exception log review: reduced from 100% of records to ~10% requiring human judgment

---

[← Projects](../)
