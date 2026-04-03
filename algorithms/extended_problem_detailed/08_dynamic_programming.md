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

**这个题型 / 算法点的总结**

`Climbing Stairs / Fibonacci` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

这两个问题本质一样：当前位置的答案只依赖前面很少几个状态，是最适合入门 DP 的模板。

**代表 Python 代码**

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(1)`。

**怎么想到这个方法**

当题目满足“当前答案只依赖固定几个更小子问题”时，就该想到线性 DP 和状态压缩。

**示例 case**

- 输入：一个最小可手算的样例
- 输出：先手推一遍算法流程，再对照代码中的循环、状态或数据结构变化。

**常见 Follow-up**

- 如果一次可以走 1/2/3 步，状态转移如何改？
- 为什么这类题常常可以压到 `O(1)` 空间？

### Best Time to Buy and Sell Stock

**这个题型 / 算法点的总结**

`Best Time to Buy and Sell Stock` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

虽然这题常用贪心写，但也可以理解成 DP。  
核心状态是“到当前位置为止的最低买入价”，然后不断更新最大利润。

**代表 Python 代码**

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        ans = 0

        for p in prices:
            min_price = min(min_price, p)
            ans = max(ans, p - min_price)

        return ans
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(1)`。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `状态维护 / Running DP State`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：`prices = [7, 1, 5, 3, 6, 4]`
- 输出：`5`。最优是在价格 `1` 买入、价格 `6` 卖出。

**常见 Follow-up**

- 能不能把空间复杂度再压缩一层？
- 有没有另一种常见模板也能解决这题？

### Maximum Subarray

**这个题型 / 算法点的总结**

`Maximum Subarray` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

定义：

```text
cur = 以当前元素结尾的最大子数组和
```

那么每一步：

- 要么从当前元素重新开始
- 要么接在前一个最优结尾后面

**代表 Python 代码**

```python
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = ans = nums[0]

        for x in nums[1:]:
            cur = max(x, cur + x)
            ans = max(ans, cur)

        return ans
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(1)`。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `Kadane / Ending-at-i DP`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：`nums = [-2,1,-3,4,-1,2,1,-5,4]`
- 输出：`6`。最大连续子数组是 `[4,-1,2,1]`。

**常见 Follow-up**

- 能不能把空间复杂度再压缩一层？
- 有没有另一种常见模板也能解决这题？

### Unique Paths / Unique Paths II

**这个题型 / 算法点的总结**

`Unique Paths / Unique Paths II` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

这两题都在问从左上走到右下，只是第二题多了障碍物。共同核心是：当前格子的答案来自上方和左方。

**代表 Python 代码**

```python
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]

        return dp[-1]
```

**时间复杂度**

`O(mn)`。

**空间复杂度**

`O(n)`。

**怎么想到这个方法**

题目一旦限制只能向右或向下移动，网格 DP 基本就是默认答案。

**示例 case**

- 输入：一个最小可手算的样例
- 输出：先手推一遍算法流程，再对照代码中的循环、状态或数据结构变化。

**常见 Follow-up**

- 没有障碍物时为什么还能用组合数学？
- 如果要求最小路径和，状态如何变化？

### Decode Ways

**这个题型 / 算法点的总结**

`Decode Ways` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

每个位置都可以考虑：

- 单独解码一位
- 或和前一位组合成两位数解码

所以 `dp[i]` 由：

- `dp[i-1]`
- `dp[i-2]`

转移而来。

