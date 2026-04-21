---
title: "LeetCode Top 100 刷题路线图（中文版）"
---

# LeetCode Top 100 刷题路线图（中文版）

> 目标：把 Top 100 按 pattern 刷完  
> 方法：按题型分组，按学习顺序推进，记“识别信号 + 模板 + 易错点”，不要死记题名

---

## 这个题型 / 算法点的总结

这份路线图想训练的核心能力不是“背 100 道题”，而是“先分类，再写代码”。真正高频的东西，是哈希、双指针、滑动窗口、树递归、图搜索、堆、动态规划这些 pattern 的识别信号。只要信号抓得准，很多题都会自动落到熟悉模板里。

## 题目含义

这页本身不是单题题解，而是一张刷题路线图。为了让路线图不只是目录，下面用最经典的代表题 `Two Sum` 示范：看到题意以后，怎么从“补数”这个信号自然想到哈希表。

## Python 代码

```python
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}

        for index, value in enumerate(nums):
            need = target - value
            if need in seen:
                return [seen[need], index]
            seen[value] = index

        return []


print(Solution().twoSum([2, 7, 11, 15], 9))
```

## 时间复杂度

数组只扫描一次，哈希查询平均是常数时间，所以时间复杂度是 `O(n)`。

## 空间复杂度

哈希表最多存下所有元素，所以空间复杂度是 `O(n)`。

## 怎么想到

`Two Sum` 最关键的不是代码，而是识别信号。题目其实在问：当前数字的“补数”有没有已经出现过？只要把这个问题说清楚，就会自然想到用哈希表做“值 -> 下标”的快速查询。这也是整张路线图想反复训练的能力：先用语言识别 pattern，再写实现。

## 示例 case

输入：`nums = [2, 7, 11, 15], target = 9`
输出：`[0, 1]`
解释：扫到 `7` 时，前面已经见过 `2`，它们加起来正好等于 `9`。

边界 case：如果题目不保证一定有解，上面的示例代码会返回空列表 `[]`。

## 常见 Follow-up

- 如果数组已经有序，什么时候应该改成双指针？
- 如果题目变成找三个数之和，为什么会过渡到 `3Sum` 模板？
- 如果题目改成“连续子数组和为 k”，为什么往往要改想前缀和而不是继续用 `Two Sum` 思路？

## 这份文档怎么用

你每做一道题，都先按这个顺序想：

```text
// 第 1 步：先判断数据结构
// 是数组、字符串、链表、树、图，还是矩阵？

// 第 2 步：再判断 pattern
// 是哈希、双指针、滑动窗口、二分、回溯、BFS/DFS、堆、DP？

// 第 3 步：写代码前先说清楚变量含义
// 每个指针表示什么？
// dp[i] / dp[i][j] 表示什么？
// 递归函数到底返回什么？

// 第 4 步：先手推一个小样例
// 确认变量更新正确，再开始写代码
```

核心原则：

```text
// 不要按题目名字记解法
// 要按识别信号和模板记解法
```

---

## 推荐刷题顺序

建议严格按这个顺序推进：

1. 数组 / 哈希 / 基础扫描
2. 双指针
3. 链表
4. 栈 / 单调栈
5. 二叉树 / BST
6. 二分查找
7. 滑动窗口
8. 回溯
9. 图 BFS / DFS
10. 堆 / 优先队列
11. 动态规划
12. Hard 综合题

原因：

```text
// 前面几组先建立基本操作能力
// 中间几组建立模板识别能力
// 后面再做 DP 和综合难题
```

---

## Pattern 1：数组 / 哈希 / 基础扫描

### 识别信号

```text
// 题目在问：是否存在、出现次数、之前有没有见过
=> 优先想 hash map / hash set

// 题目和：前缀和、连续子数组、和为 k 有关
=> 优先想 prefix sum + hash map

// 题目和：缺失值、重复值、范围 1..n 强相关
=> 优先想下标映射 / 原地交换 / 快慢指针

// 题目问：单次扫描中的最大值、最小值、最大收益
=> 优先想一边遍历一边维护状态
```

