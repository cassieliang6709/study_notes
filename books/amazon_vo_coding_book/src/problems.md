# 题目还原与解法

## 这个题型页的总结

这页不是简单列题，而是把 Amazon VO 常见高频题按题型家族整理，再补上原始信号、还原题目、核心解法和 follow-up 方向。它的重点是让你形成“同一类题怎么一起准备”的感觉。

## 本页在教什么

这页在教你如何把 cache、graph、DP、tree 这些常见 Amazon 家族题放到同一张图里理解，而不是一题一题孤立背。

## Python 代码

```python
from collections import deque


def ladder_length(begin: str, end: str, word_list: list[str]) -> int:
    words = set(word_list)
    if end not in words:
        return 0

    queue = deque([(begin, 1)])
    visited = {begin}

    while queue:
        word, steps = queue.popleft()
        if word == end:
            return steps
        for i in range(len(word)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                nxt = word[:i] + ch + word[i + 1:]
                if nxt in words and nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))
    return 0


print(ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
```

## 时间复杂度

以 `Word Ladder` 为代表题，朴素 BFS 会枚举每个位置的 26 个字符，时间复杂度常写作 `O(N * L * 26)`，其中 `N` 是词数，`L` 是单词长度。

## 空间复杂度

队列、访问集合和字典集合都与词数相关，所以空间复杂度是 `O(N)`。

## 怎么想到

准备 Amazon VO 时，不要只问“我会不会这道题”，还要问“这道题属于哪个家族、同家族的 follow-up 会怎么追”。像 `Word Ladder`、`Course Schedule`、`Word Search` 放在一起看，你会更容易形成 BFS / DFS / 图搜索的稳定模板。

## 示例 case

输入：`begin = "hit"`, `end = "cog"`
输出：`5`
解释：一条最短路径是 `hit -> hot -> dot -> dog -> cog`。这个例子能帮助你把图 BFS 和最短步数问题连起来。

## 常见 Follow-up

- 如果 interviewer 要你输出路径而不是长度，该怎么补？
- 什么情况下值得讲双向 BFS？
- 同一轮里如果又问 `Word Search` 或 `Course Schedule`，它们和 `Word Ladder` 的共同模板是什么？

## 1. Cache 家族

### 1.1 LRU / LFU / Custom Cache

`优先级：S`

社区原始描述：

- 一亩三分地有帖直接写到“实现一个 cache”
- 另一帖公开描述里写到 “missed cache 和 LRU cache simulation”
- 还有 Reddit 用户明确说 Amazon 问过 `LRU Cache`，另一个回复说自己被问到 `LFU Cache`

还原题目：

- 设计一个缓存系统，支持 `get(key)` 和 `put(key, value)`，超出容量时按最近最少使用淘汰
- follow-up 常见会改成：
  - LFU
  - 支持 `miss count`
  - 让你解释为什么能做到 `O(1)`
  - 问如果要支持并发或 TTL 怎么改

核心解法：

- `LRU`: `HashMap + Doubly Linked List`
- `LFU`: `key -> node`，`freq -> doubly linked list`，再维护 `min_freq`
- 面试时先讲：
  - 为什么单链表不够
  - 为什么需要 O(1) 删除任意节点
  - eviction 时怎么保证正确更新

易错点：

- 更新已有 key 时忘记移动节点
- 容量为 0
- `LFU` 在频率升级后没有正确更新 `min_freq`
- 删除尾节点后没同步从 map 去掉

建议练习：

- LeetCode 146 `LRU Cache`
- LeetCode 460 `LFU Cache`
- 自己口述一个 `TTL cache` 的扩展版本

## 2. Graph / BFS / DFS 家族

### 2.1 Word Ladder

`优先级：S`

社区原始描述：

- 一亩三分地总结帖直接写：`bfs dfs考的很多，word ladder，word search基本成了必考`

还原题目：

- 给 `beginWord`、`endWord` 和字典，每次只能改一个字符，问最短转换长度
- follow-up：
  - 输出路径而不只是长度
  - 优化时间复杂度

核心解法：

- 标准 `BFS`
- 进阶直接讲 `bidirectional BFS`
- 若 interviewer 追优化，讲：
  - wildcard pattern 预处理
  - 双向 BFS 降搜索空间