**代表 Python 代码**

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = dp[1] = 1

        for i in range(2, len(s) + 1):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            if "10" <= s[i - 2:i] <= "26":
                dp[i] += dp[i - 2]

        return dp[-1]
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(1)` 或 `O(n)`。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `字符串一维 DP / String 1D DP`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：一个最小可手算的样例
- 输出：先手推一遍算法流程，再对照代码中的循环、状态或数据结构变化。

**常见 Follow-up**

- 能不能把空间复杂度再压缩一层？
- 有没有另一种常见模板也能解决这题？

### Word Break

**这个题型 / 算法点的总结**

`Word Break` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

定义：

```text
dp[i] = s[:i] 能否被拆分
```

如果存在某个 `j < i`，满足：

- `dp[j] == True`
- `s[j:i]` 在词典中

那么 `dp[i] = True`。

**代表 Python 代码**

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

**时间复杂度**

`O(n^2)`。

**空间复杂度**

`O(n)`。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `前缀可达 DP / Prefix Feasibility DP`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：`s = "leetcode"`, `wordDict = ["leet","code"]`
- 输出：`True`。可以切成 `leet + code`。

**常见 Follow-up**

- 能不能把空间复杂度再压缩一层？
- 有没有另一种常见模板也能解决这题？

### Longest Increasing Subsequence

**这个题型 / 算法点的总结**

`Longest Increasing Subsequence` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

定义：

```text
dp[i] = 以 nums[i] 结尾的最长递增子序列长度
```

然后枚举前面的 `j < i`，如果 `nums[j] < nums[i]`，就可以转移：

```text
dp[i] = max(dp[i], dp[j] + 1)
```

**代表 Python 代码**

```python
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp, default=0)
```

**时间复杂度**

二分优化版 `O(n log n)`。

**空间复杂度**

`O(n)`。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `一维 DP / 1D DP`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：`nums = [10,9,2,5,3,7,101,18]`
- 输出：`4`。一个最长递增子序列是 `2,3,7,101`。

**常见 Follow-up**

- 能不能把空间复杂度再压缩一层？
- 有没有另一种常见模板也能解决这题？

### Maximum Product Subarray

**这个题型 / 算法点的总结**

`Maximum Product Subarray` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

这题不能只维护最大值，因为负数可能把最小积变成最大积。  
所以要同时维护：

- `cur_max`
- `cur_min`

**代表 Python 代码**

```python
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = ans = nums[0]

        for x in nums[1:]:
            vals = (x, cur_max * x, cur_min * x)
            cur_max = max(vals)
            cur_min = min(vals)
            ans = max(ans, cur_max)

        return ans
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(1)`。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `状态双维护 / Track Max and Min`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：`nums = [2,3,-2,4]`
- 输出：`6`。最大乘积来自连续子数组 `[2,3]`。

**常见 Follow-up**

- 能不能把空间复杂度再压缩一层？
- 有没有另一种常见模板也能解决这题？

### Regular Expression Matching / Wildcard Matching

**这个题型 / 算法点的总结**

`Regular Expression Matching / Wildcard Matching` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

这两题都属于双串匹配 DP。难点不在代码量，而在于你能不能清楚写出 `dp[i][j]` 的含义，并按字符类别列转移。

**代表 Python 代码**

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(2, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] in {s[i - 1], "."}:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] in {s[i - 1], "."}:
                        dp[i][j] |= dp[i - 1][j]

        return dp[m][n]
```

**时间复杂度**

`O(mn)`。

**空间复杂度**

`O(mn)`。

**怎么想到这个方法**

只要是两个字符串的匹配关系，就先考虑二维 DP；然后把每种特殊字符看成不同的转移分支。

**示例 case**

- 输入：一个最小可手算的样例
- 输出：先手推一遍算法流程，再对照代码中的循环、状态或数据结构变化。

**常见 Follow-up**

- `regex` 里的 `*` 和 `wildcard` 里的 `*` 语义有什么区别？
- 这种二维 DP 能不能压缩空间？

### Longest Increasing Path in a Matrix

**这个题型 / 算法点的总结**

`Longest Increasing Path in a Matrix` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

每个格子都可以看成一个状态。  
从这个格子出发，最长递增路径长度只和更大的相邻格子有关。  
所以用 DFS 搜索，并用记忆化缓存每个格子的答案。

**代表 Python 代码**

```python
from functools import lru_cache
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        @lru_cache(None)
        def dfs(r, c):
            ans = 1
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    ans = max(ans, 1 + dfs(nr, nc))
            return ans

        return max(dfs(r, c) for r in range(m) for c in range(n))
```

**时间复杂度**

`O(mn)`。

**空间复杂度**

`O(mn)`。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `DFS + 记忆化 / DFS + Memoization`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：一个小矩阵或网格
- 输出：按题意返回路径、搜索结果或区间统计。建议先手推 2x2 或 3x3 的最小样例。

**常见 Follow-up**

- 如果要返回具体路径而不是只判断可行性，额外记录什么？
- DFS、BFS、并查集三种解法分别适合什么场景？

