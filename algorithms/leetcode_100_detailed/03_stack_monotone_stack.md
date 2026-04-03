---
title: "03 栈与单调栈"
---

# 03 栈与单调栈

---

## 一、什么时候想到栈

```text
// 匹配
// 嵌套
// 最近一个更大 / 更小
// 按顺序等待未来信息
```

---

## 二、普通栈和单调栈区别

```text
// 普通栈：处理括号、表达式、递归展开
// 单调栈：处理 next greater / previous smaller 一类题
```

---

## 三、普通栈模板

```text
for ch in s:
    if 是开括号或需要延后处理的信息:
        push
    else:
        pop 并验证
```

---

## 四、单调栈模板

```text
stack = []

for i, x in enumerate(nums):
    while stack and nums[stack[-1]] < x:
        idx = stack.pop()
        // 当前 x 是 idx 的下一个更大值
    stack.append(i)
```

---

## 五、重点题

### 1. Valid Parentheses

**这个题型 / 算法点的总结**

`Valid Parentheses` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

这是最基础的栈题。  
遇到左括号就入栈，遇到右括号就检查栈顶是否是对应的左括号。

**Python 代码**

```python
class Solution:
    def isValid(self, s: str) -> bool:
        mp = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch in mp:
                if not stack or stack.pop() != mp[ch]:
                    return False
            else:
                stack.append(ch)

        return not stack
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(n)`。

**怎么想到这个方法**

看到括号匹配、嵌套结构、最近未匹配元素，这三个信号基本就能直接想到栈。

**示例 case**

- 输入：`s = "()[]{}"`
- 输出：`True`。每个右括号都能匹配最近的对应左括号。

**常见 Follow-up**

- 如果括号种类变多，代码需要变吗？
- 如果要求返回第一个非法位置怎么办？

### 2. Min Stack

**这个题型 / 算法点的总结**

`Min Stack` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

设计一个栈，同时支持 `getMin()` 返回当前最小值。关键是让最小值也跟着栈同步维护，而不是每次现扫一遍。

**Python 代码**

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

**时间复杂度**

`O(1)` 每次操作。

**空间复杂度**

`O(n)`。

**怎么想到这个方法**

设计题里一旦某个查询要做到 `O(1)`，就要问自己能不能在写入时把未来查询需要的信息一并维护起来。这里就是同步维护最小值栈。

**示例 case**

- 操作：`push(-2)`, `push(0)`, `push(-3)`, `getMin()`
- 输出：`-3`。最小值要和主栈同步维护。

**常见 Follow-up**

- 如果要支持 `getMax()` 呢？
- 能不能每个栈节点直接存当前最小值？

### 3. Decode String

**这个题型 / 算法点的总结**

`Decode String` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

当遇到 `[` 时，说明当前字符串和重复次数要暂存起来，进入新层级。  
当遇到 `]` 时，从栈里弹出之前的状态，把当前字符串按次数展开再接回去。

**Python 代码**

```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_num = 0
        cur_str = ""

        for ch in s:
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)
            elif ch == "[":
                stack.append((cur_str, cur_num))
                cur_str = ""
                cur_num = 0
            elif ch == "]":
                prev_str, num = stack.pop()
                cur_str = prev_str + num * cur_str
            else:
                cur_str += ch

        return cur_str
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(n)`。

**怎么想到这个方法**

字符串解码一看到嵌套括号，就要想到用栈保存“进入括号之前”的状态。每遇到 `]` 就把当前片段弹出并展开。

**示例 case**

- 输入：`s = "3[a2[c]]"`
- 输出：`accaccacc`。内层先展开，再乘上外层次数。

**常见 Follow-up**

- 如果出现多位数字，为什么当前写法依然对？
- 递归下降也能做，优缺点是什么？

### 4. Daily Temperatures

**这个题型 / 算法点的总结**

`Daily Temperatures` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

对每一天，题目要你找后面第一个更高温度出现的天数差。关键词是“下一个更大元素”，所以单调栈最合适。

**Python 代码**

```python
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)

        return ans
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(n)`。

**怎么想到这个方法**

“下一个更大元素”就是单调栈最经典的识别信号。栈里存还没找到答案的位置，并保持对应值单调。

**示例 case**

- 输入：`[73,74,75,71,69,72,76,73]`
- 输出：`[1,1,4,2,1,1,0,0]`。每个位置等到更高温度需要几天。

**常见 Follow-up**

- 如果问的是前一个更大元素呢？
- 如果不返回天数差，只返回温度值，怎么改？

### 5. Largest Rectangle in Histogram

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

### 6. Longest Valid Parentheses

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