### 核心模板

```text
// 哈希查找模板
for x in nums:
    // 先检查需要的东西是否已经出现
    // 再记录当前元素的信息
```

```text
// 前缀和 + 哈希表
prefix = 0
count[0] = 1

for x in nums:
    prefix += x
    // 如果 prefix - k 之前出现过
    // 说明中间这一段子数组和为 k
    ans += count[prefix - k]
    count[prefix] += 1
```

```text
// 单次扫描维护历史最优信息
for x in nums:
    // 更新“到目前为止最好的状态”
    // 用当前元素和历史状态一起更新答案
```

### 推荐顺序

1. Two Sum
2. Majority Element
3. Single Number
4. Best Time to Buy and Sell Stock
5. Maximum Subarray
6. Move Zeroes
7. Rotate Array
8. Product of Array Except Self
9. Group Anagrams
10. Longest Consecutive Sequence
11. Subarray Sum Equals K
12. Merge Intervals
13. Sort Colors
14. Find the Duplicate Number
15. First Missing Positive
16. Next Permutation

### 每题怎么想

- `Two Sum`
  ```text
  // 用哈希表存 value -> index
  // 扫到当前数 x 时，先查 target - x 是否已经存在
  ```

- `Majority Element`
  ```text
  // Boyer-Moore 投票法
  // 维护 candidate 和 count
  // 相同就加一，不同就减一
  ```

- `Single Number`
  ```text
  // 利用异或性质
  // a ^ a = 0
  // a ^ 0 = a
  // 成对出现的数会抵消
  ```

- `Best Time to Buy and Sell Stock`
  ```text
  // 维护到当前位置为止的最低价格
  // 当前利润 = 当前价格 - 历史最低价
  ```

- `Maximum Subarray`
  ```text
  // Kadane 算法
  // 当前位置结尾的最大子数组和：
  // 要么接在前面后面，要么从当前重新开始
  ```

- `Product of Array Except Self`
  ```text
  // 左边前缀乘积 * 右边后缀乘积
  // answer[i] = left[i] * right[i]
  ```

- `Group Anagrams`
  ```text
  // 异位词排序后相同
  // key 可以是排序后的字符串
  // 也可以是 26 个字母计数
  ```

- `Longest Consecutive Sequence`
  ```text
  // 先放入 set
  // 只有当 x - 1 不存在时，才从 x 开始往后数
  ```

- `Subarray Sum Equals K`
  ```text
  // 前缀和差值
  // 看有多少个历史前缀和等于 current_prefix - k
  ```

- `Merge Intervals`
  ```text
  // 区间题通常先排序
  // 当前区间起点 <= 上一个区间终点，就合并
  ```

- `Sort Colors`
  ```text
  // 荷兰国旗问题
  // 维护 0 区间、未处理区间、2 区间
  ```

- `Find the Duplicate Number`
  ```text
  // 把数组值看成链表 next 指针
  // 用 Floyd 判环找重复数
  ```

- `First Missing Positive`
  ```text
  // 把值 x 放到下标 x - 1 的位置
  // 再扫描第一个 nums[i] != i + 1 的位置
  ```

- `Next Permutation`
  ```text
  // 从右往左找第一个下降位置作为 pivot
  // 再找右侧刚好比它大的数交换
  // 最后把后缀反转
  ```

### 常见错误

- 需要原下标时却先排序
- 忘记初始化 `count[0] = 1`
- 把子数组和子序列混淆
- 可以 O(n) 做的题写成 O(n^2)

---

## Pattern 2：双指针

### 识别信号

```text
// 有序数组
// 左右夹逼
// 原地压缩 / 移动
// 回文 / 配对 / 三元组
// 链表中点 / 判环
```

### 核心模板

```text
// 左右指针
left = 0
right = n - 1

while left < right:
    // 更新答案
    // 移动更“不可能变优”的一边
```

