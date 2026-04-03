---
title: BQ Interview Prep Bilingual
permalink: /bq_prep/bilingual/
---

<section class="bq-hero">
  <p class="bq-eyebrow">Bilingual Interview Pack</p>
  <h1>BQ Interview Prep — Bilingual Version</h1>
  <p class="bq-subtitle">English + 中文 · Story Bank · Question Mapping</p>
  <div class="bq-pill-row">
    <a class="bq-pill" href="{{ '/bq_prep/' | relative_url }}">返回主页面</a>
    <a class="bq-pill" href="#story-bank">Story Bank</a>
    <a class="bq-pill" href="#question-map">Question Map</a>
  </div>
</section>

## Story Bank

<section class="bq-story-card" id="story-bank">
  <div class="bq-story-head">
    <h3>Story 1 — VisoCode: LangGraph Refactor</h3>
    <div class="bq-tag-row">
      <span class="bq-tag">Learn and Be Curious</span>
      <span class="bq-tag">Invent and Simplify</span>
    </div>
  </div>

  <details open>
    <summary>English Oral Version</summary>
    <div class="bq-story-body">
      <p>At AdventureX 2025, I was building VisoCode, a multi-agent system that turned plain English into animated educational videos. The main issue was that the agents kept calling each other in circles because we had no real state management, so on complex prompts the pipeline would spin forever and crash. We had less than two days before the demo, so patching the issue wasn't enough. I had to learn LangGraph from scratch and redesign the backend properly under a hard deadline.</p>

      <p>I started by asking what was the minimum I actually needed to understand right then. I focused on two concepts: state management and conditional edges. I spent about an hour in a Jupyter notebook building toy examples until those clicked, and only then touched the real code. During the refactor I found a second issue: memory usage kept growing on retries. The docs didn't explain it, so I went directly into LangGraph's source code, traced how messages were accumulated, and found that there was no truncation by default. I wrote a custom routing function with a retry counter and context truncation so the graph would exit cleanly instead of looping forever. Before merging, I ran a batch of complex prompts to confirm the loops were actually gone.</p>

      <p>The result was about a 50 percent improvement in video generation success rate, complete elimination of the infinite loop issue, and a system that was stable enough for a live demo. We ended up winning Most Technically Outstanding at AdventureX 2025. The biggest lesson for me was how to learn quickly under pressure: focus on the minimum knowledge you need, prototype before integrating, and when the docs stop helping, trust the source code.</p>
    </div>
  </details>

  <details>
    <summary>中文版口语版</summary>
    <div class="bq-story-body">
      <p>在 AdventureX 2025 做 VisoCode 的时候，我负责的是一个把自然语言转换成教学动画视频的 multi-agent 系统。最大的问题是 agent 之间会互相循环调用，因为当时没有真正的状态管理，所以一旦 prompt 复杂，整个 pipeline 就会无限循环甚至直接崩掉。离 demo 只剩不到两天，所以我不能只是打补丁，而是必须快速学会 LangGraph，并把后端架构重新设计好。</p>

      <p>我当时先问自己一个问题，就是我现在最小需要学会的东西是什么。我把范围收缩到两个核心概念：state management 和 conditional edges。为了先建立正确心智模型，我先花了一小时在 Jupyter notebook 里写 toy examples，直到这两个概念真正跑通后才去碰正式代码。重构过程中我又遇到第二个问题，系统在 retry 的时候上下文会不断膨胀，导致内存溢出。文档里没有解释这个行为，所以我直接去看 LangGraph 的 GitHub 源码，追踪 message accumulation 的逻辑，发现它默认不会做 truncation。于是我写了一个自定义 routing function，加上 retry counter 和 context truncation，让系统达到阈值后可以干净退出，而不是继续死循环。最后在合并前，我专门跑了一批复杂 prompt 做压力测试，确认循环问题真的消失了。</p>

      <p>最后的结果是视频生成成功率提升了大约 50%，无限循环问题被彻底消除，系统也足够稳定，可以支撑现场 demo。我们最后还拿到了 AdventureX 2025 的 Most Technically Outstanding。这个经历让我形成了一个很稳定的方法论，就是高压下快速学习时，要先抓最小必要知识、先做小实验验证心智模型、文档不够的时候就直接去看源码。</p>
    </div>
  </details>

  <details>
    <summary>Best-Fit Questions</summary>
    <div class="bq-story-body">
      <p>Best for: learn quickly, deal with ambiguity, dive deep technically, redesign instead of patch, deliver under time pressure.</p>
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
    <summary>English Oral Version</summary>
    <div class="bq-story-body">
      <p>When I was building AlgoMentor, an AI coding tutor, I started by talking to friends who were grinding LeetCode. The pattern was consistent: LeetCode hints come as one big block, so people use them the same way every time. They get stuck, click, read the approach, and then basically write the answer. What I noticed, though, was that people actually get stuck at three different levels: concept, strategy, and implementation. The existing hint design treated all of those as the same problem.</p>

      <p>So my goal was to design a hint system that still helped people, but forced them to think in the right sequence. I built a three-level structure: level one was a Socratic question for the concept, level two gave directional guidance for strategy, and level three gave pseudocode structure for implementation. Then I added friction gates between levels so users couldn't just click through instantly. I started with a five-minute delay, but users said that felt too punishing, so I adjusted it down to two minutes. I also used separate prompts and strict constraints for each level, so the model literally could not jump ahead and reveal too much too early.</p>

      <p>The result was that people stopped blasting through all the hints at once and started working through problems step by step. The key lesson for me was that good product design changes behavior by shaping the environment. If you want users to think more deeply, it's much more effective to build that into the system than to rely on them to self-regulate.</p>
    </div>
  </details>

  <details>
    <summary>中文版口语版</summary>
    <div class="bq-story-body">
      <p>我在做 AlgoMentor 这个 AI coding tutor 的时候，先去跟几个正在刷 LeetCode 的朋友聊他们真实的使用习惯。我发现一个很稳定的问题，LeetCode 的 hint 往往是一大段整体信息，所以用户的行为也很一致，就是卡住了以后点开提示、直接看到解法方向，然后开始写答案。但更关键的是，我发现大家卡住其实有三种不同层次：有的人是卡在 concept，不知道该用什么数据结构；有的人卡在 strategy，不知道这个结构怎么用；还有的人卡在 implementation，不知道代码怎么落地。而现有 hint 系统把这三种情况都混在了一起。</p>

      <p>所以我的目标不是简单做一个“更少信息”的提示，而是做一个真正逼着用户按正确顺序思考的系统。我设计了三层提示：第一层是 Socratic question，对应 concept；第二层给方向性提示，对应 strategy；第三层给 pseudocode skeleton，对应 implementation。除此之外，我还设计了 friction gate，限制用户不能连续秒点所有提示。一开始我设的是五分钟，但用户反馈太像惩罚，所以我又调成两分钟，既能逼出一次真实尝试，又不会让人太挫败。为了防止模型越界，我还给每一层单独写了不同的 prompt 和 guardrail，确保第一层不会提前泄露策略，第二层不会直接给代码，第三层也只给结构不给核心逻辑。</p>

      <p>最后的结果是，用户不再一口气点完所有提示，而是真的开始一层一层地思考和推进。这个项目让我更明确了一点，就是好的产品设计不是告诉用户“你要更自律”，而是通过系统环境本身去塑造用户行为。</p>
    </div>
  </details>

  <details>
    <summary>Best-Fit Questions</summary>
    <div class="bq-story-body">
      <p>Best for: invent and simplify, customer obsession, product thinking, behavior design, challenge the status quo.</p>
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
    <summary>English Oral Version</summary>
    <div class="bq-story-body">
      <p>At YouDescribe, volunteers write audio descriptions for YouTube videos so visually impaired users can follow the visual content. I noticed a hidden gap in how we measured quality: volunteers reviewed their descriptions at 1x speed, which feels natural if you're sighted, but many real users listen at 2x or 3x because they're very experienced. That meant a description that sounded fine to volunteers at 1x could feel rushed and hard to follow for the actual audience. It wasn't in my sprint, and nobody had flagged it yet, but I felt it was a core product quality issue.</p>

      <p>I raised the issue in standup first so the team understood why it mattered, then I built a Playback Speed Simulator in React and TypeScript and wired it into the existing Google Cloud TTS pipeline. Before submitting, volunteers had to hear the description at 3x speed. I also paid a lot of attention to the framing. Instead of presenting it as a quality check, I framed it as a way to preview how the description sounds to users. That mattered because these were volunteers doing generous work, and I didn't want the experience to feel judgmental.</p>

      <p>The result was that volunteers immediately started self-correcting. They would hear the description at 3x, realize it felt rushed, and revise it on their own. Description length dropped, quality scores improved, and user-side feedback got better. The lesson for me was that one of the best ways to build customer empathy into a product is to let the people creating it experience what the user experiences.</p>
    </div>
  </details>

  <details>
    <summary>中文版口语版</summary>
    <div class="bq-story-body">
      <p>在 YouDescribe，志愿者会给 YouTube 视频写 audio description，帮助视障用户理解画面内容。我发现当时平台衡量质量的基线有一个隐藏问题：志愿者都是按 1x 速度去试听自己的描述，这对大多数视力正常的人来说很自然；但很多真实的视障用户因为长期训练，实际会用 2x 到 3x 的速度去听。所以一个在 1x 下听起来完全合理的描述，到了 3x 可能就会显得又急又难跟上。这个问题不在我的 sprint 里，当时也没有人明确提出来，但我觉得它本质上是一个用户体验和质量基线错位的问题。</p>

      <p>我先在 standup 里把这个问题讲清楚，解释为什么 1x 和 3x 的差异会影响我们对质量的判断，得到 lead 的认可后再开始写代码。之后我用 React 和 TypeScript 做了一个 Playback Speed Simulator，并接入了现有的 Google Cloud TTS 流程，让志愿者在提交前必须先以 3x 试听。我还特意处理了产品文案，不把它写成“检查你写得够不够好”，而是写成“让你预览用户实际会怎么听到它”。因为这些志愿者本来就在做很善意的事情，我不想让这个流程变成一种被评判的感觉。</p>

      <p>最后很明显的结果是，志愿者会自己发现问题并主动修改，不需要任何人去指出来。描述长度下降了，质量分也上去了，用户侧反馈也更好了。这个故事让我最确信的一点是，想建立用户同理心，最有效的方法之一，就是让创造产品的人亲身体验到用户真正经历的东西。</p>
    </div>
  </details>

  <details>
    <summary>Best-Fit Questions</summary>
    <div class="bq-story-body">
      <p>Best for: customer obsession, ownership, finding hidden user pain, improving quality without being asked, proactive action.</p>
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
    <summary>English Oral Version</summary>
    <div class="bq-story-body">
      <p>At Deloitte, one of the biggest bottlenecks in audit engagements was journal entry data heterogeneity. Every client sent financial data in a different format with its own chart of accounts, so before we could do any analysis, the team had to spend one to two days manually cleaning and mapping thousands of account names into a common internal taxonomy. It was slow, repetitive, and very prone to silent human error.</p>

      <p>I built an automated ETL pipeline in Python with pandas to standardize and map that data reliably. First, I added a normalization layer to ingest raw CSV and Excel files, handle encoding issues, trim whitespace, and normalize column names. Second, I built a rule-based mapping engine that used a hash map for exact matching against a historical master dictionary, which handled about 70 to 80 percent of accounts immediately, and then used regex-based fuzzy matching for close variations. Third, I explicitly designed the system not to guess. If a journal entry did not meet a high-confidence match threshold, it went into an exception log instead of silently passing through.</p>

      <p>The result was that data preparation and mapping time dropped from up to two days to about three hours per engagement. More importantly, the exception log changed the team's workflow from reviewing everything manually to reviewing only the roughly 10 percent of edge cases that actually needed human judgment. The biggest lesson for me was that automated systems should never fail silently. If confidence is low, the system should surface the ambiguity instead of pretending it knows the answer.</p>
    </div>
  </details>

  <details>
    <summary>中文版口语版</summary>
    <div class="bq-story-body">
      <p>在 Deloitte，我做过一个很典型的 audit data automation 项目。最大的瓶颈其实不是分析本身，而是 journal entry 数据的异构性。每个客户给的财务数据格式都不一样，chart of accounts 也完全不同，所以在真正分析之前，团队要先花一到两天手工清洗和映射成内部统一 taxonomy，才能做到 apples-to-apples comparability。这个过程既慢，又非常容易产生 silent human error。</p>

      <p>我用 Python 和 pandas 设计并实现了一条自动化 ETL pipeline。第一层是 data normalization，用来 ingest 原始 CSV 和 Excel 文件，处理编码问题、去掉多余空格、统一列名。第二层是 mapping engine，我做了一个 rule-based 的映射系统，先用 hash map 去做 <code>O(1)</code> exact match，对历史 master dictionary 里的标准账户名可以立刻命中，大概能覆盖 70% 到 80% 的情况；剩下的再通过 regex-based fuzzy matching 去捕捉轻微命名差异。第三层，也是我觉得最重要的一层，是 exception handling。我明确把系统设计成不去“猜”。任何没达到高置信度阈值的条目，都会被打到 <code>Exception Log</code> 里，让人去 review，而不是静默通过。</p>

      <p>最后这个 pipeline 把每个 engagement 的数据准备和映射时间从最多两天降到了大约三小时。更重要的是，Exception Log 把团队的工作方式从“人工看 100% 的数据”变成了“只看大约 10% 真正需要人工判断的 edge cases”，同时也保证了下游 risk model 使用的是可比、可审计的一致数据。这个项目给我最深的工程教训是，自动化系统绝对不能 silent failure。如果系统没有把握，就应该显式暴露不确定性，而不是假装自己知道答案。</p>
    </div>
  </details>

  <details>
    <summary>Best-Fit Questions</summary>
    <div class="bq-story-body">
      <p>Best for: invent and simplify, deliver results, improve process, prevent silent failure, raise quality standards, automate repetitive work.</p>
    </div>
  </details>
