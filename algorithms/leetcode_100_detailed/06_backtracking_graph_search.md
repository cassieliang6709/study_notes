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

#### 1. Subsets

**题目含义**

给定一个数组，返回它的所有子集。子集题的本质是每个元素都面临“选 / 不选”两个决策。

**Python 代码**

```python
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i: int) -> None:
            if i == len(nums):
                ans.append(path[:])
                return

            dfs(i + 1)

            path.append(nums[i])
            dfs(i + 1)
            path.pop()

        dfs(0)
        return ans
```

**时间复杂度**

`O(n * 2^n)`。

**空间复杂度**

`O(n)` 递归栈，不计答案。

**怎么想到这个方法**

只要题目要求“所有子集”，就先把每个元素想成一个二叉决策：拿还是不拿。

**常见 Follow-up**

- 如果数组有重复元素，怎么去重？
- 如果只要大小为 `k` 的子集，怎么剪枝？

#### 2. Permutations

**题目含义**

给定一个不重复数组，返回所有排列。和子集不同，排列强调顺序，所以不能只靠位置向后推进。

**Python 代码**

```python
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        used = [False] * len(nums)

        def dfs() -> None:
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for i, x in enumerate(nums):
                if used[i]:
                    continue
                used[i] = True
                path.append(x)
                dfs()
                path.pop()
                used[i] = False

        dfs()
        return ans
```

**时间复杂度**

`O(n * n!)`。

**空间复杂度**

`O(n)` 递归栈和 `used` 数组，不计答案。

**怎么想到这个方法**

一旦题目要求“所有排列”，你就要想到每一层都要从“所有还没用过的元素”里继续选。

**常见 Follow-up**

- 如果有重复元素，怎么避免重复排列？
- 能否原地交换写出排列？

#### 3. Combination Sum

**题目含义**

给一些候选数，可以重复使用，问有哪些组合能凑出目标值。顺序不重要，所以要用 `start` 控制搜索起点。

**Python 代码**

```python
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        candidates.sort()

        def dfs(start: int, remain: int) -> None:
            if remain == 0:
                ans.append(path[:])
                return

            for i in range(start, len(candidates)):
                x = candidates[i]
                if x > remain:
                    break
                path.append(x)
                dfs(i, remain - x)
                path.pop()

        dfs(0, target)
        return ans
```

**时间复杂度**

最坏是指数级，通常写 `O(number of valid states)`。

**空间复杂度**

`O(target)` 量级的递归深度，不计答案。

**怎么想到这个方法**

看到“所有组合 + 和为 target + 元素可重复使用”，就该想到回溯里带 `start` 和剩余和。

**常见 Follow-up**

- 如果每个数只能用一次，和哪道题对应？
- 为什么排序后可以提前 `break`？

#### 4. Generate Parentheses

**题目含义**

生成所有合法括号组合。合法性的关键约束是：左括号不能超过 `n`，右括号数量不能超过左括号数量。

**Python 代码**

```python
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = []

        def dfs(left: int, right: int) -> None:
            if len(path) == 2 * n:
                ans.append("".join(path))
                return
            if left < n:
                path.append("(")
                dfs(left + 1, right)
                path.pop()
            if right < left:
                path.append(")")
                dfs(left, right + 1)
                path.pop()

        dfs(0, 0)
        return ans
```

**时间复杂度**

与合法答案数量同阶，通常写 Catalan 数量级。

**空间复杂度**

`O(n)`。

**怎么想到这个方法**

不是所有长度为 `2n` 的括号串都要枚举，而是边构造边保证合法，这就是回溯剪枝的价值。

**常见 Follow-up**

- 如果有多种括号类型，约束如何扩展？
- 为什么不能等生成完再统一判合法？

#### 5. Palindrome Partitioning

**题目含义**

把字符串切分成若干段，要求每一段都是回文串。核心是“枚举切分点 + 判断当前段是否合法”。

**Python 代码**

```python
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []

        def is_pal(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(start: int) -> None:
            if start == len(s):
                ans.append(path[:])
                return

            for end in range(start, len(s)):
                if not is_pal(start, end):
                    continue
                path.append(s[start:end + 1])
                dfs(end + 1)
                path.pop()

        dfs(0)
        return ans
```

