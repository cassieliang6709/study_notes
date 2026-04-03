---
title: "02 二分查找详细教学"
---

# 02 二分查找详细教学

二分题的核心不是“有序数组”，而是“单调性”。

---

## 一、统一模板

### 精确查找

```python
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

### 左边界

```python
while left <= right:
    mid = (left + right) // 2
    if nums[mid] >= target:
        right = mid - 1
    else:
        left = mid + 1
```

---

## 二、代表题

### Search in Rotated Sorted Array

```text
// 每次至少一半是有序的
// 判断 target 是否在有序半边
```

### Find First and Last Position

```text
// 做两次二分
// 左边界 + 右边界
```

### Find Peak Element

```text
// 如果 nums[mid] < nums[mid+1]
// 峰值一定在右边
```

### Single Element in a Sorted Array

```text
// 成对元素在单一元素前后，下标奇偶规律会改变
```

### Search a 2D Matrix

```text
// 可看成整体有序数组
```

### Find Minimum in Rotated Sorted Array

```text
// 比较 nums[mid] 和 nums[right]
```

### Kth Smallest Element in a Sorted Matrix

```text
// 不是在下标上二分
// 而是在“值域”上二分
```

### Random Pick with Weight

```text
// 前缀和 + 二分找落点
```

### Median of Two Sorted Arrays

```text
// partition 二分
// 不是简单合并
```

---

## 三、建议顺序

1. Search a 2D Matrix
2. Find First and Last Position of Element in Sorted Array
3. Search in Rotated Sorted Array
4. Find Minimum in Rotated Sorted Array
5. Find Peak Element
6. Single Element in a Sorted Array
7. Search a 2D Matrix II
8. Random Pick with Weight
9. Kth Smallest Element in a Sorted Matrix
10. Median of Two Sorted Arrays


---

## Quiz

**Q1: 二分查找的前提条件是什么？**

- [ ] 数组元素唯一
- [ ] 数组长度为偶数
- [ ] 搜索空间具有单调性（有序或能判断左/右） ✅
- [ ] 数组从小到大排列

**Q2: `while lo < hi` 和 `while lo <= hi` 的区别？**

- [ ] 没有区别
- [ ] `lo <= hi` 用于精确查找，循环结束时 lo > hi；`lo < hi` 收缩到同一点 ✅
- [ ] `lo < hi` 适合找最大值
- [ ] `lo <= hi` 只能用于整数

**Q3: `Search in Rotated Sorted Array` 的核心判断是什么？**

- [ ] 直接比较 mid 和 target
- [ ] 先判断哪半段是有序的，再决定往哪边搜索 ✅
- [ ] 先找旋转点再二分
- [ ] 线性扫描找 target

**Q4: 找"左边界"（第一个满足条件的位置）时，`mid` 满足条件应该怎么移动？**

- [ ] `lo = mid + 1`
- [ ] `hi = mid - 1`
- [ ] `hi = mid`（收缩右边，保留 mid 可能是答案） ✅
- [ ] `lo = mid`

**Q5: 二分查找时间复杂度为什么是 O(log n)？**

- [ ] 每次只访问一个元素
- [ ] 每次排除一半搜索空间 ✅
- [ ] 使用了哈希优化
- [ ] 递归深度固定为常数
