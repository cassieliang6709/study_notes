---
title: "Graph / BFS / DFS 题目分类讲义"
---

# Graph / BFS / DFS 题目分类讲义

这份笔记的目标很简单：

- 用中文把图论入门高频题按方法分类
- 让你先学会“这题为什么是图搜索”
- 不追求大而全，先掌握最常用的 BFS / DFS / 拓扑排序
- 默认以 LeetCode 高频面试题为主

---

## 这个题型 / 算法点的总结

图搜索题最重要的是先分清楚你到底要“搜完整个连通块”，还是“按层找最短步数”，还是“处理依赖顺序”。前者常用 DFS，中间常用 BFS，依赖关系常用拓扑排序。只要先把这三个角色分清楚，很多图题都会突然变得规整。

## 题目含义

这份讲义是图论入门总览，不是单独一道题。下面选 `Number of Islands` 做代表题，因为它最适合帮助 beginner 建立“把网格看成图，再做 flood fill”的第一层直觉。

## Python 代码

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

## 时间复杂度

每个格子最多访问一次，所以时间复杂度是 `O(rows * cols)`。

## 空间复杂度

递归栈最坏情况下可能达到整块连通区域大小，所以空间复杂度最坏是 `O(rows * cols)`。

## 怎么想到

看到“岛屿、区域、连通块”这类词时，不要急着想很多技巧，先把问题翻译成一句很朴素的话：如果我从一个陆地格子出发，能不能把和它连着的整块区域一次搜完？一旦这句话成立，这题就自然变成“扫描网格，发现新岛就计数并淹掉整块区域”。这就是很多网格图题的母模板。

## 示例 case

输入网格：

```text
1 1 0 0
1 0 0 1
0 0 1 1
```

输出：`2`
解释：左上角是一座岛，右侧连在一起的是另一座岛。

边界 case：如果全是 `0`，答案就是 `0`；如果只有一个 `1`，答案就是 `1`。

## 常见 Follow-up

- 如果题目问最短步数，为什么 DFS 往往不如 BFS 稳定？
- 如果一开始有多个起点同时扩散，为什么应该用多源 BFS？
- 如果题目给的是课程依赖关系，为什么要换成拓扑排序而不是普通 DFS/BFS？

## 一、先记住图题的判断信号

看到下面这些描述时，优先往图上想：

- 岛屿、连通块、区域数量
- 从一个点扩散到周围
- 最少几步到达终点
- 课程依赖、先修关系、任务顺序
- 网格里上下左右走
- 一批起点同时开始传播

一句话总结：

- `DFS` 常用来“搜完整个连通块”
- `BFS` 常用来“按层找最短步数”
- `拓扑排序` 常用来“处理依赖关系”

---

## 二、分类总表

### 1. 网格 DFS / Flood Fill

核心是：

- 把二维矩阵看成图
- 每个格子向四个方向连边
- 找到一个陆地后，把整块区域一次性搜完

典型题：

1. `Number of Islands`
2. `Max Area of Island`
3. `Surrounded Regions`
4. `Word Search`

### 2. 多源 BFS / 最短层数

核心是：

- 队列里一开始就放多个起点
- 每一层代表一步或一分钟
- 适合“同时扩散”的题

典型题：

1. `Rotting Oranges`
2. `01 Matrix`
3. `Walls and Gates`

### 3. 图的遍历 / 连通性判断

核心是：

- 把节点和边关系存成邻接表
- 从一个点出发，看能不能访问到目标
- 或者统计图里有多少个连通分量

典型题：

1. `Find if Path Exists in Graph`
2. `Number of Connected Components in an Undirected Graph`
3. `Clone Graph`

### 4. 有向图环检测 / 拓扑排序

核心是：

- 边表示依赖关系
- 有环就说明任务顺序不合法
- 无环时可以得到一个可行顺序

典型题：

1. `Course Schedule`
2. `Course Schedule II`
3. `Alien Dictionary`

---

## 三、推荐刷题顺序

建议按下面顺序练：

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

原因：

- 先把网格 DFS 和多源 BFS 打熟
- 再学一般图的邻接表遍历
- 最后再处理依赖关系和综合题

---

## 四、图题最常用模板

### 1. 网格 DFS 模板

```python
def dfs(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return
    if grid[r][c] != "1":
        return

    grid[r][c] = "0"

    dfs(r + 1, c)
    dfs(r - 1, c)
    dfs(r, c + 1)
    dfs(r, c - 1)
```

这段模板的本质是：

- 越界就停
- 不是目标格子就停
- 访问过后立刻做标记
- 再向四个方向扩展

### 2. BFS 按层遍历模板

```python
from collections import deque

queue = deque(start_nodes)
steps = 0

while queue:
    for _ in range(len(queue)):
        x = queue.popleft()
        # 处理当前节点
        # 把下一层节点放进队列
    steps += 1
```

这段模板的本质是：

- `queue` 里当前已有的元素属于同一层
- 一轮 `for` 处理完，才进入下一层
- 所以 `steps` 可以直接表示距离或时间

### 3. 拓扑排序模板

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

这段模板的本质是：

- 入度为 `0` 的点可以立刻学习或执行
- 删掉当前点后，它指向的点入度减一
- 最后若处理完所有节点，说明无环

---

## 五、逐题核心思路

## 1. Number of Islands

### 题目目标

给一个由 `'1'` 和 `'0'` 组成的网格，统计岛屿数量。

### 这题属于哪一类

属于“网格 DFS / Flood Fill”。

### 核心思路

从左到右、从上到下扫描网格。

每当遇到一个还没访问过的陆地，就说明发现了一座新岛屿，答案加一，然后立刻把整座岛全部淹掉。

### 最关键的一句话

