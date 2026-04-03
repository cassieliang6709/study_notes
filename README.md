# Study Notes

一个按主题持续整理的学习知识库，主要覆盖：

- 算法与刷题
- Python 与 OOP 基础
- OOD 设计
- BQ 面试准备
- 独立专题书籍
- 代码、数据集、模型等实验资源

这个仓库现在按“内容区”和“资源区”分开组织。最适合 GitHub 首页的读法，不是把所有目录都点一遍，而是先选你的目标，再按对应顺序走。

## 先看哪条路线

如果你不想自己判断，直接按下面选一条：

1. 想系统刷题：看 [刷题路线](#刷题路线)
2. 想补 Python 和 OOD 基础：看 [基础路线](#基础路线)
3. 想准备 Amazon / 行为面试：看 [面试路线](#面试路线)
4. 想直接读成体系的网页书：看 [书籍路线](#书籍路线)
5. 想找代码、数据或模型：看 [资源路线](#资源路线)

---

## 刷题路线

这条路线适合想建立算法 pattern 体系，而不是零散刷题的人。

### 第 1 步：先建立题型地图

先读：

1. [LeetCode 100 Pattern Roadmap CN](./algorithms/leetcode_100_pattern_roadmap_cn.md)
2. [Extended Problem Patterns CN](./algorithms/extended_problem_patterns_cn.md)

这一阶段的目标不是做题，而是先知道常见题型怎么分组，什么题应该往什么模板上靠。

### 第 2 步：补核心专题

按这个顺序读专题讲义：

1. [Linked List Study Guide](./algorithms/linked_list_study_guide.md)
2. [Binary Tree Study Guide](./algorithms/binary_tree_study_guide.md)
3. [Graph BFS DFS Study Guide](./algorithms/graph_bfs_dfs_study_guide.md)
4. [Heap Priority Queue Study Guide](./algorithms/heap_priority_queue_study_guide.md)

这一阶段的目标是把高频结构和遍历模板讲清楚。

### 第 3 步：进入详细题单

开始刷：

1. [LeetCode 100 Detailed](./algorithms/leetcode_100_detailed/)
2. [Extended Problem Detailed](./algorithms/extended_problem_detailed/)

这里适合边看边做，重点是：

- 识别题型
- 解释为什么是这个方法
- 能从 brute force 讲到最优解

### 第 4 步：卡住时再看完整答案

最后再用：

1. [Extended Problem Full Solutions](./algorithms/extended_problem_full_solutions/)

这个目录更适合查漏补缺，不适合一开始直接抄答案。

### 这条路线的终点

如果你按这条路线走完，应该能做到：

- 看到题先判断 pattern
- 高频树图题不会只靠记忆硬背
- 复杂题至少能讲清思路和转移逻辑

---

## 基础路线

这条路线适合基础还不稳，或者准备从 Python OOP 过渡到 OOD 的人。

### 第 1 步：先补 Python OOP

按顺序读：

1. [Python Overview](./python/index.md)
2. [OOP Prerequisites](./python/python_oop_prerequisites_cn.md)
3. [OOP Concepts](./python/python_oop_concepts_cn.md)

这里先解决“类、对象、继承、组合、抽象”这些基础概念。

### 第 2 步：再进入 OOD

接着读：

1. [OOD Overview](./ood/index.md)
2. [OOD Python Guide](./ood/ood_python_guide_cn.md)
3. [From OOP to OOD](./ood/from_oop_to_ood_cn.md)

这一段的目标是把“会写类”推进到“会拆职责、会建对象关系、会解释设计取舍”。

### 第 3 步：最后看案例

案例按这个顺序看最自然：

1. [Parking Lot](./ood/ood_cases/parking_lot_python.md)
2. [Amazon Locker](./ood/ood_cases/amazon_locker_python.md)
3. [Elevator System](./ood/ood_cases/elevator_system_python.md)

先看停车场，是因为它最适合练习实体、状态和规则拆分。后两个更适合练习扩展和设计约束。

### 这条路线的终点

如果你按这条路线走完，应该能做到：

- 清楚 OOP 和 OOD 的区别
- 能把小系统拆成类和职责
- 面试里不会只说“我会用 class”

---

## 面试路线

这条路线适合准备 Amazon、Meta 或通用软件工程面试。

### 第 1 步：先做行为面试框架

先读：

1. [BQ Prep](./bq_prep/)

这里先把 STAR、题型分类、Leadership Principles 映射和常见失误过一遍。

### 第 2 步：根据岗位补对应技术部分

如果你面的是偏 coding 岗位，接着走 [刷题路线](#刷题路线)。

如果你面的是偏基础或设计岗，接着走 [基础路线](#基础路线)。

### 第 3 步：如果目标是 Amazon

直接看：

1. [Amazon VO Coding Book](./books/amazon_vo_coding_book/book/)

这本书是从社区题源整理出来的 Amazon VO coding 高频题单，适合面前冲刺。

### 这条路线的终点

如果你按这条路线走完，应该能做到：

- BQ 不会只会背 STAR 空架子
- 技术准备和岗位要求能对上
- Amazon 类面试能快速进入高频题范围

---

## 书籍路线

这条路线适合你不想在仓库里跳来跳去，而是想直接读成体系内容。

当前推荐：

1. [AI Projects Self Study](./books/ai_projects_self_study/)
2. [Amazon VO Coding Book](./books/amazon_vo_coding_book/book/)

第一个更像项目型学习手册，第二个更像面试冲刺题书。

---

## 资源路线

这条路线不是“读文档”，而是“找材料”。

直接进入：

1. [resources/code](./resources/code/)
2. [resources/datasets](./resources/datasets/)
3. [resources/models](./resources/models/)

如果你只是来阅读内容，通常不需要先看这里。

---

## 仓库结构

根目录现在主要保留 6 个业务入口：

- [algorithms](./algorithms)
- [python](./python)
- [ood](./ood)
- [bq_prep](./bq_prep)
- [books](./books)
- [resources](./resources)

它们之间的关系是：

- `algorithms` 负责刷题体系
- `python` 和 `ood` 负责基础与设计
- `bq_prep` 负责行为面试
- `books` 负责专题型独立内容
- `resources` 负责代码、数据和模型

---

## 本地使用

这个仓库目前支持两种方式构建静态站点。

### 1. Jekyll

安装依赖：

```bash
bundle config set --local path vendor/bundle
bundle install
```

本地预览：

```bash
bundle exec jekyll serve
```

默认地址：

```text
http://127.0.0.1:4000
```

### 2. Python Static Builder

如果本机 Ruby / Bundler 环境不稳定，也可以直接运行：

```bash
python3 build.py
```

输出目录：

```text
_site
```

---

## 部署

仓库已经包含：

- [Gemfile](./Gemfile)
- [vercel.json](./vercel.json)

当前 Vercel 构建方式基于 Jekyll，输出目录为 `_site`。
