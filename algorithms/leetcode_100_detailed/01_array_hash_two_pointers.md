---
title: "01 数组、哈希、双指针"
---

# 01 数组、哈希、双指针

这份是最重要的起步讲义。你后面很多题，底层其实都能还原成这里的几个模板。

---

## 一、先学会识别信号

```text
// 看到“是否存在”“有没有见过”“出现次数”
=> 哈希表

// 看到“连续子数组”“和为 k”
=> 前缀和 + 哈希表

// 看到“有序”“两边夹逼”“三元组”
=> 双指针

// 看到“单次扫描最优解”
=> 维护历史状态

// 看到“缺失值 / 重复值 / 值域 1..n”
=> 原地放置 / 快慢指针 / 下标映射
```

---

## 二、必背模板

### 1. 哈希查找

```text
// 适用：
// 是否存在、补数、频率、去重、查之前有没有

for x in nums:
    // 先检查需要的数据是否已经出现
    // 再记录当前元素
```

### 2. 前缀和 + 哈希

```text
prefix = 0
count[0] = 1

for x in nums:
    prefix += x
    ans += count[prefix - k]
    count[prefix] += 1
```

解释：

```text
// 如果某个历史前缀和是 prefix - k
// 那么从那个位置之后到当前位置这一段的和就是 k
```

### 3. 左右双指针

```text
left = 0
right = n - 1

while left < right:
    // 根据题意更新答案
    // 移动更不可能变优的那边
```

### 4. 快慢双指针

```text
slow = 0

for fast in range(len(nums)):
    if 当前元素需要保留:
        nums[slow] = nums[fast]
        slow += 1
```

### 5. 单次扫描维护最优状态

```text
for x in nums:
    // 更新历史最优信息
    // 再更新当前答案
```

---

## 三、重点题详细讲

### 1. Two Sum

**题目含义**

题目问的是：是否存在两个数之和等于 `target`。  
扫到当前数字 `x` 时，只需要知道之前有没有出现过 `target - x`。  
所以用字典记录“某个值第一次出现的位置”。

**Python 代码**

```python
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}

        for i, x in enumerate(nums):
            need = target - x
            if need in pos:
                return [pos[need], i]
            pos[x] = i

        return []
```

**时间复杂度**

`O(n)`，每个元素查一次哈希表。

**空间复杂度**

`O(n)`，字典存历史元素。

**怎么想到这个方法**

看到“找两数和为 target”，先把它翻译成“当前数需要一个补数”。只要题目允许用额外空间，`hash map` 往往就是第一反应。

**常见 Follow-up**

- 如果数组已排序，能不能改成双指针？
- 如果要返回所有不重复配对，如何避免重复？

### 2. Best Time to Buy and Sell Stock

**题目含义**

虽然这题常用贪心写，但也可以理解成 DP。  
核心状态是“到当前位置为止的最低买入价”，然后不断更新最大利润。

**Python 代码**

```python
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        ans = 0

        for p in prices:
            min_price = min(min_price, p)
            ans = max(ans, p - min_price)

        return ans
```

**时间复杂度**

`O(n)`，单次扫描。

**空间复杂度**

`O(1)`。

**怎么想到这个方法**

一旦题目限制只能买卖一次，就不要去想区间枚举，而是问自己：如果今天卖，最好的买入价是谁？于是自然会维护历史最小值。

**常见 Follow-up**

- 如果可以交易多次怎么改？
- 如果有冷冻期或手续费，为什么会变成 DP？

### 3. Maximum Subarray

**题目含义**

定义：

```text
cur = 以当前元素结尾的最大子数组和
```

那么每一步：

- 要么从当前元素重新开始
- 要么接在前一个最优结尾后面

**Python 代码**

```python
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = ans = nums[0]

        for x in nums[1:]:
            cur = max(x, cur + x)
            ans = max(ans, cur)

        return ans
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(1)`。

**怎么想到这个方法**

关键词是“连续子数组最大和”。这种题先问“以当前位置结尾的最优值是什么”，就会走到 Kadane 的状态转移。

**常见 Follow-up**

- 如果还要返回具体区间，怎么记录起点终点？
- 如果数组是环形，思路怎么改？

### 4. Move Zeroes

**题目含义**

`slow` 表示下一个非零元素应该放的位置，`fast` 负责扫描数组。  
每当 `fast` 遇到非零元素，就把它交换到 `slow` 位置。

**Python 代码**

```python
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(1)` 原地。

**怎么想到这个方法**

题目要求原地、稳定地把非零元素往前放，这就是典型快慢指针信号。`slow` 负责放置位置，`fast` 负责扫描。

**常见 Follow-up**

