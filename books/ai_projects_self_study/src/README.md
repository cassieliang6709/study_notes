# AI Projects Self-Study Hub

这本书不是项目收藏夹，而是一个可执行的自学路线。

你给我的那批项目本身都不错，但如果只是把仓库链接堆在一起，基本学不会。真正需要的是三件事：

- 先做哪个，后做哪个
- 每个项目第一周到底该做什么
- 怎么验证自己不是“看懂了”，而是真的会了

这本 mdBook 就是为这个目的重做的。

---

## 这本书解决什么问题

很多 AI 项目自学最后都会卡在同一个地方：

- README 看了，但不知道先跑哪一部分
- notebook 跑通了，但说不清核心链路
- 项目做完了，但不知道自己到底学到了什么

所以这本书的结构不是“仓库介绍”，而是四层：

1. 导学页：这个项目值不值得现在做
2. `7-Day Plan`：第一周每天具体做什么
3. 自测题：检查你是否真的掌握
4. 参考答案：用来核对理解，不是先看的

---

## 推荐学习顺序

如果你是第一次系统学这条线，我建议按这个顺序：

1. [rag-from-scratch](./project_rag_from_scratch.md)
2. [Complex RAG Guide](./project_complex_rag_guide.md)
3. [RAG Techniques](./project_rag_techniques.md)
4. [DeepSearcher](./project_deep_searcher.md)
5. [MiniMind](./project_minimind.md)
6. [Stanford CS336](./project_cs336.md)
7. [ModelAlignmentFromScratch](./project_model_alignment_from_scratch.md)
8. [OpenPipe ART](./project_openpipe_art.md)
9. [full-stack-fastapi-template](./project_full_stack_fastapi_template.md)

这样排不是因为前面的“更火”，而是因为：

- 前四个先把 RAG 做扎实
- 中间两个补齐模型本体理解
- 最后两个再看 alignment 和 agent RL

---

## 三条主线

### 1. RAG / Retrieval Systems

适合你如果现在最想做：

- 企业知识库问答
- 检索增强生成
- deep research
- 多步搜索

入口：

- [RAG Systems Track](./track_1_rag_systems.md)

### 2. LLM From Scratch

适合你如果现在最想真正搞懂：

- tokenizer
- transformer
- pretraining
- 小模型从零训练

入口：

- [LLM From Scratch Track](./track_2_llm_from_scratch.md)

### 3. Alignment / Agent RL

适合你如果已经有一点模型基础，想进一步理解：

- SFT
- preference optimization
- GRPO
- agent reinforcement training

入口：

- [Alignment / Agent RL Track](./track_3_alignment_and_agent_rl.md)

### 4. FastAPI / Full Stack Web

适合你如果现在想真正补齐：

- FastAPI 后端
- 前端调用 API
- 登录认证
- 数据库和 CRUD

入口：

- [FastAPI / Full Stack Web Track](./track_4_fastapi_fullstack.md)

---

## 先看什么最有用

如果你只准备开始一个项目，不要乱翻。

按这个顺序：

1. 看 [怎么真正学会一个项目](./how_to_use_this_book.md)
2. 选一条 track
3. 打开对应项目导学页
4. 接着做对应 `7-Day Plan`

如果你现在就想从最稳的入口开始，直接去：

- [rag-from-scratch](./project_rag_from_scratch.md)

---

## 这本书里最值得你反复用的部分

### 项目导学

它回答的是：

- 这个项目最适合学什么
- 为什么现在做它
- 先看什么
- 第一周最小任务是什么

### 7-Day Plans

它回答的是：

- 今天具体做什么
- 今天结束时应该产出什么
- 哪些任务是第一轮必须完成的

### 自测题

它回答的是：

- 你会不会解释
- 你会不会比较
- 你能不能自己复盘一个系统

---

## 项目索引

### RAG

- [rag-from-scratch](./project_rag_from_scratch.md)
- [Complex RAG Guide](./project_complex_rag_guide.md)
- [RAG Techniques](./project_rag_techniques.md)
- [DeepSearcher](./project_deep_searcher.md)

### LLM / Training

- [MiniMind](./project_minimind.md)
- [Stanford CS336](./project_cs336.md)

### Alignment / Agent RL

- [ModelAlignmentFromScratch](./project_model_alignment_from_scratch.md)
- [OpenPipe ART](./project_openpipe_art.md)

### FastAPI / Full Stack Web

- [full-stack-fastapi-template](./project_full_stack_fastapi_template.md)

### Weekly execution

- [rag-from-scratch 7-Day Plan](./week_plan_rag_from_scratch.md)
- [Complex RAG Guide 7-Day Plan](./week_plan_complex_rag_guide.md)
- [RAG Techniques 7-Day Plan](./week_plan_rag_techniques.md)
- [DeepSearcher 7-Day Plan](./week_plan_deep_searcher.md)
- [MiniMind 7-Day Plan](./week_plan_minimind.md)
- [Stanford CS336 7-Day Plan](./week_plan_cs336.md)
- [ModelAlignmentFromScratch 7-Day Plan](./week_plan_model_alignment_from_scratch.md)
- [OpenPipe ART 7-Day Plan](./week_plan_openpipe_art.md)
- [full-stack-fastapi-template 7-Day Plan](./week_plan_full_stack_fastapi_template.md)

### Self-tests

- [RAG 自测](./self_test_rag.md)
- [LLM From Scratch 自测](./self_test_llm_from_scratch.md)
- [Alignment / Agent RL 自测](./self_test_alignment_agent_rl.md)
- [FastAPI / Full Stack Web 自测](./self_test_fastapi_fullstack.md)
- [综合项目自测](./self_test_capstone.md)

### Answer keys

- [RAG 参考答案](./answer_key_rag.md)
- [LLM From Scratch 参考答案](./answer_key_llm_from_scratch.md)
- [Alignment / Agent RL 参考答案](./answer_key_alignment_agent_rl.md)
- [FastAPI / Full Stack Web 参考答案](./answer_key_fastapi_fullstack.md)
- [综合项目参考答案](./answer_key_capstone.md)

---

## 最后一个提醒

这本书最核心的目标不是让你“知道更多名词”，而是让你真的能做到下面这几件事：

- 讲清一个项目的最小主链路
- 改一个局部模块并观察变化
- 比较两个相邻项目在架构上的差别
- 用自己的话复盘为什么某个设计有效

如果你做到了，这套资料才算有用。
