---
title: "08 动态规划"
---

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

**这个题型 / 算法点的总结**

`Climbing Stairs` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

到第 `i` 阶的方法数 = 到 `i-1` 阶的方法数 + 到 `i-2` 阶的方法数。  
这是最基础的 Fibonacci 型 DP。

**Python 代码**

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

每一步只能由前两步转移而来，所以本质就是 Fibonacci。只要能写出状态转移，这题就很顺。

**示例 case**

- 输入：`n = 4`
- 输出：`5`。到第 4 阶的方法数等于到第 3 阶和第 2 阶的方法数之和。

**常见 Follow-up**

- 如果一次能爬 1/2/3 阶，转移怎么改？
- 为什么可以把 DP 数组压缩成两个变量？

### 2. House Robber

**这个题型 / 算法点的总结**

`House Robber` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

每个房子都有钱，但相邻房子不能同时偷。题目本质是在每个位置做“偷 / 不偷”的最优选择，是一维 DP 模板题。

**Python 代码**

```python
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev1 = 0

        for x in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + x)

        return prev1
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(1)`。

**怎么想到这个方法**

每个位置只有“抢 / 不抢”两种选择，而且会影响下一个位置，所以非常适合一维 DP。

**示例 case**

- 输入：`nums = [1,2,3,1]`
- 输出：`4`。最优是偷第 1 和第 3 间房。

**常见 Follow-up**

- 如果房子围成一圈怎么办？
- 如果是二叉树版为什么会变成树 DP？

### 3. Unique Paths

**这个题型 / 算法点的总结**

`Unique Paths` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

到某个格子的路径数 = 上边来的路径数 + 左边来的路径数。  
因为只能向右或向下走。

**Python 代码**

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]

        return dp[-1]
