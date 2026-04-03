# 06 BFS 与图完整答案

说明：

- 本文按题目分节
- 每题包含：题型识别、中文解释、English explanation、Python 标准解法
- 图题先问自己：这是最短路、连通块、拓扑排序，还是图建模？

---

## 1. Word Ladder

**题型识别**

```text
无权图最短路径 / Shortest Path in Unweighted Graph
```

**中文解释**

每个单词都可以看成图中的一个节点。  
如果两个单词只差一个字符，就连一条边。  
题目要求最少变换次数，本质就是无权图最短路径，所以用 BFS。

**English Explanation**

Treat each word as a node in a graph.  
Two words are connected if they differ by exactly one character.  
Since the problem asks for the minimum number of transformations, it is a shortest-path problem in an unweighted graph, so BFS is the right approach.

**Python 标准解法**

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

---

## 2. Word Ladder II

**题型识别**

```text
最短路径 + 回溯构造答案 / BFS Shortest Paths + Backtracking
```

**中文解释**

这一题不仅要最短长度，还要所有最短路径。  
做法通常分两层：

1. BFS 建最短层级关系，同时记录每个单词的父节点
2. 从 `endWord` 回溯到 `beginWord`，构造所有答案

**English Explanation**

This problem asks not only for the shortest length, but for all shortest paths.  
The usual approach has two phases:

1. BFS to build shortest-level relationships while recording parent nodes
2. Backtrack from `endWord` to `beginWord` to construct all valid shortest paths

**Python 标准解法**

```python
from collections import defaultdict
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        layer = {beginWord}
        parents = defaultdict(set)

        while layer and endWord not in parents:
            next_layer = defaultdict(set)
            for word in layer:
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        nxt = word[:i] + ch + word[i + 1:]
                        if nxt in word_set and nxt not in parents:
                            next_layer[nxt].add(word)
            layer = next_layer
            parents.update(next_layer)

        ans = []
        if endWord not in parents:
            return ans

        def backtrack(word, path):
            if word == beginWord:
                ans.append(path[::-1])
                return
            for p in parents[word]:
                backtrack(p, path + [p])

        backtrack(endWord, [endWord])
        return ans
```

---

## 3. Walls and Gates

**题型识别**

```text
多源 BFS / Multi-source BFS
```

**中文解释**

所有门都是距离的起点，所以要把所有门同时入队。  
然后一层一层扩散，第一次走到某个空房间时，就是它到最近门的最短距离。

**English Explanation**

All gates are starting points for distance propagation, so we push all gates into the queue at once.  
Then we expand level by level. The first time we reach an empty room is the shortest distance from a gate.

**Python 标准解法**

```python
from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        m, n = len(rooms), len(rooms[0])
        q = deque()

        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] == 2147483647:
                    rooms[nr][nc] = rooms[r][c] + 1
                    q.append((nr, nc))
```

---

## 4. Shortest Distance from All Buildings

**题型识别**

```text
多次 BFS 汇总距离 / Repeated BFS Distance Aggregation
```

**中文解释**

对每一栋建筑都做一次 BFS：

- `dist[r][c]`：所有建筑到这个空地的距离总和
- `reach[r][c]`：有多少栋建筑能到这个空地

最后在所有空地中，找 `reach == building_count` 的最小距离。

**English Explanation**

Run BFS from each building:

- `dist[r][c]`: total distance from all buildings to this empty land
- `reach[r][c]`: how many buildings can reach this empty land

At the end, among all empty cells with `reach == building_count`, choose the minimum total distance.

**Python 标准解法**

```python
from collections import deque
from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[0] * n for _ in range(m)]
        reach = [[0] * n for _ in range(m)]
        buildings = 0

        def bfs(sr, sc):
            visited = [[False] * n for _ in range(m)]
            q = deque([(sr, sc, 0)])
            while q:
                r, c, d = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 0:
                        visited[nr][nc] = True
                        dist[nr][nc] += d + 1
                        reach[nr][nc] += 1
                        q.append((nr, nc, d + 1))

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    buildings += 1
                    bfs(r, c)

        ans = min(
            (dist[r][c] for r in range(m) for c in range(n) if grid[r][c] == 0 and reach[r][c] == buildings),
            default=float("inf"),
        )
        return ans if ans != float("inf") else -1
```

---

## 5. The Maze

**题型识别**

```text
图搜索 / Graph Search with Rolling Movement
```

**中文解释**

