---
title: BQ Interview Prep
---

<section class="bq-hero">
  <p class="bq-eyebrow">Behavioral Interview Playbook</p>
  <h1>BQ Interview Prep — Cassie (Yue Liang)</h1>
  <p class="bq-subtitle">精选故事 · 核心题目 · 补充题目</p>
  <div class="bq-pill-row">
    <a class="bq-pill" href="#精选故事">精选故事</a>
    <a class="bq-pill" href="#核心题目">核心题目</a>
    <a class="bq-pill" href="#补充题目">补充题目</a>
    <a class="bq-pill" href="{{ '/bq_prep/bilingual' | relative_url }}">中英双语版</a>
  </div>
</section>

## 精选故事

<section class="bq-story-card">
  <div class="bq-story-head">
    <h3>Story 1 — VisoCode: LangGraph Refactor</h3>
    <div class="bq-tag-row">
      <span class="bq-tag">Learn and Be Curious</span>
      <span class="bq-tag">Invent and Simplify</span>
    </div>
  </div>

  <details open>
    <summary>STARR 分析</summary>
    <div class="bq-story-body">
      <p><strong>Situation</strong><br>
      Built VisoCode at AdventureX 2025 — multi-agent system turning plain English into animated educational videos. Agents were calling each other in circles with no state management, pipeline would spin forever and crash on complex prompts. Less than 2 days to demo.</p>

      <p><strong>Task</strong><br>
      Learn LangGraph from scratch and redesign the entire backend architecture — not patch the loops, but rebuild properly — under a hard deadline with no room for error.</p>

      <p><strong>Actions</strong><br>
      Min-knowledge principle: asked "what's the minimum I actually need right now?" → state management + conditional edges only. Spent 1 hour in Jupyter Notebook writing toy examples until those two concepts clicked. Didn't touch real code until then.</p>

      <p>Source code dive: hit unexpected memory overflow mid-refactor — context growing unbounded on every retry. Docs had no answer. Went directly to LangGraph source on GitHub, traced message accumulation logic, found no truncation by default. Wrote custom routing function with retry counter + context truncation to force clean exit at threshold.</p>

      <p>Stress test before merge: ran a batch of complex prompts to confirm loops were fully gone. Only merged after that passed.</p>

      <p><strong>Result</strong><br>
      Video generation success rate ↑ ~50%. Infinite loop issue completely eliminated. System stable enough for a live demo. Won Most Technically Outstanding at AdventureX 2025.</p>

      <p><strong>Reflection</strong><br>
      Three durable learning strategies: (1) Minimum knowledge principle — work backwards from the goal, find the smallest set of things you need to understand; reading everything ≠ learning what matters. (2) Toy prototype first — 1 hour in Jupyter saved hours of building on a wrong mental model. (3) Source code over docs — when docs fail on framework-level behavior, the source code never lies.</p>
    </div>
  </details>

  <details>
    <summary>口语版本</summary>
    <div class="bq-story-body">
      <p>At AdventureX 2025, I was building VisoCode, a multi-agent system that turned plain English into animated educational videos. The biggest issue was that the agents kept calling each other in circles because we had no real state management, so on complex prompts the pipeline would spin forever and crash. We had less than two days before the demo, so patching it wasn't enough. I had to learn LangGraph from scratch and redesign the backend properly under a hard deadline.</p>

      <p>I started by asking what was the minimum I actually needed to learn right then. I decided the two critical concepts were state management and conditional edges. I spent about an hour in a Jupyter notebook writing tiny examples until those clicked, and only then touched the real code. During the refactor I hit a second issue: memory usage kept growing on retries. The docs didn't explain it, so I went directly into LangGraph's source code, traced how messages were accumulated, and found there was no truncation by default. I then wrote a custom routing function with a retry counter and context truncation so the graph would exit cleanly instead of looping forever. Before merging, I ran a batch of complex prompts to make sure the loops were gone.</p>

      <p>That refactor improved video generation success rate by about 50%, eliminated the infinite loop issue, and made the system stable enough for a live demo. We ended up winning Most Technically Outstanding at AdventureX 2025. The biggest lesson for me was how to learn fast under pressure: focus on the minimum knowledge you need, prototype before integrating, and when the docs stop helping, trust the source code.</p>
    </div>
  </details>