```text
// 快慢指针
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

### 推荐顺序

1. Move Zeroes
2. Container With Most Water
3. 3Sum
4. Trapping Rain Water
5. Linked List Cycle
6. Linked List Cycle II
7. Palindrome Linked List

### 每题怎么想

- `Move Zeroes`
  ```text
  // slow 指向下一个非零元素该放的位置
  // fast 负责扫描所有元素
  ```

- `Container With Most Water`
  ```text
  // 面积由较短那一边决定
  // 所以移动较短那边，才有可能让面积变大
  ```

- `3Sum`
  ```text
  // 先排序
  // 固定一个数，剩下部分做双指针 two-sum
  // 注意去重
  ```

- `Trapping Rain Water`
  ```text
  // 每一边能装多少水，取决于较小的最高边界
  // 维护 left_max 和 right_max
  ```

- `Linked List Cycle`
  ```text
  // slow 和 fast 能相遇，说明有环
  ```

- `Linked List Cycle II`
  ```text
  // 相遇后，一个指针回到 head
  // 两个指针都每次走一步
  // 再次相遇点就是环入口
  ```

---

## Pattern 3：链表

### 识别信号

```text
// 反转、合并、删除、交换
// 倒数第 k 个
// 中点
// 环、交点
```

### 核心模板

```text
// dummy 节点：处理头节点很方便
dummy.next = head
prev = dummy
```

```text
// 反转链表
prev = None
cur = head

while cur:
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
```

```text
// 合并两个有序链表
dummy = ListNode(0)
tail = dummy

while l1 and l2:
    // 接较小节点

// 接上剩余部分
```

### 推荐顺序

1. Reverse Linked List
2. Merge Two Sorted Lists
3. Remove Nth Node From End of List
4. Add Two Numbers
5. Intersection of Two Linked Lists
6. Swap Nodes in Pairs
7. Copy List with Random Pointer
8. Sort List
9. LRU Cache
10. Merge k Sorted Lists
11. Reverse Nodes in k-Group

### 每题怎么想

- `Remove Nth Node From End of List`
  ```text
  // fast 先走 n 步
  // 然后 slow 和 fast 一起走
  // slow 停在待删除节点前一个位置
  ```

- `Add Two Numbers`
  ```text
  // 模拟竖式加法
  // 一位一位相加，同时维护 carry
  ```

- `Intersection of Two Linked Lists`
  ```text
  // A 走完走 B，B 走完走 A
  // 路径长度被拉齐后会在交点相遇
  ```

- `Copy List with Random Pointer`
  ```text
  // 可以用 old -> new 的哈希表
  // 也可以把复制节点插到原节点后面，再拆开
  ```

- `Sort List`
  ```text
  // 链表归并排序
  // 找中点 -> 切开 -> 分别排序 -> 合并
  ```

- `LRU Cache`
  ```text
  // hash map 负责 O(1) 查找
  // 双向链表负责 O(1) 删除和移动到头部
  ```

- `Reverse Nodes in k-Group`
  ```text
  // 找到一段长度为 k 的链表
  // 反转这段
  // 再和前后部分接回去
  ```

---

## Pattern 4：栈 / 单调栈

### 识别信号

```text
// 括号匹配
// 嵌套结构
// 最近更大 / 更小
// 柱状图面积
// 等下一个更高温度
```

### 核心模板

```text
// 普通栈
for ch in s:
    // 开括号 / 数字 / 状态 入栈
    // 遇到闭括号时弹栈处理
```

```text
// 单调栈一般存下标
for i, x in enumerate(nums):
    while stack and nums[stack[-1]] < x:
        idx = stack.pop()
        // 当前元素就是 idx 的下一个更大元素
    stack.append(i)
