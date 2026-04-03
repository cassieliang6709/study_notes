# Study Notes

整理后的目录结构如下：

- [algorithms](./algorithms): 算法讲义、LeetCode 路线图、刷题笔记
- [extended_problem_detailed](./extended_problem_detailed): 扩展题单详细教学
- [extended_problem_patterns_cn.md](./extended_problem_patterns_cn.md): 扩展题型汇总总览
- [python](./python): Python OOP 学习笔记
- [ood](./ood): OOD 总结与案例
- [code](./code): 练习代码、作业代码、测试文件
- [datasets](./datasets): 训练数据与语料
- [models](./models): 训练生成的模型文件

建议使用方式：

1. 看文档时从 `algorithms`、`python`、`ood` 开始
2. 跑代码时进入 `code`
3. 处理训练数据时进入 `datasets`
4. 模型产物统一放在 `models`

说明：

- 本次整理只调整了目录位置，没有改动代码内容
- 文档内主要链接已改为相对路径，后续移动目录时更稳定

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
