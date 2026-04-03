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

```text
// 遇到陆地就把整块染掉
```

### Max Area of Island

```text
// DFS 返回面积
```

### Word Search

```text
// 矩阵 DFS + 回溯
```

### Course Schedule / II

```text
// 拓扑排序
```

### Clone Graph

```text
// 图复制 = 老节点到新节点映射
```

### Word Ladder

```text
// BFS 找最短层数
```

### Accounts Merge

```text
// 图连通块 / 并查集
```

### Alien Dictionary

```text
// 构图 + 拓扑排序
```

---

## 建议顺序

1. Number of Islands
2. Max Area of Island
3. Word Search
4. Is Graph Bipartite?
5. Course Schedule
6. Course Schedule II
7. Clone Graph
8. Pacific Atlantic Water Flow
9. Walls and Gates
10. Word Ladder
11. Accounts Merge
12. Alien Dictionary
13. Word Search II


---

## Quiz

**Q1: `Word Ladder` 为什么用 BFS 而不是 DFS？**

- [ ] BFS 代码更短
- [ ] BFS 保证第一次到达终点时路径最短 ✅
- [ ] DFS 会栈溢出
- [ ] BFS 空间复杂度更低

**Q2: `Course Schedule`（判断是否能完成所有课程）本质上是什么问题？**

- [ ] 最短路径
- [ ] 有向图的环检测 ✅
- [ ] 连通分量
- [ ] 最小生成树

**Q3: 拓扑排序 Kahn's 算法的核心是什么？**

- [ ] 每次 DFS 到最深节点
- [ ] 维护入度数组，反复取出入度为 0 的节点 ✅
- [ ] 用 BFS 按层遍历所有节点
- [ ] 用并查集合并节点

**Q4: `Accounts Merge` 使用并查集（Union-Find）解，合并的依据是什么？**

- [ ] 账户名相同就合并
- [ ] 同一个账户里出现的邮箱都属于同一个 component，用邮箱作为 key 合并 ✅
- [ ] 用 BFS 找连通节点
- [ ] 按字母序排序后合并

**Q5: 二部图（Bipartite Graph）检测的方法是什么？**

- [ ] 判断是否有环
- [ ] 用 BFS/DFS 染色，相邻节点颜色不同；若出现同色相邻则不是二部图 ✅
- [ ] 判断节点数是否为偶数
- [ ] 用拓扑排序
