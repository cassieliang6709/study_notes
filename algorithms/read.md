---
title: "二分答案模板"
---

灵神风格算法框架 — 适用场景 + 复杂度 + DFS/BFS方向数组

🧠 灵神核心方法论
灵神最强调的几点：
1. 想清楚「枚举什么」，而不是套模板
2. 对于 DP：先想「选/不选」还是「枚举选哪个」
3. 对于图/网格：方向数组 + 边界判断 是核心基础设施
4. 复杂度分析要精确，不能"感觉是O(n)"
5. 写代码前先想好状态定义，不要边写边改

一、各算法适用场景 + 精确复杂度

🔷 前缀和
适用场景：
  - 静态数组，反复查询区间和
  - 子数组和等于 k（配合 HashMap）
  - 二维矩阵区域和

不适用：数组会被修改（用树状数组/线段树）

时间：预处理 O(n)，查询 O(1)
空间：O(n)

灵神强调：
  prefix[0] = 0 这个哨兵是关键
  区间 [l,r] 的和 = prefix[r+1] - prefix[l]
  下标永远差 1，记住这个偏移
python# 灵神风格：简洁，不废话
def prefix_sum(nums):
    n = len(nums)
    pre = [0] * (n + 1)
    for i, x in enumerate(nums):
        pre[i + 1] = pre[i] + x
    # query [l, r]: pre[r+1] - pre[l]
    return pre
```

---

### 🔷 差分数组
```
适用场景：
  - 大量区间修改，最后一次性查询结果
  - 公交车乘客数量、会议室占用
  - 区间覆盖计数

时间：每次更新 O(1)，还原 O(n)
空间：O(n)

灵神强调：
  差分是前缀和的逆运算
  diff[l] += val, diff[r+1] -= val
  对 diff 做前缀和 = 还原结果
pythondef apply_ops(n, ops):
    diff = [0] * (n + 1)          # n+1 防越界
    for l, r, val in ops:
        diff[l] += val
        diff[r + 1] -= val
    # 还原
    for i in range(1, n):
        diff[i] += diff[i - 1]
    return diff[:n]
```

---

### 🔷 滑动窗口
```
适用场景：
  - 连续子数组/子串
  - 最长/最短满足条件的窗口
  - 不含重复字符、最多k个不同字符

关键判断：窗口收缩条件必须是"单调"的
  即：窗口变大，合法性只会变好或只会变差（二选一）
  如果两边都可能，滑窗失效，要用其他方法

时间：O(n)，每个元素进出窗口各一次
空间：O(k)，k 是窗口内状态大小
python# 灵神风格：最长合法窗口
def sliding_window(s, k):
    cnt = {}
    left = res = 0
    for right, c in enumerate(s):
        cnt[c] = cnt.get(c, 0) + 1
        while len(cnt) > k:             # 不合法就收缩
            x = s[left]
            cnt[x] -= 1
            if cnt[x] == 0:
                del cnt[x]
            left += 1
        res = max(res, right - left + 1)
    return res
```

---

### 🔷 二分搜索
```
适用场景（灵神分类）：
  类型1 - 搜索具体值：有序数组找target
  类型2 - 搜索左/右边界：第一个/最后一个满足条件的位置
  类型3 - 二分答案：答案有单调性，可以对答案二分

灵神核心口诀：
  "看到有序，想二分"
  "看到最小化最大值/最大化最小值，必是二分答案"
  "feasible(mid) 为 True 时，答案在 [lo, mid]"

时间：O(log n)
空间：O(1)
python# 灵神最推崇的统一写法：左闭右开
def lower_bound(nums, target):
    """找第一个 >= target 的位置"""
    lo, hi = 0, len(nums)           # 右边开区间
    while lo < hi:                  # 终止：lo == hi
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid                # 不是 mid-1
    return lo                       # lo 就是答案

# 二分答案模板
def binary_answer(lo, hi, feasible):
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid                # 答案可以更小
        else:
            lo = mid + 1
    return lo
```

---

### 🔷 单调栈
```
适用场景：
  - 下一个更大/更小元素（Next Greater Element）
  - 柱状图中最大矩形
  - 接雨水
  - 去除重复字母（字典序最小）

核心思想（灵神强调）：
  "当前元素让栈顶元素找到了答案"
  维护一个单调递增/递减的栈
  元素入栈前把比它大/小的全弹出

时间：O(n)，每个元素入栈出栈各一次
空间：O(n)
python# 找每个元素右边第一个更大的
def next_greater(nums):
    n = len(nums)
    ans = [-1] * n
    stk = []                       # 存下标

    for i, x in enumerate(nums):
        while stk and nums[stk[-1]] < x:
            j = stk.pop()
            ans[j] = x             # x 是 j 的答案
        stk.append(i)
    return ans
```

---

### 🔷 回溯 (Backtracking)
```
适用场景：
  - 所有组合/排列/子集
  - N 皇后、数独
  - 单词搜索（网格DFS）