易错点：

- `endWord` 不在字典里
- 访问标记时机不对导致重复入队
- 复杂度说不清楚

建议练习：

- LeetCode 127 `Word Ladder`
- LeetCode 126 `Word Ladder II`

### 2.2 Word Search

`优先级：S`

社区原始描述：

- 同一篇总结帖把 `word search` 和 `word ladder` 放在一起，直接说成“基本成了必考”

还原题目：

- 在二维网格中找一个单词，字符可上下左右移动，同一个格子不能重复使用
- follow-up：
  - 多个单词版本
  - 如何剪枝

核心解法：

- `DFS + Backtracking`
- 多单词时讲 `Trie + DFS`

易错点：

- 访问标记恢复
- 边界判断顺序
- 多单词版本没有做前缀剪枝

建议练习：

- LeetCode 79 `Word Search`
- LeetCode 212 `Word Search II`

### 2.3 Course Schedule

`优先级：A`

社区原始描述：

- 一亩三分地总结帖直接列出了 `210 course schedule`

还原题目：

- 给依赖关系，判断能否完成所有课程，或输出一种可行顺序

核心解法：

- `Topological Sort`
- `BFS(Kahn)` 和 `DFS cycle detection` 都要会讲

易错点：

- 边方向说反
- 只会判断可行，不会输出顺序

建议练习：

- LeetCode 207
- LeetCode 210

## 3. DP / Backtracking 家族

### 3.1 Word Break I / II

`优先级：S`

社区原始描述：

- 总结帖直接列了 `139 140 word break`
- 另一个 VO 准备帖里明确出现：`wordbreak II。follow up 问能不能更快`

还原题目：

- `Word Break I`: 判断字符串能否被字典拆分
- `Word Break II`: 输出所有合法拆分
- follow-up：
  - 如何减少重复搜索
  - 如何更快

核心解法：

- `Word Break I`: `DP`
- `Word Break II`: `DFS + memo`
- 如果 interviewer 继续问优化，可以讲 `Trie + memo`

易错点：

- `Word Break II` 没做 memo 导致指数爆炸
- 字符串切片过多，解释不清性能瓶颈

建议练习：

- LeetCode 139
- LeetCode 140
- LeetCode 472 `Concatenated Words`

### 3.2 0-1 Knapsack / Edit Distance

`优先级：B`

社区原始描述：

- 总结帖列出 `0-1 knapsack`
- 同帖列出 `72 edit distance`

还原题目：

- 这类题在 Amazon VO 里更像“验证你是否掌握标准 DP 推导”的保底题

核心解法：

- 背包：状态定义、二维到一维压缩
- 编辑距离：`dp[i][j]` 表示前缀最小编辑次数

建议练习：

- LeetCode 72
- 经典 0-1 背包模板

## 4. Tree 家族

### 4.1 LCA / Diameter / Path Sum / Boundary / Vertical Order

`优先级：S`

社区原始描述：

- 总结帖列出：
  - `236 lca of tree`
  - `545 boundary of tree`
  - `314 binary vertical traversal`
  - `437 path sum`
  - `543 diameter of tree`
- 另一帖还有一句：`bottom view of a binary tree，题目一贴出来我就觉得和 vertical 那道题差不多`

还原题目：

- Amazon 很喜欢把二叉树基础题包装成 traversal 变体
- 常见问法：
  - 最近公共祖先
  - 树的直径
  - 路径和计数
  - 边界遍历
  - vertical order / bottom view

核心解法：

- `LCA`: 递归返回左右子树命中情况
- `Diameter`: 后序遍历，同时维护最大值
- `Path Sum III`: 前缀和 + hashmap
- `Vertical Order / Bottom View`: `BFS` 配合列坐标
- `Boundary`: 分左边界、叶子、右边界

易错点：

- 把 `Path Sum I` 和 `Path Sum III` 混了
- `vertical order` 不清楚同列同层的输出顺序
- `bottom view` 和 `vertical traversal` 混用

建议练习：

- LeetCode 236
- LeetCode 543
- LeetCode 437
- LeetCode 314
- LeetCode 545

## 5. 随机结构 / O(1) 设计

### 5.1 Insert Delete GetRandom O(1)

`优先级：A`

社区原始描述：

