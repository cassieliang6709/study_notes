---
title: BQ Prep
---

# Behavioral Interview Prep

Four stories mapped to Amazon Leadership Principles.

## Story Bank

### Story 1 — VisoCode: LangGraph Refactor
**LPs: Learn and Be Curious · Invent and Simplify**

At AdventureX 2025, I was building VisoCode, a multi-agent system that turned plain English into animated educational videos. The main issue was that agents kept calling each other in circles because we had no real state management — on complex prompts the pipeline would spin forever and crash. We had less than two days before the demo.

I started by asking what was the minimum I actually needed to understand right then. I focused on two concepts: state management and conditional edges. I spent about an hour in a Jupyter notebook building toy examples until those clicked, then touched the real code. During the refactor I found a second issue: memory usage kept growing on retries. The docs didn't explain it, so I went directly into LangGraph's source code, traced how messages were accumulated, and found there was no truncation by default. I wrote a custom routing function with a retry counter and context truncation so the graph would exit cleanly instead of looping forever.

**Result:** ~50% improvement in video generation success rate, complete elimination of infinite loops, stable enough for a live demo. We won Most Technically Outstanding at AdventureX 2025.

**Best for:** learn quickly, dive deep technically, redesign instead of patch, deliver under time pressure.

---

### Story 2 — AlgoMentor: 3-Level Hint System
**LPs: Invent and Simplify · Customer Obsession**

When building AlgoMentor, an AI coding tutor, I started by talking to friends grinding LeetCode. The pattern was consistent: LeetCode hints come as one big block, so people use them the same way every time — get stuck, click, read the approach, write the answer. But people actually get stuck at three different levels: concept, strategy, and implementation. Existing hints treated all three as the same problem.

I built a three-level structure: level one was a Socratic question for concept, level two gave directional guidance for strategy, level three gave pseudocode structure for implementation. I added friction gates between levels — started with a five-minute delay, adjusted to two minutes after user feedback. I used separate prompts and strict constraints for each level so the model literally couldn't reveal too much too early.

**Result:** Users stopped blasting through all hints at once and started working through problems step by step.

**Best for:** invent and simplify, customer obsession, product thinking, behavior design.

---

### Story 3 — YouDescribe: Playback Speed Simulator
**LPs: Customer Obsession · Ownership**

At YouDescribe, volunteers write audio descriptions for YouTube videos for visually impaired users. I noticed a hidden gap: volunteers reviewed at 1x speed, but many real users listen at 2x or 3x. A description that sounded fine at 1x could feel rushed and hard to follow at 3x. This wasn't in my sprint — nobody had flagged it — but it was a core product quality issue.

I raised it in standup first, then built a Playback Speed Simulator in React and TypeScript wired into the existing Google Cloud TTS pipeline. Before submitting, volunteers had to hear their description at 3x. I framed it as "preview how your description sounds to users" rather than a quality check — these were volunteers doing generous work, and I didn't want the experience to feel judgmental.

**Result:** Volunteers immediately started self-correcting. Description length dropped, quality scores improved, user-side feedback improved — without any manual review intervention.

**Best for:** customer obsession, ownership, finding hidden user pain, proactive action.

---

### Story 4 — Deloitte: Journal Entry ETL Pipeline
**LPs: Invent and Simplify · Deliver Results**

At Deloitte, every client sent financial data in a different format with its own chart of accounts. Before any analysis, the team spent 1–2 days manually cleaning and mapping thousands of account names into a common taxonomy. Slow, repetitive, and prone to silent human error.

I built an automated ETL pipeline in Python with pandas. First, a normalization layer for raw CSV/Excel files — encoding issues, whitespace, column names. Second, a rule-based mapping engine: hash map for exact matches (~75% of accounts hit immediately), regex-based fuzzy matching for close variations. Third — most importantly — explicit exception routing: anything below a confidence threshold went into an exception log instead of silently passing through. The system never guesses.

**Result:** Data preparation time dropped from 1–2 days to ~3 hours per engagement. The exception log shifted the team from reviewing 100% of records manually to reviewing ~10% of edge cases that actually needed human judgment.

**Best for:** invent and simplify, deliver results, process improvement, prevent silent failure.

---

## Question Map

| Question | Best Story | Key Angle |
|---|---|---|
| Learn something fast | Story 1 | Narrow scope, toy examples, source code when docs fail |
| Invent / simplify a process | Story 4 | Manual → automated, with explicit validation |
| Customer obsession | Story 3 or 2 | Story 3: redefine the quality baseline; Story 2: design around how users actually get stuck |
| Ownership | Story 3 | Not in sprint, raised it, built it, shipped it |
| Deliver results under constraints | Story 1 or 4 | Story 1: hard deadline + technical risk; Story 4: measurable time savings |
| Dive deep technically | Story 1 | Went into source code when docs stopped helping |
| Challenge the status quo | Story 2 or 3 | Story 2: product design; Story 3: questioned the quality metric |
| Prevent a hidden risk | Story 4 or 3 | Story 4: data integrity; Story 3: bad quality baseline |
