---
title: "09 堆、设计、区间与杂项详细教学"
---

# 09 堆、设计、区间与杂项详细教学

这组题跨度很大，所以最重要的不是把它们混着刷，而是先判断每题最像哪个主模板。

## 这个题型 / 算法点的总结

这一页其实包含四组完全不同的能力：

- 堆 / Top K
- 设计类数据结构
- 区间题
- 数学与杂项

真正容易丢分的点，不是某个公式忘了，而是把不同题型混在一起，导致第一反应就走错方向。

## 示例 case

- 场景：看到 `Top K Frequent Elements`
- 目标：应该优先想到“频次统计 + 小根堆”或“桶排序”，而不是先整体排序
- 为什么：这正是这页想训练的模式识别能力

---

## 一、堆 / Top K

### 识别信号

```text
// top k
// 优先弹出最值
// 数据流
```

### 代表题

- Kth Largest Element in an Array
- K Closest Points to Origin
- Top K Frequent Elements
- Top K Frequent Words
- Reorganize String
- Find Median from Data Stream

---

## 二、设计类

### 核心方法

```text
// 先列操作
// 再列复杂度目标
// 再决定组合数据结构
```

### 代表题

- LRU Cache
- Insert Delete GetRandom O(1)
- Implement Trie
- Add and Search Word
- Design Tic-Tac-Toe
- Binary Search Tree Iterator

---

## 三、区间

### 核心原则

```text
// 区间题通常先排序
```

### 代表题

- Merge Intervals
- Insert Interval
- Meeting Rooms II

---

## 四、数学与杂项

### 代表题

- Pow(x, n)
- Divide Two Integers
- Rotate Image
- Spiral Matrix
- Set Matrix Zeroes
- String to Integer (atoi)
- Roman to Integer
- First Missing Positive
- Longest Consecutive Sequence
- Task Scheduler
- Sudoku Solver

### 提醒

```text
// 杂项题不要混刷
// 每题都要先识别它最像哪个主模板
```

---

## 五、建议顺序

1. Kth Largest Element in an Array
2. Top K Frequent Elements
3. Implement Trie
4. Binary Search Tree Iterator
5. Insert Delete GetRandom O(1)
6. LRU Cache
7. Merge Intervals
8. Insert Interval
9. Meeting Rooms II
10. Rotate Image
11. Spiral Matrix
12. Set Matrix Zeroes
13. Roman to Integer
14. String to Integer (atoi)
15. Longest Consecutive Sequence
16. First Missing Positive
17. Pow(x, n)
18. Task Scheduler
19. Sudoku Solver


---

## Quiz

**Q1: `LRU Cache` 的数据结构组合是什么，为什么？**

- [ ] 数组 + 排序
- [ ] 哈希表 + 双向链表：O(1) 访问 + O(1) 移动节点到头部 ✅
- [ ] 单链表 + 哈希表
- [ ] 优先队列

**Q2: 合并区间（Merge Intervals）的第一步是什么？**

- [ ] 直接遍历合并
- [ ] 按区间起点排序 ✅
- [ ] 找最大终点
- [ ] 用堆维护

**Q3: `Find Median from Data Stream` 为什么用两个堆而不是一个排序数组？**

- [ ] 两个堆更省空间
- [ ] 每次插入 O(log n)，取中位数 O(1)；排序数组插入 O(n) ✅
- [ ] 堆能保证元素唯一
- [ ] 数组无法求中位数

**Q4: 区间调度问题（最多不重叠区间数）的贪心策略是什么？**

- [ ] 按起点最早排序，依次选
- [ ] 按终点最早排序，依次选不重叠的区间 ✅
- [ ] 选最短的区间
- [ ] 动态规划

**Q5: `Insert Interval` 插入一个新区间后，与现有区间重叠的判断条件是什么？**

- [ ] `new.start <= existing.end`
- [ ] `new.start <= existing.end AND new.end >= existing.start` ✅
- [ ] `new.start == existing.start`
- [ ] `new.end >= existing.start`