灵神分类（重要）：
  子集型：每个元素选/不选
  组合型：选 k 个，有顺序无所谓（用 start 指针）
  排列型：全排列，元素有顺序之分（用 used 数组）

时间：指数级，组合 O(2^n)，排列 O(n!)
空间：O(n) 递归栈

灵神强调：
  "答案加到 res 的时机"决定是子集还是组合
  剪枝要在 for 循环里做，不是在递归里
python# 灵神风格：子集型（每个元素选/不选）
def subsets(nums):
    res, path = [], []

    def dfs(i):
        if i == len(nums):
            res.append(path[:])    # 到底了才收集
            return
        # 不选 nums[i]
        dfs(i + 1)
        # 选 nums[i]
        path.append(nums[i])
        dfs(i + 1)
        path.pop()

    dfs(0)
    return res

# 组合型（从 start 开始选）
def combine(nums, k):
    res, path = [], []
    n = len(nums)

    def dfs(start):
        if len(path) == k:
            res.append(path[:])
            return
        # 剪枝：剩余元素不够了就停
        for i in range(start, n - (k - len(path)) + 1):
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

    dfs(0)
    return res
```

---

### 🔷 动态规划 (DP)
```
适用场景：
  - 最优子结构 + 重叠子问题
  - 计数、最值、是否可行

灵神分类（最清晰）：
  线性DP：爬楼梯、打家劫舍、最长递增子序列
  区间DP：矩阵链乘、回文子串、戳气球
  树形DP：打家劫舍III、树的最大独立集
  状态机DP：买卖股票（有/无持股状态）
  背包DP：0/1背包、完全背包、分组背包
  数位DP：满足某条件的数字个数

灵神最强调：
  "先想状态定义，定义清楚了转移自然出来"
  "状态压缩：二维DP能不能滚动数组优化到一维"

时间/空间：
  线性DP  O(n)   /  O(n) → O(1)（空间优化后）
  二维DP  O(mn)  /  O(mn) → O(n)（滚动数组）
  区间DP  O(n²)  /  O(n²)
  背包    O(nW)  /  O(W)
python# 状态机DP：买卖股票（灵神最爱的例子）
def max_profit(prices):
    # 状态：持股 / 不持股
    hold = -float('inf')           # 持股状态（初始不可能）
    empty = 0                      # 不持股状态

    for p in prices:
        hold = max(hold, empty - p)    # 买入
        empty = max(empty, hold + p)   # 卖出
    return empty

# LIS 最长递增子序列（O(n log n) 二分优化版）
def length_of_LIS(nums):
    tails = []                     # tails[i] = 长度i+1的子序列末尾最小值
    for x in nums:
        import bisect
        pos = bisect.bisect_left(tails, x)
        if pos == len(tails):
            tails.append(x)
        else:
            tails[pos] = x
    return len(tails)

二、DFS / BFS + 方向数组（灵神核心基础设施）
灵神在所有网格/图题中都用这套统一结构，不要每道题重新想方向。

🔷 方向数组定义（统一规范）
python# ✅ 四方向（上下左右）
DIRS4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# ✅ 八方向（含斜角，用于国际象棋/单词搜索）
DIRS8 = [(-1,-1),(-1,0),(-1,1),
         ( 0,-1),        (0,1),
         ( 1,-1),( 1,0),( 1,1)]

# ✅ 骑士跳（马步，L型）
KNIGHT = [(-2,-1),(-2,1),(-1,-2),(-1,2),
          ( 1,-2),( 1,2),( 2,-1),( 2,1)]

# ✅ 通用边界判断（做成函数复用）
def in_bounds(r, c, m, n):
    return 0 <= r < m and 0 <= c < n
```

---

### 🔷 网格 DFS 模板（灵神风格）
```
适用场景：
  - 岛屿数量/面积/周长
  - 路径是否存在
  - 连通分量染色
  - 单词搜索（Word Search）

时间：O(m × n)，每个格子访问常数次
空间：O(m × n)，递归栈最坏情况
pythondef dfs_grid(grid):
    m, n = len(grid), len(grid[0])
    DIRS = [(-1,0),(1,0),(0,-1),(0,1)]

    def dfs(r, c):
        # 边界 + 已访问/障碍 判断
        if not (0 <= r < m and 0 <= c < n):
            return
        if grid[r][c] != '1':       # 已访问或水域
            return

        grid[r][c] = '0'            # 标记已访问（原地修改省空间）

        for dr, dc in DIRS:
            dfs(r + dr, c + dc)

    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count
```

---

### 🔷 网格 BFS 模板（灵神风格）
```
适用场景：
  - 最短路径（无权图/等权图必用BFS）
  - 多源BFS（同时从多个起点扩散）
  - 01 BFS（边权只有0或1，用双端队列）

BFS vs DFS 选择原则（灵神强调）：
  "问最短/最少步数 → BFS"
  "问是否存在/所有路径 → DFS/回溯"
  "BFS天然保证第一次到达就是最短"

时间：O(m × n)
空间：O(m × n)，队列最大存整个边界
pythonfrom collections import deque

