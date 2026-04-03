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

```text
// 窗口里不能有重复
// 一重复就缩
```

### 2. Find All Anagrams in a String

```text
// 固定大小窗口
// 比较字符频率
```

### 3. Minimum Window Substring

```text
// 先扩到满足要求
// 再缩到不能再缩
```

### 4. Sliding Window Maximum

```text
// 本质是窗口题，但实现要用单调队列
```

---

## 三、推荐刷题顺序

1. Search Insert Position
2. Find First and Last Position of Element in Sorted Array
3. Search a 2D Matrix
4. Find Minimum in Rotated Sorted Array
5. Search in Rotated Sorted Array
6. Longest Substring Without Repeating Characters
7. Find All Anagrams in a String
8. Minimum Window Substring
9. Sliding Window Maximum
10. Median of Two Sorted Arrays

