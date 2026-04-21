---
title: YouDescribe
permalink: /projects/youdescribe/
---

# YouDescribe

Production internship: accessibility tooling and AI-assisted audio description authoring.

## Overview

YouDescribe is a platform where volunteers write audio descriptions for YouTube videos so visually impaired users can follow visual content. During my internship, I built two features: a Playback Speed Simulator that exposed a hidden quality gap in the volunteer workflow, and AI-assisted authoring tools that reduced the time cost of writing high-quality descriptions.

## Stack

- **Frontend**: React, TypeScript
- **TTS**: Google Cloud Text-to-Speech API
- **Backend**: Node.js (existing platform)
- **AI**: LLM-assisted description drafting (integrated into existing authoring flow)

## Playback Speed Simulator

**The problem**: Volunteers reviewed their descriptions at 1x speed, which felt natural to them. But many real users listen at 2x–3x because they are experienced. A description that sounds clear at 1x can feel rushed and hard to follow at 3x. The quality bar volunteers were using was not the quality bar that mattered to the actual audience.

**The fix**: I built a Playback Speed Simulator in React + TypeScript wired into the existing Google Cloud TTS pipeline. Before submitting, volunteers must hear their description at 3x speed. The UX framing matters: I presented it as "preview how your description sounds to users," not as a quality check. These are volunteers doing generous work — the experience should feel useful, not judgmental.

**Result**: Volunteers started self-correcting immediately. They would hear the description at 3x, notice it felt rushed, and revise on their own. Description length dropped, quality scores improved, and user-side feedback got better — without any manual review intervention.

## AI-Assisted Authoring

Integrated an LLM drafting step into the description authoring flow to reduce cold-start friction for volunteers. The draft is surfaced as a starting point, not an answer — the UI makes it easy to edit rather than accept, because volunteer-written descriptions consistently outperform raw model output on nuance and emotional register.

## Key Engineering Notes

- The playback simulator required careful sync between the TTS audio stream and the video timeline so volunteers could evaluate descriptions in context, not in isolation.
- Accessibility constraints applied to the tooling itself — the authoring interface needed to be usable by volunteers who also use screen readers.
- Shipped to production during internship; features are live on the YouDescribe platform.

## What I Learned

The most reliable way to improve content quality at scale is to let the people creating it experience what the end user experiences. Volunteers didn't need feedback from a quality system — they needed to hear what 3x playback sounds like. Once they did, they fixed it themselves.

---

[← Projects](../)
