---
title: "Graph / BFS / DFS Study Guide (English)"
lang: en
lang_pair: /algorithms/graph_bfs_dfs_study_guide
---

# Graph / BFS / DFS Study Guide

This guide covers graph traversal patterns for interviews: DFS flood fill, BFS shortest path, and topological sort.

---

## Pattern Summary

Graph search problems become much easier once you separate three roles clearly: DFS for exploring an entire connected component, BFS for shortest distance by layers, and topological sort for dependency order. A lot of interview graph problems are just variations of those three patterns.

## Problem Meaning

This guide is a graph-pattern overview, not one single problem. The representative example below uses `Number of Islands`, because it is one of the best starter problems for learning how to treat a grid as a graph and flood-fill one connected component at a time.

## Python Code

```python
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] != '1':
                return

            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)

        return islands


sample = [
    ['1', '1', '0', '0'],
    ['1', '0', '0', '1'],
    ['0', '0', '1', '1'],
]
print(Solution().numIslands(sample))
```

## Time Complexity

Each cell is visited at most once, so the time complexity is `O(rows * cols)`.

## Space Complexity

The recursion stack can grow as large as a connected region, so the worst-case space complexity is `O(rows * cols)`.

## How To Think About It

When you see words like island, region, component, or spread, first translate the problem into a simpler sentence: if I start from one valid cell, can I visit the whole connected region from there? Once that is true, the problem becomes “scan the grid; every time you discover new land, count it and flood-fill it.” That is the parent template for many graph/grid questions.

## Example Case

Input grid:

```text
1 1 0 0
1 0 0 1
0 0 1 1
```

Output: `2`
Explanation: the top-left land is one island, and the connected land on the right is the second island.

Edge case: an all-water grid returns `0`, and a single land cell returns `1`.

## Common Follow-up Questions

- Why is BFS usually the safer choice when the question asks for the minimum number of steps?
- Why should simultaneous spread problems use multi-source BFS?
- When the input represents prerequisites, why do we switch to topological sort instead of plain DFS/BFS?

## Part 1: Signals That Point to a Graph Problem

- Counting islands, connected regions, or components
- Spreading from one cell to its neighbors
- "Minimum number of steps to reach the destination"
- Course prerequisites, task dependencies, ordering constraints
- Grid problems where you move up/down/left/right
- Multiple sources that all spread simultaneously

One-liner summary:
- **DFS** → search an entire connected component
- **BFS** → find shortest path by layer
- **Topological sort** → resolve dependency ordering

---

## Part 2: Problem Categories

### 1. Grid DFS / Flood Fill

Treat the grid as a graph. Each cell connects to its four neighbors. When you find an unvisited land cell, DFS to "sink" the entire island.

1. `Number of Islands`
2. `Max Area of Island`
3. `Surrounded Regions`
4. `Word Search`

### 2. Multi-Source BFS / Layer-by-Layer Shortest Path

Start BFS with multiple sources simultaneously. Each layer represents one step/minute.

1. `Rotting Oranges`
2. `01 Matrix`
3. `Walls and Gates`

### 3. Graph Traversal / Connectivity

Build an adjacency list. From a starting node, traverse to check reachability or count connected components.

1. `Find if Path Exists in Graph`
2. `Number of Connected Components in an Undirected Graph`
3. `Clone Graph`

### 4. Cycle Detection / Topological Sort

Edges represent dependencies. A cycle means the ordering is impossible. Without a cycle, you can produce a valid order.

1. `Course Schedule`
2. `Course Schedule II`
3. `Alien Dictionary`

---

## Part 3: Recommended Practice Order

1. `Number of Islands`
2. `Max Area of Island`
3. `Rotting Oranges`
4. `Find if Path Exists in Graph`
5. `Clone Graph`
6. `Course Schedule`
7. `Course Schedule II`
8. `Surrounded Regions`
9. `01 Matrix`
10. `Word Search`

Reasoning: master grid DFS and multi-source BFS first, then move to general adjacency-list graphs, and finally handle dependency/ordering problems.

---

## Part 4: Key Templates

### Template 1: Grid DFS

```python
def dfs(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return
    if grid[r][c] != "1":
        return

    grid[r][c] = "0"  # mark visited by modifying in place

    dfs(r + 1, c)
    dfs(r - 1, c)
    dfs(r, c + 1)
    dfs(r, c - 1)
```

What this does:
- Stop if out of bounds
- Stop if not a target cell
- Mark as visited immediately (before recursing)
- Expand to all four directions

### Template 2: BFS Layer-by-Layer

```python
from collections import deque

queue = deque(start_nodes)
steps = 0

while queue:
    for _ in range(len(queue)):
        x = queue.popleft()
        # process current node
        # push neighbors into queue
    steps += 1
```

