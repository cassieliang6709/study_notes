---
title: "05 DFS 与回溯详细教学"
---

# 05 DFS 与回溯详细教学

回溯题不是一题一个解法，而是统一模板换参数。

---

## 一、统一模板

```python
path = []

def backtrack(state):
    if 到达终点:
        ans.append(path[:])
        return

    for choice in 可选项:
        if 不合法:
            continue
        path.append(choice)
        backtrack(next_state)
        path.pop()
```

---

## 二、代表题

### Subsets

```text
// start 控制起点
// 每层都可以收集答案
```

### Permutations

```text
// order matters
// 需要 used[]
```

### Combination Sum

```text
// 可重复使用元素
// 下一层可以继续从当前位置开始
```

### Generate Parentheses

```text
// left <= n
// right <= left
```

### Restore IP Addresses

```text
// 每段长度 1~3
// 不能有前导 0
// 值 <= 255
```

### Word Break II

```text
// DFS + memo
// 否则重复搜索严重
```

### Partition to K Equal Sum Subsets

```text
// 回溯 + 排序 + 剪枝
```

---

## 建议顺序

1. Letter Combinations of a Phone Number
2. Subsets
3. Permutations
4. Combination Sum
5. Generate Parentheses
6. Restore IP Addresses
7. Binary Tree Paths
8. Word Break II
9. Partition to K Equal Sum Subsets


---

## Quiz

**Q1: 回溯模板中 `path.pop()` 的作用是什么？**

- [ ] 删除重复元素
- [ ] 撤销上一步选择，回到上层状态 ✅
- [ ] 清空整个路径
- [ ] 标记当前节点已访问

**Q2: `Subsets` 和 `Permutations` 的主要区别是什么？**

- [ ] Subsets 有剪枝，Permutations 没有
- [ ] Subsets 通过 start 参数避免重复选取前面的元素；Permutations 每次从全集中选未用过的 ✅
- [ ] 两者完全相同
- [ ] Permutations 用 BFS，Subsets 用 DFS

**Q3: `Combination Sum`（元素可重复使用）和普通组合题的区别在递归调用上体现在哪里？**

- [ ] 加入结果集的条件不同
- [ ] 递归时 start 不 +1，允许再次选同一个元素 ✅
- [ ] 用 visited 数组标记
- [ ] 不需要回溯

**Q4: `Generate Parentheses` 的剪枝条件是什么？**

- [ ] 左括号数等于右括号数就停止
- [ ] 右括号数不能超过左括号数；左括号数不能超过 n ✅
- [ ] 只要总长度达到 2n 就是合法答案
- [ ] 不需要剪枝

**Q5: 回溯的时间复杂度通常是什么量级？**

- [ ] O(n)
- [ ] O(n log n)
- [ ] 指数级或阶乘级，取决于题目 ✅
- [ ] O(n²)