- 如果不能交换、只能覆盖写，怎么实现？
- 如果要把指定值移到末尾，模板是否相同？

### 5. Container With Most Water

**题目含义**

面积由宽度和较短的板决定。  
如果不移动短板，宽度只会变小，而短板不变，面积不可能更优。  
所以每次移动较短的一边。

**Python 代码**

```python
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0

        while left < right:
            h = min(height[left], height[right])
            ans = max(ans, h * (right - left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(1)`。

**怎么想到这个方法**

题目同时给你左右边界和面积公式，通常就该考虑双指针。因为面积瓶颈由短板决定，所以每次移动更短的一边才有希望变优。

**常见 Follow-up**

- 为什么移动更高的一边没有意义？
- 如果需要输出具体下标，代码怎么保留答案？

### 6. 3Sum

**题目含义**

先排序。  
枚举第一个数 `nums[i]`，然后在右边区间用双指针找两数之和等于 `-nums[i]`。  
为了避免重复答案，要对 `i`、`left`、`right` 都做去重处理。

**Python 代码**

```python
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return ans
```

**时间复杂度**

`O(n^2)`，排序后枚举一个数再双指针。

**空间复杂度**

排序开销外额外 `O(1)`；若计入排序栈通常写 `O(log n)`。

**怎么想到这个方法**

看到“三元组 + 去重 + 和为 0”，就要想到先排序，把问题降成固定一个数后的 `Two Sum`。

**常见 Follow-up**

- 如果是 `3Sum Closest` 怎么改？
- 如果是 `4Sum`，思路如何继续套？

### 7. Subarray Sum Equals K

**题目含义**

虽然这题常被归在 DP 一组里，但本质不是传统 DP，而是前缀和。  
如果当前前缀和是 `prefix`，那么只要之前有前缀和 `prefix - k`，中间这段子数组和就是 `k`。

**Python 代码**

```python
from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        prefix = 0
        ans = 0

        for x in nums:
            prefix += x
            ans += count[prefix - k]
            count[prefix] += 1

        return ans
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(n)`，前缀和计数表。

**怎么想到这个方法**

只要题目问“连续子数组和为 k 的个数”，先把区间和写成两个前缀和之差，问题就能转成哈希计数。

**常见 Follow-up**

- 如果数组都是非负数，能不能改滑窗？
- 如果要找最长而不是个数，哈希表存什么？

### 8. Product of Array Except Self

**题目含义**

`answer[i]` 要等于 `i` 左边所有数的乘积乘上右边所有数的乘积。  
第一遍从左到右，把左边乘积存进 `answer`。  
第二遍从右到左，再乘上右边乘积。

**Python 代码**

```python
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        left = 1
        for i in range(n):
            ans[i] = left
            left *= nums[i]

        right = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]

        return ans
```

**时间复杂度**

`O(n)`。

**空间复杂度**

额外空间 `O(1)`；如果把输出数组也算上则是 `O(n)`。

**怎么想到这个方法**

不能用除法时，最自然的拆法就是“左边乘积 * 右边乘积”。这类题一般都会想到前缀/后缀信息预处理。

**常见 Follow-up**

- 如果数组有 0，用除法法为什么麻烦？
- 能否只用一个输出数组完成？

### 9. Longest Consecutive Sequence

**题目含义**

只有当 `x - 1` 不存在时，`x` 才可能是一个连续序列的起点。  
从起点开始不断往后数，就能得到该序列长度。

**Python 代码**

```python
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0

        for x in s:
            if x - 1 not in s:
                y = x
                while y in s:
                    y += 1
                ans = max(ans, y - x)

        return ans
```

**时间复杂度**

`O(n)` 平均。

**空间复杂度**

`O(n)`。

**怎么想到这个方法**

题目要的是“连续值”，不是连续下标，所以别急着排序。哈希集合更适合做“某个数是不是序列起点”的判断。

**常见 Follow-up**

- 如果要求输出序列本身怎么做？
- 排序做法为什么是 `O(n log n)`？

### 10. Trapping Rain Water

**题目含义**

这题可以用单调栈，也可以用双指针。  
双指针更直观：

- 左边能装多少水取决于 `left_max`
- 右边能装多少水取决于 `right_max`

每次先处理较低的一边，因为它的装水上限已经确定。

**Python 代码**

```python
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        ans = 0

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                ans += right_max - height[right]
                right -= 1

        return ans
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(1)` 双指针版；单调栈版是 `O(n)` 空间。

**怎么想到这个方法**

题目本质是每个位置能装多少水取决于左右最高板。你可以从“预处理左右最大值”出发，再进一步优化成双指针。

**常见 Follow-up**

- 你能讲单调栈解法吗？
- 如果要输出每格积水量，需要额外存什么？