```

### 推荐顺序

1. Valid Parentheses
2. Min Stack
3. Decode String
4. Daily Temperatures
5. Largest Rectangle in Histogram
6. Longest Valid Parentheses

### 每题怎么想

- `Min Stack`
  ```text
  // 维护一个最小值栈
  // 或者每个位置直接存 (当前值, 当前最小值)
  ```

- `Decode String`
  ```text
  // 遇到 '[' 时，把之前的字符串和倍数压栈
  // 遇到 ']' 时，弹栈并拼接
  ```

- `Daily Temperatures`
  ```text
  // 维护一个递减温度栈
  // 当前更高温出现时，结算前面等待的天数
  ```

- `Largest Rectangle in Histogram`
  ```text
  // 某个柱子被弹出时
  // 它就是那一段矩形的最矮高度
  // 宽度由当前下标和新的栈顶决定
  ```

---

## Pattern 5：二叉树 / BST

### 识别信号

```text
// 深度、路径、直径、左右子树
// BST 有序性
// 每层遍历
// 子树向父节点返回信息
```

### 遍历怎么选

```text
// 前序：构造、路径、先处理当前节点
// 中序：BST 排序性质
// 后序：左右子树先算完，再合并
// 层序：按层 BFS
```

### 核心模板

```text
def dfs(node):
    if not node:
        return 基础值

    left = dfs(node.left)
    right = dfs(node.right)

    // 用 left 和 right 组合当前答案
    return 要返回给父节点的信息
```

### 推荐顺序

1. Maximum Depth of Binary Tree
2. Invert Binary Tree
3. Binary Tree Inorder Traversal
4. Symmetric Tree
5. Binary Tree Level Order Traversal
6. Diameter of Binary Tree
7. Validate Binary Search Tree
8. Convert Sorted Array to Binary Search Tree
9. Kth Smallest Element in a BST
10. Lowest Common Ancestor of a Binary Tree
11. Binary Tree Right Side View
12. Path Sum III
13. Flatten Binary Tree to Linked List
14. Construct Binary Tree from Preorder and Inorder Traversal
15. Binary Tree Maximum Path Sum

### 每题怎么想

- `Symmetric Tree`
  ```text
  // 比较一边的左子树和另一边的右子树
  ```

- `Diameter of Binary Tree`
  ```text
  // 经过当前节点的最长路径 = 左高度 + 右高度
  // 返回给父节点的是当前高度
  ```

- `Validate Binary Search Tree`
  ```text
  // 不能只看 node.left < node < node.right
  // 必须维护整棵子树的上下界
  ```

- `Kth Smallest Element in a BST`
  ```text
  // BST 的中序遍历是有序的
  // 遍历时计数
  ```

- `Lowest Common Ancestor of a Binary Tree`
  ```text
  // 如果左右子树都找到了目标节点
  // 当前节点就是最近公共祖先
  ```

- `Path Sum III`
  ```text
  // 本质和 Subarray Sum Equals K 一样
  // 只是前缀和现在发生在树路径上
  ```

- `Flatten Binary Tree to Linked List`
  ```text
  // 把左子树拍平后插到 root 和右子树之间
  ```

- `Binary Tree Maximum Path Sum`
  ```text
  // 返回给父节点的只能是“单边最大贡献”
  // 但全局答案要考虑 left + node + right
  ```

---

## Pattern 6：二分查找

### 识别信号

```text
// 有序
// 找边界
// 第一个 / 最后一个
// 旋转数组
// 满足条件的最小答案
// 单调性
```

### 核心模板

```text
// 精确查找
left = 0
right = n - 1

while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

```text
// 找左边界
while left <= right:
    mid = (left + right) // 2
    if nums[mid] >= target:
        right = mid - 1
    else:
        left = mid + 1
```

### 推荐顺序

1. Search Insert Position
2. Find First and Last Position of Element in Sorted Array
3. Search a 2D Matrix
4. Find Minimum in Rotated Sorted Array
5. Search in Rotated Sorted Array
6. Search a 2D Matrix II
7. Median of Two Sorted Arrays

### 每题怎么想

- `Find First and Last Position`
  ```text
  // 二分两次
  // 一次找左边界，一次找右边界
  ```

- `Find Minimum in Rotated Sorted Array`
  ```text
  // 用 nums[mid] 和 nums[right] 比较
  // 决定最小值在哪一半
  ```

