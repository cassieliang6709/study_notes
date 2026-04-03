---
title: "Word Search"
---

# Word Search

## 题目含义

在二维网格里找一个单词。字符可以上下左右移动，同一个格子不能重复使用。

这题本质是“网格 DFS + 回溯 + 访问标记恢复”。

## Python 代码

```python
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            if board[r][c] != word[i]:
                return False

            ch = board[r][c]
            board[r][c] = "#"
            found = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            board[r][c] = ch
            return found

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True
        return False
```

## 时间复杂度

最坏 `O(mn * 4^L)`，`L` 是单词长度。

## 空间复杂度

`O(L)` 递归栈。

## 怎么想到这个方法

只要题目同时满足：

- 网格搜索
- 路径约束
- 同一格不能重复使用

那几乎就是回溯模板题。

## 常见 Follow-up

- 如果要同时找很多单词，怎么升级成 `Trie + DFS`？
- 如果允许走斜方向，代码怎么改？
- 如何提前用字符频率剪枝？

## 常见易错点

- 标记访问后忘记恢复
- 边界判断顺序写错
- 把全局 `visited` 写成不能回退的结构
