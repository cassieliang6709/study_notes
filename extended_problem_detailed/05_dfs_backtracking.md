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