- 一亩三分地帖子直接写到：`类似 380 + - random O(1)，follow up 如果有dup怎么办`

还原题目：

- 设计一个数据结构，支持：
  - `insert`
  - `remove`
  - `getRandom`
- 所有操作尽量 `O(1)`
- follow-up：如果允许重复值怎么办

核心解法：

- 标准版：`array + value_to_index`
- 重复值版：`array + value_to_indices(set)`

易错点：

- 删除时忘记交换最后一个元素
- 交换后没更新被换元素的下标
- 重复值版没同步更新 index set

建议练习：

- LeetCode 380
- LeetCode 381

## 6. Binary Search / Unknown Size

### 6.1 Search in Sorted Array of Unknown Length

`优先级：A`

社区原始描述：

- 一亩三分地 Amazon VO 帖里明确写到：`search element in one sorted array which has infinate length`

还原题目：

- 给一个有序数组，但你不知道长度，查目标值位置
- follow-up：如果数组其实是有限的，只是你拿不到长度，怎么办

核心解法：

- 先指数扩张右边界：`1, 2, 4, 8...`
- 再在 `[left, right]` 上做二分

易错点：

- 边界扩张时越界处理说不清
- 把“未知长度”误解成“真的无限”

建议练习：

- LeetCode 702 `Search in a Sorted Array of Unknown Size`

## 7. Sliding Window / String

### 7.1 找所有排列出现位置

`优先级：A`

社区原始描述：

- 一亩三分地帖子给出的描述非常接近原题：`给两个string，在string1中找到所有符合string2的排列组合的subsequence，返回相应的index`

还原题目：

- 在长串中找所有子串起点，使该子串是短串的一个排列
- 本质是 `find all anagrams / permutation in string`

核心解法：

- 固定窗口长度
- 维护频次数组或 hashmap
- 窗口右移时增一个、减一个

易错点：

- `subsequence` 和 `substring` 在原帖里可能被混说，但题意明显是固定长度窗口匹配
- 字典比较复杂度不会讲

建议练习：

- LeetCode 438 `Find All Anagrams in a String`
- LeetCode 567 `Permutation in String`

## 8. Heap / Selection

### 8.1 Kth Largest Element

`优先级：A`

社区原始描述：

- 一亩三分地总结帖直接列出 `215 kth largest element in array`

还原题目：

- 给数组和 `k`，返回第 `k` 大元素

核心解法：

- `min-heap` 大小 `k`
- 或 `quickselect`

易错点：

- 第 `k` 大和排序下标混淆
- 只会堆，不会解释 quickselect 的平均复杂度

建议练习：

- LeetCode 215

## 9. Greedy

### 9.1 Gas Station

`优先级：B`

社区原始描述：

- 一亩三分地总结帖直接列出 `134 gas station`

还原题目：

- 判断从哪个站点出发可以环绕一圈

核心解法：

- 总油量不足直接失败
- 线性扫描维护当前油量，跌破 0 就重置起点

## 10. 小型设计编码题

### 10.1 Calendar / Meeting Schedule

`优先级：B`

社区原始描述：

- 一亩三分地 VO 帖里明确写到：`设计一个日历系统`，要求支持“创建事件”“查看某个时间是否 busy”“查看某日的所有事件”

还原题目：

- 这类题介于 coding 和 LLD 之间
- 面试官想看：
  - 数据结构选择
  - 时间区间冲突判断
  - API 设计
  - 复杂度解释

核心解法：

- 单用户版可先用：
  - `date -> sorted intervals`
  - `TreeMap / ordered list`
- 如果 interviewer 继续问，讲：
  - 重叠校验
  - recurring events
  - 多时区
  - 并发写入

## 最后怎么刷

推荐顺序：

1. `LRU / LFU`
2. `Word Ladder / Word Search`
3. `Word Break / Concatenated Words`
4. `LCA / Diameter / Path Sum / Vertical Order`
5. `Random O(1) / Unknown Size Binary Search`
6. `Course Schedule / Kth Largest / Gas Station`

如果你要 mock Amazon VO，建议每题都强制自己回答这 4 句：

1. 暴力解是什么
2. 为什么不够好
3. 最优结构为什么是这个
4. 如果 interviewer 要我继续优化，我准备怎么扩展
