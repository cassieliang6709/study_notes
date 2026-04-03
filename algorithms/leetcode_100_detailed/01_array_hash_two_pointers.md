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

识别：

```text
// 问：是否存在一对数，和为 target
// 关键词：查补数
=> 哈希表
```

暴力：

```text
// 枚举两层循环
// O(n^2)
```

最优：

```text
// 扫描到 x 时
// 只需要知道 target - x 之前是否出现过
```

注释模板：

```text
map = {}

for i, x in enumerate(nums):
    need = target - x

    // 先查补数
    if need in map:
        return [map[need], i]

    // 再记录当前值
    map[x] = i
```

易错点：

- 先存再查，可能把同一个元素用两次
- 排序会破坏原始下标

---

### 2. Best Time to Buy and Sell Stock

识别：

```text
// 一次买卖
// 只需要知道历史最低价
=> 单次扫描
```

最优思路：

```text
// 到第 i 天卖出时，最优利润取决于：
// price[i] - 前面最小价格
```

注释模板：

```text
min_price = +inf
ans = 0

for price in prices:
    min_price = min(min_price, price)
    ans = max(ans, price - min_price)
```

易错点：

- 把“未来最低价”当成可以买入点，这是不合法的

---

### 3. Maximum Subarray

识别：

```text
// 连续子数组最大和
=> Kadane
```

核心问题：

```text
// 以 nums[i] 结尾的最大子数组和是什么？
// 要么接前面的最佳结尾
// 要么从当前重新开始
```

注释模板：

```text
cur = nums[0]
ans = nums[0]

for i in range(1, n):
    // 当前位置结尾的最佳值
    cur = max(nums[i], cur + nums[i])
    ans = max(ans, cur)
```

易错点：

- 忘记数组可能全是负数

---

### 4. Move Zeroes

识别：

```text
// 原地移动、保持相对顺序
=> 快慢指针
```

注释模板：

```text
slow = 0

for fast in range(len(nums)):
    if nums[fast] != 0:
        nums[slow], nums[fast] = nums[fast], nums[slow]
        slow += 1
```

不变量：

```text
// [0, slow) 始终都是已经放好的非零元素
```

---

### 5. Container With Most Water

识别：

```text
// 左右边界、求最大面积
=> 左右双指针
```

为什么移动短板：

```text
// 面积 = 宽度 * min(height[left], height[right])
// 如果不移动短板，宽度变小，短板不变，面积不会更优
```

注释模板：

```text
left = 0
right = n - 1
ans = 0

while left < right:
    h = min(height[left], height[right])
    ans = max(ans, h * (right - left))

    if height[left] < height[right]:
        left += 1
    else:
        right -= 1
```

---

### 6. 3Sum

识别：

```text
// 三元组、和为 0、要求去重
=> 排序 + 固定一个数 + 双指针
```

步骤：

```text
// 1. 排序
// 2. 枚举第一个数 nums[i]
// 3. 在右边区间做 two-sum
// 4. 小心去重
```

注释模板：

```text
sort(nums)

for i in range(n):
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    left = i + 1
    right = n - 1

    while left < right:
        s = nums[i] + nums[left] + nums[right]

        if s == 0:
            收集答案
            left += 1
            right -= 1
            跳过重复值
        elif s < 0:
            left += 1
        else:
            right -= 1
```

易错点：

- 去重位置写错
- 找到答案后只移动一边

---

### 7. Subarray Sum Equals K

识别：

```text
// 连续子数组 + 和为 k
=> 前缀和 + 哈希表
```

注释模板：

```text
prefix = 0
count = {0: 1}
ans = 0

for x in nums:
    prefix += x

    // 看之前有多少前缀和能和当前组成 k
    ans += count.get(prefix - k, 0)

    // 记录当前前缀和
    count[prefix] = count.get(prefix, 0) + 1
```

易错点：

- 忘记 `count[0] = 1`

---

### 8. Product of Array Except Self

识别：

```text
// 每个位置都要“除了自己之外”的乘积
// 不能用除法
=> 前后缀乘积
```

注释模板：

```text
ans = [1] * n

// ans[i] 先存左边所有数的乘积
left = 1
for i in range(n):
    ans[i] = left
    left *= nums[i]

// 再乘上右边所有数的乘积
right = 1
for i in range(n - 1, -1, -1):
    ans[i] *= right
    right *= nums[i]
```

---

### 9. Longest Consecutive Sequence

识别：

```text
// 连续序列长度
// 不关心原顺序
=> set
```

注释模板：

```text
s = set(nums)
ans = 0

for x in s:
    // 只有当 x 是序列起点时才开始扩展
    if x - 1 not in s:
        y = x
        while y in s:
            y += 1
        ans = max(ans, y - x)
```

---

### 10. Trapping Rain Water

识别：

```text
// 每个位置能装多少水
=> 双指针 / 前后缀最大值
```

双指针版本核心：

```text
// 左边装水取决于 left_max
// 右边装水取决于 right_max
// 谁更小，就先结算谁
```

---

## 四、这一组题的总复盘

你做数组 / 哈希 / 双指针题时，脑子里应该只保留下面这些问题：

```text
// 是不是在查“有没有见过”？
=> hash

// 是不是在查“连续子数组”？
=> prefix sum

// 是不是在查“有序关系 / 左右夹逼”？
=> two pointers

// 是不是只需要单次扫描维护历史最优？
=> running state
```

---

## 五、推荐刷题顺序

1. Two Sum
2. Best Time to Buy and Sell Stock
3. Maximum Subarray
4. Move Zeroes
5. Container With Most Water
6. 3Sum
7. Product of Array Except Self
8. Subarray Sum Equals K
9. Merge Intervals
10. Sort Colors
11. Group Anagrams
12. Longest Consecutive Sequence
13. Find the Duplicate Number
14. First Missing Positive
15. Next Permutation
16. Trapping Rain Water

