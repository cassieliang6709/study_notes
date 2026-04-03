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

**这个题型 / 算法点的总结**

`Subsets` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

子集题的特点是：每一层递归都代表一种当前选择结果，所以每层都可以把 `path` 加入答案。  
然后从 `start` 开始继续尝试后续元素。

**代表 Python 代码**

```python
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []

        def backtrack(start: int) -> None:
            ans.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return ans
```

**时间复杂度**

`O(n * 2^n)`。

**空间复杂度**

`O(n)`，不计答案。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `子集回溯 / Subset Backtracking`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：一个最小可手算的样例
- 输出：先手推一遍算法流程，再对照代码中的循环、状态或数据结构变化。

**常见 Follow-up**

- 哪些剪枝最值得优先做？
- 如果只要求返回数量而不是全部方案，代码能如何简化？

### Permutations

**这个题型 / 算法点的总结**

`Permutations` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

排列和子集不同，因为顺序重要。  
所以不能只用 `start`，而要用 `used` 数组表示哪些元素已经被选过。

**代表 Python 代码**

```python
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        used = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack()
                path.pop()
                used[i] = False

        backtrack()
        return ans
```

**时间复杂度**

`O(n * n!)`。

**空间复杂度**

`O(n)`，不计答案。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `排列回溯 / Permutation Backtracking`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：一个最小可手算的样例
- 输出：先手推一遍算法流程，再对照代码中的循环、状态或数据结构变化。

**常见 Follow-up**

- 哪些剪枝最值得优先做？
- 如果只要求返回数量而不是全部方案，代码能如何简化？

### Combination Sum

**这个题型 / 算法点的总结**

`Combination Sum` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

这题是“组合”，顺序不重要，而且同一个元素可以重复用。  
因此递归进入下一层时，仍然可以从当前下标 `i` 开始，而不是 `i + 1`。

**代表 Python 代码**

```python
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []

        def backtrack(start: int, remain: int) -> None:
            if remain == 0:
                ans.append(path[:])
                return
            if remain < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, remain - candidates[i])
                path.pop()

        backtrack(0, target)
        return ans
```

**时间复杂度**

最坏指数级。

**空间复杂度**

`O(target)` 量级递归深度，不计答案。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `组合回溯 / Combination Backtracking`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：一个最小可手算的样例
- 输出：先手推一遍算法流程，再对照代码中的循环、状态或数据结构变化。

**常见 Follow-up**

- 哪些剪枝最值得优先做？
- 如果只要求返回数量而不是全部方案，代码能如何简化？

### Generate Parentheses

**这个题型 / 算法点的总结**

`Generate Parentheses` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

这题的核心约束有两个：

- 左括号数量不能超过 `n`
- 右括号数量不能超过左括号数量

只要始终保持这两个条件，生成出来的字符串就一定合法。

**代表 Python 代码**

```python
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(cur: str, left: int, right: int) -> None:
            if len(cur) == 2 * n:
                ans.append(cur)
                return

            if left < n:
                backtrack(cur + "(", left + 1, right)
            if right < left:
                backtrack(cur + ")", left, right + 1)

        backtrack("", 0, 0)
        return ans
```

**时间复杂度**

Catalan 数量级。

**空间复杂度**

`O(n)`，不计答案。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `约束回溯 / Constraint Backtracking`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：一个最小可手算的样例
- 输出：先手推一遍算法流程，再对照代码中的循环、状态或数据结构变化。

**常见 Follow-up**

- 哪些剪枝最值得优先做？
- 如果只要求返回数量而不是全部方案，代码能如何简化？

### Restore IP Addresses

**这个题型 / 算法点的总结**

`Restore IP Addresses` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

把字符串分成 4 段，每段必须满足：

- 长度在 `1..3`
- 不能有前导零（除非就是 `"0"`）
- 数值不能超过 `255`

**代表 Python 代码**

```python
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        path = []

        def backtrack(start: int) -> None:
            if len(path) == 4:
                if start == len(s):
                    ans.append(".".join(path))
                return

            for end in range(start, min(start + 3, len(s))):
                part = s[start:end + 1]
                if (part.startswith("0") and len(part) > 1) or int(part) > 255:
                    continue
                path.append(part)
                backtrack(end + 1)
                path.pop()

        backtrack(0)
        return ans
```

**时间复杂度**

常数上界内枚举，通常写 `O(1)`。

**空间复杂度**

`O(1)`，不计答案。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `分段回溯 / Segment Partition Backtracking`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：一个最小可手算的样例
- 输出：先手推一遍算法流程，再对照代码中的循环、状态或数据结构变化。

**常见 Follow-up**

- 哪些剪枝最值得优先做？
- 如果只要求返回数量而不是全部方案，代码能如何简化？

### Word Break II

**这个题型 / 算法点的总结**

`Word Break II` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

如果只用普通回溯，会重复拆分同一个后缀很多次。  
所以要加记忆化：

- `dfs(start)` 返回从 `start` 开始能组成的所有句子

这样每个起点只会计算一次。

**代表 Python 代码**

```python
from functools import lru_cache
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)

        @lru_cache(None)
        def dfs(start: int):
            if start == len(s):
                return [""]

            ans = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    for suffix in dfs(end):
                        ans.append(word if suffix == "" else word + " " + suffix)
            return ans

        return dfs(0)
```

**时间复杂度**

最坏指数级，`memo` 可显著剪枝。

**空间复杂度**

`O(n + 输出规模)`。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `DFS + 记忆化 / DFS with Memoization`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：一个最小可手算的样例
- 输出：先手推一遍算法流程，再对照代码中的循环、状态或数据结构变化。

**常见 Follow-up**

- 如果要返回具体路径而不是只判断可行性，额外记录什么？
- DFS、BFS、并查集三种解法分别适合什么场景？

### Partition to K Equal Sum Subsets

**这个题型 / 算法点的总结**

`Partition to K Equal Sum Subsets` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

把数组元素依次放入 `k` 个桶里，使每个桶的和都等于目标值。  
常见优化：

- 先排序，优先放大的数
- 如果某个空桶放不下当前数，后面其他空桶也没必要试

**代表 Python 代码**

```python
from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        nums.sort(reverse=True)
        buckets = [0] * k

        def backtrack(i: int) -> bool:
            if i == len(nums):
                return True

            for j in range(k):
                if buckets[j] + nums[i] <= target:
                    buckets[j] += nums[i]
                    if backtrack(i + 1):
                        return True
                    buckets[j] -= nums[i]

                if buckets[j] == 0:
                    break

            return False

        return backtrack(0)
```

**时间复杂度**

最坏指数级。

**空间复杂度**

`O(n)` 到 `O(2^n)`，取决于状态表示。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `回溯装桶 / Bucket Backtracking`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：一个最小可手算的样例
- 输出：先手推一遍算法流程，再对照代码中的循环、状态或数据结构变化。

**常见 Follow-up**

- 哪些剪枝最值得优先做？
- 如果只要求返回数量而不是全部方案，代码能如何简化？