- `找到一个新岛 = 答案加一 + flood fill 整个连通块`

### 容易错的点

- 只加一，不把整座岛搜完，后面会重复计数
- 忘记做访问标记，导致死循环

---

## 2. Max Area of Island

### 题目目标

求网格中最大岛屿面积。

### 核心思路

和 `Number of Islands` 几乎一模一样，只是 DFS 返回的不再是“有没有岛”，而是“这座岛一共有多少格”。

### 返回值怎么设计

```python
area = 1 + 上下左右四个方向返回面积之和
```

### 这题真正练的东西

- 学会让递归函数“返回信息”
- 不只是遍历，还要从子问题拿结果

---

## 3. Rotting Oranges

### 题目目标

求所有新鲜橘子腐烂所需的最少分钟数。

### 这题属于哪一类

属于“多源 BFS / 最短层数”。

### 核心思路

所有一开始腐烂的橘子，都是 BFS 的起点。

每一层扩散一次，就代表过了一分钟。

### 最关键的一句话

- `所有初始腐烂点同时入队`

这就是多源 BFS 最重要的信号。

### 容易错的点

- 把多个腐烂点拆开分别 BFS，会错
- 分钟数和层数经常加错一

---

## 4. Find if Path Exists in Graph

### 题目目标

判断无向图中 `source` 能不能到达 `destination`。

### 核心思路

先建邻接表，再从起点做一次 DFS 或 BFS。

只要能访问到终点，就返回 `True`。

### 邻接表模板

```python
graph = [[] for _ in range(n)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)
```

### 容易错的点

- 无向图忘记双向加边
- 没有 `visited`，在环里反复绕圈

---

## 5. Clone Graph

### 题目目标

复制一张连通图。

### 核心思路

这题不是单纯搜索，而是“搜索 + 映射”。

你需要一边遍历原图，一边建立：

- 原节点 -> 新节点

的对应关系。

### 最关键的一句话

- `先克隆当前节点，再递归克隆邻居`

### 容易错的点

- 没有哈希表保存映射，会无限重复创建节点
- 先处理邻居，结果当前节点副本还没建好

---

## 6. Course Schedule

### 题目目标

判断能否完成所有课程。

### 这题属于哪一类

属于“有向图环检测 / 拓扑排序”。

### 核心思路

如果依赖图里有环，就不可能学完。

最稳定的做法是：

- 建图
- 统计每个点入度
- 不断取出入度为 `0` 的点

如果最后处理的课程数量等于总课程数，说明无环。

### 最关键的一句话

- `能被拓扑排序完 = 无环`

---

## 7. Course Schedule II

### 题目目标

输出一个合法的修课顺序。

### 核心思路

和 `Course Schedule` 一模一样，只是多维护一个结果数组，把弹出队列的顺序记录下来。

### 易错点

- 最后长度不等于 `numCourses` 时要返回空数组

---

## 8. Word Search

### 题目目标

判断单词是否能在网格里连成。

### 这题为什么容易错

因为它同时用了：

- 网格搜索
- DFS
- 回溯

### 核心思路

从每个可能的起点出发，尝试匹配单词的第 `i` 个字符。

当前格子用过以后要临时标记，递归结束后还原。

### 最关键的一句话

- `当前路径上不能重复使用格子，所以要恢复现场`

---

## 六、图题统一检查清单

写图题前，先检查这 6 件事：

1. 节点是什么
2. 边是什么
3. 需要 DFS 还是 BFS
4. 需不需要 `visited`
5. 是否要按层处理
6. 递归函数到底返回什么

---

## 七、最常见错误

- 把网格题当普通二维遍历，忘了它本质上是图
- 无向图只加单向边
- BFS 没分层，导致步数不准
- DFS 没标记访问，导致重复搜索
- 拓扑排序边方向写反
- 递归返回值设计不清楚

---

## 八、一句话速记

- `DFS`：把一个连通块彻底搜干净
- `BFS`：一层一层往外扩，天然适合最短步数
- `多源 BFS`：多个起点同时扩散
- `拓扑排序`：谁入度为 0，谁先做

---

## 九、建议下一步

最好的继续方式是：

1. 先手写一遍 `Number of Islands`
2. 再手写一遍 `Rotting Oranges`
3. 再手写一遍 `Course Schedule`

因为这三题分别对应：

- 连通块 DFS
- 多源 BFS
- 拓扑排序

这三个打通之后，图题主干就出来了。

---

## Quiz

**Q1: 网格 DFS 染色时，访问过的格子应该怎么处理？**

- [ ] 不处理，让递归自然结束
- [ ] 标记为 -1 或修改值，避免重复访问 ✅
- [ ] 存入 visited 字典
- [ ] 删除该格子

**Q2: BFS 和 DFS 的主要区别在于？**

- [ ] BFS 用递归，DFS 用迭代
- [ ] BFS 用队列按层扩展，DFS 用栈（或递归）深入搜索 ✅
- [ ] BFS 只能用于树，DFS 只能用于图
- [ ] BFS 空间更小

**Q3: 拓扑排序的应用场景是什么？**

- [ ] 求最短路径
- [ ] 找最大连通分量
- [ ] 检测有向图中的依赖顺序 / 是否有环 ✅
- [ ] 求最小生成树

**Q4: 多源 BFS（Multi-source BFS）的初始化方式是什么？**

- [ ] 从一个起点开始
- [ ] 把所有源节点同时加入队列 ✅
- [ ] 从终点往回搜索
- [ ] 用 DFS 代替

**Q5: `Number of Islands` 时间复杂度是多少（m×n 网格）？**

- [ ] O(m + n)
- [ ] O(m × n × log(mn))
- [ ] O(m × n) ✅
- [ ] O((m × n)²)
