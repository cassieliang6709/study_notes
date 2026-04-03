---
title: "07 栈与队列详细教学"
---

# 07 栈与队列详细教学

---

## 一、什么时候想到栈

```text
// 括号匹配
// 表达式求值
// 最近更大更小
// 等未来信息
```

---

## 二、代表题

### Valid Parentheses

```text
// 栈基础题
```

### Simplify Path

```text
// 用栈维护路径片段
```

### Decode String

```text
// 嵌套结构，遇到 ] 结算
```

### Basic Calculator / II / III

```text
// II 先掌握乘除即时结算
// I / III 再处理括号
```

### Longest Valid Parentheses

```text
// 栈 or DP
```

### Trapping Rain Water

```text
// 双指针更直观
// 单调栈也要会
```

### Exclusive Time of Functions

```text
// 模拟调用栈
```

---

## 建议顺序

1. Valid Parentheses
2. Simplify Path
3. Decode String
4. Basic Calculator II
5. Basic Calculator
6. Longest Valid Parentheses
7. Trapping Rain Water
8. Design Circular Queue
9. Exclusive Time of Functions
10. Basic Calculator III


---

## Quiz

**Q1: 单调栈（Monotonic Stack）适合解决什么类型的题？**

- [ ] 求最短路径
- [ ] 找每个元素左边/右边第一个比它大或小的元素 ✅
- [ ] 括号匹配
- [ ] 字符串解码

**Q2: `Trapping Rain Water` 用单调栈，栈里存的是什么？**

- [ ] 水的高度
- [ ] 每个位置的雨水量
- [ ] 下标（对应一个递减单调栈） ✅
- [ ] 左右边界

**Q3: `Decode String`（如 `3[a2[bc]]`）用栈解，遇到 `]` 时怎么处理？**

- [ ] 直接输出
- [ ] 弹出栈顶字符直到遇到 `[`，取出次数，将重复结果压回栈 ✅
- [ ] 继续入栈
- [ ] 递归调用

**Q4: `Basic Calculator` 遇到 `(` 时应该做什么？**

- [ ] 报错
- [ ] 把当前结果和符号压栈，重置当前计算状态 ✅
- [ ] 直接跳过
- [ ] 立即计算括号内的表达式

**Q5: `Largest Rectangle in Histogram` 用单调栈，栈维护什么性质？**

- [ ] 递减序列
- [ ] 递增序列（当遇到更矮的柱子时，弹出计算面积） ✅
- [ ] 所有柱子的下标
- [ ] 柱子高度的前缀和