</section>

<section class="bq-story-card">
  <div class="bq-story-head">
    <h3>Story 2 — AlgoMentor: 3-Level Hint System</h3>
    <div class="bq-tag-row">
      <span class="bq-tag">Invent and Simplify</span>
      <span class="bq-tag">Customer Obsession</span>
    </div>
  </div>

  <details open>
    <summary>STARR 分析</summary>
    <div class="bq-story-body">
      <p><strong>Situation</strong><br>
      Building AlgoMentor, an AI coding tutor. Before designing the hint system, talked to several friends grinding LeetCode. Consistent finding: LeetCode hints are one big block that reveals the approach — everyone uses them the same way (get stuck → click → read → write answer). Deeper finding: people get stuck at 3 distinct levels — concept (what data structure?), strategy (how to apply it?), implementation (how to code it?). LeetCode's hint doesn't distinguish between these.</p>

      <p><strong>Task</strong><br>
      Design a hint system that makes users actually think — and enforce that through system design, not by asking users to be disciplined on their own.</p>

      <p><strong>Actions</strong><br>
      3-level hint design: L1 = Socratic question ("what data structure gives O(1) lookup?") — targets concept. L2 = directional hint ("try a HashMap to track what you've seen") — targets strategy. L3 = pseudocode skeleton — targets implementation. Each level exactly matches the type of stuck.</p>

      <p>Friction gates: time delay between levels to prevent click-through. Started at 5 minutes — users said it felt punishing. Tuned down to 2 minutes — long enough to force a real attempt, short enough not to frustrate.</p>

      <p>Prompt chaining with strict constraints: each level has its own system prompt with explicit guardrails — L1 can never hint at strategy, L2 can give direction but no code, L3 can give structure but not the core logic. Enforced by the system, not the LLM's judgment.</p>

      <p><strong>Result</strong><br>
      Click-through-all-hints behavior dropped significantly. Users started working through problems in steps. The system solved a different problem than LeetCode's hint — not just less information, but the right information at the right moment for where the person was actually stuck.</p>

      <p><strong>Reflection</strong><br>
      Good product design changes behavior by changing the environment, not by asking users to try harder. A friction gate &gt; a message saying "please think before you click." One is a system constraint, the other is just a suggestion. Next: data-driven delay tuning per problem difficulty; adaptive starting hint level based on user history.</p>
    </div>
  </details>

  <details>
    <summary>口语版本</summary>
    <div class="bq-story-body">
      <p>When I was building AlgoMentor, an AI coding tutor, I started by talking to friends who were grinding LeetCode. The pattern was really consistent: LeetCode hints come as one big block, so people use them the same way every time. They get stuck, click, read the approach, and then basically write the answer. What I noticed, though, was that people actually get stuck at three different levels: concept, strategy, and implementation. The existing hint design treated all of those as the same problem.</p>

      <p>So my goal was to design a hint system that still helped people, but forced them to think in the right sequence. I built a three-level structure: level one was a Socratic question for the concept, level two gave directional guidance for strategy, and level three gave pseudocode structure for implementation. Then I added friction gates between levels so users couldn't just click through instantly. I started with a five-minute delay, but users said that felt too punishing, so I adjusted it down to two minutes. I also used separate prompts and strict constraints for each level, so the model literally could not jump ahead and reveal too much too early.</p>

      <p>The result was that people stopped blasting through all the hints at once and started working through problems step by step. The key lesson for me was that good product design changes behavior by shaping the environment. If you want users to think more deeply, it's much more effective to build that into the system than to rely on them to self-regulate.</p>
    </div>
  </details>
</section>