- `Search in Rotated Sorted Array`
  ```text
  // 每次至少有一半是有序的
  // 判断 target 是否落在这个有序区间里
  ```

- `Median of Two Sorted Arrays`
  ```text
  // 不是合并，而是做 partition 二分
  // 保证左半边总长度固定
  // 并满足 maxLeft <= minRight
  ```

---

## Pattern 7：滑动窗口

### 识别信号

```text
// 子串 / 连续子数组
// 最长 / 最短合法区间
// 不重复字符
// 包含所有目标字符
// 固定大小窗口
```

### 核心模板

```text
// 可变窗口
left = 0

for right in range(n):
    // 扩张窗口，加入 nums[right]

    while 窗口不合法:
        // 从左边收缩
        left += 1

    // 更新答案
```

```text
// 固定窗口
// 先建长度为 k 的初始窗口
// 再每次右进一个、左出一个
```

### 推荐顺序

1. Longest Substring Without Repeating Characters
2. Find All Anagrams in a String
3. Minimum Window Substring
4. Sliding Window Maximum

### 每题怎么想

- `Longest Substring Without Repeating Characters`
  ```text
  // 维护一个窗口，保证窗口内字符不重复
  // 一旦重复，就移动 left 直到恢复合法
  ```

- `Find All Anagrams in a String`
  ```text
  // 固定长度窗口 + 字符频率统计
  ```

- `Minimum Window Substring`
  ```text
  // 先扩张到“已经覆盖所有需要字符”
  // 再尽可能收缩，找到最短合法窗口
  ```

- `Sliding Window Maximum`
  ```text
  // 用 deque，不用普通堆
  // 维护一个递减队列
  ```

---

## Pattern 8：回溯

### 识别信号

```text
// 所有组合
// 所有排列
// 所有划分
// 是否存在一条路径
// 做选择 -> 递归 -> 撤销选择
```

### 核心模板

```text
path = []

def backtrack(state):
    if 到达终点:
        ans.append(path 的拷贝)
        return

    for choice in 当前所有选择:
        if choice 不合法:
            continue

        // 做选择
        path.append(choice)

        // 递归
        backtrack(next_state)

        // 撤销选择
        path.pop()
```

### 推荐顺序

1. Letter Combinations of a Phone Number
2. Subsets
3. Permutations
4. Combination Sum
5. Generate Parentheses
6. Palindrome Partitioning
7. Word Search
8. N-Queens

### 每题怎么想

- `Subsets`
  ```text
  // 每个元素：选 或 不选
  // 通常用 start 控制下一层从哪里开始
  ```

- `Permutations`
  ```text
  // 顺序重要
  // 要用 used[] 标记哪些元素已经用过
  ```

- `Combination Sum`
  ```text
  // 顺序不重要，但可以重复用同一个元素
  // 递归时经常继续传当前下标
  ```

- `Generate Parentheses`
  ```text
  // 左括号数量不能超过 n
  // 右括号数量不能超过左括号数量
  ```

- `Palindrome Partitioning`
  ```text
  // 每次切出一个子串
  // 只有这个子串是回文时才继续
  ```

- `Word Search`
  ```text
  // 矩阵 DFS
  // 当前路径访问过的格子要标记
  // 回溯时恢复
  ```

- `N-Queens`
  ```text
  // 记录列、主对角线、副对角线是否冲突
  // 越早剪枝越重要
  ```

---

## Pattern 9：图 BFS / DFS

### 识别信号

```text
// 岛屿、连通块
// 依赖关系
// 一层一层扩散
// 无权图最短步数
```

### 核心模板

```text
// DFS 染色 / flood fill
def dfs(r, c):
    if 越界 或 不合法:
        return
    标记访问
    往四个方向继续 dfs
```

```text
// BFS 按层扩散
queue = 所有起点
steps = 0

while queue:
    for _ in range(len(queue)):
        处理一个节点
        把下一层节点加入队列
    steps += 1
```

### 推荐顺序

1. Number of Islands
2. Rotting Oranges
3. Course Schedule

