---
title: "07 堆、Trie、贪心"
---

# 07 堆、Trie、贪心

---

## 第一部分：堆

### 识别信号

```text
// top k
// 数据流
// 不断取最小 / 最大
// 合并多个有序结构
```

### 模板

```text
// 保留前 k 大
for x in nums:
    heappush(heap, x)
    if len(heap) > k:
        heappop(heap)
```

重点题：

- `Kth Largest Element in an Array`
- `Top K Frequent Elements`
- `Merge k Sorted Lists`
- `Find Median from Data Stream`

---

## 第二部分：Trie

### 识别信号

```text
// 前缀
// 字典树
// 单词搜索 / 前缀匹配
```

### 模板

```text
class TrieNode:
    children = {}
    is_end = False
```

重点：

```text
// insert
// search
// startsWith
```

---

## 第三部分：贪心

### 识别信号

```text
// 局部最优能推出全局最优
// 维护最远覆盖
// 按最后出现位置切分
```

重点题：

### 1. Jump Game

**这个题型 / 算法点的总结**

`Jump Game` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

数组中每个位置给出你最多能跳多远，问能否到达终点。贪心的核心是维护当前能到达的最远位置。

**Python 代码**

```python
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i, step in enumerate(nums):
            if i > farthest:
                return False
            farthest = max(farthest, i + step)
        return True
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(1)`。

**怎么想到这个方法**

题目不是问具体路径，只问能不能到，所以没必要做 DP。贪心维护“目前最远能到哪”就足够了。

**示例 case**

- 输入：`nums = [2,3,1,1,4]`
- 输出：`True`。维护最远可达位置就能判断能否到终点。

**常见 Follow-up**

- 如果要求最少步数，怎么升级成 `Jump Game II`？
- 为什么当 `i > farthest` 时就能提前返回？

### 2. Jump Game II

**这个题型 / 算法点的总结**

`Jump Game II` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

和 `Jump Game` 不同，这次要你求最少跳跃次数。仍然是贪心，但多维护一层当前步数能覆盖的边界。

**Python 代码**

```python
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                steps += 1
                end = farthest

        return steps
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(1)`。

**怎么想到这个方法**

最少步数版可以把每一步看成一层区间扩展，和 BFS 分层很像，但可以压缩成贪心边界写法。

**示例 case**

- 输入：`nums = [2,3,1,1,4]`
- 输出：`2`。最少跳两次即可到末尾。

**常见 Follow-up**

- 为什么不需要真的把每个位置入队？
- 如果还要返回路径，数据结构怎么变？

### 3. Partition Labels

**这个题型 / 算法点的总结**

`Partition Labels` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

你要把字符串切成尽量多段，并保证同一个字符只出现在一段里。关键是先知道每个字符最后一次出现的位置，然后贪心切段。

**Python 代码**

```python
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {ch: i for i, ch in enumerate(s)}
        ans = []
        start = 0
        end = 0

        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                ans.append(end - start + 1)
                start = i + 1

        return ans
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(1)` 或 `O(k)`。

**怎么想到这个方法**

先预处理每个字符最后出现位置，然后一遍扫描动态扩展当前段的右边界。这是很典型的区间贪心。

**示例 case**

- 输入：`s = "ababcbacadefegdehijhklij"`
- 输出：`[9,7,8]`。每段内部完整包含各字符的全部出现位置。

**常见 Follow-up**

- 如果字符集不是小写字母，写法要改吗？
- 为什么在 `i == end` 时就能安全切段？