<section class="bq-story-card">
  <div class="bq-story-head">
    <h3>Story 3 — YouDescribe: Playback Speed Simulator</h3>
    <div class="bq-tag-row">
      <span class="bq-tag">Customer Obsession</span>
      <span class="bq-tag">Ownership</span>
    </div>
  </div>

  <details open>
    <summary>STARR 分析</summary>
    <div class="bq-story-body">
      <p><strong>Situation</strong><br>
      YouDescribe — platform where volunteers write audio descriptions of YouTube videos for visually impaired users. Volunteers review their descriptions at 1x speed (natural for sighted people). Real users listen at 2x–3x (trained over years). A description that sounds perfect at 1x becomes rushed and hard to follow at 3x. Our entire quality measurement baseline was wrong. Nobody had flagged it. Not in my sprint.</p>

      <p><strong>Task</strong><br>
      Fix the quality measurement baseline gap — without being asked, and without making volunteers feel judged or criticized.</p>

      <p><strong>Actions</strong><br>
      Communicate before coding: raised in standup with a clear explanation of the 1x vs 3x gap and why it mattered for quality measurement. Got lead's agreement before writing a line of code.</p>

      <p>Built Playback Speed Simulator: required 3x playback before submit, no option to skip. Built in React and TypeScript, wired into existing Google Cloud TTS audio pipeline.</p>

      <p>Deliberate UX framing: "preview how your description sounds to users" — not "check if your description is good enough." The first is informational. The second is evaluative. That difference matters because these are volunteers doing something generous.</p>

      <p><strong>Result</strong><br>
      Volunteers immediately started self-correcting — hearing their description at 3x and going back to edit without anyone telling them to. Description length dropped, quality scores went up, user-side feedback improved. Designed and shipped entirely without being asked.</p>

      <p><strong>Reflection</strong><br>
      Best way to build user empathy into a product: make the people building it actually experience what users experience. If I'd thought about this earlier, I would have been testing AI descriptions at 3x from day one. Next: talk directly to visually impaired users to validate whether 3x is the right benchmark; possibly make it user-configurable rather than hardcoded.</p>
    </div>
  </details>

  <details>
    <summary>口语版本</summary>
    <div class="bq-story-body">
      <p>At YouDescribe, volunteers write audio descriptions for YouTube videos so visually impaired users can follow the visual content. I noticed a hidden gap in how we measured quality: volunteers reviewed their descriptions at 1x speed, which feels natural if you're sighted, but many real users listen at 2x or 3x because they're very experienced. That meant a description that sounded fine to volunteers at 1x could feel rushed and hard to follow for the actual audience. It wasn't in my sprint, and nobody had flagged it yet, but I felt it was a core product quality issue.</p>

      <p>I raised the issue in standup first so the team understood why it mattered, then I built a Playback Speed Simulator in React and TypeScript and wired it into the existing Google Cloud TTS pipeline. Before submitting, volunteers had to hear the description at 3x speed. I also paid a lot of attention to the framing. Instead of presenting it as a quality check, I framed it as a way to preview how the description sounds to users. That mattered because these were volunteers doing generous work, and I didn't want the experience to feel judgmental.</p>

      <p>The result was that volunteers immediately started self-correcting. They would hear the description at 3x, realize it felt rushed, and revise it on their own. Description length dropped, quality scores improved, and user-side feedback got better. The lesson for me was that one of the best ways to build customer empathy into a product is to let the people creating it experience what the user experiences.</p>
    </div>
  </details>
</section>