**时间复杂度**

最坏是指数级。

**空间复杂度**

`O(n)` 递归深度，不计答案。

**怎么想到这个方法**

只要题目出现“把字符串切成所有合法方案”，就该想到以当前位置为起点，枚举下一刀切在哪里。

**常见 Follow-up**

- 怎么用 DP 预处理回文判断来加速？
- 如果只要求最少切几刀，会转成什么模型？

#### 6. Word Search

**题目含义**

在二维网格中找一个单词，字符可上下左右走，而且同一个格子不能重复使用。它本质是网格 DFS + 回溯。

**Python 代码**

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

**时间复杂度**

最坏 `O(mn * 4^L)`，`L` 为单词长度。

**空间复杂度**

`O(L)` 递归栈。

**怎么想到这个方法**

二维网格 + 路径约束 + 不可重复使用，基本就是 DFS 回溯的标准信号。

**常见 Follow-up**

- 如果要同时找多个单词，怎么升级成 `Trie + DFS`？
- 为什么访问标记必须回退？

#### 7. N-Queens

**题目含义**

在 `n x n` 棋盘上放 `n` 个皇后，要求互不攻击。回溯时每一行只放一个皇后，再检查列和对角线冲突。

**Python 代码**

```python
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag1 = set()
        diag2 = set()
        board = [["."] * n for _ in range(n)]
        ans = []

        def dfs(r: int) -> None:
            if r == n:
                ans.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or r - c in diag1 or r + c in diag2:
                    continue
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)
                board[r][c] = "Q"
                dfs(r + 1)
                board[r][c] = "."
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)

        dfs(0)
        return ans
```

**时间复杂度**

`O(n!)` 量级。

**空间复杂度**

`O(n)` 递归栈和辅助集合。

**怎么想到这个方法**

要求枚举所有合法摆法时，先按行逐层放置，每层做合法性剪枝，是最自然的回溯框架。

**常见 Follow-up**

- 如果只返回解的数量，代码怎么改？
- 位运算优化为什么会更快？

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

#### 1. Number of Islands

**题目含义**

给你一张由 `'1'` 和 `'0'` 组成的网格，问有多少块彼此连通的陆地。发现一块陆地后，要把整块岛都遍历干净。

**Python 代码**

```python
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    ans += 1
                    dfs(r, c)
        return ans
```

**时间复杂度**

`O(mn)`。

**空间复杂度**

`O(mn)` 最坏递归栈。

**怎么想到这个方法**

网格里一旦问“连通块数量”，第一反应就是 DFS/BFS 染色，每发现一个新块就把它整片标记掉。

**常见 Follow-up**

- BFS 版怎么写？
- 如果是八连通而不是四连通，哪里要改？

#### 2. Rotting Oranges

**题目含义**

所有腐烂橘子会同时向四周扩散，问几分钟后全部腐烂。这是典型多源 BFS。

**Python 代码**

```python
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        while q and fresh:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            minutes += 1

        return minutes if fresh == 0 else -1
```

**时间复杂度**

`O(mn)`。

**空间复杂度**

`O(mn)`。

**怎么想到这个方法**

看到“多个起点同时扩散、按分钟分层推进”，就应该想到多源 BFS，而不是从每个新鲜橘子反向暴力搜。

**常见 Follow-up**

- 为什么这里要按层处理？
- 如果每条边的传播时间不同，还能用普通 BFS 吗？

#### 3. Course Schedule

**题目含义**

课程依赖本质是有向图，问能不能学完所有课，就是看图里有没有环。BFS 版通常用拓扑排序。

**Python 代码**

```python
from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        q = deque(i for i in range(numCourses) if indegree[i] == 0)
        taken = 0

        while q:
            node = q.popleft()
            taken += 1
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return taken == numCourses
```

**时间复杂度**

`O(V + E)`。

**空间复杂度**

`O(V + E)`。

**怎么想到这个方法**

只要题目是“依赖关系 + 是否存在可行顺序”，就优先想到拓扑排序；入度为 0 的节点就是当前能先做的事。

**常见 Follow-up**

- 如果要返回一种合法顺序，对应哪道题？
- DFS 判环和 BFS 拓扑排序怎么比较？

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
