---
title: 行为面试准备
---

# 行为面试准备

四个故事，按 Amazon LP 映射。

## 故事库

### Story 1 — VisoCode：LangGraph 重构
**LP：Learn and Be Curious · Invent and Simplify**

在 AdventureX 2025 做 VisoCode 的时候，我负责的是一个把自然语言转成教学动画视频的 multi-agent 系统。最大的问题是 agent 之间会互相循环调用，因为当时没有真正的状态管理，一旦 prompt 复杂，整个 pipeline 就会无限循环甚至直接崩掉。离 demo 只剩不到两天。

我先问自己一个问题：我现在最小需要学会的东西是什么。我把范围收缩到两个核心概念：state management 和 conditional edges。先花了一小时在 Jupyter notebook 里写 toy examples，直到这两个概念真正跑通后才去碰正式代码。重构过程中发现第二个问题：系统在 retry 时上下文不断膨胀，导致内存溢出。文档里没有解释这个行为，所以我直接去看 LangGraph 的 GitHub 源码，追踪 message accumulation 的逻辑，发现它默认不做 truncation。于是我写了一个自定义 routing function，加上 retry counter 和 context truncation，让系统达到阈值后可以干净退出。

**结果：** 视频生成成功率提升约 50%，无限循环问题彻底消除，系统稳定支撑了现场 demo。我们拿到了 AdventureX 2025 的 Most Technically Outstanding。

**适用题型：** 快速学习、技术深挖、重新设计而非打补丁、deadline 压力下交付。

---

### Story 2 — AlgoMentor：三层提示系统
**LP：Invent and Simplify · Customer Obsession**

做 AlgoMentor 这个 AI coding tutor 时，我先跟几个正在刷 LeetCode 的朋友聊了他们的真实使用习惯。问题很稳定：LeetCode 的 hint 往往是一大段整体信息，用户行为也很一致——卡住了就点开提示、看到解法方向、然后开始写答案。但更关键的是，大家卡住有三种不同层次：卡在 concept、卡在 strategy、卡在 implementation。现有 hint 系统把这三种情况都混在一起。

我设计了三层提示：第一层是 Socratic question（concept 层），第二层给方向性提示（strategy 层），第三层给 pseudocode skeleton（implementation 层）。还设计了 friction gate，一开始设 5 分钟，用户反馈太像惩罚后调成 2 分钟。每一层单独写了 prompt 和 guardrail，确保第一层不会泄露策略，第三层也只给结构不给核心逻辑。

**结果：** 用户不再一口气点完所有提示，而是真的开始一层一层地思考和推进。

**适用题型：** Invent and simplify、customer obsession、产品思维、行为设计。

---

### Story 3 — YouDescribe：播放速度模拟器
**LP：Customer Obsession · Ownership**

在 YouDescribe，志愿者会给 YouTube 视频写 audio description，帮助视障用户理解画面内容。我发现了一个隐藏问题：志愿者都按 1x 速度试听自己的描述，但很多真实的视障用户因为长期训练，实际会用 2x 到 3x 的速度去听。一个在 1x 下听起来完全合理的描述，到了 3x 可能就会显得又急又难跟上。这个问题不在我的 sprint 里，当时也没有人提出来，但我觉得它本质上是质量基线错位的问题。

我先在 standup 里把问题讲清楚，得到 lead 认可后再开始写代码。用 React 和 TypeScript 做了一个 Playback Speed Simulator，接入现有的 Google Cloud TTS 流程，让志愿者在提交前必须先以 3x 试听。我特意把产品文案写成"让你预览用户实际会怎么听到它"，而不是"检查你写得够不够好"——这些志愿者在做很善意的事情，我不想让这个流程变成一种被评判的感觉。

**结果：** 志愿者会自己发现问题并主动修改，不需要任何人指出来。描述长度下降，质量分上升，用户侧反馈也更好了。

**适用题型：** Customer obsession、ownership、发现隐藏的用户痛点、主动推动落地。

---

### Story 4 — 德勤：分录数据 ETL 与映射流水线
**LP：Invent and Simplify · Deliver Results**

在德勤，audit engagement 最大的瓶颈是 journal entry 数据的异构性。每个客户给的财务数据格式都不一样，chart of accounts 也完全不同，所以在真正分析之前，团队要先花 1 到 2 天手工清洗和映射成内部统一 taxonomy。这个过程既慢，又非常容易产生 silent human error。

我用 Python 和 pandas 设计了一条自动化 ETL pipeline。第一层是 data normalization，ingest 原始 CSV 和 Excel 文件，处理编码问题、去掉多余空格、统一列名。第二层是 mapping engine，先用 hash map 做 O(1) exact match，覆盖约 75% 的情况；剩下的通过 regex-based fuzzy matching 捕捉轻微命名差异。第三层——也是最重要的——是 exception handling：任何没达到高置信度阈值的条目都进 Exception Log，而不是静默通过。系统不会去猜。

**结果：** 数据准备时间从最多 2 天降到约 3 小时。Exception Log 把团队的工作方式从"人工看 100% 的数据"变成了"只看约 10% 真正需要人工判断的 edge cases"。

**适用题型：** Invent and simplify、deliver results、流程改进、防止 silent failure。

---

## 题目映射

| 题型 | 最佳故事 | 核心角度 |
|---|---|---|
| 快速学习 | Story 1 | 筛选最小必要知识、toy examples、看源码 |
| 简化流程 / 自动化 | Story 4 | 手工 → 自动化，配显式异常路由 |
| Customer obsession | Story 3 或 2 | Story 3：重新定义质量基线；Story 2：理解用户真正卡在哪 |
| Ownership | Story 3 | 不在 sprint 里，自己发现、推动、落地 |
| 在约束下交付结果 | Story 1 或 4 | Story 1：deadline 压力；Story 4：可量化效率提升 |
| 技术深挖 | Story 1 | 文档不够时直接看源码 |
| 挑战现状 | Story 2 或 3 | Story 2：产品设计创新；Story 3：质疑质量衡量标准 |
| 提前发现隐患 | Story 4 或 3 | Story 4：数据完整性；Story 3：错误的质量基线 |
