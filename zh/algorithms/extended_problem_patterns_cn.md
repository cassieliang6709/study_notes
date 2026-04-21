---
title: "扩展题单 Pattern 分类汇总（中文版）"
---

# 扩展题单 Pattern 分类汇总（中文版）

> 目标：把你这份更大的题单重新按 pattern 汇总，方便刷题时按“题型”而不是按题名记忆  
> 使用方法：先判断题目属于哪个 pattern，再从该组里按顺序推进

---

## 这个题型 / 算法点的总结

这份扩展题单的重点，是让你面对更大的题库时，依然按“题型”而不是按“题名”去组织知识。真正需要记住的不是长长的问题清单，而是每道题背后的识别信号：哈希、双指针、滑动窗口、二分、递归、图搜索、堆、动态规划。

## 题目含义

这页不是单独一道题，而是一个更大的 pattern 分类入口。为了让这页本身也能直接学习，下面用代表题 `Longest Substring Without Repeating Characters` 演示：怎么从“连续子串 + 不能重复”立刻想到滑动窗口。

## Python 代码

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen: dict[str, int] = {}
        best = 0

        for right, ch in enumerate(s):
            if ch in seen and seen[ch] >= left:
                left = seen[ch] + 1
            seen[ch] = right
            best = max(best, right - left + 1)

        return best