What this does:
- All nodes currently in the queue belong to the same layer
- One `for` loop processes one full layer
- `steps` directly tracks distance or time elapsed

### Template 3: Topological Sort (Kahn's Algorithm / BFS)

```python
from collections import deque

graph = [[] for _ in range(numCourses)]
indegree = [0] * numCourses

for a, b in prerequisites:
    graph[b].append(a)
    indegree[a] += 1

queue = deque(i for i in range(numCourses) if indegree[i] == 0)
visited = 0

while queue:
    node = queue.popleft()
    visited += 1

    for nxt in graph[node]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)
```

What this does:
- Nodes with in-degree 0 have no prerequisites — process them first
- After processing a node, decrement in-degree of its dependents
- If `visited == numCourses` at the end, the graph has no cycle

### Template 4: Adjacency List Construction

```python
graph = [[] for _ in range(n)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)  # undirected: add both directions
```

For directed graphs, only add one direction.

---

## Part 5: Problem Walkthroughs

## 1. Number of Islands

### Goal

Count the number of islands in a grid of `'1'` (land) and `'0'` (water).

### Category

Grid DFS / Flood Fill.

### Core Idea

Scan the grid left to right, top to bottom. Every time you encounter an unvisited land cell, you've found a new island — increment the count, then DFS to sink the entire island so it isn't counted again.

**Key rule**: find a new island → count++ and flood-fill the whole connected component.

### Python Code

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] != '1':
                return
            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)

        return count
```

### Common Mistakes

- Counting the same island multiple times (forgot to mark as visited)
- Infinite recursion (no visited marking → keeps revisiting)

---

## 2. Max Area of Island

### Goal

Find the maximum area (cell count) among all islands.

### Core Idea

Same as Number of Islands, but the DFS function now returns the area of the island instead of just marking it. Each cell adds 1 to the area.

```python
def dfs(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return 0
    if grid[r][c] != 1:
        return 0
    grid[r][c] = 0
    return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
```

**What this teaches**: recursive functions can return useful values, not just traverse.

---

## 3. Rotting Oranges

### Goal

Find the minimum number of minutes until all fresh oranges are rotten, or return -1 if impossible.

### Category

Multi-source BFS.

### Core Idea

All initially-rotten oranges are the starting points. Put them all into the queue at once. Every layer of BFS represents one minute passing. Each layer spreads rot to adjacent fresh oranges.

**Key rule**: all initial rotten oranges enter the queue simultaneously — this is the defining characteristic of multi-source BFS.

### Python Code

```python
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            minutes += 1

        return minutes - 1 if fresh == 0 else -1
```

### Common Mistakes

- Starting one rotten orange's BFS separately, then another's — this gives wrong timing
- Off-by-one in counting minutes

---

## 4. Clone Graph

### Goal

Deep-copy a connected undirected graph.

### Core Idea

DFS through the original graph. Maintain a hash map: `original node → cloned node`. Before recursing into neighbors, create the clone of the current node first. This prevents infinite recursion on cycles.

**Key rule**: clone the current node first, record it in the map, then clone its neighbors.

```python
class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        cloned = {}

        def dfs(n):
            if n in cloned:
                return cloned[n]
            clone = Node(n.val)
            cloned[n] = clone
            for neighbor in n.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone

        return dfs(node)
```

### Common Mistake

Without the hash map, you'd create infinite nodes in a cyclic graph.

---

## 5. Course Schedule

### Goal

Determine if it's possible to finish all courses given prerequisite constraints.

### Category

Cycle detection / Topological sort.

### Core Idea

Build a directed graph where an edge from A to B means "A must be taken before B." A valid schedule exists if and only if there's no cycle.

Use topological sort (Kahn's algorithm): count in-degrees, start from zero-in-degree nodes, and check if all nodes are eventually processed.

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        queue = deque(i for i in range(numCourses) if indegree[i] == 0)
        visited = 0

        while queue:
            node = queue.popleft()
            visited += 1
            for nxt in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        return visited == numCourses
```

### Course Schedule II

Same logic, but collect the topological order in a list. If `len(order) == numCourses`, return it; otherwise return `[]`.

---

## Part 6: Summary

| Scenario | Algorithm |
|---|---|
| Search entire connected component | DFS with visited marking |
| Shortest path (unweighted) | BFS, layer by layer |
| Multiple sources spreading simultaneously | Multi-source BFS (all sources in queue from the start) |
| Dependency resolution / cycle detection | Topological sort (Kahn's algorithm) |
| Graph copying | DFS + hash map (original → clone) |

**The single most important habit**: always mark nodes as visited before recursing or enqueuing — never after. This prevents revisits and infinite loops.
