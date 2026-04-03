# 2. 矩阵搜索 / 岛屿 / 最短路

## 面试题目怎么问

- 给一个二维网格，统计有多少个岛屿
- 从起点走到终点最少需要多少步
- 网格里有障碍物，问能否走到终点
- 多源扩散，例如腐烂橘子、火焰传播、离最近目标距离

## 识别信号

- 输入是 `grid`
- 只能上下左右或加上对角线移动
- 问最短路径
- 问连通块数量
- 问扩散层数 / 最少轮数

## Amazon 风格业务包装

- warehouse 里机器人从起点走到货架，障碍物不能穿过
- delivery drone 在地图网格里找最短路线
- 一批坏货从某些仓位开始扩散，问多久影响整个仓库
- 仓库区域由可通行和不可通行位置组成，问有多少独立区域

## 你该怎么想

- 只要是二维格子，先问自己：这是 shortest path 还是 connected components
- 如果问最少几步，直接想到 BFS
- 如果问连通块数量、独立区域、岛屿数，直接想到 flood fill

## 标准代码模板 1：BFS 最短路

```python
from collections import deque

def shortest_path(grid, start, end):
    m, n = len(grid), len(grid[0])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque([(start[0], start[1], 0)])
    visited = set([start])

    while q:
        x, y, dist = q.popleft()
        if (x, y) == end:
            return dist

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if grid[nx][ny] != 1 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((nx, ny, dist + 1))
    return -1
```

## 标准代码模板 2：DFS 统计岛屿

```python
def num_islands(grid):
    m, n = len(grid), len(grid[0])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(x, y):
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != "1":
            return
        grid[x][y] = "0"
        for dx, dy in dirs:
            dfs(x + dx, y + dy)

    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                count += 1
                dfs(i, j)
    return count
```

## 标准代码模板 3：多源 BFS

```python
from collections import deque

def multi_source_bfs(grid, sources):
    m, n = len(grid), len(grid[0])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque()
    visited = set()

    for x, y in sources:
        q.append((x, y, 0))
        visited.add((x, y))

    while q:
        x, y, dist = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if grid[nx][ny] != 1 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((nx, ny, dist + 1))
```

## 标准代码模板 4：状态 BFS 打破 k 个墙

```python
from collections import deque

def shortest_path_break_k_walls(grid, start, end, k):
    m, n = len(grid), len(grid[0])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    sx, sy = start
    ex, ey = end

    q = deque([(sx, sy, k, 0)])
    visited = set([(sx, sy, k)])

    while q:
        x, y, remain, dist = q.popleft()
        if (x, y) == (ex, ey):
            return dist

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                nr = remain - grid[nx][ny]
                state = (nx, ny, nr)
                if nr >= 0 and state not in visited:
                    visited.add(state)
                    q.append((nx, ny, nr, dist + 1))
    return -1
```

## 标准代码模板 5：Dijkstra on Grid

```python
import heapq

def dijkstra_grid(cost, start, end):
    m, n = len(cost), len(cost[0])
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    INF = float('inf')

    dist = [[INF] * n for _ in range(m)]
    sx, sy = start
    ex, ey = end
    dist[sx][sy] = 0

    pq = [(0, sx, sy)]

    while pq:
        cur_cost, x, y = heapq.heappop(pq)
        if (x, y) == (ex, ey):
            return cur_cost
        if cur_cost > dist[x][y]:
            continue

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                new_cost = cur_cost + cost[nx][ny]
                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny))
    return -1
```

## 代码讲解

- 无权最短路：BFS
- 连通块：DFS / BFS flood fill
- 多个起点同时扩散：multi-source BFS
- 同一个格子但资源状态不同：状态 BFS
- 边权不同：Dijkstra 或 0-1 BFS

## 面试时怎么讲

- 如果问最短步数，我第一反应是 BFS，因为无权图的最短路就是按层扩展
- 如果问区域数量，我会从每个未访问格子出发做一次 flood fill
- 如果同一个格子在不同资源状态下意义不同，我会把状态扩成 `(x, y, extra_state)`

## 常见 follow-up 和回答

**Q1：为什么最短路要用 BFS，不用 DFS？**  
因为每走一步代价都一样，BFS 按层扩展，第一次到终点时一定最短。

**Q2：如果可以斜着走怎么办？**  
把 `dirs` 改成 8 个方向。

**Q3：visited 一定要单独开吗？**  
不一定。允许修改输入时可以原地标记。

**Q4：如果有多个起点同时扩散怎么办？**  
用多源 BFS。

**Q5：如果边有不同权重怎么办？**  
非负权重用 Dijkstra；只有 0 和 1 时用 0-1 BFS。

**Q6：如果最多可以打破一个墙怎么办？**  
把状态从 `(x, y)` 扩成 `(x, y, remain_k)`。

## Amazon 风格完整题面

> A warehouse robot starts at the entrance and needs to reach a target shelf.  
> The floor is represented as a grid. Some cells are blocked by obstacles.  
> Return the minimum number of steps needed to reach the shelf, or `-1` if it is impossible.

## 可直接背的口语回答稿

“虽然题目在讲机器人和仓库，但抽象后就是一个二维 grid 上的无权最短路问题。每个可走格子是一个节点，机器人每次上下左右移动一步，所以边权相同。我会用 BFS 按层扩展，第一次到达终点时就是最短距离。如果题目变成区域数量，我就改成 DFS/BFS flood fill；如果出现多个起点或资源状态，我会切到多源 BFS 或状态 BFS。”

## 推荐代表题

- Number of Islands
- Shortest Path in Binary Matrix
- Walls and Gates
- Rotten Oranges

