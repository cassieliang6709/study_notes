---
title: "09 Hard 专题与总复习"
---

# 09 Hard 专题与总复习

这份不是新模板，而是告诉你 Hard 题到底难在哪。

---

## 一、Hard 题为什么难

通常不是因为知识点全新，而是因为：

```text
// 1. 一个题里叠了两个以上模板
// 2. 状态设计更抽象
// 3. 实现细节更多
// 4. 容易在边界上出错
```

---

## 二、Top 100 里最值得最后攻克的 Hard 题

### 1. Median of Two Sorted Arrays

**这个题型 / 算法点的总结**

`Median of Two Sorted Arrays` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

这题核心不是“合并两个数组”，而是“找一个合法划分”。

设两个数组是 `A` 和 `B`，我们想把它们划成左右两半，满足：

1. 左半边元素总数和右半边平衡
2. 左半边最大值 `<=` 右半边最小值

只需要在较短数组上二分划分点 `i`，另一个数组的划分点 `j` 就能确定。  
一旦满足边界关系，答案就能直接算出来。

**Python 代码**

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

这题难在把“求中位数”转成“找一个合法切分”。只要切分左边元素个数正确，再保证左半最大值不超过右半最小值即可。

**示例 case**

- 输入：`nums1 = [1,3]`, `nums2 = [2]`
- 输出：`2.0`。总长度是奇数时取左半最大值。

**常见 Follow-up**

- 为什么要优先在更短数组上二分？
- 如果总长度是奇数和偶数，答案如何取？

### 2. Binary Tree Maximum Path Sum

**这个题型 / 算法点的总结**

`Binary Tree Maximum Path Sum` 主要在练树的递归返回值设计。做这类题时先决定遍历方式，再决定递归函数返回什么。

**题目含义**

这题最容易混淆的点是：

- 返回给父节点的值
- 全局最大路径值

不是一回事。

对每个节点：

- 向父节点返回：`node.val + max(left_gain, right_gain)`
- 更新全局答案：`node.val + left_gain + right_gain`

负贡献要直接丢掉，所以要和 `0` 比较。

**Python 代码**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def maxPathSum(self, root: Optional['TreeNode']) -> int:
        ans = float("-inf")

        def dfs(node):
            nonlocal ans
            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            ans = max(ans, node.val + left + right)
            return node.val + max(left, right)

        dfs(root)
        return ans
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(h)`。

**怎么想到这个方法**

最大路径和的难点是区分“往上返回给父节点的值”和“当前节点内部更新答案的值”。这通常是树 DP 的标志。

**示例 case**

- 输入：可能包含负数的二叉树
- 输出：任意路径的最大路径和。

**常见 Follow-up**

- 为什么返回值不能同时带左右两边？
- 如果节点值全负，初始化要注意什么？

### 3. Longest Valid Parentheses

**这个题型 / 算法点的总结**

`Longest Valid Parentheses` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

栈里不直接存括号，而是存下标。  
初始化放一个 `-1`，表示“上一个无法匹配的位置”。  
这样每当找到一个合法区间时，就可以用：

```text
当前下标 - 栈顶下标
```

计算区间长度。

**Python 代码**

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ans = 0

        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])

        return ans
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(n)`。

**怎么想到这个方法**

这题表面像括号匹配，实际上是“最长合法区间”。栈里放下标而不是字符，才能顺手算长度。

**示例 case**

- 输入：`s = ")()())"`
- 输出：`4`。最长合法括号子串是 `()()`。

**常见 Follow-up**

- DP 解法也能做吗？
- 为什么栈里常先压入 `-1`？

### 4. Find Median from Data Stream

**这个题型 / 算法点的总结**

`Find Median from Data Stream` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

维护两个堆：

- `small`：大顶堆，保存较小的一半
- `large`：小顶堆，保存较大的一半

保证：

- 两边元素数平衡
- `small` 中最大值 <= `large` 中最小值

**Python 代码**

```python
import heapq


class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
```

**时间复杂度**

