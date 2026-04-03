---
title: "05 DFS 与回溯完整答案"
---

# 05 DFS 与回溯完整答案

说明：

- 本文按题目分节
- 每题包含：题型识别、题目含义、Python 代码、复杂度、思路来源、常见 Follow-up
- 回溯题统一模板是：做选择 -> 递归 -> 撤销选择

---

## 1. Subsets

**题型识别**

```text
子集回溯 / Subset Backtracking
```

**题目含义**

子集题的特点是：每一层递归都代表一种当前选择结果，所以每层都可以把 `path` 加入答案。  
然后从 `start` 开始继续尝试后续元素。

**Python 代码**

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

**常见 Follow-up**

- 哪些剪枝最值得优先做？
- 如果只要求返回数量而不是全部方案，代码能如何简化？

## 2. Permutations

**题型识别**

```text
排列回溯 / Permutation Backtracking
```

**题目含义**

排列和子集不同，因为顺序重要。  
所以不能只用 `start`，而要用 `used` 数组表示哪些元素已经被选过。

**Python 代码**

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

**常见 Follow-up**

- 哪些剪枝最值得优先做？
- 如果只要求返回数量而不是全部方案，代码能如何简化？

## 3. Combination Sum

**题型识别**

```text
组合回溯 / Combination Backtracking
```

**题目含义**

这题是“组合”，顺序不重要，而且同一个元素可以重复用。  
因此递归进入下一层时，仍然可以从当前下标 `i` 开始，而不是 `i + 1`。

**Python 代码**

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

**常见 Follow-up**

- 哪些剪枝最值得优先做？
- 如果只要求返回数量而不是全部方案，代码能如何简化？

## 4. Generate Parentheses

**题型识别**

```text
约束回溯 / Constraint Backtracking
```

**题目含义**

这题的核心约束有两个：

- 左括号数量不能超过 `n`
- 右括号数量不能超过左括号数量

只要始终保持这两个条件，生成出来的字符串就一定合法。

**Python 代码**

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

**常见 Follow-up**

- 哪些剪枝最值得优先做？
- 如果只要求返回数量而不是全部方案，代码能如何简化？

## 5. Letter Combinations of a Phone Number

**题型识别**

```text
逐层选择回溯 / Multi-choice DFS
```

**题目含义**

每个数字对应若干个字母。  
回溯时每一层处理一个数字，从该数字能映射的所有字母中选一个加入路径。

**Python 代码**

```python
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mp = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        ans = []

        def backtrack(i: int, path: str) -> None:
            if i == len(digits):
                ans.append(path)
                return

            for ch in mp[digits[i]]:
                backtrack(i + 1, path + ch)

        backtrack(0, "")
        return ans
```

**时间复杂度**

通常取决于搜索树大小，常见为指数级。

**空间复杂度**

递归栈加辅助状态，通常 `O(depth)` 到指数级状态空间。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `逐层选择回溯 / Multi-choice DFS`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**常见 Follow-up**

- 如果要返回具体路径而不是只判断可行性，额外记录什么？
- DFS、BFS、并查集三种解法分别适合什么场景？

## 6. Restore IP Addresses

**题型识别**

```text
分段回溯 / Segment Partition Backtracking
```

**题目含义**

把字符串分成 4 段，每段必须满足：

- 长度在 `1..3`
- 不能有前导零（除非就是 `"0"`）
- 数值不能超过 `255`

**Python 代码**

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

**常见 Follow-up**

- 哪些剪枝最值得优先做？
- 如果只要求返回数量而不是全部方案，代码能如何简化？

## 7. Binary Tree Paths

**题型识别**

```text
树路径 DFS / Tree Path DFS
```

**题目含义**

从根一路走到叶子，把路径上的节点值收集起来。  
到叶子时把路径拼成字符串加入答案。

**Python 代码**

```python
from typing import List, Optional

class Solution:
    def binaryTreePaths(self, root: Optional['TreeNode']) -> List[str]:
        ans = []

        def dfs(node, path):
            if not node:
                return

            path.append(str(node.val))

            if not node.left and not node.right:
                ans.append("->".join(path))

            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()

        dfs(root, [])
        return ans
```

**时间复杂度**

通常取决于搜索树大小，常见为指数级。

**空间复杂度**

递归栈加辅助状态，通常 `O(depth)` 到指数级状态空间。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `树路径 DFS / Tree Path DFS`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**常见 Follow-up**

- 如果要返回具体路径而不是只判断可行性，额外记录什么？
- DFS、BFS、并查集三种解法分别适合什么场景？

## 8. Word Break II

**题型识别**

```text
DFS + 记忆化 / DFS with Memoization
```

**题目含义**

如果只用普通回溯，会重复拆分同一个后缀很多次。  
所以要加记忆化：

- `dfs(start)` 返回从 `start` 开始能组成的所有句子

这样每个起点只会计算一次。

**Python 代码**

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

**常见 Follow-up**

- 如果要返回具体路径而不是只判断可行性，额外记录什么？
- DFS、BFS、并查集三种解法分别适合什么场景？

## 9. Partition to K Equal Sum Subsets

**题型识别**

```text
回溯装桶 / Bucket Backtracking
```

**题目含义**

把数组元素依次放入 `k` 个桶里，使每个桶的和都等于目标值。  
常见优化：

- 先排序，优先放大的数
- 如果某个空桶放不下当前数，后面其他空桶也没必要试

**Python 代码**

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

**常见 Follow-up**

- 哪些剪枝最值得优先做？
- 如果只要求返回数量而不是全部方案，代码能如何简化？