```

**时间复杂度**

`O(mn)`。

**空间复杂度**

`O(mn)`；可压缩到 `O(n)`。

**怎么想到这个方法**

只能向右或向下，所以到达当前格子的路径数只来自上方和左方，这是最标准的网格 DP 信号。

**示例 case**

- 输入：`m = 3`, `n = 7`
- 输出：`28`。每格只依赖上方和左方。

**常见 Follow-up**

- 如果有障碍物怎么办？
- 组合数学解法为什么也成立？

### 4. Minimum Path Sum

**这个题型 / 算法点的总结**

`Minimum Path Sum` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

从左上角走到右下角，每次只能向右或向下，求路径和最小值。因为当前格子的最优值只依赖上方和左方，所以是标准网格 DP。

**Python 代码**

```python
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[-1][-1]
```

**时间复杂度**

`O(mn)`。

**空间复杂度**

`O(mn)`；可压缩到 `O(n)`。

**怎么想到这个方法**

和 `Unique Paths` 相比，这题只是把“路径条数”换成了“最小路径和”。网格 DP 模板完全一致。

**示例 case**

- 输入：`grid = [[1,3,1],[1,5,1],[4,2,1]]`
- 输出：`7`。最优路径是 `1→3→1→1→1`。

**常见 Follow-up**

- 如何原地修改 `grid` 省空间？
- 如果允许对角线移动，状态要怎么改？

### 5. Coin Change

**这个题型 / 算法点的总结**

`Coin Change` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

给硬币面额和目标金额，求凑出目标金额的最少硬币数。因为目标金额可以由更小金额推出来，所以是完全背包 / 一维 DP。

**Python 代码**

```python
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if coin <= a:
                    dp[a] = min(dp[a], dp[a - coin] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1
```

**时间复杂度**

`O(amount * len(coins))`。

**空间复杂度**

`O(amount)`。

**怎么想到这个方法**

问最少硬币数时，先想“凑出金额 `a` 的答案能不能由更小金额推出来”。这就是完全背包 / 一维 DP。

**示例 case**

- 输入：`coins = [1,2,5]`, `amount = 11`
- 输出：`3`。最优组合是 `5 + 5 + 1`。

**常见 Follow-up**

- 如果问方案数而不是最少个数，转移怎么改？
- 如果每种硬币只能用一次，会变成什么模型？

### 6. Word Break

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

**Python 代码**

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

`O(n^2)`，若切片和集合查找都算上通常这样写。

**空间复杂度**

`O(n)`。

**怎么想到这个方法**

题目问字符串能不能被字典切开，最自然的状态是：前 `i` 个字符能不能被拆分。

**示例 case**

- 输入：`s = "leetcode"`, `wordDict = ["leet","code"]`
- 输出：`True`。可以切成 `leet + code`。

**常见 Follow-up**

- 如果要输出所有方案，就变成哪道题？
- `Trie + DFS + memo` 为什么有时更快？

### 7. Partition Equal Subset Sum

**这个题型 / 算法点的总结**

`Partition Equal Subset Sum` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

这题是把数组分成两个和相等的子集，等价于看能不能选出一部分数，和恰好是总和的一半，所以直接转成 0-1 背包。

**Python 代码**

```python
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[target]
```

**时间复杂度**

`O(n * target)`。

**空间复杂度**

`O(target)`。

**怎么想到这个方法**

一看到“能不能选一些数凑出某个和”，就要往 0-1 背包上靠。这里目标值正好是总和的一半。

**示例 case**

- 输入：`nums = [1,5,11,5]`
- 输出：`True`。可以分成和都为 `11` 的两个子集。

**常见 Follow-up**

- 为什么内层循环要倒序？
- 如果要输出具体子集，如何回溯路径？

### 8. Longest Common Subsequence

**这个题型 / 算法点的总结**

`Longest Common Subsequence` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

题目要你求两个字符串的最长公共子序列长度。典型状态是 `dp[i][j]` 表示前 `i` 个字符和前 `j` 个字符的答案。

**Python 代码**

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]
```

**时间复杂度**

`O(mn)`。

**空间复杂度**

`O(mn)`；可压缩到 `O(n)`。

**怎么想到这个方法**

两个字符串问题优先想二维 DP。LCS 的关键是明确字符相等和不等时分别继承哪个子问题。

**示例 case**

- 输入：`text1 = "abcde"`, `text2 = "ace"`
- 输出：`3`。最长公共子序列是 `ace`。

**常见 Follow-up**

- 如果要恢复出子序列本身，需要怎么做？
- 和最长公共子串有什么区别？

### 9. Longest Increasing Subsequence

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

**Python 代码**

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

`O(n log n)`。

**空间复杂度**

`O(n)`。

**怎么想到这个方法**

这题有 `O(n^2)` DP，但面试里经常追问更优解。想到“维护每个长度的最小结尾”后，就能配合二分优化。

**示例 case**

- 输入：`nums = [10,9,2,5,3,7,101,18]`
- 输出：`4`。一个最长递增子序列是 `2,3,7,101`。

**常见 Follow-up**

- 你也能讲 `O(n^2)` 版本吗？
- 如果要恢复具体序列，需额外存什么？

### 10. Longest Palindromic Substring

**这个题型 / 算法点的总结**

`Longest Palindromic Substring` 属于滑动窗口类问题，关键是想清楚窗口什么时候合法、什么时候需要收缩。

**题目含义**

虽然也能用区间 DP，但最适合面试手写的是中心扩展。  
每个回文串都有一个中心：

- 奇数长度：单个字符
- 偶数长度：两个字符之间

从中心向两边扩展即可。

**Python 代码**

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(len(s)):
            s1 = expand(i, i)
            s2 = expand(i, i + 1)
            ans = max(ans, s1, s2, key=len)

        return ans
```

**时间复杂度**

`O(n^2)`。

**空间复杂度**

`O(1)` 中心扩展版。

**怎么想到这个方法**

子串回文题最先想到的通常是“以某个中心向两边扩”。这样既好写，也容易现场讲清楚。

**示例 case**

- 输入：`s = "babad"`
- 输出：`"bab"` 或 `"aba"`。中心扩展能自然找到答案。

**常见 Follow-up**

- DP 版怎么定义状态？
- 为什么奇数长度和偶数长度都要枚举？

### 11. Maximum Product Subarray

**这个题型 / 算法点的总结**

`Maximum Product Subarray` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

这题不能只维护最大值，因为负数可能把最小积变成最大积。  
所以要同时维护：

- `cur_max`
- `cur_min`

**Python 代码**

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

乘积题和加法题不同，负数会让最大最小互换，所以你要同时维护当前位置结尾的最大值和最小值。

**示例 case**

- 输入：`nums = [2,3,-2,4]`
- 输出：`6`。最大乘积来自连续子数组 `[2,3]`。

**常见 Follow-up**

- 为什么只维护最大值不够？
- 如果数组里有 0，会发生什么？

### 12. Edit Distance

**这个题型 / 算法点的总结**

`Edit Distance` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

题目要求把 `word1` 变成 `word2` 的最少操作数。每一步只有插入、删除、替换三种操作，所以状态转移非常标准。

**Python 代码**

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1],
                    )

        return dp[m][n]
```

**时间复杂度**

`O(mn)`。

**空间复杂度**

`O(mn)`；可压缩到 `O(n)`。

**怎么想到这个方法**

操作只有插入、删除、替换三种，所以二维 DP 非常自然。想清楚 `dp[i][j]` 的含义就能稳住。

**示例 case**

- 输入：`word1 = "horse"`, `word2 = "ros"`
- 输出：`3`。三步操作可完成转换。

**常见 Follow-up**

- 如果替换代价不是 1，状态怎么改？
- 如何压缩空间？

