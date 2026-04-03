# Study Notes

这是一个按学习路径组织的知识库，目标不是“把文件都放上来”，而是让 beginner 也能看懂：

- 先学什么
- 每一类文档分别负责什么
- 哪些文档是导航，哪些文档是真正的学习正文
- 遇到 coding 问题时，应该怎么从题意走到代码和算法点

## 导航文档 vs 学习文档

### 导航文档

这些文档负责带路，不负责展开所有题解正文：

- 根 `README.md`
- 根 `index.md`
- 各模块 `index.md`

### 学习文档

这些文档负责真正讲知识：

- 算法路线图
- 专题讲义
- 详细题解
- 完整答案
- Python / OOP / OOD 概念文档
- OOD 案例

学习文档会尽量统一成这套 beginner 友好的模板：

- 这个题型 / 算法点 / 概念点的总结
- 题目含义或本节目标
- Python 代码
- 时间复杂度
- 空间复杂度
- 怎么想到
- 示例 case
- 常见 follow-up

如果某篇主要讲概念而不是算法，会明确写“本节不以复杂度为重点”。

## 这个仓库适合谁

- 想系统刷题，而不是随机刷题的人
- Python / OOP / OOD 基础不稳的人
- 准备 coding interview / design interview 的人
- 想把笔记、题解、案例、专题书放在一个地方统一学习的人

## 六个主入口

- [algorithms](./algorithms/)
- [python](./python/)
- [ood](./ood/)
- [bq_prep](./bq_prep/)
- [books](./books/)
- [resources](./resources/)

## 推荐学习路线

### 1. 想系统刷题

从 [algorithms/index.md](./algorithms/index.md) 开始。

推荐顺序：

1. Pattern Roadmap
2. Study Guide
3. LeetCode 100 Detailed
4. Extended Problems Detailed
5. Extended Problems Full Solutions
6. Company Hot Questions

### 2. 想补 Python / OOP / OOD

推荐顺序：

1. [python/index.md](./python/index.md)
2. [ood/index.md](./ood/index.md)
3. [ood/ood_cases/index.md](./ood/ood_cases/index.md)

### 3. 想准备 Amazon / 面试冲刺

推荐顺序：

1. [bq_prep/index.md](./bq_prep/index.md)
2. [algorithms/company_hot_questions/index.md](./algorithms/company_hot_questions/index.md)
3. [books/amazon_vo_coding_book/book/](./books/amazon_vo_coding_book/book/)

### 4. 想按专题书来学

从 [books/index.md](./books/index.md) 开始。

## Algorithms 模块内部怎么分工

这是仓库里最容易重复的部分，所以这里明确边界。

### 路线图 / 总览

负责建立题型地图，不负责写全题答案。

### Study Guide

负责一个专题的模式总结和代表题。

### LeetCode 100 Detailed

负责高频核心题的详细教学版。

### Extended Problems Detailed

负责扩展题单的教学版。

### Extended Problems Full Solutions

负责完整答案和系统复盘，适合查漏补缺。

### Company Hot Questions

负责把高频公司题拆成一题一页，适合单点冲刺。

## 读题解时怎么读最有效

不要只看代码。推荐顺序：

1. 先看“这个题型 / 算法点的总结”
2. 再看“题目含义”
3. 试着自己判断应该用什么方法
4. 再看 Python 代码
5. 看复杂度
6. 看“怎么想到”
7. 最后看示例 case 和 follow-up

## Online Preview

- 主站：
  <https://study-notes-murex-ten.vercel.app>
- 旧站：
  <https://study-notes.vercel.app>
- `AI Projects Self-Study Hub`：
  <https://aiprojectsselfstudy.vercel.app>
- `Amazon VO Coding Book`：
  <https://amazon-vo-coding-book.vercel.app>
- `BQ Prep`：
  <https://bq-prep.vercel.app>

## 本地构建

### 主站

```bash
python3 build.py
```

### mdBook

```bash
mdbook build books/amazon_vo_coding_book
mdbook build books/ai_projects_self_study
```

## 如果你现在就想开始

- 想刷题：去 [algorithms](./algorithms/)
- 想补 OOP：去 [python](./python/)
- 想做设计题：去 [ood](./ood/)
- 想冲 Amazon：去 [company_hot_questions](./algorithms/company_hot_questions/)
