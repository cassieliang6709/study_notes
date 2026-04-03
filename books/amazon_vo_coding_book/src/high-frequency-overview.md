# 高频题型总表

## 最值得优先刷的模板顺序

1. `Graph topo`
2. `Grid BFS/DFS`
3. `Heap merge / Top K`
4. `Stack calculator`
5. `Sliding window`
6. `HashSet longest consecutive`
7. `Spiral / matrix simulation`
8. `Intervals`
9. `Linked list basics`
10. `Ordered map / binary search`

## 10 类高频题型

| 题型 | 识别信号 | 标准模板 |
| --- | --- | --- |
| 图论拓扑排序 | 依赖、先做 A 才能做 B、顺序、能否完成 | 邻接表 + 入度 + Kahn / DFS 染色 |
| 矩阵搜索 / 岛屿 / 最短路 | grid、障碍、最少步数、区域数、扩散 | BFS / DFS / 多源 BFS |
| 堆 / 多路归并 | 多个有序流、Top K、K closest | min-heap / size-k heap |
| 栈 / 表达式解析 | 括号、嵌套、作用域、命令块 | stack 保存上下文 |
| HashSet / HashMap | 查存在、频率、分组、最长连续 | set / map / Counter |
| 双指针 / 滑窗 | 连续区间、最长、最短、至多 K | left/right + while 收缩 |
| 矩阵遍历模拟 | 顺时针、逆时针、一圈圈 | 四边界收缩 |
| 区间 / 扫描线 | [start, end]、冲突、并发峰值 | 排序 + merge / heap / sweep line |
| 链表基础操作 | node.next、原地反转、中点、环 | dummy + 三指针 + 快慢指针 |
| 有序映射 / TreeMap | floor / ceiling、前驱后继、历史生效值 | TreeMap / 排序 + 二分 |

## Amazon VO 里最常见的业务伪装

- workflow / dependency / pipeline -> 拓扑排序
- warehouse robot / obstacle / route -> Grid BFS
- event stream / top products -> 堆
- pricing rule / nested config / logs -> 栈
- inventory / dedupe / frequency -> Hash
- time window / user behavior -> 滑窗
- loading dock / meeting room / station -> 区间
- linked sequence of tasks -> 链表
- latest valid price before timestamp -> ordered map

## 面试现场通用拆题口诀

1. 这是图、区间、网格，还是字符串？
2. 问的是存在、最短、最大、顺序，还是个数？
3. 业务词能不能换成 node、edge、grid、interval、stream？
4. 我最熟的模板里，哪个能一把套上去？

