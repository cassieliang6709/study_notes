# 6. 双指针 / 滑动窗口

## 面试题目怎么问

- 最长无重复子串
- 最多包含 `K` 种不同字符的最长子串
- 和至少为 `target` 的最短子数组
- 统计满足条件的子数组个数

## 识别信号

- 子串 / 子数组连续
- 最长 / 最短
- “至多 K 个”“不超过 K 个”“满足某个窗口条件”

## Amazon 风格业务包装

- 找一段连续时间窗口，使某类商品种类数不超过 `K`
- 在用户行为日志里找最长不重复序列
- 找最短连续区间，使销量总和达到目标
- 分析订单流中满足条件的连续片段

## 你该怎么想

- 看到“连续区间”先想到滑窗
- 再问自己：窗口合法条件是什么
- 最后问自己：答案在扩张时更新，还是在收缩时更新

## 标准代码模板 1：至多 K 种字符

```python
from collections import defaultdict

def longest_substring_at_most_k(s, k):
    count = defaultdict(int)
    left = 0
    ans = 0

    for right, ch in enumerate(s):
        count[ch] += 1

        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1

        ans = max(ans, right - left + 1)

    return ans
```

## 标准代码模板 2：最长无重复子串

```python
def length_of_longest_substring(s):
    pos = {}
    left = 0
    ans = 0

    for right, ch in enumerate(s):
        if ch in pos and pos[ch] >= left:
            left = pos[ch] + 1
        pos[ch] = right
        ans = max(ans, right - left + 1)

    return ans
```

## 标准代码模板 3：最短子数组和至少为 target

```python
def min_subarray_len(target, nums):
    left = 0
    total = 0
    ans = float('inf')

    for right, x in enumerate(nums):
        total += x
        while total >= target:
            ans = min(ans, right - left + 1)
            total -= nums[left]
            left += 1

    return 0 if ans == float('inf') else ans
```

## 代码讲解

- `right` 负责扩张窗口
- `left` 在窗口不合法时收缩
- 求最长通常在合法时更新答案
- 求最短通常在合法后收缩过程中更新答案

## 面试时怎么讲

- 这是连续区间问题，所以优先想滑动窗口
- 我会定义一个“窗口合法条件”
- 右指针扩张纳入新元素，左指针收缩直到重新合法

## 常见 follow-up 和回答

**Q1：为什么滑窗是 `O(n)`？**  
因为每个元素最多被左右指针各访问一次。

**Q2：什么时候更新答案？**  
求最长一般在窗口合法时；求最短一般在收缩时。

**Q3：恰好 `K` 个怎么做？**  
`exactly(K) = atMost(K) - atMost(K - 1)`。

**Q4：如果不是连续子数组，还能用滑窗吗？**  
通常不行。

## Amazon 风格完整题面

> You are given a stream of user actions.  
> Find the longest contiguous window that contains no more than `K` distinct action types.

## 可直接背的口语回答稿

“这是一个连续区间优化问题，所以我会优先考虑滑动窗口。右指针负责扩张窗口，把新元素加入统计；如果窗口不合法，我就移动左指针收缩，直到重新满足条件。因为每个元素最多被两个指针访问一次，所以整体时间复杂度是 `O(n)`。”

## 推荐代表题

- Longest Substring Without Repeating Characters
- Longest Substring with At Most K Distinct Characters
- Minimum Size Subarray Sum

