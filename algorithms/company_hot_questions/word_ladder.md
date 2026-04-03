---
title: "Word Ladder"
---

# Word Ladder

## 这个题型 / 算法点的总结

这题本质是“无权图最短路”。只要题目问最少转换步数、每一步代价相同，就应该优先想到 BFS。

## 题目含义

给 `beginWord`、`endWord` 和字典。每次只能改一个字符，且改后的单词必须在字典中，问最短转换序列长度。

关键词是“最短步数”，所以第一反应应该是 BFS。

## Python 代码

```python
from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        q = deque([(beginWord, 1)])
        visited = {beginWord}

        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    nxt = word[:i] + ch + word[i + 1:]
                    if nxt in word_set and nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, steps + 1))

        return 0
```

## 时间复杂度

经典写法约 `O(N * L * 26)`，`N` 是字典大小，`L` 是单词长度。

## 空间复杂度

`O(N * L)`

## 怎么想到这个方法

题目不是问“有没有路径”，而是问“最短转换长度”。只要是无权图最短路，标准答案就是 BFS。

## 示例 case

- 输入：`beginWord = "hit"`, `endWord = "cog"`, `wordList = ["hot","dot","dog","lot","log","cog"]`
- 输出：`5`
- 为什么：最短路径是 `hit -> hot -> dot -> dog -> cog`

## 常见 Follow-up

- 如果要输出所有最短路径，就会升级成 `Word Ladder II`
- 如何用双向 BFS 优化？
- 如何用 wildcard pattern 预处理邻接关系？

## 常见易错点

- `endWord` 不在字典里时忘记提前返回 `0`
- 访问标记时机不对，导致同一个词重复入队
- 把 DFS 写成了指数级搜索
