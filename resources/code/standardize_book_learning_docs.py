from pathlib import Path


ROOT = Path("/Users/cassie/study_notes")


def insert_after_title(path: Path, block: str) -> None:
    text = path.read_text()
    first_line = block.strip().splitlines()[0]
    if first_line in text:
        return

    first_heading = text.find("\n## ", text.find("\n# ") + 1)
    if first_heading == -1:
        raise RuntimeError(f"Could not find insertion point in {path}")

    updated = text[:first_heading].rstrip() + "\n\n" + block.strip() + "\n\n" + text[first_heading:].lstrip("\n")
    path.write_text(updated)


BLOCKS = {
    "books/ai_projects_self_study/src/how_to_use_this_book.md": """
## 这个方法页的总结

这页真正想教你的不是某一个仓库，而是“怎么学项目才不会停留在看 README”。核心原则很稳定：先找最小主链路，再跑通最小版本，再做一个小改动，最后用自己的话复盘。很多人学不会项目，不是因为材料少，而是因为一开始就把目标定成“全部看懂”。

## 本页在教什么

这页在教你一套通用项目学习法。无论你后面读的是 RAG、LLM from scratch、alignment 还是全栈模板，都可以先用这套顺序把项目拆小，再决定深入哪一层。

## Python 代码

```python
from dataclasses import dataclass


@dataclass
class ExperimentLog:
    change: str
    result: str
    why: str


log = ExperimentLog(
    change="top_k: 3 -> 5",
    result="answer used more supporting context",
    why="retrieval covered more relevant chunks",
)

print(log)
```

## 时间复杂度

本页主要是学习方法论，不以算法复杂度为重点。

## 空间复杂度

本页主要是学习方法论，不以算法复杂度为重点。

## 怎么想到

如果你一上来就试图理解整个项目，信息量会大到无法吸收。更稳的做法是先把问题降维成三个问题：最小输入是什么、最关键的中间步骤是什么、最后输出是什么。只要主链路清楚了，代码阅读和实验就会有抓手。

## 示例 case

例子：学习一个最小 RAG notebook 时，不先追问所有 embedding 细节，而是先确认 `question -> retrieval -> context -> answer` 这条链路真的跑通。然后只改一个参数，例如 `top_k`，再记录结果变化。

## 常见 Follow-up

- 如果项目太大，怎么找第一天应该看的文件？
- 如果跑不通，应该先修环境还是先读代码？
- 如果时间有限，什么样的“最小改动”最值得做？
""",
    "books/ai_projects_self_study/src/project_rag_from_scratch.md": """
## 这个项目 / 学习主题的总结

`rag-from-scratch` 最适合拿来建立 RAG 的第一性原理。它把系统压到最小，只保留最关键的几层：检索、上下文拼接、生成和结果检查。你真正要学到的不是“会跑 notebook”，而是为什么检索质量会直接决定回答质量。

## 本页在教什么

这页在教你怎么看一个最小 RAG 项目。重点不是功能多，而是链路清楚，方便你建立第一个稳定心智模型。

## Python 代码

```python
def retrieve(question: str, docs: list[str], top_k: int) -> list[str]:
    question_words = set(question.lower().split())
    ranked = sorted(
        docs,
        key=lambda doc: len(question_words & set(doc.lower().split())),
        reverse=True,
    )
    return ranked[:top_k]


docs = [
    "RAG uses retrieved context to ground answers",
    "FastAPI is a Python web framework",
    "Chunking affects retrieval quality",
]

print(retrieve("How does RAG use context", docs, 2))
```

## 时间复杂度

这个最小示例会把每个文档都扫描一次，所以时间复杂度近似为 `O(n * m)`，其中 `n` 是文档数，`m` 是单份文档平均词数。

## 空间复杂度

主要是临时集合和排序结果，额外空间复杂度近似为 `O(n)`。

## 怎么想到

初学 RAG 时，不要先想复杂 agent、reranker 或 evaluation 框架，先问自己一句话：模型回答时，外部知识是怎么被接进来的？一旦把这个问题盯住，RAG 的最小链路就会非常清楚。

## 示例 case

输入问题：`How does RAG use context`
输出上下文：优先返回和 `RAG`、`context` 更相关的文档。
解释：这能帮助你看懂“为什么最终答案不是凭空来的，而是被检索结果约束住的”。

## 常见 Follow-up

- `top_k` 变大后，答案一定更好吗？
- `chunk_size` 为什么会改变检索效果？
- 为什么看检索结果往往比只看最终答案更重要？
""",
    "books/ai_projects_self_study/src/project_complex_rag_guide.md": """
## 这个项目 / 学习主题的总结

`complex-RAG-guide` 的价值在于告诉你：真实 RAG 系统为什么会长出 cleaning、rewriting、filtering、planning、evaluation 这些层。它适合用来回答“最小 RAG 跑通以后，下一步复杂度到底从哪里来”。

## 本页在教什么

这页在教你怎么看“复杂 RAG”不是乱堆模块，而是针对不同失败点逐层补结构。

## Python 代码

```python
def rewrite_query(query: str) -> str:
    return query.replace("it", "the retrieved document")


def filter_docs(docs: list[str], keyword: str) -> list[str]:
    return [doc for doc in docs if keyword.lower() in doc.lower()]


query = "How do I use it safely?"
docs = [
    "The retrieved document should be cited in the answer.",
    "FastAPI app startup sequence.",
]

rewritten = rewrite_query(query)
filtered = filter_docs(docs, "document")
print(rewritten)
print(filtered)
```

## 时间复杂度

示例里主要做一次字符串处理和一次线性过滤，所以时间复杂度是 `O(n)`。

## 空间复杂度

过滤后的结果列表最多保留所有文档，所以空间复杂度是 `O(n)`。

## 怎么想到

复杂 RAG 的每一层都不是凭空加出来的，而是某个失败模式逼出来的。比如检索不稳，就会想到 query rewriting 或 filtering；回答不可信，就会想到 citation 和 evaluation。

## 示例 case

例子：用户问题里出现模糊代词 `it`，系统先把 query 改写得更明确，再过滤掉明显不相关文档。这样你就能看到“复杂度”其实是在修正系统失误。

## 常见 Follow-up

- 什么情况下值得加 query rewriting？
- filtering 和 reranking 在职责上有什么区别？
- evaluation 为什么是复杂 RAG 里迟早会补的一层？
""",
    "books/ai_projects_self_study/src/project_rag_techniques.md": """
## 这个项目 / 学习主题的总结

`rag_techniques` 更像 RAG 技术实验场，而不是单一系统。它的核心价值是帮你建立技术地图：不同技巧到底在优化哪一层，以及什么时候值得试它们。

## 本页在教什么

这页在教你不要把各种 RAG 技巧当成孤立术语，而是要把它们放回“检索前、检索中、检索后、生成前”这些位置里理解。

## Python 代码

```python
techniques = {
    "query_rewrite": "improve retrieval input",
    "rerank": "improve retrieval output order",
    "citation": "improve answer trust",
}

for name, goal in techniques.items():
    print(f"{name}: {goal}")
```

## 时间复杂度

这个示例只是遍历一个小字典，本页主要目标是理解技术分类，不以复杂度为重点。

## 空间复杂度

本页主要目标是理解技术分类，不以复杂度为重点。

## 怎么想到

当你看到很多 technique 时，最容易迷路。最稳的方法不是记名字，而是问一句：它到底在优化哪一层？只要这个问题答出来，技术地图就会开始成形。

## 示例 case

例子：如果系统主要问题是检索回来的内容顺序不对，那优先考虑 rerank；如果问题是用户提问方式和文档写法差很远，那优先考虑 query rewrite。

## 常见 Follow-up

- 哪些 technique 最适合先做对照实验？
- 什么情况下先换 retrieval，而不是先换模型？
- citation 和 evaluation 分别解决什么问题？
""",
    "books/ai_projects_self_study/src/project_deep_searcher.md": """
## 这个项目 / 学习主题的总结

`DeepSearcher` 更接近“能做成系统”的形态。它的重点不是最小原理，而是工程分层：provider、数据加载、查询流程、配置管理。这能帮助你从 demo 心智切到产品心智。

## 本页在教什么

这页在教你怎么看一个搜索系统为什么要拆成多层，而不是所有逻辑都塞进一个 notebook。

## Python 代码

```python
class SearchProvider:
    def search(self, query: str) -> list[str]:
        return [f"result for: {query}"]


def run_pipeline(query: str, provider: SearchProvider) -> list[str]:
    normalized_query = query.strip().lower()
    return provider.search(normalized_query)


print(run_pipeline("Private Data Search", SearchProvider()))
```

## 时间复杂度

示例重点是分层而不是算法优化，本节不以复杂度为重点。

## 空间复杂度

示例重点是分层而不是算法优化，本节不以复杂度为重点。

## 怎么想到

当系统开始有多种 provider、多种数据源和多种调用方式时，继续把逻辑写在一个地方会很快失控。把 provider 层和 pipeline 层拆开，是从“能跑”走向“能维护”的第一步。

## 示例 case

例子：同一个查询流程不变，只替换 `SearchProvider` 的实现，就能切不同搜索后端。这正是工程化系统要保留的能力。

## 常见 Follow-up

- provider 抽象为什么重要？
- 数据加载和查询为什么应该分阶段？
- 从 demo 到系统时，最先需要补的工程层有哪些？
""",
    "books/ai_projects_self_study/src/project_minimind.md": """
## 这个项目 / 学习主题的总结

`MiniMind` 很适合第一次把“小模型从输入到输出”的主链路串起来。它能帮你把 tokenizer、model、loss、generation 不再看成分散术语，而是看成一个连续流程。

## 本页在教什么

这页在教你用最小模型项目建立“文本是怎么变成 token，再变成预测”的基本直觉。

## Python 代码

```python
text = "hello"
vocab = {ch: idx for idx, ch in enumerate(sorted(set(text)))}
tokens = [vocab[ch] for ch in text]

print(vocab)
print(tokens)
```

## 时间复杂度

这个最小 tokenizer 示例线性扫描字符串，所以时间复杂度是 `O(n)`。

## 空间复杂度

词表和 token 序列都和输入长度相关，所以空间复杂度是 `O(n)`。

## 怎么想到

很多人一看到 LLM 就直接跳到 attention 或训练技巧，但更稳的入门顺序是先把最基础的问题搞懂：原始文本到底怎么进模型？只要 token 化这一步清楚了，后面的 embedding、forward、loss 才有真实落点。

## 示例 case

输入：`hello`
输出：字符词表和对应 token id 序列。
解释：这能帮助你把“文本进模型”从抽象名词变成可见的数据流。

## 常见 Follow-up

- tokenizer 和 embedding 的边界在哪里？
- logits 和 loss 是怎么从 token 序列继续算出来的？
- 为什么训练脚本和推理脚本的关注点不一样？
""",
    "books/ai_projects_self_study/src/project_cs336.md": """
## 这个项目 / 学习主题的总结

`CS336` 更像系统化课程主线，而不是单个仓库。它适合把你从“会跑一个小项目”推进到“知道语言模型训练从数据到系统是怎么接起来的”。

## 本页在教什么

这页在教你如何读一条完整课程路线，不只是看单个作业，而是把 tokenizer、模型、训练、系统、评估当成一个整体。

## Python 代码

```python
tokens = [3, 5, 8, 13, 21, 34]
context_length = 3
batches = [
    (tokens[i:i + context_length], tokens[i + 1:i + context_length + 1])
    for i in range(len(tokens) - context_length)
]

print(batches)
```

## 时间复杂度

构造训练窗口会线性扫描 token 序列，所以时间复杂度是 `O(n)`。

## 空间复杂度

窗口列表与训练样本数成正比，所以空间复杂度是 `O(n)`。

## 怎么想到

课程型资源最容易让人只记住章节名。更有效的方式是抓住一条主链：数据怎么被切成训练窗口，窗口怎么进模型，模型怎么产生 logits，再怎么变成 loss。这样课程知识才会连起来。

## 示例 case

输入 token：`[3, 5, 8, 13, 21, 34]`
输出窗口：例如 `([3, 5, 8], [5, 8, 13])`
解释：这展示了语言模型训练中“下一个 token 预测”的最小监督形式。

## 常见 Follow-up

- 为什么语言模型训练不只是写一个 Transformer 类？
- 数据、优化器、系统工程在课程里分别承担什么角色？
- 做完课程后，最值得自己手写重做的是哪些模块？
""",
    "books/ai_projects_self_study/src/project_model_alignment_from_scratch.md": """
## 这个项目 / 学习主题的总结

`ModelAlignmentFromScratch` 的价值在于把 SFT、EI、GRPO 这些名字拉回实现层。它能帮助你看懂：预训练以后，模型为什么还需要进一步对齐，以及对齐到底在优化什么。

## 本页在教什么

这页在教你从“训练名称”走向“训练目标”，理解 alignment 为什么会比普通监督学习多出 reward、grading、sampling 这些部件。

## Python 代码

```python
responses = {
    "answer_a": 0.55,
    "answer_b": 0.82,
    "answer_c": 0.61,
}

best_answer = max(responses, key=responses.get)
print(best_answer, responses[best_answer])
```

## 时间复杂度

遍历候选回答找最高分，时间复杂度是 `O(n)`。

## 空间复杂度

额外空间主要是候选回答表，本例空间复杂度是 `O(n)`。

## 怎么想到

理解 alignment 时，最稳的切入点不是公式，而是问：系统凭什么知道哪种回答更好？一旦你盯住“评分信号”这个核心，SFT、偏好优化和 RL 的区别就会更好理解。

## 示例 case

例子：三条候选回答分别有不同分数，系统选择奖励更高的一条。这能帮你抓住“alignment 在做偏好选择”这件事。

## 常见 Follow-up

- SFT 和 preference optimization 的核心差别是什么？
- reward signal 从哪里来？
- 为什么 agent RL 往往比单轮回答训练更不稳定？
""",
    "books/ai_projects_self_study/src/project_openpipe_art.md": """
## 这个项目 / 学习主题的总结

`OpenPipe ART` 让你第一次认真面对 agent reinforcement training 的复杂度。它的重点不只是“再训练一次模型”，而是 trajectory、rollout、reward over interaction 这些多步问题。

## 本页在教什么

这页在教你区分单轮回答训练和 agent 训练，理解为什么一旦任务跨多步，训练难度会迅速上升。

## Python 代码

```python
trajectories = {
    "plan_a": [0.2, 0.4, 0.1],
    "plan_b": [0.3, 0.5, 0.6],
}

total_reward = {name: sum(scores) for name, scores in trajectories.items()}
print(total_reward)
print(max(total_reward, key=total_reward.get))
```

## 时间复杂度

遍历所有 trajectory 分数求和，时间复杂度是 `O(n)`。

## 空间复杂度

额外空间是奖励汇总字典，所以空间复杂度是 `O(n)`。

## 怎么想到

想理解 agent RL，先不要急着看大框架，先抓住一个最朴素的问题：系统不是只输出一句话，而是连续执行多步动作时，奖励该怎么累计？一旦这个问题清楚了，trajectory 的意义就出来了。

## 示例 case

例子：`plan_b` 三步累计奖励更高，因此训练更倾向保留它。这个简单例子能帮助你建立多步奖励不是“一次打分”的直觉。

## 常见 Follow-up

- rollout 为什么会让训练成本更高？
- reward design 为什么会直接影响 agent 行为？
- agent RL 和普通偏好优化最大的工程差异是什么？
""",
    "books/ai_projects_self_study/src/project_full_stack_fastapi_template.md": """
## 这个项目 / 学习主题的总结

`full-stack-fastapi-template` 的价值在于把“后端 API、前端、数据库、认证、部署”这些真实产品层一次性摆到你面前。它适合帮助你从脚本和 notebook 心智切到完整应用心智。

## 本页在教什么

这页在教你怎么看一个完整 Web 应用的最小分层，而不是只会写一个单文件 API。

## Python 代码

```python
users = []


def create_user(email: str) -> dict[str, str]:
    user = {"email": email, "status": "active"}
    users.append(user)
    return user


print(create_user("cassie@example.com"))
print(users)
```

## 时间复杂度

这个最小示例只做一次追加，时间复杂度是 `O(1)`。

## 空间复杂度

用户列表随着数据增长，空间复杂度是 `O(n)`。

## 怎么想到

学全栈模板时，不要先陷进框架细节，先问自己：一个真实产品最小需要哪些层？只要先看清 API、状态、数据存储、用户身份这几层，后面的框架代码才有意义。

## 示例 case

输入：新增一个邮箱为 `cassie@example.com` 的用户
输出：返回用户对象，并保存到列表里
解释：这对应了真实应用里“请求到达后端，后端处理并持久化状态”的最小版本。

## 常见 Follow-up

- router、schema、model、db 这几层为什么要分开？
- 登录态为什么会显著提升项目复杂度？
- 从本地跑通到部署上线，中间还会多哪些系统问题？
""",
    "books/ai_projects_self_study/src/track_1_rag_systems.md": """
## 这个学习主线的总结

这条主线的核心不是把所有 RAG 仓库都看一遍，而是按难度和抽象层次逐步升级：先学最小链路，再看复杂组件，再建技术地图，最后接近系统形态。这样 beginner 才不会一开始就被复杂度淹没。

## 本页在教什么

这页在教你为什么 RAG 相关项目不能乱序看，以及每一站分别在补哪一层能力。

## Python 代码

```python
steps = ["retrieve", "build context", "generate answer"]
for step in steps:
    print(step)
```

## 时间复杂度

本页重点是学习路径设计，不以复杂度为重点。

## 空间复杂度

本页重点是学习路径设计，不以复杂度为重点。

## 怎么想到

RAG 相关资源太多时，最容易犯的错是按 star 数或热度乱看。更有效的顺序应该由“学习阻力”决定，而不是由“功能多少”决定。

## 示例 case

例子：先做 `rag-from-scratch`，你会先看懂主链路；再做 `complex-RAG-guide`，你才知道 rewriting、filtering 这些层为什么出现。

## 常见 Follow-up

- 为什么不建议 beginner 第一站就上 deep research 系统？
- 基础 RAG 和复杂 RAG 的分水岭是什么？
- 什么时候说明你已经可以从 demo 进入系统级项目？
""",
    "books/ai_projects_self_study/src/track_2_llm_from_scratch.md": """
## 这个学习主线的总结

这条主线是从“我知道 LLM 很强”走到“我能解释 token、batch、loss、sampling 怎么连起来”。它强调的是模型本体理解，而不是 API 调用熟练度。

## 本页在教什么

这页在教你为什么先从 `MiniMind` 这种低门槛实现入手，再去 `CS336` 这种系统课程，会更稳。

## Python 代码

```python
tokens = [1, 2, 3, 4]
inputs = tokens[:-1]
targets = tokens[1:]

print(inputs)
print(targets)
```

## 时间复杂度

这个最小样例只切分一次序列，时间复杂度是 `O(n)`。

## 空间复杂度

输入输出序列都和原长度相关，空间复杂度是 `O(n)`。

## 怎么想到

很多人学模型会直接看最复杂的课程或仓库，结果术语很多但链路不清。更好的顺序是先建立“下一个 token 预测”这个最小直觉，再逐步扩到完整训练系统。

## 示例 case

输入 token：`[1, 2, 3, 4]`
输出训练对：`[1, 2, 3] -> [2, 3, 4]`
解释：这就是语言模型训练最小监督形式的雏形。

## 常见 Follow-up

- tokenizer、embedding、attention 应该按什么顺序学？
- 为什么只会调 API 不等于理解模型本体？
- 做完 MiniMind 后，读 CS336 时最该抓哪条主线？
""",
    "books/ai_projects_self_study/src/track_3_alignment_and_agent_rl.md": """
## 这个学习主线的总结

这条主线解决的是“模型为什么在预训练后还不够可用”。它会带你从单模型对齐走到多步 agent 强化训练，让你看到稳定性和奖励设计为什么会变成核心问题。

## 本页在教什么

这页在教你为什么要先理解 SFT / 偏好优化，再去理解 agent RL，而不是一上来直接看最复杂的 rollout 框架。

## Python 代码

```python
preferences = {"response_a": 1, "response_b": 0}
chosen = max(preferences, key=preferences.get)
print(chosen)
```

## 时间复杂度

本页重点是训练思路，不以复杂度为重点。

## 空间复杂度

本页重点是训练思路，不以复杂度为重点。

## 怎么想到

alignment 最容易让人困惑的地方，是一堆训练名词并排出现。更稳的方法是按问题难度排序：先理解单步偏好，再理解多步奖励，这样 agent RL 的复杂度才不会显得跳跃。

## 示例 case

例子：如果两个回答里一个更符合偏好标注，系统会更倾向保留高分回答。再往后，agent RL 只是把这个选择问题扩展到多步轨迹上。

## 常见 Follow-up

- SFT、偏好优化、GRPO 的差别怎么用一句话讲清？
- 为什么 agent 任务训练更不稳定？
- reward model 和 grader 在实践里分别扮演什么角色？
""",
    "books/ai_projects_self_study/src/track_4_fastapi_fullstack.md": """
## 这个学习主线的总结

这条主线的目标是把你从“会写一些 Python”推进到“会做一个能用的产品”。核心不是框架名，而是后端、前端、数据、认证、部署这些层真正怎么接起来。

## 本页在教什么

这页在教你为什么全栈学习要尽快进入一个完整模板，而不是长期停留在零散 API demo。

## Python 代码

```python
tasks = []


def create_task(title: str) -> dict[str, str]:
    task = {"title": title, "done": "false"}
    tasks.append(task)
    return task


print(create_task("build first CRUD route"))
```

## 时间复杂度

追加一条任务记录，时间复杂度是 `O(1)`。

## 空间复杂度

任务列表增长时，空间复杂度是 `O(n)`。

## 怎么想到

如果你一直只写小 demo，就很难感受到真实产品为什么会需要 schema、db、auth、deploy。进入完整模板的价值，就是让这些层同时出现，帮助你建立产品整体感。

## 示例 case

例子：创建一条任务记录，对应到真实应用里就是“前端发请求，后端处理，状态被保存”。虽然例子很小，但它保留了全栈系统的基本信息流。

## 常见 Follow-up

- 为什么全栈模板比单个 API demo 更适合进阶？
- 数据库和认证通常在哪一步开始成为阻力？
- AI 项目从 notebook 走到产品时，为什么经常需要补这条主线？
""",
    "books/amazon_vo_coding_book/src/methodology.md": """
## 这个准备方法的总结

这本书最核心的方法不是背题号，而是把“公开题源信号、题目还原、可讲解法、follow-up 扛压”连成一套准备方式。你真正要练的是：短时间内说清思路、写出代码、处理追问。

## 本页在教什么

这页在教你如何理解这本书里的“高频”定义、题目还原方法，以及为什么 Amazon VO 不能只准备标准答案。

## Python 代码

```python
signals = {
    "forum_repeat_mentions": 3,
    "summary_post": 2,
    "reddit_confirmation": 1,
}

priority_score = sum(signals.values())
print(priority_score)
```

## 时间复杂度

示例只是汇总少量信号，本页重点是准备方法，不以复杂度为重点。

## 空间复杂度

本页重点是准备方法，不以复杂度为重点。

## 怎么想到

Amazon VO 的难点往往不在于题特别偏，而在于时间被压缩、BQ 会占时长、follow-up 会继续往下追。所以准备时必须从“能做出来”升级成“能讲清、能扩展、能扛追问”。

## 示例 case

例子：一道题如果在一亩三分地多次出现，又被总结帖点名，还在 Reddit 有人确认，那它就比只出现一次的题更值得优先投入时间。

## 常见 Follow-up

- 什么样的公开线索足够支持“高频”判断？
- 为什么 Amazon VO 里 follow-up 准备和主题本身一样重要？
- 如果时间只剩几天，应该怎么压缩准备顺序？
""",
    "books/amazon_vo_coding_book/src/problems.md": """
## 这个题型页的总结

这页不是简单列题，而是把 Amazon VO 常见高频题按题型家族整理，再补上原始信号、还原题目、核心解法和 follow-up 方向。它的重点是让你形成“同一类题怎么一起准备”的感觉。

## 本页在教什么

这页在教你如何把 cache、graph、DP、tree 这些常见 Amazon 家族题放到同一张图里理解，而不是一题一题孤立背。

## Python 代码

```python
from collections import deque


def ladder_length(begin: str, end: str, word_list: list[str]) -> int:
    words = set(word_list)
    if end not in words:
        return 0

    queue = deque([(begin, 1)])
    visited = {begin}

    while queue:
        word, steps = queue.popleft()
        if word == end:
            return steps
        for i in range(len(word)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                nxt = word[:i] + ch + word[i + 1:]
                if nxt in words and nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))
    return 0


print(ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
```

## 时间复杂度

以 `Word Ladder` 为代表题，朴素 BFS 会枚举每个位置的 26 个字符，时间复杂度常写作 `O(N * L * 26)`，其中 `N` 是词数，`L` 是单词长度。

## 空间复杂度

队列、访问集合和字典集合都与词数相关，所以空间复杂度是 `O(N)`。

## 怎么想到

准备 Amazon VO 时，不要只问“我会不会这道题”，还要问“这道题属于哪个家族、同家族的 follow-up 会怎么追”。像 `Word Ladder`、`Course Schedule`、`Word Search` 放在一起看，你会更容易形成 BFS / DFS / 图搜索的稳定模板。

## 示例 case

输入：`begin = "hit"`, `end = "cog"`
输出：`5`
解释：一条最短路径是 `hit -> hot -> dot -> dog -> cog`。这个例子能帮助你把图 BFS 和最短步数问题连起来。

## 常见 Follow-up

- 如果 interviewer 要你输出路径而不是长度，该怎么补？
- 什么情况下值得讲双向 BFS？
- 同一轮里如果又问 `Word Search` 或 `Course Schedule`，它们和 `Word Ladder` 的共同模板是什么？
""",
}


if __name__ == "__main__":
    for relative_path, block in BLOCKS.items():
        insert_after_title(ROOT / relative_path, block)
    print(f"Updated {len(BLOCKS)} book learning docs.")