print(Solution().lengthOfLongestSubstring('abcabcbb'))
```

## 时间复杂度

每个字符最多被窗口左右边界处理常数次，所以时间复杂度是 `O(n)`。

## 空间复杂度

哈希表要记录字符最后一次出现位置，所以空间复杂度是 `O(min(n, 字符集大小))`。

## 怎么想到

看到“最长子串”“连续区间”“满足某个限制条件”这几个词时，就要先警觉滑动窗口。因为题目要的不是离散选择，而是一段连续范围，并且这段范围的合法性会随着左右边界变化。这时最自然的做法就是：右边界不断扩张，窗口不合法时左边界再收缩。

## 示例 case

输入：`s = "abcabcbb"`
输出：`3`
解释：最长的不重复子串可以是 `"abc"`、`"bca"` 或 `"cab"`。

边界 case：如果输入是 `"bbbbb"`，答案是 `1`，因为窗口里不能同时保留两个相同字符。

## 常见 Follow-up

- 如果题目改成“最多包含 k 个不同字符”，窗口里该维护什么状态？
- 哪些连续区间题适合滑动窗口，哪些反而更适合前缀和或动态规划？
- 如果题目不再要求连续子串，而是子序列，为什么通常要换思路？

## 一、总学习顺序

建议按这个顺序刷：

1. 数组、双指针、滑动窗口
2. 二分查找
3. 链表
4. 树与递归
5. DFS / 回溯
6. BFS / 图
7. 栈与队列
8. 动态规划
9. 堆与 Top K
10. 设计类
11. 区间、数学及其他

原因：

```text
// 前面先建立基础操作和识别能力
// 中间建立树图回溯模板
// 后面再做 DP、设计和综合题
```

---

## 二、数组、双指针与滑动窗口

### 识别信号

```text
// 补数、频率、查重 -> 哈希
// 左右夹逼、有序数组、三元组 -> 双指针
// 连续子串 / 子数组、最长最短区间 -> 滑动窗口
// 原地修改、保持相对顺序 -> 快慢指针
```

### 核心子类

#### 1. 哈希 / 基础数组

- Two Sum
- Group Anagrams
- Intersection of Two Arrays
- Intersection of Two Arrays II
- Single Number
- Find All Duplicates in an Array
- Find the Duplicate Number

关键：

```text
// 用 dict / set 换时间
// 先查再存
```

#### 2. 原地数组操作

- Move Zeroes
- Sort Colors
- Merge Sorted Array
- String Compression
- Next Permutation

关键：

```text
// 边界指针含义必须非常清楚
// 哪一段已经处理好了，是这类题的核心
```

#### 3. 双指针

- 3Sum
- 3Sum Closest
- Container With Most Water
- Squares of a Sorted Array
- Reverse String
- Valid Anagram

关键：

```text
// 排序后固定一个数，再缩两边
// 或左右夹逼
```

#### 4. 滑动窗口

- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Longest Substring with At Most K Distinct Characters
- Max Consecutive Ones III
- Permutation in String
- Sliding Window Maximum

关键：

```text
// 扩张窗口
// 直到不合法
// 再收缩到合法
```

### 推荐顺序

1. Two Sum
2. Move Zeroes
3. Valid Anagram
4. Reverse String
5. Group Anagrams
6. Intersection of Two Arrays
7. Product of Array Except Self
8. Sort Colors
9. Merge Sorted Array
10. Container With Most Water
11. 3Sum
12. Longest Substring Without Repeating Characters
13. Permutation in String
14. Minimum Window Substring
15. Sliding Window Maximum
16. Next Permutation
17. Find the Duplicate Number

---

## 三、二分查找

### 识别信号

```text
// 有序
// 旋转数组
// 第一个 / 最后一个
// 单调条件
// 找最小满足条件的值
```

### 基础二分

- Search in Rotated Sorted Array
- Find First and Last Position of Element in Sorted Array
- Find Peak Element
- Single Element in a Sorted Array
- Search a 2D Matrix
- Find Minimum in Rotated Sorted Array
- Search in Rotated Sorted Array II
- Search a 2D Matrix II

### 进阶二分 / 答案二分

- Random Pick with Weight
- Kth Smallest Element in a Sorted Matrix
- Median of Two Sorted Arrays
- Closest Binary Search Tree Value
- Find the Celebrity

### 推荐顺序

1. Search a 2D Matrix
2. Find First and Last Position of Element in Sorted Array
3. Search in Rotated Sorted Array
4. Find Minimum in Rotated Sorted Array
5. Find Peak Element
6. Single Element in a Sorted Array
7. Search a 2D Matrix II
8. Search in Rotated Sorted Array II
9. Kth Smallest Element in a Sorted Matrix
10. Random Pick with Weight
11. Median of Two Sorted Arrays

### 重点总结

```text
// 二分不是只能“找某个数”
// 它更本质是在利用单调性
```

---

## 四、链表

### 识别信号

```text
// 反转
// 删除倒数第 k 个
// 合并有序链表
// 随机指针
// 重排 / 局部翻转
```

### 分类

#### 1. 翻转与基础操作

- Reverse Linked List
- Reverse Linked List II
- Reorder List
- Remove Nth Node From End of List

#### 2. 合并与计算

- Add Two Numbers
- Add Two Numbers II
- Merge Two Sorted Lists
- Merge k Sorted Lists
- Sort List

#### 3. 特殊结构

- Intersection of Two Linked Lists
- Copy List with Random Pointer

### 推荐顺序

1. Reverse Linked List
2. Merge Two Sorted Lists
3. Remove Nth Node From End of List
4. Add Two Numbers
5. Intersection of Two Linked Lists
6. Reorder List
7. Reverse Linked List II
8. Copy List with Random Pointer
9. Sort List
10. Merge k Sorted Lists
11. Add Two Numbers II

### 重点总结

```text
// dummy
// 快慢指针
// 反转
// 合并
// 断开再接回去
```

---

## 五、树与递归

### 识别信号

```text
// 深度、高度、路径、祖先、构造、序列化
// BST 有序性质
// 每层信息
```

### 分类

#### 1. 遍历 / 视图

- Binary Tree Level Order Traversal
- Binary Tree Right Side View
- Binary Tree Vertical Order Traversal
- Vertical Order Traversal of a Binary Tree
- Find Largest Value in Each Tree Row
- Maximum Width of Binary Tree
- Populating Next Right Pointers in Each Node
- Populating Next Right Pointers in Each Node II

#### 2. 路径与和

- Binary Tree Maximum Path Sum
- Path Sum
- Path Sum II
- Path Sum III
- Sum Root to Leaf Numbers

#### 3. 性质与转换

- Symmetric Tree
- Diameter of Binary Tree
- Flatten Binary Tree to Linked List
- Construct Binary Tree from Preorder and Inorder Traversal
- Lowest Common Ancestor of a Binary Tree

#### 4. BST 与序列化

- Validate Binary Search Tree
- Lowest Common Ancestor of a Binary Search Tree
- Convert Sorted Array to Binary Search Tree
- Convert Binary Search Tree to Sorted Doubly Linked List
- Kth Smallest Element in a BST
- Range Sum of BST
- Serialize and Deserialize Binary Tree
- Serialize and Deserialize BST

### 推荐顺序

1. Symmetric Tree
2. Binary Tree Level Order Traversal
3. Binary Tree Right Side View
4. Diameter of Binary Tree
5. Path Sum
6. Path Sum II
7. Sum Root to Leaf Numbers
8. Lowest Common Ancestor of a Binary Tree
9. Flatten Binary Tree to Linked List
10. Construct Binary Tree from Preorder and Inorder Traversal
11. Validate Binary Search Tree
12. Kth Smallest Element in a BST
13. Lowest Common Ancestor of a Binary Search Tree
14. Convert Sorted Array to Binary Search Tree
15. Path Sum III
16. Binary Tree Maximum Path Sum
17. Serialize and Deserialize Binary Tree
18. Serialize and Deserialize BST

### 重点总结

```text
// 树题先选遍历方式
// 前序：构造
// 中序：BST
// 后序：子树信息
// 层序：每层视图
```

---

## 六、DFS / 回溯

### 识别信号

```text
// 所有组合
// 所有排列
// 所有合法方案
// 尝试 + 回退
```

### 题目

- Subsets
- Permutations
- Combination Sum
- Generate Parentheses
- Letter Combinations of a Phone Number
- Restore IP Addresses
- Binary Tree Paths
- Word Break II
- Partition to K Equal Sum Subsets

### 推荐顺序

1. Letter Combinations of a Phone Number
2. Subsets
3. Permutations
4. Combination Sum
5. Generate Parentheses
6. Restore IP Addresses
7. Binary Tree Paths
8. Word Break II
9. Partition to K Equal Sum Subsets

### 重点总结

```text
// path 存什么
// start 从哪开始
// used 是否需要
// 什么条件下剪枝
```

---

## 七、BFS 与图

### 识别信号

```text
// 最短路径
// 一层一层扩散
// 岛屿 / 连通块
// 依赖关系 / 拓扑排序
```

### 分类

#### 1. BFS / 最短路径

- Word Ladder
- Word Ladder II
- Walls and Gates
- Shortest Distance from All Buildings
- The Maze

#### 2. 连通分量 / 岛屿 / 搜索

- Number of Islands
- Max Area of Island
- Island Perimeter
- Battleships in a Board
- Is Graph Bipartite?
- Word Search
- Word Search II

#### 3. 拓扑排序 / 依赖

- Course Schedule
- Course Schedule II
- Alien Dictionary

#### 4. 其他图论

- Clone Graph
- Reconstruct Itinerary
- Pacific Atlantic Water Flow
- Accounts Merge
- All Nodes Distance K in Binary Tree
- Number of Connected Components in an Undirected Graph
- Minesweeper

### 推荐顺序

1. Number of Islands
2. Max Area of Island
3. Island Perimeter
4. Word Search
5. Is Graph Bipartite?
6. Course Schedule
7. Course Schedule II
8. Clone Graph
9. Walls and Gates
10. Pacific Atlantic Water Flow
11. Word Ladder
12. Word Ladder II
13. Word Search II
14. Accounts Merge
15. Alien Dictionary
16. Reconstruct Itinerary

### 重点总结

```text
// 图题先分清：
// DFS 染色
// BFS 按层
// 拓扑排序
// 并查集 / 映射图
```

---

## 八、栈与队列

### 识别信号

```text
// 括号匹配
// 表达式解析
// 单调关系
// 调用栈 / 时间片
```

### 分类

#### 1. 单调栈 / 结构栈

- Trapping Rain Water
- Longest Valid Parentheses

#### 2. 括号 / 计算器 / 解析

- Valid Parentheses
- Simplify Path
- Basic Calculator
- Basic Calculator II
- Basic Calculator III
- Decode String

#### 3. 队列 / 栈模拟

- Design Circular Queue
- Exclusive Time of Functions

### 推荐顺序

1. Valid Parentheses
2. Simplify Path
3. Decode String
4. Basic Calculator II
5. Basic Calculator
6. Longest Valid Parentheses
7. Trapping Rain Water
8. Design Circular Queue
9. Exclusive Time of Functions
10. Basic Calculator III

### 重点总结

```text
// 栈里存值还是存下标
// 弹栈时如何计算答案
// 计算器题核心是“何时结算前面的表达式”
```

---

## 九、动态规划

### 识别信号

```text
// 最优值
// 多少种方法
// 能不能组成
// 重复子问题
```

### 分类

#### 1. 序列 DP

- Climbing Stairs
- Fibonacci Number
- Best Time to Buy and Sell Stock
- Longest Increasing Subsequence
- Maximum Product Subarray
- Word Break
- Decode Ways
- Longest Palindromic Subsequence

#### 2. 路径与子数组

- Maximum Subarray
- Unique Paths
- Unique Paths II
- Subarray Sum Equals K
- Continuous Subarray Sum

#### 3. 字符串 / 匹配

- Longest Palindromic Substring
- Regular Expression Matching
- Wildcard Matching
- Longest Increasing Path in a Matrix

### 推荐顺序

1. Fibonacci Number
2. Climbing Stairs
3. Best Time to Buy and Sell Stock
4. Maximum Subarray
5. Unique Paths
6. Unique Paths II
7. Decode Ways
8. Word Break
9. Longest Increasing Subsequence
10. Maximum Product Subarray
11. Longest Palindromic Substring
12. Longest Palindromic Subsequence
13. Continuous Subarray Sum
14. Longest Increasing Path in a Matrix
15. Regular Expression Matching
16. Wildcard Matching

### 重点总结

```text
// 先定义状态
// 再写转移
// 再想初始化
// 最后决定遍历顺序
```

---

## 十、堆与 Top K

### 识别信号

```text
// top k
// 动态最大 / 最小
// 数据流
// 按优先级弹出
```

### 题目

- Kth Largest Element in an Array
- K Closest Points to Origin
- Top K Frequent Elements
- Top K Frequent Words
- Reorganize String
- Find Median from Data Stream
- Kth Largest Element in a Stream

### 推荐顺序

1. Kth Largest Element in an Array
2. K Closest Points to Origin
3. Top K Frequent Elements
4. Kth Largest Element in a Stream
5. Top K Frequent Words
6. Reorganize String
7. Find Median from Data Stream

### 重点总结

```text
// 小顶堆保留前 k 大
// 大顶堆处理最大优先
// 两个堆维护中位数
```

---

## 十一、设计类

### 识别信号

```text
// 需要设计数据结构
// 多个操作都要高效
// insert / delete / get / iterator
```

### 题目

- LRU Cache
- Insert Delete GetRandom O(1)
- Implement Trie (Prefix Tree)
- Add and Search Word - Data structure design
- Design Tic-Tac-Toe
- Binary Search Tree Iterator

### 推荐顺序

1. Implement Trie
2. Binary Search Tree Iterator
3. Design Tic-Tac-Toe
4. Insert Delete GetRandom O(1)
5. LRU Cache
6. Add and Search Word

### 重点总结

```text
// 先列操作
// 再确定每个操作复杂度目标
// 再选组合数据结构
```

---

## 十二、区间、数学及其他

### 分类

#### 1. 区间

- Merge Intervals
- Insert Interval
- Meeting Rooms II

关键：

```text
// 区间题几乎都先排序
```

#### 2. 数学与矩阵

- Pow(x, n)
- Divide Two Integers
- Rotate Image
- Spiral Matrix
- Set Matrix Zeroes

#### 3. 杂项 / 逻辑

- String to Integer (atoi)
- Roman to Integer
- First Missing Positive
- Longest Consecutive Sequence
- Palindrome Permutation
- Integer to English Words
- First Unique Character in a String
- Validate IP Address
- Task Scheduler
- Pancake Sorting
- Sudoku Solver

### 推荐顺序

1. Merge Intervals
2. Insert Interval
3. Meeting Rooms II
4. Rotate Image
5. Spiral Matrix
6. Set Matrix Zeroes
7. Roman to Integer
8. String to Integer (atoi)
9. First Unique Character in a String
10. Validate IP Address
11. Longest Consecutive Sequence
12. First Missing Positive
13. Pow(x, n)
14. Divide Two Integers
15. Task Scheduler
16. Sudoku Solver
17. Integer to English Words

### 重点总结

```text
// 这组题分散
// 不要混着刷
// 要先识别它更像哪类模板
```

---

## 十三、建议你怎么用这份题单

不要按网站顺序刷，按下面方式更有效：

### 第 1 轮：模板建立

每组先刷最基础的 3 到 5 题。

### 第 2 轮：同类强化

同一 pattern 连刷 5 到 10 题。

### 第 3 轮：综合难题

把每组最难的题拿出来集中突破。

---

## 十四、你可以这样标记题目

建议自己给每题打标签：

- `A`：看题就知道模板
- `B`：能做出来，但不稳
- `C`：不会 or 需要看题解

然后复习顺序：

1. 先清 `C`
2. 再压缩 `B`
3. 最后用 `A` 维持手感

---

## 十五、最值得优先做的核心题

如果你现在不想被题海压住，先抓这批：

- Two Sum
- Move Zeroes
- Product of Array Except Self
- 3Sum
- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Search in Rotated Sorted Array
- Reverse Linked List
- Add Two Numbers
- Binary Tree Level Order Traversal
- Lowest Common Ancestor of a Binary Tree
- Subsets
- Permutations
- Number of Islands
- Course Schedule
- Valid Parentheses
- Decode String
- Climbing Stairs
- Word Break
- Kth Largest Element in an Array
- LRU Cache
- Merge Intervals

这批覆盖了最常见模板。

---

## 十六、下一步最合理的动作

如果你要，我下一步可以继续做这两件事之一：

1. 把这份扩展题单也拆成 `详细讲义版`
2. 直接给你做一个 `刷题计划表（按周安排）`
