---
title: "Search in Sorted Array of Unknown Size"
---

# Search in Sorted Array of Unknown Size

## 这个题型 / 算法点的总结

这题本质是“先翻倍扩边界，再做二分查找”。难点不在二分本身，而在于你一开始没有数组长度。

## 题目含义

给一个有序数组接口 `ArrayReader`，你不能直接知道数组长度，只能调用 `reader.get(i)`。如果越界会返回一个很大的哨兵值。要求找 `target` 的下标。

这题的关键是：先把搜索区间“翻倍扩出来”，再做二分。

## Python 代码

```python
class Solution:
    def search(self, reader: "ArrayReader", target: int) -> int:
        left = 0
        right = 1

        while reader.get(right) < target:
            left = right
            right *= 2

        while left <= right:
            mid = (left + right) // 2
            value = reader.get(mid)

            if value == target:
                return mid
            if value < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
```

## 时间复杂度

`O(log k)`，`k` 是目标位置附近的索引规模。

## 空间复杂度

`O(1)`。

## 怎么想到这个方法

普通二分需要已知右边界，这题没有长度，所以先要想办法找到一个肯定覆盖 `target` 的区间。最常见技巧就是指数扩张：

- `1, 2, 4, 8, ...`

一旦包住目标，再回到普通二分。

## 示例 case

- 输入：一个升序数组接口，目标值是 `23`
- 输出：先把右边界翻倍扩到覆盖 `23` 的区间，再在这个区间里二分
- 为什么：二分必须先知道搜索区间，而这题的第一步就是主动把区间找出来

## 常见 Follow-up

- 为什么翻倍扩张的总复杂度仍然是对数级？
- 如果数组里有重复元素，如何找第一个出现位置？
- 如果越界不返回哨兵，而是直接抛异常，代码应怎么调整？
