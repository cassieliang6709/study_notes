# Project Guide: rag-from-scratch

原项目：

- https://github.com/langchain-ai/rag-from-scratch

---

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

## 这页为什么值得看

`rag-from-scratch` 不是“RAG 仓库之一”，而是你最适合开始的那个。

原因很简单：

- 它足够轻
- 它的主链路清楚
- 你能很快把注意力放在真正重要的地方

如果你一开始就去做复杂 agent RAG，通常会学乱。你会看到很多组件，但不知道哪些才是第一性原理。

这个项目的价值就在于，它会逼你先把最小 RAG 想清楚。

---

## 你到底应该从它学到什么

不是“我会调一个 notebook”。

你真正应该从它学到的是：

1. 一个最小 RAG 系统到底由哪些步骤组成
2. 检索结果为什么比最终答案更值得先看
3. 改 retrieval 参数时，回答为什么会跟着变
4. 为什么 context grounding 是 RAG 的核心，不是可选项

---

## 最小主链路

你第一遍必须能自己复述这条链路：

```text
user question
-> embed / retrieve relevant chunks
-> select context
-> build prompt with retrieved context
-> generate answer
-> inspect whether answer is actually grounded in context
```

如果你讲不出这条链路，就说明你还没有真的理解这个项目。

---

## 这项目最适合学的三个观察点

### 1. 检索出来了什么

大多数初学者只看最终回答，这是错的。

你应该先盯：

- 检索到了哪些 chunk
- 这些 chunk 和问题是否真的相关
- 是不是召回太少或太多

### 2. 最终 prompt 长什么样

你要知道模型不是“自动懂了”，而是被塞了一个包含上下文的 prompt。

你应该看：

- 原始问题是什么
- 被拼进去的 context 是什么
- prompt 是否清楚地区分了“用户问题”和“可参考资料”

### 3. 改一个参数后发生了什么

真正的学习发生在你改动以后。

你最适合先改这三个变量：

- `chunk_size`
- `top_k`
- prompt 里的回答约束

---

## 为什么它适合作为第一站

因为它把复杂度压低了。

你在这里不用先处理：

- 多步 query planning
- reranker 组合
- agent orchestration
- 复杂评估框架

这不是缺点，反而是优点。第一站就应该先把主链路和观察方法学会。

---

## 第一周不要做什么

第一周最容易把自己带偏的行为有这些：

- 一上来就换成自己的大数据集
- 一上来就加 UI
- 试图把 notebook 全看完
- 看到效果不好就立刻怀疑模型本身

第一周你只需要做“小而可解释”的实验。

---

## 第一周真正该做什么

### Day 1

- 跑通最基础 notebook
- 记录最小输入和最小输出

### Day 2

- 画出 retrieval -> context -> answer 主链路
- 把每一步写成一句人话

### Day 3

- 看 retrieval 结果，而不是只看 final answer
- 记录“召回正确”和“召回错误”的例子

### Day 4

- 修改 `top_k`
- 观察 context 变长之后回答有没有变稳

### Day 5

- 修改 `chunk_size`
- 观察检索粒度变化带来的影响

### Day 6

- 改 prompt 里的回答约束
- 比如要求“只能根据 context 回答”

### Day 7

- 用自己的话复盘：
  - 最小 RAG 是什么
  - 这个仓库最关键的学习价值是什么
  - 如果自己重写，你先做哪一层

更细的执行版在这里：

- [rag-from-scratch 7-Day Plan](./week_plan_rag_from_scratch.md)

---

## 你真正要产出的东西

别把“跑通 notebook”当成完成。

这一页最推荐你产出的是下面三样：

### 1. 一张主链路图

```text
question -> retrieval -> context assembly -> generation -> inspection
```

### 2. 一份参数实验记录

至少记两组：

- `top_k` 从小到大怎么变
- `chunk_size` 从小到大怎么变

### 3. 一段自己的解释

你要能不看仓库，自己说：

“RAG 不是把 LLM 和向量库硬拼起来，而是通过检索到的外部上下文来约束回答。”

如果说不出来，就说明你还在“看”，不是“学会”。

---

## 常见误区

### 误区 1：只看最终回答

真正的问题通常出在检索阶段，不在生成阶段。

### 误区 2：一开始就追求复杂

你现在需要的是可解释性，不是复杂度。

### 误区 3：不做对照实验

不改参数，你学不到系统行为。

---

## 最小完成标准

你至少要满足下面三条中的两条：

- 能自己复述最小 RAG 主链路
- 能解释 `top_k` 或 `chunk_size` 改动后的结果变化
- 能用自己的小文档重跑一次并观察差异

---

## 做完它以后该去哪

下一站建议直接去：

- [Complex RAG Guide](./project_complex_rag_guide.md)

理由是你会立刻看见“一个最小 RAG”和“一个更复杂 RAG”之间到底多出了哪些层：

- query rewriting
- reranking
- routing
- evaluation

这时你的学习就不是乱看，而是有参照系地升级。