### 每题怎么想

- `Number of Islands`
  ```text
  // 遍历整个矩阵
  // 每发现一块新陆地，就把整座岛 DFS/BFS 淹掉
  ```

- `Rotting Oranges`
  ```text
  // 所有腐烂橘子同时作为 BFS 起点
  // 每一层表示一分钟
  ```

- `Course Schedule`
  ```text
  // 有向图判环
  // 用拓扑排序，看能否处理完所有点
  ```

---

## Pattern 10：堆 / 优先队列

### 识别信号

```text
// top k
// 数据流中位数
// 不断取最小 / 最大
// 合并多个有序结构
```

### 核心模板

```text
// 保留前 k 大：用大小为 k 的小顶堆
for x in nums:
    push x
    if heap size > k:
        pop 最小值
```

```text
// 两个堆维护中位数
// 左边大顶堆，右边小顶堆
// 插入后保持两边平衡
```

### 推荐顺序

1. Kth Largest Element in an Array
2. Top K Frequent Elements
3. Merge k Sorted Lists
4. Find Median from Data Stream

### 每题怎么想

- `Top K Frequent Elements`
  ```text
  // 先统计频率
  // 再用堆或桶排序取前 k
  ```

- `Merge k Sorted Lists`
  ```text
  // 堆里放每条链表当前节点
  // 每次弹出最小节点，再把它的 next 放进去
  ```

- `Find Median from Data Stream`
  ```text
  // 把数据分成左右两半
  // 保持左边最大值 <= 右边最小值
  // 并保持数量平衡
  ```

---

## Pattern 11：动态规划

### DP 四步法

```text
// 1. 状态是什么？
// 2. 转移是什么？
// 3. 初始化是什么？
// 4. 遍历顺序是什么？
```

### 识别信号

```text
// 最优值
// 多少种方法
// 选或不选
// 重复子问题
// 最少步数、最大长度、能否组成
```

### 推荐顺序

1. Climbing Stairs
2. Pascal's Triangle
3. House Robber
4. Unique Paths
5. Minimum Path Sum
6. Coin Change
7. Perfect Squares
8. Word Break
9. Partition Equal Subset Sum
10. Longest Common Subsequence
11. Longest Increasing Subsequence
12. Longest Palindromic Substring
13. Maximum Product Subarray
14. Edit Distance
15. Longest Valid Parentheses

### 核心模板

```text
// 一维 DP
dp[i] = 前 i 个位置 / 到位置 i 为止的答案
```

```text
// 二维网格 DP
dp[r][c] = 到达 (r, c) 或处理到 (r, c) 的答案
```

```text
// 双串 DP
dp[i][j] = s1[:i] 和 s2[:j] 的答案
```

### 每题怎么想

- `Climbing Stairs`
  ```text
  // Fibonacci 型
  // dp[i] = dp[i-1] + dp[i-2]
  ```

- `House Robber`
  ```text
  // 抢当前 => 不能抢前一个
  // 不抢当前 => 继承前一个状态
  ```

- `Unique Paths`
  ```text
  // 到当前格子的路径数 = 上面 + 左边
  ```

- `Minimum Path Sum`
  ```text
  // 到当前格子的最小代价 = 当前值 + min(上, 左)
  ```

- `Coin Change`
  ```text
  // dp[a] = 凑出金额 a 的最少硬币数
  ```

- `Perfect Squares`
  ```text
  // 和 Coin Change 同型
  // 只是可用的“硬币”变成平方数
  ```

- `Word Break`
  ```text
  // dp[i] 表示 s[:i] 能否被拆分
  // 枚举最后一段从哪里切过来
  ```

- `Partition Equal Subset Sum`
  ```text
  // 0-1 背包
  // 看能不能凑出 total_sum / 2
  ```

- `Longest Common Subsequence`
  ```text
  // 字符相同：看左上角 + 1
  // 字符不同：看上边和左边的较大值
  ```

- `Longest Increasing Subsequence`
  ```text
  // 先掌握 O(n^2) DP
  // 再学二分优化版本
  ```

