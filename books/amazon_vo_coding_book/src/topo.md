# 1. 图论拓扑排序

## 面试题目怎么问

- 有 `numCourses` 门课，`prerequisites[i] = [a, b]` 表示学 `a` 之前必须先学 `b`，问是否能学完所有课
- 如果可以学完，输出一种可行的上课顺序
- 给你若干任务和依赖关系，判断有没有环

## 识别信号

- 任务之间有依赖关系
- 出现 “先做 A 才能做 B”
- 问是否有环
- 问能否完成全部任务
- 问输出一个合法顺序

## Amazon 风格业务包装

- fulfillment workflow 里，某些任务必须先做完才能做后续任务
- deployment pipeline 里，某些服务必须先启动依赖服务
- package processing system 里，某些步骤存在前置依赖
- training modules 之间有先修顺序

## 你该怎么想

- “A 依赖 B” 就翻译成有向边 `B -> A`
- 问能不能做完，就是判环
- 问执行顺序，就是拓扑排序

## 标准代码模板 1：BFS Kahn 拓扑排序

```python
from collections import defaultdict, deque

def topo_sort(n, edges):
    graph = defaultdict(list)
    indegree = [0] * n

    for nxt, pre in edges:
        graph[pre].append(nxt)
        indegree[nxt] += 1

    q = deque([i for i in range(n) if indegree[i] == 0])
    order = []

    while q:
        cur = q.popleft()
        order.append(cur)
        for nei in graph[cur]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    return len(order) == n, order
```

## 标准代码模板 2：DFS 染色判环

```python
from collections import defaultdict

def has_cycle(n, edges):
    graph = defaultdict(list)
    for nxt, pre in edges:
        graph[pre].append(nxt)

    color = [0] * n
    # 0 = 未访问, 1 = 正在访问, 2 = 已完成

    def dfs(node):
        if color[node] == 1:
            return True
        if color[node] == 2:
            return False

        color[node] = 1
        for nei in graph[node]:
            if dfs(nei):
                return True
        color[node] = 2
        return False

    for i in range(n):
        if color[i] == 0 and dfs(i):
            return True
    return False
```

## 标准代码模板 3：字典序最小拓扑序

```python
import heapq
from collections import defaultdict

def topo_smallest(n, edges):
    graph = defaultdict(list)
    indegree = [0] * n

    for nxt, pre in edges:
        graph[pre].append(nxt)
        indegree[nxt] += 1

    heap = []
    for i in range(n):
        if indegree[i] == 0:
            heapq.heappush(heap, i)

    order = []
    while heap:
        cur = heapq.heappop(heap)
        order.append(cur)
        for nei in graph[cur]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                heapq.heappush(heap, nei)

    return order if len(order) == n else []
```

## 标准代码模板 4：DFS 返回拓扑序

```python
from collections import defaultdict

def topo_dfs(n, edges):
    graph = defaultdict(list)
    for nxt, pre in edges:
        graph[pre].append(nxt)

    color = [0] * n
    order = []

    def dfs(node):
        if color[node] == 1:
            return False
        if color[node] == 2:
            return True

        color[node] = 1
        for nei in graph[node]:
            if not dfs(nei):
                return False
        color[node] = 2
        order.append(node)
        return True

    for i in range(n):
        if color[i] == 0:
            if not dfs(i):
                return []

    return order[::-1]
```

## 代码讲解

- Kahn 的核心是“入度为 0 的节点就是当前可以做的任务”
- DFS 染色的核心是“再次碰到正在访问的节点，就说明出现回边，也就是有环”
- DFS 返回列表时，使用“后序加入 + reverse”

## 面试时怎么讲

- 这是一个有向图判环 / 拓扑排序问题
- 如果图里有环，就不可能完成所有任务
- 我会先建邻接表和入度数组
- 入度为 0 的节点先入队，逐步解锁后续任务

## 常见 follow-up 和回答

**Q1：如果只需要判断能不能完成，不需要顺序呢？**  
还是同一个模板，最后检查处理过的节点数是否等于总节点数。

**Q2：如果需要返回任意一个合法顺序呢？**  
在 BFS 过程中把出队顺序记录到 `order` 数组里。

**Q3：如果有多个合法顺序怎么办？**  
普通拓扑排序返回任意一个即可；如果要字典序最小，改成最小堆。

**Q4：如果图不连通怎么办？**  
没关系，所有入度为 0 的节点都会进队。

**Q5：DFS 和 BFS 该怎么选？**  
只判环时两者都行；要输出顺序时，BFS Kahn 通常更直观。

**Q6：DFS 也能返回列表吗？**  
能。后序加入 `order`，最后 `reverse`。

## Amazon 风格完整题面

> You are given a list of tasks in a fulfillment workflow.  
> Some tasks depend on other tasks being completed first.  
> Determine whether all tasks can be completed.  
> If yes, return one valid execution order.

## 可直接背的口语回答稿

“我先把业务任务抽象成有向图。每个任务是一个节点，如果 task A 依赖 task B，我就建一条 `B -> A` 的边。这样问题就变成判断图里是否有环；如果无环，再输出一个拓扑序。我会优先用 Kahn 算法，维护每个节点的入度，把所有入度为 0 的任务先放进队列。每完成一个任务，就把它后继节点的入度减一。最后如果能处理完所有节点，就说明没有环，出队顺序也是一种合法的执行顺序。”

## 推荐代表题

- Course Schedule
- Course Schedule II
- Alien Dictionary

