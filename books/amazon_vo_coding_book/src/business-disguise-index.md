# 附录：业务伪装索引

这一章不是按算法分类，而是按 Amazon 题面里常见的业务词来反查原题类型。

## workflow / dependency / pipeline

- 对应题型：图论拓扑排序
- 你该怎么翻译：
  - task = 节点
  - depends on = 有向边
  - can finish = 判环
  - execution order = 拓扑序

## warehouse robot / route / obstacle

- 对应题型：Grid BFS / DFS
- 你该怎么翻译：
  - warehouse map = grid
  - robot moves one step = 无权图最短路
  - blocked cell = 障碍物
  - isolated region = 连通块

## event stream / sorted feeds / earliest event

- 对应题型：堆 / 多路归并
- 你该怎么翻译：
  - multiple sorted streams = merge k sorted
  - earliest event = min-heap

## top products / hot items / most popular

- 对应题型：Top K / Hash + Heap
- 你该怎么翻译：
  - frequency analytics = Counter
  - top sellers = Top K

## pricing rule / discount expression / nested config / logs

- 对应题型：栈 / 表达式解析
- 你该怎么翻译：
  - expression = 表达式求值
  - nested config = 栈保存上下文
  - start/end logs = 调用栈

## inventory / dedupe / user status map

- 对应题型：HashSet / HashMap
- 你该怎么翻译：
  - quick lookup = set
  - frequency = Counter
  - user -> status = map

## time window / user behavior / continuous range

- 对应题型：滑动窗口
- 你该怎么翻译：
  - contiguous range = 子数组 / 子串
  - at most K types = 滑窗合法条件

## loading dock / station scheduling / time slots

- 对应题型：区间 / 扫描线
- 你该怎么翻译：
  - time slot = interval
  - number of docks / stations needed = Meeting Rooms II
  - max concurrent jobs = 扫描线

## linked sequence of tasks

- 对应题型：链表
- 你该怎么翻译：
  - node.next = 链表
  - reorder in place = 指针操作

## latest valid price before t / first station after x

- 对应题型：有序映射 / 二分
- 你该怎么翻译：
  - latest valid before `t` = floor
  - first not smaller than `x` = ceiling