球不是一步一步走，而是会一直滚到撞墙才停。  
所以从某个位置出发时，每个方向的“下一状态”不是相邻格子，而是滚动停止后的格子。

**English Explanation**

The ball does not move one cell at a time. It keeps rolling until it hits a wall.  
So from one state, the next state in each direction is not the adjacent cell, but the stopping cell after rolling.

**Python 标准解法**

```python
from collections import deque
from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        q = deque([tuple(start)])
        seen = {tuple(start)}

        while q:
            r, c = q.popleft()
            if [r, c] == destination:
                return True

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r, c
                while 0 <= nr + dr < m and 0 <= nc + dc < n and maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc

                if (nr, nc) not in seen:
                    seen.add((nr, nc))
                    q.append((nr, nc))

        return False
```

---

## 6. Number of Islands

**题型识别**

```text
连通块 DFS / Connected Components DFS
```

**中文解释**

每发现一个新的陆地 `1`，就说明找到一座新岛。  
然后用 DFS 把整座岛全部“淹掉”，避免重复计数。

**English Explanation**

Whenever we find a new land cell `1`, we have discovered a new island.  
Then use DFS to flood-fill the whole island so it will not be counted again.

**Python 标准解法**

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

---

## 7. Max Area of Island

**题型识别**

```text
连通块面积 DFS / DFS Area Counting
```

**中文解释**

和 `Number of Islands` 很像，只不过不是数岛屿个数，而是让 DFS 返回当前岛屿的面积。

**English Explanation**

This is similar to `Number of Islands`, except instead of counting islands, DFS returns the area of the current island.

**Python 标准解法**

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

---

## 8. Island Perimeter

**题型识别**

```text
网格计数 / Grid Counting
```

**中文解释**

每个陆地格子先贡献 `4` 条边。  
如果和上方或左方陆地相邻，就说明有公共边，要减去 `2`。

**English Explanation**

Each land cell initially contributes `4` edges.  
If it touches land above or to the left, they share one boundary, so subtract `2`.

**Python 标准解法**

```python
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    ans += 4
                    if r > 0 and grid[r - 1][c] == 1:
                        ans -= 2
                    if c > 0 and grid[r][c - 1] == 1:
                        ans -= 2

        return ans
```

---

## 9. Battleships in a Board

**题型识别**

```text
扫描计数 / Pattern Counting
```

**中文解释**

一艘战舰的左边和上边都不会再有 `X`。  
所以只统计那些“左边不是 X 且上边不是 X”的 `X`，它们就是每艘战舰的起点。

**English Explanation**

The topmost-leftmost cell of a battleship has no `X` above it and no `X` to its left.  
So count only those `X` cells that do not have another `X` above or to the left.

**Python 标准解法**

```python
from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        ans = 0

        for r in range(m):
            for c in range(n):
                if board[r][c] == "X":
                    if r > 0 and board[r - 1][c] == "X":
                        continue
                    if c > 0 and board[r][c - 1] == "X":
                        continue
                    ans += 1

        return ans
```

---

## 10. Is Graph Bipartite?

**题型识别**

```text
图染色 / Graph Coloring
```

**中文解释**

二分图的定义是：可以把所有点染成两种颜色，且相邻点颜色不同。  
所以 BFS/DFS 过程中，尝试给相邻点染相反颜色；如果冲突，就不是二分图。

**English Explanation**

A graph is bipartite if we can color all nodes with two colors such that adjacent nodes have different colors.  
So during BFS/DFS, assign opposite colors to neighbors. If a conflict appears, the graph is not bipartite.

**Python 标准解法**

```python
from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        for i in range(len(graph)):
            if i in color:
                continue

            q = deque([i])
            color[i] = 0

            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if nei in color:
                        if color[nei] == color[node]:
                            return False
                    else:
                        color[nei] = 1 - color[node]
                        q.append(nei)

        return True
```

---

## 11. Word Search

**题型识别**

```text
矩阵 DFS 回溯 / Grid DFS Backtracking
```

**中文解释**

从每个起点开始 DFS，尝试匹配单词的第 `i` 个字符。  
访问过的格子在当前路径里不能重复使用，所以要做标记再恢复。

**English Explanation**

Start DFS from each cell and try to match the `i`-th character of the word.  
Cells already used in the current path cannot be reused, so we mark them temporarily and restore them afterward.

**Python 标准解法**

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

---

## 12. Word Search II

**题型识别**

