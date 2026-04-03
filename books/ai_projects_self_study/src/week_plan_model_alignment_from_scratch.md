title: "7-Day Plan: ModelAlignmentFromScratch"
---

# 7-Day Plan: ModelAlignmentFromScratch

对应项目：

- [项目导学页](./project_model_alignment_from_scratch.md)
- 原仓库: https://github.com/Sherlock1956/ModelAlignmentFromScratch

---

## 目标

7 天后你应该能：

- 说清 SFT、EI、GRPO 的差别
- 找到仓库里对应实现
- 跑通至少一种方法的最小流程

---

## Day 1

任务：

- 读 README
- 记录三种方法分别是什么

产出：

- 一张三方法总览表

---

## Day 2

任务：

- 浏览 `cs336_alignment/` 目录
- 定位各脚本职责

产出：

- 一张文件职责表

---

## Day 3

任务：

- 精读 `sft.py`
- 把它看成 baseline

产出：

- 一页 SFT 流程笔记

---

## Day 4

任务：

- 看 `expert_iteration.py`
- 记录它比 SFT 多出的循环逻辑

产出：

- 一张 SFT vs EI 对比表

---

## Day 5

任务：

- 看 `GRPO.py`
- 重点理解 reward 和组内比较

产出：

- 一页 GRPO 笔记

---

## Day 6

任务：

- 看 grader / reward 相关代码
- 记录回答是怎么被评估的

产出：

- 一张 reward 流程图

---

## Day 7

任务：

- 做整体复盘
- 写出这三种方法在你心里的分工

产出：

- 一页 alignment 总结

---

## 完成标准

- 你能区分三种训练方式
- 你能指出核心实现位置
- 你能继续进入 agent RL 方向