- `Longest Palindromic Substring`
  ```text
  // 可以做区间 DP
  // 但更推荐先掌握中心扩展法
  ```

- `Maximum Product Subarray`
  ```text
  // 同时维护最大积和最小积
  // 因为负数会翻转大小关系
  ```

- `Edit Distance`
  ```text
  // 插入、删除、替换 三种操作取最小
  ```

- `Longest Valid Parentheses`
  ```text
  // 可以用栈做，也可以用 DP 做
  // 很适合理解“以 i 结尾”的状态设计
  ```

### 常见错误

- 状态都没定义清楚就开始写转移
- 初始化写错
- 遍历顺序不对
- 把“恰好到 i”和“前 i 个”的含义混了

---

## Pattern 12：矩阵题

### 识别信号

```text
// 二维遍历
// 原地旋转 / 修改
// 行列搜索
// 网格上的 DFS / BFS
```

### 推荐顺序

1. Rotate Image
2. Spiral Matrix
3. Set Matrix Zeroes
4. Search a 2D Matrix
5. Search a 2D Matrix II
6. Number of Islands
7. Rotting Oranges
8. Word Search

### 矩阵题检查清单

```text
// 1. 四个方向怎么写？
// 2. 需不需要 visited？
// 3. 能不能原地修改？
// 4. 一个格子会不会被重复访问？
// 5. 边界判断写在哪？
```

---

## Pattern 13：Trie

### 题目

1. Implement Trie (Prefix Tree)

### 核心思想

```text
// Trie 不是存整个单词
// 而是按字符一层一层存
// node.children[ch]
// node.is_end 表示一个完整单词结尾
```

### 适用场景

- 前缀匹配
- 字典查找
- 单词搜索扩展题

---

## Pattern 14：贪心

### 识别信号

```text
// 每一步做一个局部最优选择
// 并且这个选择不会破坏全局最优
// 常见于跳跃、区间切分、覆盖范围
```

### 推荐顺序

1. Best Time to Buy and Sell Stock
2. Jump Game
3. Jump Game II
4. Partition Labels

### 每题怎么想

- `Jump Game`
  ```text
  // 维护最远可达位置
  // 如果当前下标已经超过最远可达位置，直接失败
  ```

- `Jump Game II`
  ```text
  // current_end 表示当前这一步能覆盖到哪里
  // farthest 表示下一步最远能到哪里
  // 到 current_end 时，步数 +1
  ```

- `Partition Labels`
  ```text
  // 一段区间必须覆盖其中所有字符的最后出现位置
  ```

---

## 最后再做的 Hard 题

- Median of Two Sorted Arrays
- Binary Tree Maximum Path Sum
- Longest Valid Parentheses
- Find Median from Data Stream
- Merge k Sorted Lists
- Reverse Nodes in k-Group
- Sliding Window Maximum
- Largest Rectangle in Histogram
- Trapping Rain Water
- First Missing Positive
- N-Queens
- Edit Distance
- Minimum Window Substring

原因：

```text
// 这些题不是新题型
// 而是前面多个基础模板的组合
```

---

## 6 个阶段刷完全部题

### 第 1 阶段：建立基础反射

- Two Sum
- Best Time to Buy and Sell Stock
- Maximum Subarray
- Move Zeroes
- Reverse Linked List
- Merge Two Sorted Lists
- Valid Parentheses
- Maximum Depth of Binary Tree
- Invert Binary Tree
- Binary Tree Inorder Traversal
- Search Insert Position
- Climbing Stairs
- House Robber
- Longest Substring Without Repeating Characters
- Number of Islands

### 第 2 阶段：巩固高频模板

- 3Sum
- Product of Array Except Self
- Merge Intervals
- Linked List Cycle
- Remove Nth Node From End of List
- Add Two Numbers
- Diameter of Binary Tree
- Validate Binary Search Tree
- Binary Tree Level Order Traversal
- Kth Smallest Element in a BST
- Search in Rotated Sorted Array
- Find First and Last Position of Element
- Subsets
- Permutations
- Combination Sum
- Course Schedule
- Rotting Oranges
- Daily Temperatures
- Top K Frequent Elements
- Coin Change
- Word Break
- Unique Paths
- Minimum Path Sum