def bfs_grid(grid, start_r, start_c):
    m, n = len(grid), len(grid[0])
    DIRS = [(-1,0),(1,0),(0,-1),(0,1)]

    queue = deque([(start_r, start_c, 0)])  # (行, 列, 步数)
    visited = [[False] * n for _ in range(m)]
    visited[start_r][start_c] = True

    while queue:
        r, c, step = queue.popleft()

        # 到达终点
        if grid[r][c] == 'E':
            return step

        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if (0 <= nr < m and 0 <= nc < n
                    and not visited[nr][nc]
                    and grid[nr][nc] != '#'):   # '#' 是墙
                visited[nr][nc] = True          # 入队时就标记！
                queue.append((nr, nc, step + 1))

    return -1  # 不可达
```

**⚠️ 灵神强调的 BFS 最常见 Bug：**
```
visited 要在「入队时」标记，不是「出队时」
出队时标记会导致同一个节点被入队多次 → TLE
```

---

### 🔷 多源 BFS（灵神常用技巧）
```
适用场景：
  - 从所有 '1' 同时出发找最近的 '0'
  - 腐烂的橘子（994题）
  - 地图中所有陆地到海洋的最远距离

核心思想：
  把所有起点一次性放入队列
  等价于"虚拟超级源点"同时向外扩散
pythondef multi_source_bfs(grid):
    m, n = len(grid), len(grid[0])
    DIRS = [(-1,0),(1,0),(0,-1),(0,1)]

    queue = deque()
    dist = [[-1] * n for _ in range(m)]

    # 所有源点一起入队
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:     # 源点条件
                queue.append((i, j))
                dist[i][j] = 0

    while queue:
        r, c = queue.popleft()
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if (0 <= nr < m and 0 <= nc < n
                    and dist[nr][nc] == -1):   # -1 表示未访问
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

    return dist
```

---

### 🔷 一般图 DFS（非网格，灵神风格）
```
适用场景：
  - 连通分量
  - 拓扑排序（检测环）
  - 二分图判断

时间：O(V + E)
空间：O(V)
pythondef dfs_graph(graph, n):
    visited = [False] * n
    DIRS = None  # 图用邻接表，不用方向数组

    def dfs(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs(v)

    components = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            components += 1
    return components
```

---

### 🔷 拓扑排序 BFS（Kahn 算法）
```
适用场景：
  - 课程安排（有向无环图）
  - 任务依赖顺序
  - 检测有向图中是否有环

时间：O(V + E)
空间：O(V)
pythondef topo_sort(n, prerequisites):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    in_degree = [0] * n

    for u, v in prerequisites:
        graph[v].append(u)
        in_degree[u] += 1

    queue = deque(i for i in range(n) if in_degree[i] == 0)
    order = []

    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return order if len(order) == n else []  # 长度不等说明有环
```

---

## 三、复杂度速查（灵神风格精简版）
```
算法                时间复杂度         空间复杂度      何时用
─────────────────────────────────────────────────────────────────
前缀和              O(n) 预处理         O(n)          静态区间查询
差分数组            O(n) 还原           O(n)          批量区间修改
滑动窗口            O(n)                O(k)          连续子数组条件
二分搜索            O(log n)            O(1)          有序 or 答案单调
单调栈/队列         O(n)                O(n)          NGE/维护区间极值
回溯（组合）        O(2^n)              O(n)          枚举所有方案
回溯（排列）        O(n!)               O(n)          全排列
线性DP              O(n)                O(1)*         最优子结构
区间DP              O(n²)~O(n³)         O(n²)         区间合并
背包DP              O(nW)               O(W)*         选不选问题
网格DFS/BFS         O(mn)               O(mn)         连通/最短路
图DFS/BFS           O(V+E)              O(V)          连通分量/最短路
Dijkstra            O((V+E)log V)       O(V)          带权最短路
拓扑排序            O(V+E)              O(V)          有向无环图排序
堆 Top-K            O(n log k)          O(k)          第K大/小

* 表示空间优化后
```

---

## 四、看题时的 High-Level 决策树（灵神思路）
```
读完题后问自己：

Q1: 数据有序吗？
  → 是 → 考虑二分

Q2: 要找连续子数组/子串？
  → 是 → 考虑滑窗 or 前缀和+哈希

Q3: 要找所有方案？
  → 是 → 回溯

Q4: 要找最优解（最大/最小/计数）？
  → 考虑 DP，想状态定义

Q5: 是图/网格，问最短路？
  → 无权 → BFS
  → 带权 → Dijkstra

Q6: 是图/网格，问连通/路径存在？
  → DFS + visited

Q7: 维护某个区间的最大/最小？
  → 单调栈/单调队列

Q8: 数据范围 n ≤ 20？
  → 状态压缩DP or 回溯都行
  n ≤ 1000 → O(n²) 可以
  n ≤ 10^5 → 需要 O(n log n) 或 O(n)
  n ≤ 10^9 → 必须 O(log n) 或数学公式