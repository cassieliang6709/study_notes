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

