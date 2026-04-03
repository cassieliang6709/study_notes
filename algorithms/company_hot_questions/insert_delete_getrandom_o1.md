---
title: "Insert Delete GetRandom O1"
---

# Insert Delete GetRandom O(1)

## 这个题型 / 算法点的总结

这题本质是“设计类 + 数组 + 哈希表”的组合。数组负责 `getRandom`，哈希表负责快速定位元素位置。

## 题目含义

设计一个数据结构，支持：

- `insert(val)`
- `remove(val)`
- `getRandom()`

并且平均时间复杂度都要是 `O(1)`。

## Python 代码

```python
import random


class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False

        idx = self.pos[val]
        last_val = self.nums[-1]

        self.nums[idx] = last_val
        self.pos[last_val] = idx

        self.nums.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
```

## 时间复杂度

三个操作平均都是 `O(1)`。

## 空间复杂度

`O(n)`。

## 怎么想到这个方法

题目同时要：

- 快速存在性判断和定位
- 随机等概率取一个元素

所以需要组合：

- 数组负责 `getRandom`
- 哈希表负责 `value -> index`

删除时的关键是“和末尾交换再 pop”，这样就不用在数组中间删元素。

## 示例 case

- 输入操作：`insert(1)`, `insert(2)`, `remove(1)`, `getRandom()`
- 输出行为：`getRandom()` 只可能返回 `2`
- 为什么：删除时通过和末尾交换再弹出，数组仍然保持连续可随机访问

## 常见 Follow-up

- 如果允许重复元素，对应哪道题？
- 为什么删除时一定要和最后一个元素交换？
- 如果 interviewer 问 `getRandom` 是否等概率，你怎么解释？
