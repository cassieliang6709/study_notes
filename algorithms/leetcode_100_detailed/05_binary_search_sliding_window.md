---
title: "05 二分与滑动窗口"
---

# 05 二分与滑动窗口

这两类题都不是靠“暴力枚举”，而是靠维护一个结构或区间。

---

## 第一部分：二分查找

### 识别信号

```text
// 有序
// 找第一个 / 最后一个
// 旋转数组
// 单调条件
// 满足条件的最小值
```

### 模板 1：精确查找

```text
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

### 模板 2：找左边界

```text
while left <= right:
    mid = (left + right) // 2
    if nums[mid] >= target:
        right = mid - 1
    else:
        left = mid + 1
```

重点题：

- `Search Insert Position`
- `Find First and Last Position`
- `Find Minimum in Rotated Sorted Array`
- `Search in Rotated Sorted Array`
- `Median of Two Sorted Arrays`

关键理解：

```text
// 二分的本质不是“数组一半一半砍”
// 而是“条件具有单调性”
```

---

## 第二部分：滑动窗口

### 识别信号

```text
// 子串
// 连续区间
// 最长 / 最短合法区间
// 覆盖所有字符
// 固定长度窗口
```

### 模板 1：可变窗口

```text
left = 0

for right in range(n):
    // 扩张窗口

    while 窗口不合法:
        // 收缩窗口
        left += 1

    // 更新答案
```

### 模板 2：固定窗口

```text
// 初始化长度 k 窗口
// 然后每次右进一个、左出一个
```

重点题：

### 1. Longest Substring Without Repeating Characters

**这个题型 / 算法点的总结**

`Longest Substring Without Repeating Characters` 属于滑动窗口类问题，关键是想清楚窗口什么时候合法、什么时候需要收缩。

**题目含义**

维护一个无重复字符的窗口。  
当右边加入一个重复字符时，就不断移动左边界直到窗口重新合法。

**Python 代码**

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        ans = 0

        for right, ch in enumerate(s):
            while ch in seen:
                seen.remove(s[left])
                left += 1
            seen.add(ch)
            ans = max(ans, right - left + 1)

        return ans
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(k)`，`k` 为窗口内字符种类。

**怎么想到这个方法**

题目是典型的“最长 + 子串 + 无重复”，三个关键词凑在一起几乎就是可变滑窗。

**示例 case**

- 输入：`s = "abcabcbb"`
- 输出：`3`。最长无重复子串是 `abc`。

**常见 Follow-up**

- 如果字符集固定，能不能用数组替代哈希表？
- 如果允许最多重复一次，窗口条件怎么改？

### 2. Find All Anagrams in a String

**这个题型 / 算法点的总结**

`Find All Anagrams in a String` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

题目让你找出 `s` 中所有和 `p` 互为字母异位词的子串起点。因为窗口长度固定为 `len(p)`，所以这是固定滑窗。

**Python 代码**

```python
from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = Counter(p)
        window = Counter()
        left = 0
        ans = []

        for right, ch in enumerate(s):
            window[ch] += 1

            if right - left + 1 > len(p):
                left_ch = s[left]
                window[left_ch] -= 1
                if window[left_ch] == 0:
                    del window[left_ch]
                left += 1

            if right - left + 1 == len(p) and window == need:
                ans.append(left)

        return ans
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(1)` 或 `O(k)`，取决于字符集实现。

**怎么想到这个方法**

因为窗口长度固定为 `len(p)`，所以它不是可变滑窗，而是固定滑窗加频次比较。

**示例 case**

- 输入：`s = "cbaebabacd"`, `p = "abc"`
- 输出：`[0,6]`。这两个起点对应的窗口都是 `abc` 的异位词。

**常见 Follow-up**

- 如果字符集特别大，频次数组还合适吗？
- 能不能维护一个 `matches` 计数避免整张表比较？

### 3. Minimum Window Substring

**这个题型 / 算法点的总结**

`Minimum Window Substring` 属于滑动窗口类问题，关键是想清楚窗口什么时候合法、什么时候需要收缩。

**题目含义**

先扩张窗口，直到它已经覆盖了 `t` 中所有需要的字符。  
然后尽量收缩左边界，找到最短合法窗口。  
核心是维护：

- `need`: 目标频率
- `window`: 当前窗口频率
- `have`: 当前已经满足的字符种类数

**Python 代码**

```python
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        window = {}
        have = 0
        need_count = len(need)

        res = [-1, -1]
        res_len = float("inf")
        left = 0

        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == need_count:
                if right - left + 1 < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                left += 1

        left, right = res
        return s[left:right + 1] if res_len != float("inf") else ""
```

**时间复杂度**

`O(m+n)`。

**空间复杂度**

`O(k)`。

**怎么想到这个方法**

题目要最短合法窗口，固定窗口不适合，应该想到可变滑窗。关键是先定义什么叫“窗口已经覆盖了 t”。

**示例 case**

- 输入：`s = "ADOBECODEBANC"`, `t = "ABC"`
- 输出：`"BANC"`。它是覆盖 `ABC` 的最短窗口。

**常见 Follow-up**

- 如果 `t` 中有重复字符，为什么需要计数而不是集合？
- 如果要返回长度而不是子串，代码怎么简化？

### 4. Sliding Window Maximum

**这个题型 / 算法点的总结**

`Sliding Window Maximum` 属于滑动窗口类问题，关键是想清楚窗口什么时候合法、什么时候需要收缩。

**题目含义**

队列中存下标，并保持对应值单调递减。  
这样队首始终是当前窗口最大值的下标。  
每次移动窗口时：

- 移除过期下标
- 把所有比当前值小的尾部下标弹出

**Python 代码**

```python
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []

        for i, x in enumerate(nums):
            while dq and dq[0] <= i - k:
                dq.popleft()

            while dq and nums[dq[-1]] <= x:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(k)`。

**怎么想到这个方法**

窗口里既要滑动，又要随时拿最大值，这类题最常见的组合就是单调队列。

**示例 case**

- 输入：`nums = [1,3,-1,-3,5,3,6,7]`, `k = 3`
- 输出：`[3,3,5,5,6,7]`。每个长度为 3 的窗口都要取最大值。

**常见 Follow-up**

- 为什么普通队列不够？
- 如果还要拿窗口最小值，能不能一起维护？