</section>

## Question Map

<section class="bq-story-card" id="question-map">
  <div class="bq-story-head">
    <h3>不同问题下应该怎么回答</h3>
    <div class="bq-tag-row">
      <span class="bq-tag">Question Strategy</span>
      <span class="bq-tag">Story Selection</span>
    </div>
  </div>

  <div class="bq-story-body">
    <table>
      <thead>
        <tr>
          <th>Question Type</th>
          <th>Best Story</th>
          <th>How To Frame It</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Learn something fast</td>
          <td>Story 1</td>
          <td>Emphasize how you narrowed scope, built toy examples first, and learned only the most relevant concepts under time pressure.</td>
        </tr>
        <tr>
          <td>Invent / simplify a process</td>
          <td>Story 4</td>
          <td>Lead with the repetitive manual workflow, then show how you turned it into a scalable system with validation.</td>
        </tr>
        <tr>
          <td>Customer obsession</td>
          <td>Story 3 or Story 2</td>
          <td>Story 3 if you want to emphasize deep empathy for real users. Story 2 if you want to emphasize understanding how users get stuck and designing around it.</td>
        </tr>
        <tr>
          <td>Ownership</td>
          <td>Story 3</td>
          <td>Stress that it was not assigned to you, but you raised it, built it, and shipped it because it mattered to user quality.</td>
        </tr>
        <tr>
          <td>Deliver results under constraints</td>
          <td>Story 1 or Story 4</td>
          <td>Story 1 for hard deadline and technical risk. Story 4 for operational impact and measurable time savings.</td>
        </tr>
        <tr>
          <td>Process improvement</td>
          <td>Story 4</td>
          <td>Focus on before/after: 1 to 2 days down to about 3 hours, plus earlier detection of bad data.</td>
        </tr>
        <tr>
          <td>Challenge the status quo</td>
          <td>Story 2 or Story 3</td>
          <td>Story 2 if you want product design innovation. Story 3 if you want to show you questioned the team's quality baseline.</td>
        </tr>
        <tr>
          <td>Dive deep technically</td>
          <td>Story 1</td>
          <td>Talk about the moment the docs stopped being enough and how you used source code to find root cause.</td>
        </tr>
        <tr>
          <td>Prevent a hidden risk early</td>
          <td>Story 4 or Story 3</td>
          <td>Story 4 if the risk is data integrity. Story 3 if the risk is a bad quality metric that does not reflect real user experience.</td>
        </tr>
      </tbody>
    </table>

    <h3>中文面试时的答题切法</h3>
    <p><strong>如果题目问 Learn Quickly / Learn and Be Curious：</strong>优先用 Story 1。重点不要只是说“我学了 LangGraph”，而要说你是怎么在时间不够的情况下筛选重点、搭 toy example、再去看源码，体现你有方法地学，而不是靠硬熬。</p>

    <p><strong>如果题目问 Invent and Simplify / Process Improvement：</strong>优先用 Story 4。开头先把手工流程有多重复、多慢、多危险讲清楚，再讲你怎么把它系统化、自动化，最后一定要落到时间从 1 到 2 天降到 3 小时这个量化结果。</p>

    <p><strong>如果题目问 Customer Obsession：</strong>优先用 Story 3，其次 Story 2。Story 3 更适合讲“我真正站在用户体验上重定义质量标准”；Story 2 更适合讲“我发现用户卡住点并不是一个问题，而是三个不同层次的问题”。</p>

    <p><strong>如果题目问 Ownership：</strong>优先用 Story 3。核心不是你写了一个功能，而是这件事不在你 sprint 里、没人要求你做、但你主动发现问题并推动落地。</p>

    <p><strong>如果题目问 Deliver Results：</strong>Story 1 和 Story 4 都能用。Story 1 更适合强调 deadline 压力和技术复杂度；Story 4 更适合强调稳定的业务结果和可量化效率提升。</p>

    <p><strong>如果题目问 Dive Deep：</strong>一定优先 Story 1。关键点是“文档无法解释时，我直接去看源代码定位框架层行为”。这是非常强的技术判断和 debug 深度。</p>

    <h3>一个万能回答框架</h3>
    <p>你可以把绝大多数问题都收敛成同一个结构：先用一句话定义问题本质，再讲你做的最关键决策，最后讲可量化结果和一个可迁移的方法论。这样不管题目是 leadership、ownership 还是 invent and simplify，你都不会答散。</p>
  </div>
</section>
