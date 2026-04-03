# 01 数组、双指针、滑动窗口详细教学

这部分题量大，但底层模板很少。你真正要学的是：

```text
// hash
// 快慢指针
// 左右双指针
// 固定窗口
// 可变窗口
```

---

## 一、先记 5 个核心模板

### 1. 哈希查找

```text
for x in nums:
    // 先查需要的值
    // 再记录当前值
```

### 2. 快慢指针原地修改

```text
slow = 0
for fast in range(n):
    if 当前元素保留:
        nums[slow] = nums[fast]
        slow += 1
```

### 3. 左右双指针

```text
left = 0
right = n - 1

while left < right:
    // 更新答案
    // 根据性质移动一边
```

### 4. 可变滑窗

```text
left = 0
for right in range(n):
    加入 nums[right]
    while 窗口不合法:
        移除 nums[left]
        left += 1
    更新答案
```

### 5. 固定滑窗

```text
先构造长度 k 窗口
然后每次右进一个、左出一个
```

---

## 二、详细题解

## 1. Two Sum

### 识别

```text
// 问是否存在两个数和为 target
// 第一反应：补数
=> hash map
```

### 思路

```text
// 当前数是 x
// 如果之前见过 target - x
// 就找到答案
```

### 解法骨架

```python
def twoSum(nums, target):
    pos = {}

    for i, x in enumerate(nums):
        need = target - x
        if need in pos:
            return [pos[need], i]
        pos[x] = i
```

### 易错点

- 先存再查，可能重复使用同一元素
- 排序后会丢失原下标

---

## 2. Product of Array Except Self

### 识别

```text
// 每个位置要“除自己以外所有数的乘积”
// 不能用除法
=> 前缀乘积 + 后缀乘积
```

### 思路

```text
// answer[i] = 左边所有数乘积 * 右边所有数乘积
```

### 解法骨架

```python
def productExceptSelf(nums):
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

### 易错点

- 额外开两个完整数组可以，但空间不够优
- 忘记第二遍是“乘上”右边乘积，不是覆盖

---

## 3. Move Zeroes

### 识别

```text
// 原地移动
// 保持非零元素相对顺序
=> 快慢指针
```

### 思路

```text
// slow 指向下一个非零元素应放位置
// fast 负责扫描
```

### 解法骨架

```python
def moveZeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
```

---

## 4. Next Permutation

### 识别

```text
// 字典序下一个排列
=> 从后往前找 pivot
```

### 思路

```text
// 1. 从右往左找第一个 nums[i] < nums[i+1]
// 2. 再从右往左找第一个比 nums[i] 大的数交换
// 3. 将 i+1 后面反转
```

### 易错点

- 找不到 pivot 时要整体反转
- 交换对象要从右边找“刚好大一点”的

---

## 5. Merge Sorted Array

### 识别

```text
// 两个有序数组合并到 nums1
=> 从后往前双指针
```

### 思路

```text
// 从尾部填，避免覆盖 nums1 前面的有效元素
```

### 解法骨架

```python
def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
```

---

## 6. Sort Colors

### 识别

```text
// 只有 0,1,2 三种颜色
// 原地排序
=> Dutch National Flag
```

### 思路

```text
// 左边放 0
// 右边放 2
// 中间自然就是 1
```

### 解法骨架

```python
def sortColors(nums):
    left = 0
    i = 0
    right = len(nums) - 1

    while i <= right:
        if nums[i] == 0:
            nums[left], nums[i] = nums[i], nums[left]
            left += 1
            i += 1
        elif nums[i] == 2:
            nums[right], nums[i] = nums[i], nums[right]
            right -= 1
        else:
            i += 1
```

### 易错点

- 遇到 2 交换后，`i` 不能立刻加一

---

## 7. Group Anagrams

### 识别

```text
// 异位词分组
=> 排序后同 key / 频次数组同 key
```

### 思路

```text
// 把排序后的字符串作为 key
```

### 解法骨架

```python
from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    return list(groups.values())
```

---

## 8. Find the Duplicate Number

### 识别

```text
// n+1 个数，值在 1..n
// 只有一个重复数
=> 判环 / Floyd
```

### 思路

```text
// 把 nums[i] 看成 next 指针
// 重复数会导致成环
```

### 解法骨架

```python
def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow
```

---

## 9. 3Sum

### 识别

```text
// 三元组
// 和为目标
// 需要去重
=> 排序 + 固定一个数 + 双指针
```

### 思路

```text
// 固定 nums[i]
// 在右边区间里做 two-sum
```

### 解法骨架

```python
def threeSum(nums):
    nums.sort()
    ans = []
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                ans.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
    return ans
```

---

## 10. Container With Most Water

### 识别

```text
// 左右边界决定面积
=> 双指针
```

### 思路

```text
// 每次移动短板
// 因为面积受短板限制
```

### 解法骨架

```python
def maxArea(height):
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

---

## 11. Longest Substring Without Repeating Characters

### 识别

```text
// 最长子串
// 无重复
=> 可变滑窗
```

### 思路

```text
// 窗口里保持所有字符唯一
// 有重复就缩左边
```

### 解法骨架

```python
def lengthOfLongestSubstring(s):
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

---

## 12. Minimum Window Substring

### 识别

```text
// 最短覆盖子串
=> 可变滑窗 + 频率统计
```

### 思路

```text
// 先不断扩直到满足覆盖
// 再不断缩直到刚好不满足
```

### 核心难点

```text
// 维护“当前窗口已经满足了多少个需要的字符”
```

---

## 13. Max Consecutive Ones III

### 识别

```text
// 最长连续区间
// 最多翻转 k 个 0
=> 滑窗
```

### 思路

```text
// 窗口中 0 的数量不能超过 k
// 超过就缩
```

---

## 14. Permutation in String

### 识别

```text
// 是否存在某个排列子串
=> 固定窗口 + 频率统计
```

### 思路

```text
// 长度固定为 len(s1)
// 比较窗口频率和目标频率
```

---

## 15. Sliding Window Maximum

### 识别

```text
// 固定窗口最大值
=> 单调队列
```

### 思路

```text
// 队列里保持下标对应值单调递减
// 队首永远是当前窗口最大值
```

### 解法骨架

```python
from collections import deque

def maxSlidingWindow(nums, k):
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

---

## 三、这一组最容易混的点

```text
// 哈希：查有没有、统计频率
// 双指针：利用相对位置关系
// 滑窗：维护连续合法区间
// 单调队列：固定窗口最大最小
```

---

## 四、建议刷题顺序

1. Two Sum
2. Move Zeroes
3. Reverse String
4. Valid Anagram
5. Group Anagrams
6. Merge Sorted Array
7. Product of Array Except Self
8. Sort Colors
9. Container With Most Water
10. 3Sum
11. Longest Substring Without Repeating Characters
12. Max Consecutive Ones III
13. Permutation in String
14. Minimum Window Substring
15. Sliding Window Maximum
16. Next Permutation
17. Find the Duplicate Number