<section class="bq-story-card">
  <div class="bq-story-head">
    <h3>Story 4 — Deloitte: Journal Entry ETL &amp; Mapping Pipeline</h3>
    <div class="bq-tag-row">
      <span class="bq-tag">Invent and Simplify</span>
      <span class="bq-tag">Deliver Results</span>
    </div>
  </div>

  <details open>
    <summary>STARR 分析</summary>
    <div class="bq-story-body">
      <p><strong>Situation</strong><br>
      At Deloitte, a major bottleneck in audit engagements was data heterogeneity. Every client provided journal entry data in different formats with custom charts of accounts. Before any analysis could happen, we needed apples-to-apples comparability. The team was spending 1 to 2 days manually cleaning and mapping thousands of client-specific accounts to our standard internal taxonomy, and the process was highly prone to silent human error.</p>

      <p><strong>Task</strong><br>
      I needed to build an automated, scalable solution to ingest this unstructured client data, standardize it, and map it reliably, so the team could focus on risk assessment instead of manual data entry.</p>

      <p><strong>Actions</strong><br>
      I designed and built an automated ETL pipeline using Python and pandas. First, I created a data normalization layer that ingested raw CSV and Excel files, handled encoding issues, stripped whitespace, and normalized column names so downstream logic could run on a consistent schema.</p>

      <p>Second, I built a rule-based mapping engine. It first used a hash map for <code>O(1)</code> exact matching against a historical master dictionary, which categorized about 70 to 80 percent of standard accounts instantly. For the remaining entries, I added a regex-based fuzzy matching layer to catch slight naming variations.</p>

      <p>Third, and most importantly, I designed the system not to guess. Any entry that did not meet a high-confidence threshold was routed into an <code>Exception Log</code>. That validation layer made sure ambiguous data never silently slipped through the pipeline.</p>

      <p><strong>Result</strong><br>
      The pipeline reduced data preparation and mapping time from up to 2 days to about 3 hours per engagement. By generating the exception log, I shifted the team's workflow from reviewing 100 percent of the data to reviewing only the roughly 10 percent of edge cases that actually required human judgment. It also guaranteed consistent account mapping for downstream risk models.</p>

      <p><strong>Reflection</strong><br>
      The biggest engineering lesson for me was to never let an automated system fail silently. By explicitly isolating unmapped or low-confidence items into a validation layer, errors were caught at the ingestion stage rather than deep in the analysis phase. That mental model — designing strict validation and exception handling before core processing logic — is something I carried forward into later pipeline work, including BERTScore.</p>
    </div>
  </details>

  <details>
    <summary>口语版本</summary>
    <div class="bq-story-body">
      <p>At Deloitte, one of the biggest bottlenecks in audit engagements was journal entry data heterogeneity. Every client sent financial data in a different format with its own chart of accounts, so before we could do any analysis, the team had to spend one to two days manually cleaning and mapping thousands of account names into a common internal taxonomy. It was slow, repetitive, and very prone to silent human error.</p>

      <p>I built an automated ETL pipeline in Python with pandas to standardize and map that data reliably. First, I added a normalization layer to ingest raw CSV and Excel files, handle encoding issues, trim whitespace, and normalize column names. Second, I built a rule-based mapping engine that used a hash map for exact matching against a historical master dictionary, which handled about 70 to 80 percent of accounts immediately, and then used regex-based fuzzy matching for close variations. Third, I explicitly designed the system not to guess. If a journal entry did not meet a high-confidence match threshold, it went into an exception log instead of silently passing through.</p>

      <p>The result was that data preparation and mapping time dropped from up to two days to about three hours per engagement. More importantly, the exception log changed the team's workflow from reviewing everything manually to reviewing only the roughly 10 percent of edge cases that actually needed human judgment. The biggest lesson for me was that automated systems should never fail silently. If confidence is low, the system should surface the ambiguity instead of pretending it knows the answer.</p>
    </div>
  </details>
</section>

## 核心题目

- Tell me about a time you had to learn something quickly under pressure.
- Tell me about a time you simplified a complex process.
- Describe a time you built something based on a deep user need.
- Tell me about a time you took ownership of something that was not assigned to you.
- Describe a time you improved quality by finding a hidden problem early.
- Tell me about a time you designed a system instead of just solving a one-off task.
- Tell me about a time you delivered results with limited time or resources.
- Describe a time when your technical judgment changed the outcome of a project.

## 补充题目

- Tell me about a time you challenged the status quo.
- Tell me about a time you used data to make a decision.
- Describe a time you prevented a problem before it became serious.
- Tell me about a time you earned trust from teammates or stakeholders.
- Describe a time you balanced user experience with system constraints.
- Tell me about a time you had to make a decision with incomplete information.
- Describe a time you improved a process for other people, not just for yourself.
- Tell me about a time you discovered that your first solution was not enough and had to redesign it.

## STAR 方法框架

行为面试的核心是用 **STAR** 结构把故事讲清楚，每个 situation 都要有清晰的因果链：

