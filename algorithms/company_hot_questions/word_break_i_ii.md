---
title: "Word Break I II"
---

# Word Break I / II

## 题目含义

这一组题经常一起出现：

- `Word Break I`：判断字符串能不能被字典拆开
- `Word Break II`：返回所有合法拆分方案

第一题偏 DP，第二题偏 DFS + memo。

## Word Break I

### Python 代码

```python
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[-1]
```

### 时间复杂度

通常写 `O(n^2)`。

### 空间复杂度

`O(n)`。

### 怎么想到这个方法

题目问“前缀能不能被拆开”，最自然的状态就是：

- `dp[i]` 表示前 `i` 个字符是否可拆分

## Word Break II

### Python 代码

```python
from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)

        @lru_cache(None)
        def dfs(start: int) -> List[str]:
            if start == len(s):
                return [""]

            ans = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word not in word_set:
                    continue
                for tail in dfs(end):
                    ans.append(word if not tail else word + " " + tail)
            return ans

        return dfs(0)
```

### 时间复杂度

最坏指数级，但 `memo` 会显著减少重复搜索。

### 空间复杂度

`O(n + 输出规模)`。

### 怎么想到这个方法

第二题不是只判断真假，而是要输出所有方案，所以纯 DP 不够顺手。最自然的做法是：

- DFS 枚举切分点
- `memo` 记住某个起点后面的所有答案

## 常见 Follow-up

- 如何先用 `Word Break I` 作为剪枝？
- 如果 interviewer 问更快，能不能讲 `Trie + memo`？
- 为什么 `Word Break II` 不做 memo 会很慢？