```text
Trie + DFS / Trie-guided DFS
```

**中文解释**

如果对每个单词都单独做一遍 `Word Search`，会非常慢。  
更高效的做法是：

1. 把所有单词建成 Trie
2. 在棋盘上 DFS
3. 当前路径只沿着 Trie 中存在的前缀继续搜索

**English Explanation**

Running `Word Search` independently for every word is too slow.  
The efficient approach is:

1. build a Trie from all words
2. DFS on the board
3. continue only if the current path is still a valid Trie prefix

**Python 标准解法**

```python
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            cur = root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            cur.word = word

        m, n = len(board), len(board[0])
        ans = []

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return

            nxt = node.children[ch]
            if nxt.word:
                ans.append(nxt.word)
                nxt.word = None

            board[r][c] = "#"
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != "#":
                    dfs(nr, nc, nxt)
            board[r][c] = ch

        for r in range(m):
            for c in range(n):
                dfs(r, c, root)

        return ans
```

---

## 13. Course Schedule

**题型识别**

```text
拓扑排序判环 / Topological Sort for Cycle Detection
```

**中文解释**

课程依赖可以看成有向图。  
如果图中有环，就无法完成所有课程。  
用入度数组 + 队列做拓扑排序：

- 入度为 0 的课程先学
- 学完后减少后续课程入度

最后如果处理的课程数等于总课程数，就说明无环。

**English Explanation**

Course prerequisites form a directed graph.  
If the graph contains a cycle, it is impossible to finish all courses.  
Use indegrees + queue for topological sorting:

- courses with indegree 0 can be taken first
- after taking one, reduce indegrees of dependent courses

If the number of processed courses equals the total number of courses, the graph has no cycle.

**Python 标准解法**

```python
from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indeg = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1

        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        seen = 0

        while q:
            node = q.popleft()
            seen += 1
            for nei in graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)

        return seen == numCourses
```

---

## 14. Course Schedule II

**题型识别**

```text
拓扑排序输出顺序 / Topological Ordering
```

**中文解释**

和上一题同样是拓扑排序，只不过这次不仅要判断能否完成，还要返回一种合法学习顺序。

**English Explanation**

This is the same topological sort idea as the previous problem, but now we must return one valid ordering instead of just checking feasibility.

**Python 标准解法**

```python
from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indeg = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1

        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        ans = []

        while q:
            node = q.popleft()
            ans.append(node)
            for nei in graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)

        return ans if len(ans) == numCourses else []
```

---

## 15. Alien Dictionary

**题型识别**

```text
建图 + 拓扑排序 / Graph Construction + Topological Sort
```

**中文解释**

根据字典序相邻两个单词，找到第一个不同字符，就能得到一个顺序关系：

```text
a -> b
```

然后在所有字符之间做拓扑排序。  
还要注意非法情况：前一个单词更长但前缀和后一个相同。

**English Explanation**

From each adjacent pair of words, find the first differing character and derive an order relation:

```text
a -> b
```

Then run topological sorting on all characters.  
Also handle the invalid case where the earlier word is longer but has the later word as a prefix.

**Python 标准解法**

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

---

## 16. Clone Graph

**题型识别**

```text
图复制 / Graph Copy with Hash Map
```

**中文解释**

图复制的核心永远是：

```text
老节点 -> 新节点
```

只要有这个映射，就能避免重复创建节点，也能正确连接邻居。

**English Explanation**

The core of graph cloning is always:

```text
old node -> new node
```

Once we maintain this mapping, we avoid duplicate node creation and can connect neighbors correctly.

**Python 标准解法**

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

---

## 17. Reconstruct Itinerary

**题型识别**

```text
欧拉路径 / Eulerian Path with Lexicographical Order
```

**中文解释**

这题的技巧是 Hierholzer 算法。  
把机票按逆序排序后放入邻接表，这样每次 `pop()` 出来的都是字典序最小的下一站。  
DFS 走到走不动时，再把机场加入答案，最后反转。

**English Explanation**

The trick is Hierholzer’s algorithm for Eulerian path construction.  
Sort tickets in reverse order when building adjacency lists so that each `pop()` gives the lexicographically smallest next airport.  
During DFS, add the airport to the answer only when no further edge remains, then reverse the result at the end.

**Python 标准解法**

```python
from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        ans = []

        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            ans.append(airport)

        dfs("JFK")
        return ans[::-1]
```

---

## 18. Pacific Atlantic Water Flow