### 第 3 阶段：树 / 滑窗 / 回溯增强

- Lowest Common Ancestor of a Binary Tree
- Path Sum III
- Binary Tree Right Side View
- Flatten Binary Tree to Linked List
- Letter Combinations of a Phone Number
- Generate Parentheses
- Palindrome Partitioning
- Word Search
- Find All Anagrams in a String
- Partition Equal Subset Sum
- Longest Common Subsequence
- Implement Trie

### 第 4 阶段：数据结构和高级数组题

- Group Anagrams
- Longest Consecutive Sequence
- Subarray Sum Equals K
- Sort Colors
- Rotate Array
- Next Permutation
- Find the Duplicate Number
- Copy List with Random Pointer
- Sort List
- LRU Cache
- Kth Largest Element in an Array
- Search a 2D Matrix
- Search a 2D Matrix II
- Find Minimum in Rotated Sorted Array

### 第 5 阶段：控制节奏突破 Hard

- Trapping Rain Water
- Largest Rectangle in Histogram
- Sliding Window Maximum
- Minimum Window Substring
- Edit Distance
- Binary Tree Maximum Path Sum
- Merge k Sorted Lists
- Reverse Nodes in k-Group
- Find Median from Data Stream
- First Missing Positive
- N-Queens

### 第 6 阶段：最后攻坚

- Median of Two Sorted Arrays
- Longest Valid Parentheses

---

## 每天怎么练

建议你固定用这个格式：

1. 1 道新模板题
2. 1 道同 pattern 的中等题
3. 1 道前几天错过或做慢的复盘题

示例：

```text
// A：学模板
// B：套模板
// C：闭眼重做
```

为什么这样更有效：

```text
// 随机刷题只会增加“见过”
// 同类重复才能建立“真正会做”
```

---

## 复盘规则

如果不会做：

```text
// 不要只看题解就结束
// 至少写下：
// 1. 它属于什么 pattern
// 2. 核心不变量是什么
// 3. 你错在什么地方
// 4. 下次复用哪个模板
```

如果做出来了但很慢：

```text
// 标记为 2 天后重做
```

如果做得很顺：

```text
// 标记为 1 周后复习
```

---

## 每种 pattern 的一句话总结

- `哈希`：用空间换查找速度
- `双指针`：利用位置关系缩小范围
- `滑动窗口`：维护一个动态合法区间
- `链表`：dummy 节点 + 指针重连
- `栈`：处理嵌套和最近匹配
- `单调栈`：找下一个更大 / 更小
- `树 DFS`：让子树先回答问题
- `BFS`：一层一层扩散
- `二分`：利用单调性砍一半
- `回溯`：试一个选择，不行就撤回
- `堆`：维护 top-k 或当前最优候选
- `DP`：定义状态，用小问题推大问题

---

## 现在最适合开始的一组

你现在直接从这 10 题开始最稳：

1. Two Sum
2. Best Time to Buy and Sell Stock
3. Maximum Subarray
4. Move Zeroes
5. Reverse Linked List
6. Merge Two Sorted Lists
7. Valid Parentheses
8. Maximum Depth of Binary Tree
9. Search Insert Position
10. Climbing Stairs

这组的意义：

```text
// 快速建立信心
// 覆盖最常见基础模板
// 后面的中等题会明显容易很多
```

---

## 下一步最合理的动作

接下来最值得做的是再补一份详细教学文档，例如：

`pattern_1_数组哈希双指针_详细讲解.md`

里面每道题都写成：

- 怎么识别这题属于什么 pattern
- 暴力解为什么不够好
- 最优解怎么想到
- 注释版模板怎么写
- 容易错在哪里
- 做完以后要记住什么

如果你要，我下一条就直接继续给你生成这份中文版详细教学文档。
