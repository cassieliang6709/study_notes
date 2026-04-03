# 05 DFS 与回溯完整答案

说明：

- 本文按题目分节
- 每题包含：题型识别、中文解释、English explanation、Python 标准解法
- 回溯题统一模板是：做选择 -> 递归 -> 撤销选择

---

## 1. Subsets

**题型识别**

```text
子集回溯 / Subset Backtracking
```

**中文解释**

子集题的特点是：每一层递归都代表一种当前选择结果，所以每层都可以把 `path` 加入答案。  
然后从 `start` 开始继续尝试后续元素。

**English Explanation**

In subset problems, each recursion level already represents a valid partial selection, so we can add the current `path` to the answer at every level.  
Then we continue trying later elements starting from `start`.

**Python 标准解法**

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

---

## 2. Permutations

**题型识别**

```text
排列回溯 / Permutation Backtracking
```

**中文解释**

排列和子集不同，因为顺序重要。  
所以不能只用 `start`，而要用 `used` 数组表示哪些元素已经被选过。

**English Explanation**

Permutations differ from subsets because order matters.  
So instead of using only `start`, we need a `used` array to mark which elements have already been chosen.

**Python 标准解法**

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

---

## 3. Combination Sum

**题型识别**

```text
组合回溯 / Combination Backtracking
```

**中文解释**

这题是“组合”，顺序不重要，而且同一个元素可以重复用。  
因此递归进入下一层时，仍然可以从当前下标 `i` 开始，而不是 `i + 1`。

**English Explanation**

This is a combination problem, so order does not matter, and each candidate can be reused.  
Therefore, when recursing, we can continue from the same index `i` instead of moving to `i + 1`.

**Python 标准解法**

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

---

## 4. Generate Parentheses

**题型识别**

```text
约束回溯 / Constraint Backtracking
```

**中文解释**

这题的核心约束有两个：

- 左括号数量不能超过 `n`
- 右括号数量不能超过左括号数量

只要始终保持这两个条件，生成出来的字符串就一定合法。

**English Explanation**

There are two key constraints:

- the number of left parentheses cannot exceed `n`
- the number of right parentheses cannot exceed the number of left parentheses

As long as we maintain these constraints, every generated string will be valid.

**Python 标准解法**

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

---

## 5. Letter Combinations of a Phone Number

**题型识别**

```text
逐层选择回溯 / Multi-choice DFS
```

**中文解释**

每个数字对应若干个字母。  
回溯时每一层处理一个数字，从该数字能映射的所有字母中选一个加入路径。

**English Explanation**

Each digit maps to several letters.  
At each recursion level, process one digit and choose one possible letter from its mapping.

**Python 标准解法**

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

---

## 6. Restore IP Addresses

**题型识别**

```text
分段回溯 / Segment Partition Backtracking
```

**中文解释**

把字符串分成 4 段，每段必须满足：

- 长度在 `1..3`
- 不能有前导零（除非就是 `"0"`）
- 数值不能超过 `255`

**English Explanation**

Split the string into 4 parts, where each part must satisfy:

- length between `1` and `3`
- no leading zero unless the part is exactly `"0"`
- numeric value at most `255`

**Python 标准解法**

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

---

## 7. Binary Tree Paths

**题型识别**

```text
树路径 DFS / Tree Path DFS
```

**中文解释**

从根一路走到叶子，把路径上的节点值收集起来。  
到叶子时把路径拼成字符串加入答案。

**English Explanation**

Walk from the root to every leaf and collect node values along the path.  
When reaching a leaf, join the path into a string and append it to the answer.

**Python 标准解法**

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

---

## 8. Word Break II

**题型识别**

```text
DFS + 记忆化 / DFS with Memoization
```

**中文解释**

如果只用普通回溯，会重复拆分同一个后缀很多次。  
所以要加记忆化：

- `dfs(start)` 返回从 `start` 开始能组成的所有句子

这样每个起点只会计算一次。

**English Explanation**

If we use plain backtracking, the same suffix gets recomputed many times.  
So we add memoization:

- `dfs(start)` returns all valid sentences starting from index `start`

This ensures each suffix is computed only once.

**Python 标准解法**

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

---

## 9. Partition to K Equal Sum Subsets

**题型识别**

```text
回溯装桶 / Bucket Backtracking
```

**中文解释**

把数组元素依次放入 `k` 个桶里，使每个桶的和都等于目标值。  
常见优化：

- 先排序，优先放大的数
- 如果某个空桶放不下当前数，后面其他空桶也没必要试

**English Explanation**

Try placing numbers one by one into `k` buckets so that each bucket sums to the target.  
Common optimizations:

- sort descending first, so large numbers are placed earlier
- if placing a number into one empty bucket fails, there is no need to try other empty buckets

**Python 标准解法**

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