| 维度 | 关键问题 | 注意点 |
|------|---------|--------|
| **S**ituation | 背景是什么？规模/时间/团队？ | 30 秒内说清，别铺太长 |
| **T**ask | 你的职责是什么？为什么是你？ | 明确个人 ownership |
| **A**ction | 你具体做了什么？为什么这样做？ | 用 "I" 而不是 "We"，突出个人决策 |
| **R**esult | 结果如何？量化了吗？学到了什么？ | 数字优先，无法量化也要说影响范围 |

---

## 核心题型分类

### Leadership & Influence
> 考察：没有直接权力时如何推动事情

- Tell me about a time you led a project without formal authority.
- Describe a situation where you had to influence stakeholders who disagreed with your approach.
- Give an example of when you had to make a decision with incomplete information.
- Tell me about a time you set a vision and got others on board.

**答题重点**：强调你如何建立 trust、align incentives、用数据说服人，而不是靠职位。

---

### Conflict & Disagreement
> 考察：如何处理分歧、保持专业、最终 align

- Tell me about a time you disagreed with your manager. How did you handle it?
- Describe a conflict with a coworker and how you resolved it.
- Tell me about a time you had to push back on a decision you thought was wrong.
- Give an example of when you had to deliver difficult feedback to someone.

**答题重点**：不要回避冲突，也不要说对方错了。展示你如何 listen、find common ground、保持 outcome-first 的心态。

---

### Ownership & Accountability
> 考察：是否 take ownership，是否对结果负责

- Tell me about a time you took ownership of a project that wasn't originally yours.
- Describe a situation where something went wrong and it was partly your fault.
- Tell me about a time you went above and beyond your job description.
- Give an example of when you delivered results despite unclear requirements or limited resources.

**答题重点**：失败故事要展示你 learned & fixed，不是 blame 别人。用具体的后续行动证明 accountability。

---

### Ambiguity & Prioritization
> 考察：在不确定环境中能否独立判断、合理排优先级

- Tell me about a time you had to work with ambiguous requirements.
- Describe a situation where you had too many competing priorities. How did you decide?
- Give an example of a project where the scope kept changing.
- Tell me about a time you had to quickly learn something new to complete a task.

**答题重点**：展示你如何 clarify、make trade-offs、communicate 决策过程。

---

### Collaboration & Teamwork
> 考察：跨团队合作、处理复杂人际关系

- Tell me about a time you worked on a highly cross-functional team.
- Describe a situation where you had to help a struggling teammate.
- Give an example of when you built a relationship with someone who was initially difficult to work with.
- Tell me about your most successful collaboration and what made it work.

**答题重点**：展示 empathy + task focus 的平衡，不要只说"大家配合很好"。

---

### Innovation & Problem Solving
> 考察：是否主动寻找更好的方法、能否跳出框架思考

- Tell me about a time you came up with a creative solution to a hard problem.
- Describe a situation where you challenged the status quo.
- Give an example of a time you identified a process improvement and implemented it.
- Tell me about a project where you had to think differently to succeed.

**答题重点**：量化 before/after，说清楚你的 insight 来自哪里，不是灵光一现。

---

### Failure & Growth
> 考察：self-awareness，是否能从失败中学习

- Tell me about your biggest professional failure.
- Describe a time your project didn't go as planned. What did you learn?
- Give an example of feedback you received that was hard to hear but ultimately helpful.
- Tell me about a time you misjudged a situation.

**答题重点**：不要选太小的失败（显得没自知力），不要选太大的灾难。展示 genuine reflection + concrete change after.

---

## Amazon Leadership Principles 映射

