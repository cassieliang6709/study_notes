---
title: "06 回溯与图搜索"
---

# 06 回溯与图搜索

---

## 第一部分：回溯

### 识别信号

```text
// 所有组合
// 所有排列
// 所有合法方案
// 试一个选择，不行再撤回
```

### 统一模板

```text
path = []

def backtrack(state):
    if 到达终点:
        收集答案
        return

    for choice in 所有可能选择:
        if 不合法:
            continue

        做选择
        backtrack(next_state)
        撤销选择
```

### 重点题

- `Subsets`
  ```text
  // 子集：每个元素选或不选
  ```

- `Permutations`
  ```text
  // 排列：顺序重要，通常用 used[]
  ```

- `Combination Sum`
  ```text
  // 组合：顺序不重要，通常用 start 控制起点
  ```

- `Generate Parentheses`
  ```text
  // 左括号数 <= n
  // 右括号数 <= 左括号数
  ```

- `Palindrome Partitioning`
  ```text
  // 切一段，只有这段是回文才继续
  ```

- `Word Search`
  ```text
  // DFS + 回溯 + visited
  ```

- `N-Queens`
  ```text
  // 列、主对角线、副对角线约束
  ```

---

## 第二部分：图搜索

### 识别信号

```text
// 岛屿、连通块
// 扩散过程
// 依赖关系
// 最短步数
```

### DFS 模板

```text
def dfs(r, c):
    if 越界 或 无效:
        return
    标记访问
    向四个方向继续
```

### BFS 模板

```text
queue = 初始节点

while queue:
    for _ in range(len(queue)):
        处理当前层节点
        把下一层加入队列
```

### 重点题

- `Number of Islands`
  ```text
  // 发现一块陆地，就把整块岛染掉
  ```

- `Rotting Oranges`
  ```text
  // 多源 BFS
  // 所有腐烂橘子同时出发
  ```

- `Course Schedule`
  ```text
  // 拓扑排序
  // 入度为 0 的点先处理
  ```

---

## 三、推荐刷题顺序

1. Letter Combinations of a Phone Number
2. Subsets
3. Permutations
4. Combination Sum
5. Generate Parentheses
6. Palindrome Partitioning
7. Number of Islands
8. Rotting Oranges
9. Word Search
10. Course Schedule
11. N-Queens

