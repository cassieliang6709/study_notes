---
title: OrderFlow
permalink: /projects/orderflow/
---

# OrderFlow

Java Spring Boot backend for order lifecycle, inventory, and payment workflows.

## Overview

OrderFlow is a backend service that manages the full lifecycle of an e-commerce order: creation, inventory reservation, payment processing, fulfillment state transitions, and cancellation with rollback. The system is designed around correctness and consistency — every state transition is explicit, logged, and recoverable.

## Stack

- **Language**: Java 17
- **Framework**: Spring Boot 3, Spring Data JPA
- **Database**: PostgreSQL (transactions, row-level locking)
- **Messaging**: (async event publishing for downstream consumers)
- **Testing**: JUnit 5, Mockito, Testcontainers

## Key Design Decisions

**State machine for order lifecycle** — Orders move through a fixed set of states (`CREATED → RESERVED → PAID → FULFILLED → CANCELLED`). Transitions are validated at the service layer so invalid moves (e.g., paying a cancelled order) are rejected before hitting the database.

**Inventory reservation with optimistic locking** — Instead of a simple decrement, inventory reservation uses a two-phase approach: `RESERVED` before payment confirmation, `COMMITTED` after. This prevents overselling under concurrent load without holding long-lived locks.

**Idempotent payment handler** — Payment events are deduplicated by idempotency key so retried requests (from network failures or client retries) don't result in double charges.

**Compensating transactions for rollback** — Cancellation triggers compensating writes (release inventory, void payment hold) rather than hard deletes, preserving audit history.

## Challenges

The hardest problem was handling partial failures in the payment → inventory → fulfillment sequence. If payment succeeds but inventory commit fails, the system needs to rollback payment without user-visible inconsistency. The solution was a local saga pattern: each step writes a rollback record before executing, so a background reconciler can finish or undo incomplete transactions after a crash.

## Results

- Order creation and state transitions: <5ms p99 under load testing
- Zero oversell events in concurrent stress tests (100 concurrent reservation requests on a single SKU with quantity 1)
- Rollback coverage: all failure paths tested with Testcontainers + simulated partial failures

---

[← Projects](../)