| LP | 对应题型 | 核心故事要素 |
|----|---------|------------|
| Customer Obsession | 用户影响类 | 主动发现用户需求，超越 spec |
| Ownership | Ownership 类 | 主动接下、不推卸 |
| Invent & Simplify | Innovation 类 | 简化流程 / 技术创新 |
| Are Right, A Lot | Disagreement 类 | 坚持有数据支撑的判断 |
| Learn and Be Curious | Failure / Growth 类 | 学习型心态 |
| Hire and Develop the Best | Teamwork 类 | Mentor、帮助他人成长 |
| Insist on the Highest Standards | Quality 类 | 推动 quality bar |
| Think Big | Vision 类 | 影响范围超出当前角色 |
| Bias for Action | Ambiguity 类 | 快速迭代，不等完美信息 |
| Frugality | Constraints 类 | 有限资源做更多 |
| Earn Trust | Conflict 类 | 透明、follow-through |
| Dive Deep | Technical 类 | 深入细节，不只看大图 |
| Have Backbone; Disagree and Commit | Disagreement 类 | 表达 then commit |
| Deliver Results | Accountability 类 | 最终结果，不是 effort |

---

## 准备策略

### Story Bank 建立方法

把你的经历按维度列出，每个维度准备 2-3 个故事（不同规模、不同结果类型）：

```
维度           故事 A (主故事)      故事 B (备用)      故事 C (失败版)
Leadership     [项目 X]            [跨组 Y]           [推动失败 Z]
Conflict       [与 PM 分歧]        [团队内部冲突]     —
Ownership      [接手遗留项目]      [自发 fix 问题]    —
Ambiguity      [需求不清的项目]    [优先级变化]       —
Innovation     [流程改进]          [技术方案]         —
```

### 量化模版

即使没有精确数字，也可以用以下方式表达：
- `reduced X by ~Y%` (估算要诚实)
- `impacted N users / teams`
- `saved approximately X hours per week`
- `from weekly incidents to zero in 3 months`

### 时间控制

- 完整 STAR：**2-3 分钟**
- 开场 Situation：**< 30 秒**
- Action 部分：**占比最大，1-1.5 分钟**
- Result + reflection：**30-45 秒**

---

## 常见失误

- **太多 "We"**：面试官考察的是你，用 "I" 描述你的具体贡献
- **Situation 铺太长**：背景超过 45 秒就是跑题
- **Action 太模糊**：说了做了什么，没说为什么这样做、有哪些选项
- **Result 没量化**：哪怕说"这让团队 velocity 提升了，接下来的 sprint 我们提前两天完成"也比没有强
- **Failure 题没有 reflection**：必须说清楚你从中学到了什么、以后怎么做不同

---

## 练习清单

**每周做法**：选 3 道题，限时 3 分钟口头作答（或写下来），然后检查是否符合 STAR 结构、有没有量化。

- [ ] 准备 10 个核心故事，覆盖上面 6 个题型
- [ ] 针对目标公司 LP 列表做映射
- [ ] 每个故事反复精简，减少不必要的 context
- [ ] 找人做 mock，重点反馈 Action 部分是否清晰
- [ ] 录音听自己的回答，检查节奏和是否有填充词

---

## Quiz

**Q1: STAR 中 Action 部分应该占整个回答的多少比重？**

- [ ] 最少，30 秒内说完
- [ ] 约一半，1-1.5 分钟 ✅
- [ ] 和 Situation 一样长
- [ ] 比 Result 短

**Q2: 回答 BQ 题时说 "We did X" 和 "I did X" 有什么区别？**

- [ ] 没有区别，团队成果最重要
- [ ] "I" 更清晰展示个人 ownership 和决策，面试官考察的是你 ✅
- [ ] "We" 显示协作能力，更好
- [ ] 应该两个混用

**Q3: 遇到 Failure 类题（"Tell me about your biggest failure"），最重要的是什么？**

- [ ] 选择一个影响很小的小失败
- [ ] 展示 genuine reflection + 你之后具体改变了什么 ✅
- [ ] 把责任分散到团队
- [ ] 转移到成功的结果

**Q4: Amazon Leadership Principles 中 "Disagree and Commit" 的正确处理方式是？**

- [ ] 沉默接受决定
- [ ] 坚决反对到最后
- [ ] 明确表达不同意见，但一旦决定做出，全力执行 ✅
- [ ] 私下找人推翻决定

**Q5: 没有精确数字时，如何量化你的 Result？**

- [ ] 不量化，只描述过程
- [ ] 编造一个看起来合理的数字
- [ ] 用估算表达：影响范围、频率变化、时间节省等 ✅
- [ ] 说"很显著"就够了
