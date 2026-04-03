# Project Guide: OpenPipe ART

原项目：

- https://github.com/OpenPipe/ART

---

## 这个项目最适合你学什么

`ART` 是 Agent Reinforcement Trainer。

你在这里主要学：

- agent reinforcement training 的任务形式
- 多步任务上的 GRPO 风格训练思路
- 为什么 agent 训练和普通 supervised fine-tuning 不一样

---

## 为什么应该放在后面做

因为它依赖的前置理解更多：

- 你最好已经知道 LLM 基础训练链路
- 最好已经知道 alignment / policy optimization 的基本概念
- 最好已经理解多步 agent 不只是“一次输出”

所以它更适合放在后段。

---

## 前置知识

- [Track 2](./track_2_llm_from_scratch.md) 基础
- [ModelAlignmentFromScratch](./project_model_alignment_from_scratch.md) 里至少看懂一种对齐方法
- trajectory / reward / rollout 的基本概念

---

## 先看什么

建议顺序：

1. README 的项目定位
2. quick start 或最小示例
3. 任务定义方式
4. rollout / reward / optimization 的主流程
5. notebooks 或 examples

---

## 第一周最小任务

第一周不要想着完整训练大 agent。

只要做到：

1. 跑通一个最小示例
2. 弄清输入任务、交互轨迹、奖励、更新之间的关系
3. 用自己的话写出 agent RL 和 SFT 的差别

---

## 开做指南

### 环境要求

- 能跑深度学习训练的环境
- 最好有 GPU
- 对依赖和训练配置有耐心

### 最小启动动作

1. 克隆仓库
2. 安装依赖
3. 找最小 example
4. 跑一次极小规模训练或演示流程

### 第一遍不要改什么

- 不要先扩大任务规模
- 不要先魔改 reward
- 不要先追求 benchmark 成绩

### 第二遍建议你改什么

- 改一个小 reward 定义
- 改一个任务模板
- 观察 agent 轨迹变化

---

## 你做完后应该掌握什么

- 知道 agent RL 为什么关注多步 interaction
- 知道 rollout 数据和普通 supervised 数据的差异
- 知道框架在帮你管理哪些复杂性

---

## 常见卡点

- 把它当成普通微调框架
- 没理解任务轨迹就开始调超参
- 对奖励设计没有基本假设，导致看不懂训练结果

---

## 最小完成标准

- 你能运行一个最小 agent training / demo
- 你能说清 agent RL 和单步 alignment 的区别
- 你能指出这个框架最核心的两个抽象层

---

## 下一站

这个项目更像这条线的高阶实践点。

如果做完它，建议你自己做一个非常小的实验：

- 设计一个简单多步任务
- 定义一个很朴素的 reward
- 看 agent 是否能学到更稳定的行为
