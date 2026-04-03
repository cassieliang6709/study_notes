# Study Notes

一个持续整理中的学习知识库，内容覆盖：

- 算法与刷题
- Python 与 OOP 基础
- OOD 设计
- BQ 面试准备
- 独立专题书籍与网页化笔记
- 代码、数据集、模型等实验资源

这个仓库现在按“主题内容”和“运行资源”分开组织，GitHub 首页主要用于快速导航。

## Quick Start

如果你第一次打开这个仓库，建议按这个顺序看：

1. [Algorithms](./algorithms)
2. [Python](./python)
3. [OOD](./ood)
4. [BQ Prep](./bq_prep)
5. [Books](./books)

## Main Sections

### [algorithms](./algorithms)

算法主目录，包含路线图、专题讲义、扩展题单和完整答案。

重点入口：

- [LeetCode 100 Pattern Roadmap CN](./algorithms/leetcode_100_pattern_roadmap_cn.md)
- [Extended Problem Patterns CN](./algorithms/extended_problem_patterns_cn.md)
- [Extended Problem Detailed](./algorithms/extended_problem_detailed/)
- [Extended Problem Full Solutions](./algorithms/extended_problem_full_solutions/)
- [LeetCode 100 Detailed](./algorithms/leetcode_100_detailed/)

### [python](./python)

Python OOP 基础与面向对象概念笔记。

重点入口：

- [Python Overview](./python/index.md)
- [OOP Prerequisites](./python/python_oop_prerequisites_cn.md)
- [OOP Concepts](./python/python_oop_concepts_cn.md)

### [ood](./ood)

面向对象设计总结、案例和桥接文档。

重点入口：

- [OOD Overview](./ood/index.md)
- [OOD Python Guide](./ood/ood_python_guide_cn.md)
- [From OOP to OOD](./ood/from_oop_to_ood_cn.md)
- [OOD Cases](./ood/ood_cases/)

### [bq_prep](./bq_prep)

行为面试与 STAR 方法准备区。

### [books](./books)

独立成册的学习项目，适合直接网页阅读。

当前项目：

- [AI Projects Self Study](./books/ai_projects_self_study/)
- [Amazon VO Coding Book](./books/amazon_vo_coding_book/book/)

### [resources](./resources)

运行资源集中区，避免代码、数据和模型与笔记正文混在一起。

包含：

- [code](./resources/code/)
- [datasets](./resources/datasets/)
- [models](./resources/models/)

## Suggested Usage

### 如果你是来刷题

从 [algorithms](./algorithms) 开始，优先看：

- `leetcode_100_pattern_roadmap_cn.md`
- `extended_problem_patterns_cn.md`
- `extended_problem_detailed/`

### 如果你是来补基础

从 [python](./python) 和 [ood](./ood) 开始。

### 如果你是来看完整网页书

直接进 [books](./books)。

### 如果你是来找代码或实验材料

直接进 [resources](./resources)。

## Local Development

这个仓库目前主要支持两种本地构建方式。

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

如果本机 Ruby / Bundler 环境不稳定，也可以直接用项目内脚本生成静态站点：

```bash
python3 build.py
```

输出目录：

```text
_site
```

## Deploy

仓库已经包含：

- [Gemfile](./Gemfile)
- [vercel.json](./vercel.json)

当前 Vercel 构建方式基于 Jekyll，输出目录为 `_site`。

## Notes

- 根目录现在尽量只保留“入口”和“主分类”
- 独立书籍型项目统一放在 [books](./books)
- 代码、数据集、模型统一放在 [resources](./resources)
