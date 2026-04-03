# Amazon VO Coding 高频题清单

这是一个本地可维护的 `mdBook` 项目，用来整理 Amazon VO coding 高频题型、业务伪装、代码模板、follow-up 和口语回答稿。

## 项目链接

- GitHub 仓库：
  [https://github.com/cassieliang6709/study_notes](https://github.com/cassieliang6709/study_notes)
- 当前分支：
  [https://github.com/cassieliang6709/study_notes/tree/codex/amazon-vo-coding-book-refresh](https://github.com/cassieliang6709/study_notes/tree/codex/amazon-vo-coding-book-refresh)
- PR 入口：
  [https://github.com/cassieliang6709/study_notes/pull/new/codex/amazon-vo-coding-book-refresh](https://github.com/cassieliang6709/study_notes/pull/new/codex/amazon-vo-coding-book-refresh)
- Vercel Production：
  [https://amazon-vo-coding-book.vercel.app](https://amazon-vo-coding-book.vercel.app)

## 本地预览

```bash
cd /Users/cassie/projects/study_notes/books/amazon_vo_coding_book
mdbook serve
```

默认会启动本地预览服务。

## 本地构建

```bash
cd /Users/cassie/projects/study_notes/books/amazon_vo_coding_book
mdbook build
```

生成结果会在 `book/` 目录下。

## 部署到 Vercel

推荐直接部署构建产物目录：

```bash
cd /Users/cassie/projects/study_notes/books/amazon_vo_coding_book
mdbook build
cd book
vercel --yes
```

如果需要生产部署：

```bash
cd /Users/cassie/projects/study_notes/books/amazon_vo_coding_book
mdbook build
cd book
vercel --prod --yes
```

这样可以把 `mdBook` 生成的静态页面直接作为 Vercel 静态站发布。

## 内容来源

- 主底稿来自本地整理文档：
  - Amazon VO coding 高频整理稿
- 结构化重写目标：
  - 按题型组织
  - 每章统一包含题面、识别信号、业务包装、代码模板、follow-up、口语稿

## 结构说明

- `src/README.md`：首页
- `src/high-frequency-overview.md`：总表
- `src/*.md`：各题型章节
- `src/business-disguise-index.md`：业务题面反查索引
- `src/speaking-scripts.md`：面试开口和口语回答稿
- `src/cheatsheet.md`：一页速记和 3 天冲刺顺序
- `book/`：`mdbook build` 生成的静态站点输出目录
