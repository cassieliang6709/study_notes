# 08 动态规划

DP 最容易卡住，所以一定要按固定顺序思考。

---

## 一、DP 四步法

```text
// 1. dp 状态表示什么？
// 2. 状态转移是什么？
// 3. 初始化是什么？
// 4. 遍历顺序是什么？
```

你只要跳过第 1 步，后面基本都会乱。

---

## 二、最常见几类 DP

### 1. 一维线性 DP

题目：

- Climbing Stairs
- House Robber
- Coin Change
- Perfect Squares
- Word Break

模板：

```text
dp[i] = 到位置 i / 前 i 个元素的答案
```

---

### 2. 网格 DP

题目：

- Unique Paths
- Minimum Path Sum

模板：

```text
dp[r][c] = 到格子 (r, c) 的答案
// 通常来自上边和左边
```

---

### 3. 背包 DP

题目：

- Partition Equal Subset Sum
- Coin Change
- Perfect Squares

关键：

```text
// 是 0-1 背包，还是完全背包
// 内层循环顺序非常重要
```

---

### 4. 双串 DP

题目：

- Longest Common Subsequence
- Edit Distance

模板：

```text
dp[i][j] = s1[:i] 和 s2[:j] 的答案
```

---

### 5. 区间 / 字符串 DP

题目：

- Longest Palindromic Substring
- Longest Valid Parentheses

---

## 三、重点题

### 1. Climbing Stairs

```text
// 最基础 DP
// 到第 i 阶，可以从 i-1 或 i-2 来
```

### 2. House Robber

```text
// 选当前，就不能选前一个
// 不选当前，就沿用前一个最优解
```

### 3. Unique Paths

```text
// 从上或从左走到当前位置
```

### 4. Minimum Path Sum

```text
// 当前位置最小和 = 当前值 + min(上, 左)
```

### 5. Coin Change

```text
// 最少硬币数
// 非常适合练“状态 + 转移”
```

### 6. Word Break

```text
// 枚举最后一刀切在哪里
```

### 7. Partition Equal Subset Sum

```text
// 是否能凑出 target
// 标准 0-1 背包
```

### 8. Longest Common Subsequence

```text
// 相同看左上角 + 1
// 不同看左边和上边最大值
```

### 9. Longest Increasing Subsequence

```text
// 先掌握 O(n^2) DP 版本
```

### 10. Longest Palindromic Substring

```text
// 初学更建议中心扩展
// 之后再看区间 DP
```

### 11. Maximum Product Subarray

```text
// 同时维护最大积和最小积
```

### 12. Edit Distance

```text
// 插入、删除、替换
```

---

## 四、DP 题统一自检

```text
// dp[i] 到底表示“前 i 个”还是“以 i 结尾”？
// base case 是否覆盖最小情况？
// 遍历顺序是否满足依赖关系？
```

---

## 五、推荐刷题顺序

1. Climbing Stairs
2. Pascal's Triangle
3. House Robber
4. Unique Paths
5. Minimum Path Sum
6. Coin Change
7. Perfect Squares
8. Word Break
9. Partition Equal Subset Sum
10. Longest Common Subsequence
11. Longest Increasing Subsequence
12. Longest Palindromic Substring
13. Maximum Product Subarray
14. Edit Distance
15. Longest Valid Parentheses

