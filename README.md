---
title: "Study Notes"
---

# Study Notes

整理后的目录结构如下：

- [algorithms](./algorithms): 算法讲义、LeetCode 路线图、刷题笔记
- [python](./python): Python OOP 学习笔记
- [ood](./ood): OOD 总结与案例
- [books](./books): 独立书籍型项目与生成网页
- [resources](./resources): 代码、数据集、模型等运行资源

主要专题入口：

- [扩展题型总览（中文）](./algorithms/extended_problem_patterns_cn.md)
- [扩展题单详细教学](./algorithms/extended_problem_detailed/)
- [扩展题单完整答案](./algorithms/extended_problem_full_solutions/)
- [From OOP to OOD](./ood/from_oop_to_ood_cn.md)
- [AI Projects Self Study](./books/ai_projects_self_study/)
- [Amazon VO Coding Book](./books/amazon_vo_coding_book/book/)

建议使用方式：

1. 看笔记时从 `algorithms`、`python`、`ood` 开始
2. 看独立网页书时进入 `books`
3. 跑代码、处理数据、查看模型时进入 `resources`

说明：

- 这次整理主要做目录重组，没有改动学习内容本身
- 根目录现在只保留“入口”和“主分类”，减少源码、数据和生成物混放

## Local Development

首次安装依赖：

```bash
bundle config set --local path vendor/bundle
bundle install
```

本地启动预览：

```bash
bundle exec jekyll serve
```

启动后默认访问：

```text
http://127.0.0.1:4000
```

如果本机还没装 Jekyll，可以先确认 Ruby / Bundler 可用，再执行上面的 `bundle install`。

## Deploy To Vercel

仓库已经添加了：

- `Gemfile`
- `vercel.json`

Vercel 使用的构建方式是：

```bash
bundle exec jekyll build
```

构建输出目录是：

```text
_site
```

部署步骤：

1. 把当前改动 push 到 GitHub
2. 登录 Vercel 并导入这个仓库
3. 保持项目根目录为仓库根目录
4. 首次部署后拿到线上 URL
5. 以后每次 push，Vercel 会自动生成新的预览部署

## Optional GitHub Pages

这个项目本身也是标准 Jekyll 结构，所以如果后续你想切回 GitHub Pages，也可以直接使用 GitHub Pages 继续托管。
