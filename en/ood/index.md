---
title: OOD
---

# Object-Oriented Design

Practice cases for OOD interview questions — from class structure to full system modeling.

## Cases

- [Amazon Locker](./amazon_locker/)
- [Parking Lot](./parking_lot/)
- [Elevator System](./elevator_system/)

## Core Concepts

**Single Responsibility** — each class has one reason to change. If a class handles both storage logic and notification, split it.

**Encapsulation** — hide state, expose behavior. Callers shouldn't need to know how something is stored, only what it can do.

**Open/Closed** — open for extension (add new types), closed for modification (don't touch existing logic). Use inheritance or composition.

**Dependency Inversion** — high-level modules shouldn't depend on low-level details. Depend on abstractions (interfaces), not concrete implementations.

## OOD Interview Pattern

1. Clarify requirements — ask about actors, constraints, scale
2. Identify core entities — nouns in the problem statement
3. Define relationships — has-a vs is-a, one-to-many vs many-to-many
4. Assign responsibilities — which class owns which behavior
5. Consider edge cases — concurrent access, state transitions, invalid inputs

## Amazon Locker — Key Design

Three layers: `LockerSystem` (manager) → `LockerBank` (location) → `Locker` (unit).

State machine: `AVAILABLE → RESERVED → OCCUPIED → AVAILABLE`.

Key decisions:
- The system assigns a locker by size fit, not first-available — this requires a size-bucketed lookup structure.
- Package pickup uses a code, not a user reference — decouples the delivery and pickup actors.
- Locker expiry is handled by a background sweep, not inline on every operation.

## Parking Lot — Key Design

Three layers: `ParkingLot` → `ParkingFloor` → `ParkingSpot`.

Spot types: `COMPACT`, `LARGE`, `HANDICAPPED`, `MOTORCYCLE`.

Key decisions:
- Each floor owns its spots and tracks availability independently — avoids a central bottleneck.
- Ticket is issued at entry, closed at exit — the ticket holds the entry time for fee calculation.
- Fee strategy is injected (strategy pattern) so the pricing model can change without touching the lot logic.

## Elevator System — Key Design

Entities: `ElevatorController`, `Elevator`, `Floor`, `Request`.

Key decisions:
- Controller uses a SCAN algorithm (sweep up, sweep down) to minimize direction changes.
- Requests are queued per direction, not per elevator — the controller dispatches.
- Each elevator tracks its own state (`IDLE`, `MOVING_UP`, `MOVING_DOWN`, `DOOR_OPEN`).
