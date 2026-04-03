---
title: "06 BFS 与图详细教学"
---

# 06 BFS 与图详细教学

图题先问：这是按层扩散、连通块、还是依赖关系？

---

## 一、三大模板

### 1. DFS 染色

```text
// 连通块、岛屿、矩阵搜索
```

### 2. BFS 按层

```text
// 最短步数、扩散过程
```

### 3. 拓扑排序

```text
// 依赖关系
// 入度为 0 先处理
```

---

## 二、代表题

### Number of Islands

**题目含义**

每发现一个新的陆地 `1`，就说明找到一座新岛。  
然后用 DFS 把整座岛全部“淹掉”，避免重复计数。

**代表 Python 代码**

```python
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
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

`O(mn)` 最坏递归栈或队列。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `连通块 DFS / Connected Components DFS`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**常见 Follow-up**

- 如果要返回具体路径而不是只判断可行性，额外记录什么？
- DFS、BFS、并查集三种解法分别适合什么场景？

### Max Area of Island

**题目含义**

和 `Number of Islands` 很像，只不过不是数岛屿个数，而是让 DFS 返回当前岛屿的面积。

**代表 Python 代码**

```python
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        ans = 0
        for r in range(m):
            for c in range(n):
                ans = max(ans, dfs(r, c))

        return ans
```

**时间复杂度**

`O(mn)`。

**空间复杂度**

`O(mn)` 最坏递归栈。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `连通块面积 DFS / DFS Area Counting`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**常见 Follow-up**

- 如果要返回具体路径而不是只判断可行性，额外记录什么？
- DFS、BFS、并查集三种解法分别适合什么场景？

### Word Search

**题目含义**

从每个起点开始 DFS，尝试匹配单词的第 `i` 个字符。  
访问过的格子在当前路径里不能重复使用，所以要做标记再恢复。

**代表 Python 代码**

```python
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[i]:
                return False

            tmp = board[r][c]
            board[r][c] = "#"
            found = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            board[r][c] = tmp
            return found

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True

        return False
```

**时间复杂度**

通常取决于搜索树大小，常见为指数级。

**空间复杂度**

递归栈加辅助状态，通常 `O(depth)` 到指数级状态空间。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `矩阵 DFS 回溯 / Grid DFS Backtracking`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**常见 Follow-up**

- 如果要返回具体路径而不是只判断可行性，额外记录什么？
- DFS、BFS、并查集三种解法分别适合什么场景？

### Course Schedule / II

**题目含义**

这组题都在处理课程依赖。`Course Schedule I` 问有没有合法顺序，本质是看图里有没有环；`II` 进一步要求你返回一种可行顺序。

**代表 Python 代码**

```python
from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        q = deque(i for i in range(numCourses) if indegree[i] == 0)
        order = []

        while q:
            node = q.popleft()
            order.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return order if len(order) == numCourses else []
```

**时间复杂度**

`O(V+E)`。

**空间复杂度**

`O(V+E)`。

**怎么想到这个方法**

一看到“依赖关系”和“能不能安排顺序”，就该把题目翻译成有向图，再决定是 DFS 判环还是 BFS 拓扑排序。

**常见 Follow-up**

- 如果只判断能否完成，和返回顺序相比代码差在哪？
- DFS 判环法和 Kahn 算法怎么选？

### Clone Graph

**题目含义**

图复制的核心永远是：

```text
老节点 -> 新节点
```

只要有这个映射，就能避免重复创建节点，也能正确连接邻居。

**代表 Python 代码**

```python
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        old_to_new = {}

        def dfs(cur):
            if cur in old_to_new:
                return old_to_new[cur]

            copy = Node(cur.val)
            old_to_new[cur] = copy

            for nei in cur.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)
```

**时间复杂度**

`O(V+E)`。

**空间复杂度**

`O(V)`。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `图复制 / Graph Copy with Hash Map`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**常见 Follow-up**

- 如果要返回具体路径而不是只判断可行性，额外记录什么？
- DFS、BFS、并查集三种解法分别适合什么场景？

### Word Ladder

**题目含义**

每个单词都可以看成图中的一个节点。  
如果两个单词只差一个字符，就连一条边。  
题目要求最少变换次数，本质就是无权图最短路径，所以用 BFS。

**代表 Python 代码**

```python
from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        q = deque([(beginWord, 1)])

        while q:
            word, dist = q.popleft()
            if word == endWord:
                return dist

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    nxt = word[:i] + ch + word[i + 1:]
                    if nxt in word_set:
                        word_set.remove(nxt)
                        q.append((nxt, dist + 1))

        return 0
```

**时间复杂度**

经典写法约 `O(N * L * 26)`。

**空间复杂度**

`O(N * L)`。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `无权图最短路径 / Shortest Path in Unweighted Graph`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**常见 Follow-up**

- 如果要返回具体路径而不是只判断可行性，额外记录什么？
- DFS、BFS、并查集三种解法分别适合什么场景？

### Accounts Merge

**题目含义**

邮箱之间如果出现在同一个账户里，就应该属于同一个人。  
所以可以把邮箱看成图节点，把同账户里的邮箱连边。  
最后求每个连通分量即可。

**代表 Python 代码**

```python
from collections import defaultdict
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        email_to_name = {}

        for acc in accounts:
            name = acc[0]
            first = acc[1]
            for email in acc[1:]:
                graph[first].add(email)
                graph[email].add(first)
                email_to_name[email] = name

        seen = set()
        ans = []

        for email in email_to_name:
            if email in seen:
                continue

            stack = [email]
            comp = []
            seen.add(email)

            while stack:
                cur = stack.pop()
                comp.append(cur)
                for nei in graph[cur]:
                    if nei not in seen:
                        seen.add(nei)
                        stack.append(nei)

            ans.append([email_to_name[email]] + sorted(comp))

        return ans
```

**时间复杂度**

约 `O(N alpha(N) + M log M)`。

**空间复杂度**

`O(N)`。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `图连通分量 / Graph Connected Components`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**常见 Follow-up**

- 如果要返回具体路径而不是只判断可行性，额外记录什么？
- DFS、BFS、并查集三种解法分别适合什么场景？

### Alien Dictionary

**题目含义**

根据字典序相邻两个单词，找到第一个不同字符，就能得到一个顺序关系：

```text
a -> b
```

然后在所有字符之间做拓扑排序。  
还要注意非法情况：前一个单词更长但前缀和后一个相同。

**代表 Python 代码**

```python
from collections import defaultdict, deque
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indeg = {ch: 0 for word in words for ch in word}

        for w1, w2 in zip(words, words[1:]):
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for a, b in zip(w1, w2):
                if a != b:
                    if b not in graph[a]:
                        graph[a].add(b)
                        indeg[b] += 1
                    break

        q = deque([ch for ch in indeg if indeg[ch] == 0])
        ans = []

        while q:
            ch = q.popleft()
            ans.append(ch)
            for nei in graph[ch]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)

        return "".join(ans) if len(ans) == len(indeg) else ""
```

**时间复杂度**

`O(C)` 到 `O(C + V + E)`。

**空间复杂度**

`O(V+E)`。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `建图 + 拓扑排序 / Graph Construction + Topological Sort`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**常见 Follow-up**

- 如果要返回具体路径而不是只判断可行性，额外记录什么？
- DFS、BFS、并查集三种解法分别适合什么场景？

