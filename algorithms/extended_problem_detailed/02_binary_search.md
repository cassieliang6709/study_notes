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

**题目含义**

虽然数组被旋转了，但每次二分后，至少有一半区间是有序的。  
我们先判断左半边是否有序：

- 如果左半边有序，再判断 `target` 是否落在这个有序区间内
- 否则说明右半边有序，再判断 `target` 是否落在右半边

**代表 Python 代码**

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
```

**时间复杂度**

`O(log n)`。

**空间复杂度**

`O(1)`。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `旋转数组二分 / Binary Search on Rotated Array`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**常见 Follow-up**

- 如果数组里有重复元素，边界条件怎么改？
- 如果不能直接按下标访问，还适合二分吗？

### Find First and Last Position

```text
// 做两次二分
// 左边界 + 右边界
```

### Find Peak Element

**题目含义**

如果 `nums[mid] < nums[mid + 1]`，说明右边是上坡，峰值一定在右边。  
如果 `nums[mid] > nums[mid + 1]`，说明峰值在左边或当前点。  
所以可以通过比较相邻元素，逐步缩小区间。

**代表 Python 代码**

```python
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
```

**时间复杂度**

`O(log n)`。

**空间复杂度**

`O(1)`。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `单调趋势二分 / Binary Search on Slope`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**常见 Follow-up**

- 如果数组里有重复元素，边界条件怎么改？
- 如果不能直接按下标访问，还适合二分吗？

### Single Element in a Sorted Array

**题目含义**

在有序数组里，如果每个元素都成对出现，那么：

- 第一个元素对会从偶数下标开始
- 第二个元素对也会从偶数下标开始

一旦唯一元素出现，这个规律就被打破。  
所以我们让 `mid` 落在偶数位，然后检查：

- 如果 `nums[mid] == nums[mid + 1]`，唯一元素在右边
- 否则在左边或就是 `mid`

**代表 Python 代码**

```python
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid

        return nums[left]
```

**时间复杂度**

`O(log n)`。

**空间复杂度**

`O(1)`。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `奇偶规律二分 / Binary Search with Pair Parity`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**常见 Follow-up**

- 如果数组里有重复元素，边界条件怎么改？
- 如果不能直接按下标访问，还适合二分吗？

### Search a 2D Matrix

**题目含义**

因为题目满足：

- 每一行有序
- 每一行的第一个数大于上一行最后一个数

所以整个矩阵其实相当于一个升序一维数组。  
只要把一维下标 `mid` 映射回二维：

- 行号：`mid // n`
- 列号：`mid % n`

**代表 Python 代码**

```python
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            value = matrix[mid // n][mid % n]

            if value == target:
                return True
            if value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
```

**时间复杂度**

`O(log(mn))`。

**空间复杂度**

`O(1)`。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `二维转一维二分 / 2D as 1D Binary Search`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**常见 Follow-up**

- 如果数组里有重复元素，边界条件怎么改？
- 如果不能直接按下标访问，还适合二分吗？

### Find Minimum in Rotated Sorted Array

**题目含义**

比较 `nums[mid]` 和 `nums[right]`：

- 如果 `nums[mid] > nums[right]`，最小值一定在右边
- 否则最小值在左边，包括 `mid`

这题的本质是：最小值所在位置把数组分成了两段有序区间。

**代表 Python 代码**

```python
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
```

**时间复杂度**

`O(log n)`。

**空间复杂度**

`O(1)`。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `旋转数组最小值二分 / Rotated Array Minimum`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**常见 Follow-up**

- 如果数组里有重复元素，边界条件怎么改？
- 如果不能直接按下标访问，还适合二分吗？

### Kth Smallest Element in a Sorted Matrix

**题目含义**

这题容易误以为是对下标二分，其实不是。  
我们在“值的范围”上二分：

- `left = matrix[0][0]`
- `right = matrix[-1][-1]`

对于某个 `mid`，统计矩阵里有多少个数 `<= mid`：

- 如果数量小于 `k`，说明第 `k` 小更大
- 否则说明答案不大于 `mid`

**代表 Python 代码**

```python
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def count_le(x: int) -> int:
            count = 0
            row, col = n - 1, 0
            while row >= 0 and col < n:
                if matrix[row][col] <= x:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count

        left, right = matrix[0][0], matrix[-1][-1]

        while left < right:
            mid = (left + right) // 2
            if count_le(mid) < k:
                left = mid + 1
            else:
                right = mid

        return left
```

**时间复杂度**

若按值域二分，`O(n log(range))`。

**空间复杂度**

`O(1)` 或 `O(n)`，取决于计数实现。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `值域二分 / Binary Search on Value Space`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**常见 Follow-up**

- 如果数组里有重复元素，边界条件怎么改？
- 如果不能直接按下标访问，还适合二分吗？

### Random Pick with Weight

**题目含义**

如果权重是 `[1, 3, 2]`，那么前缀和是 `[1, 4, 6]`。  
随机生成 `1..6` 之间的一个数，看它落在哪个前缀区间里：

- `1` -> 下标 0
- `2,3,4` -> 下标 1
- `5,6` -> 下标 2

所以本质是：

1. 建前缀和
2. 随机取一个数
3. 二分找第一个 `>= x` 的位置

**代表 Python 代码**

```python
from bisect import bisect_left
from random import randint
from typing import List

class Solution:
    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for x in w:
            total += x
            self.prefix.append(total)
        self.total = total

    def pickIndex(self) -> int:
        x = randint(1, self.total)
        return bisect_left(self.prefix, x)
```

**时间复杂度**

预处理 `O(n)`，每次查询 `O(log n)`。

**空间复杂度**

`O(n)`。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `前缀和 + 二分 / Prefix Sum + Binary Search`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**常见 Follow-up**

- 如果数组里有重复元素，边界条件怎么改？
- 如果不能直接按下标访问，还适合二分吗？

### Median of Two Sorted Arrays

**题目含义**

这题核心不是“合并两个数组”，而是“找一个合法划分”。

设两个数组是 `A` 和 `B`，我们想把它们划成左右两半，满足：

1. 左半边元素总数和右半边平衡
2. 左半边最大值 `<=` 右半边最小值

只需要在较短数组上二分划分点 `i`，另一个数组的划分点 `j` 就能确定。  
一旦满足边界关系，答案就能直接算出来。

**代表 Python 代码**

```python
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2
        left, right = 0, len(A)

        while True:
            i = (left + right) // 2
            j = half - i

            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < len(A) else float("inf")
            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1
```

**时间复杂度**

`O(log(min(m,n)))`。

**空间复杂度**

`O(1)`。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `划分二分 / Partition Binary Search`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**常见 Follow-up**

- 如果数组里有重复元素，边界条件怎么改？
- 如果不能直接按下标访问，还适合二分吗？