`O(log n)` 插入，`O(1)` 查询。

**空间复杂度**

`O(n)`。

**怎么想到这个方法**

数据流中位数一看到“动态插入 + 随时查询中位数”，就该想到两个堆维持左右两半。

**示例 case**

- 操作：持续插入数字后随时查询中位数
- 结果：通常用一个最大堆和一个最小堆平衡左右两半。

**常见 Follow-up**

- 为什么一个最大堆一个最小堆？
- 如果要删除元素，还能怎么设计？

### 5. Reverse Nodes in k-Group

**这个题型 / 算法点的总结**

`Reverse Nodes in k-Group` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

链表每 `k` 个节点翻转一次，不足 `k` 个保持不变。面试重点在于分组、断开、反转、再接回。

**Python 代码**

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next
            prev = group_next
            cur = group_prev.next

            while cur != group_next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(1)`。

**怎么想到这个方法**

这题是在局部反转基础上再加“按组处理”。真正的面试重点是把一组的边界找出来，再把反转后的头尾接回原链表。

**示例 case**

- 输入：`1 -> 2 -> 3 -> 4 -> 5`, `k = 2`
- 输出：`2 -> 1 -> 4 -> 3 -> 5`。不足 `k` 个的尾段保持不变。

**常见 Follow-up**

- 如果最后不足 `k` 个也要反转，哪里改？
- 你会写递归版吗？

### 6. Sliding Window Maximum

**这个题型 / 算法点的总结**

`Sliding Window Maximum` 属于滑动窗口类问题，关键是想清楚窗口什么时候合法、什么时候需要收缩。

**题目含义**

队列中存下标，并保持对应值单调递减。  
这样队首始终是当前窗口最大值的下标。  
每次移动窗口时：

- 移除过期下标
- 把所有比当前值小的尾部下标弹出

**Python 代码**

```python
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
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

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(k)`。

**怎么想到这个方法**

窗口里既要滑动，又要随时拿最大值，这类题最常见的组合就是单调队列。

**示例 case**

- 输入：`nums = [1,3,-1,-3,5,3,6,7]`, `k = 3`
- 输出：`[3,3,5,5,6,7]`。每个长度为 3 的窗口都要取最大值。

**常见 Follow-up**

- 为什么普通队列不够？
- 如果还要拿窗口最小值，能不能一起维护？

### 7. Largest Rectangle in Histogram

**这个题型 / 算法点的总结**

`Largest Rectangle in Histogram` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

题目要你在柱状图里找到最大矩形面积。关键在于固定某根柱子当最矮高度，然后往左右找到第一个更矮的位置，所以这是单调栈的经典题。

**Python 代码**

```python
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                ans = max(ans, height * width)
            stack.append(i)

        heights.pop()
        return ans
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(n)`。

**怎么想到这个方法**

看到“每根柱子向左右扩展到哪里”，就要想到找左右第一个更小元素，这正是单调栈的拿手戏。

**示例 case**

- 输入：`heights = [2,1,5,6,2,3]`
- 输出：`10`。最大矩形由高度 `5,6` 这段组成。

**常见 Follow-up**

- 如果是二维 `maximal rectangle`，怎么降维？
- 为什么结尾常常补一个 0？

### 8. Trapping Rain Water

**这个题型 / 算法点的总结**

`Trapping Rain Water` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

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

**示例 case**

- 输入：`height = [0,1,0,2,1,0,1,3,2,1,2,1]`
- 输出：`6`。每个位置的积水取决于左右最高板中的较小值。

**常见 Follow-up**

- 你能讲单调栈解法吗？
- 如果要输出每格积水量，需要额外存什么？

### 9. First Missing Positive

**这个题型 / 算法点的总结**

`First Missing Positive` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

如果数组长度是 `n`，那么答案一定在 `1..n+1` 之间。  
理想状态是把数字 `x` 放到下标 `x-1` 上。  
最后第一个不满足 `nums[i] == i+1` 的位置就是答案。

**Python 代码**

```python
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(1)` 原地。

**怎么想到这个方法**

数组值域落在 `1..n` 时，面试高频套路是把值尽量放回它应该在的位置，再扫描第一个不匹配的位置。

**示例 case**

- 输入：`nums = [3,4,-1,1]`
- 输出：`2`。原地放置后第一个不匹配的位置就是答案。

**常见 Follow-up**

- 为什么答案一定在 `1..n+1`？
- 用哈希集合能做，但为什么不是最优？

### 10. N-Queens

**这个题型 / 算法点的总结**

`N-Queens` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

在 `n x n` 棋盘上放 `n` 个皇后，要求互不攻击。典型回溯题，关键是列、主对角线、副对角线的冲突判断。

**Python 代码**

```python
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag1 = set()
        diag2 = set()
        board = [['.'] * n for _ in range(n)]
        ans = []

        def dfs(r: int) -> None:
            if r == n:
                ans.append([''.join(row) for row in board])
                return

            for c in range(n):
                if c in cols or r - c in diag1 or r + c in diag2:
                    continue
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)
                board[r][c] = 'Q'
                dfs(r + 1)
                board[r][c] = '.'
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)

        dfs(0)
        return ans