**题型识别**

```text
反向 DFS / Reverse Reachability DFS
```

**中文解释**

正向思考会比较难，因为要从每个点判断能不能流到两个海。  
更聪明的方式是反过来想：

- 从太平洋边界出发，往更高或等高的点爬
- 从大西洋边界出发，往更高或等高的点爬

能同时被两边访问到的点就是答案。

**English Explanation**

The forward direction is hard because from each cell we would need to test reachability to both oceans.  
The better idea is reverse thinking:

- start from the Pacific border and climb to higher or equal heights
- start from the Atlantic border and climb to higher or equal heights

Cells reachable from both searches are the answer.

**Python 标准解法**

```python
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def dfs(r, c, seen):
            seen.add((r, c))
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and (nr, nc) not in seen
                    and heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, seen)

        pac, atl = set(), set()

        for r in range(m):
            dfs(r, 0, pac)
            dfs(r, n - 1, atl)
        for c in range(n):
            dfs(0, c, pac)
            dfs(m - 1, c, atl)

        return [[r, c] for r, c in pac & atl]
```

---

## 19. Accounts Merge

**题型识别**

```text
图连通分量 / Graph Connected Components
```

**中文解释**

邮箱之间如果出现在同一个账户里，就应该属于同一个人。  
所以可以把邮箱看成图节点，把同账户里的邮箱连边。  
最后求每个连通分量即可。

**English Explanation**

If two emails appear in the same account, they belong to the same person.  
So model emails as graph nodes and connect emails that appear in the same account.  
Then each connected component becomes one merged account.

**Python 标准解法**

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

---

## 20. All Nodes Distance K in Binary Tree

**题型识别**

```text
树转无向图 + BFS / Tree to Undirected Graph + BFS
```

**中文解释**

树节点通常只能往下走，但这题允许“向上”走到父节点。  
所以先把树转成无向图，再从 `target` 做 BFS，找距离为 `k` 的所有节点。

**English Explanation**

Normally tree traversal only goes downward, but here we also need to move upward to parents.  
So first convert the tree into an undirected graph, then run BFS from the `target` node to find all nodes at distance `k`.

**Python 标准解法**

```python
from collections import defaultdict, deque
from typing import List


class Solution:
    def distanceK(self, root: 'TreeNode', target: 'TreeNode', k: int) -> List[int]:
        graph = defaultdict(list)

        def build(node, parent):
            if not node:
                return
            if parent:
                graph[node].append(parent)
                graph[parent].append(node)
            build(node.left, node)
            build(node.right, node)

        build(root, None)

        q = deque([(target, 0)])
        seen = {target}
        ans = []

        while q:
            node, dist = q.popleft()
            if dist == k:
                ans.append(node.val)
            elif dist < k:
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append((nei, dist + 1))

        return ans
```

---

## 21. Number of Connected Components in an Undirected Graph

**题型识别**

```text
图连通分量计数 / Connected Components Counting
```

**中文解释**

每碰到一个未访问过的节点，就说明发现了一个新的连通分量。  
然后 DFS/BFS 把整个分量都访问掉。

**English Explanation**

Whenever we encounter an unvisited node, we have found a new connected component.  
Then DFS/BFS is used to traverse that entire component.

**Python 标准解法**

```python
from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set()

        def dfs(node):
            seen.add(node)
            for nei in graph[node]:
                if nei not in seen:
                    dfs(nei)

        ans = 0
        for i in range(n):
            if i not in seen:
                ans += 1
                dfs(i)

        return ans
```

---

## 22. Minesweeper

**题型识别**

```text
网格 DFS 展开 / Grid DFS Expansion
```

**中文解释**

点击规则是：

- 如果点到雷，直接变 `X`
- 如果周围有雷，显示数字
- 如果周围没有雷，显示 `B`，并继续递归展开周围格子

**English Explanation**

The click rules are:

- if we click on a mine, it becomes `X`
- if adjacent mines exist, show the count
- if no adjacent mines exist, mark `B` and recursively reveal surrounding cells

**Python 标准解法**

```python
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        dirs = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        def dfs(r, c):
            if board[r][c] != "E":
                return

            mines = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "M":
                    mines += 1

            if mines:
                board[r][c] = str(mines)
                return

            board[r][c] = "B"
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    dfs(nr, nc)

        r, c = click
        if board[r][c] == "M":
            board[r][c] = "X"
        else:
            dfs(r, c)

        return board
```
