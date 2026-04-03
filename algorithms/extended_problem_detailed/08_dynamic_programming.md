---
title: "08 动态规划详细教学"
---

# 08 动态规划详细教学

DP 的难点永远不在代码，而在“状态定义”。

---

## 一、统一四步法

```text
// 1. dp state 是什么
// 2. transition 是什么
// 3. base case 是什么
// 4. iteration order 是什么
```

---

## 二、代表题

### Climbing Stairs / Fibonacci

```text
// 最基础一维 DP
```

### Best Time to Buy and Sell Stock

```text
// 也可看成状态压缩 DP
```

### Maximum Subarray

```text
// 以 i 结尾的最大和
```

### Unique Paths / Unique Paths II

```text
// 网格 DP
```

### Decode Ways

```text
// 看 1 位和 2 位能否组成合法编码
```

### Word Break

```text
// dp[i] 表示前 i 个字符能否拆分
```

### Longest Increasing Subsequence

```text
// 先学 O(n^2)
// 再学二分优化
```

### Maximum Product Subarray

```text
// 同时维护 max 和 min
```

### Regular Expression Matching / Wildcard Matching

```text
// 二维匹配 DP
```

### Longest Increasing Path in a Matrix

```text
// DFS + memo
// 也可视作 DP
```

---

## 建议顺序

1. Fibonacci Number
2. Climbing Stairs
3. Maximum Subarray
4. Best Time to Buy and Sell Stock
5. Unique Paths
6. Unique Paths II
7. Decode Ways
8. Word Break
9. Longest Increasing Subsequence
10. Maximum Product Subarray
11. Longest Palindromic Substring
12. Longest Palindromic Subsequence
13. Continuous Subarray Sum
14. Longest Increasing Path in a Matrix
15. Regular Expression Matching
16. Wildcard Matching


---

## Quiz

**Q1: DP 的四步法第一步是什么？**

- [ ] 写出递推公式
- [ ] 定义 dp[i] 的含义（subproblem representation） ✅
- [ ] 初始化 base case
- [ ] 确定遍历顺序

**Q2: `Longest Increasing Subsequence` 的 dp[i] 代表什么？**

- [ ] 前 i 个元素的最长子序列长度
- [ ] 以 nums[i] 结尾的最长递增子序列长度 ✅
- [ ] 从 i 开始的最长递增子序列长度
- [ ] 整个数组的 LIS 长度

**Q3: 背包 DP 中，为什么遍历顺序很关键？**

- [ ] 顺序不影响结果
- [ ] 0/1 背包用逆序遍历容量防止重复选取；完全背包用正序允许重复 ✅
- [ ] 背包问题必须从大到小遍历物品
- [ ] 只要初始化正确，顺序无所谓

**Q4: `Word Break` 的 dp[i] 代表什么？**

- [ ] 前 i 个字符能否被分割成字典中的单词 ✅
- [ ] 到位置 i 使用了几个单词
- [ ] 以位置 i 结尾的最长单词
- [ ] 字典中第 i 个单词是否被用到

**Q5: 区间 DP（如矩阵链乘、戳气球）的枚举顺序是什么？**

- [ ] 从左到右枚举左端点
- [ ] 按区间长度从小到大枚举，保证子区间先被计算 ✅
- [ ] 从中心向两边扩展
- [ ] 随机枚举