```

**时间复杂度**

`O(n!)` 量级，精确值取决于剪枝。

**空间复杂度**

`O(n)` 递归栈加集合。

**怎么想到这个方法**

题目让你枚举所有合法摆法，而且每行只能放一个皇后，这就是标准回溯。列和对角线冲突检查是剪枝重点。

**示例 case**

- 输入：`n = 4`
- 输出：两种合法摆法。回溯时每层放一行并检查列与对角线。

**常见 Follow-up**

- 如果只要求返回解的数量，怎么改？
- 位运算优化为什么会更快？

### 11. Edit Distance

**这个题型 / 算法点的总结**

`Edit Distance` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

题目要求把 `word1` 变成 `word2` 的最少操作数。每一步只有插入、删除、替换三种操作，所以状态转移非常标准。

**Python 代码**

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1],
                    )

        return dp[m][n]
```

**时间复杂度**

`O(mn)`。

**空间复杂度**

`O(mn)`；可压缩到 `O(n)`。

**怎么想到这个方法**

操作只有插入、删除、替换三种，所以二维 DP 非常自然。想清楚 `dp[i][j]` 的含义就能稳住。

**示例 case**

- 输入：`word1 = "horse"`, `word2 = "ros"`
- 输出：`3`。三步操作可完成转换。

**常见 Follow-up**

- 如果替换代价不是 1，状态怎么改？
- 如何压缩空间？

### 12. Minimum Window Substring

**这个题型 / 算法点的总结**

`Minimum Window Substring` 属于滑动窗口类问题，关键是想清楚窗口什么时候合法、什么时候需要收缩。

**题目含义**

先扩张窗口，直到它已经覆盖了 `t` 中所有需要的字符。  
然后尽量收缩左边界，找到最短合法窗口。  
核心是维护：

- `need`: 目标频率
- `window`: 当前窗口频率
- `have`: 当前已经满足的字符种类数

**Python 代码**

```python
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        window = {}
        have = 0
        need_count = len(need)

        res = [-1, -1]
        res_len = float("inf")
        left = 0

        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == need_count:
                if right - left + 1 < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                left += 1

        left, right = res
        return s[left:right + 1] if res_len != float("inf") else ""
```

**时间复杂度**

`O(m+n)`。

**空间复杂度**

`O(k)`。

**怎么想到这个方法**

题目要最短合法窗口，固定窗口不适合，应该想到可变滑窗。关键是先定义什么叫“窗口已经覆盖了 t”。

**示例 case**

- 输入：`s = "ADOBECODEBANC"`, `t = "ABC"`
- 输出：`"BANC"`。它是覆盖 `ABC` 的最短窗口。

**常见 Follow-up**

- 如果 `t` 中有重复字符，为什么需要计数而不是集合？
- 如果要返回长度而不是子串，代码怎么简化？

