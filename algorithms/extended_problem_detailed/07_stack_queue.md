---
title: "07 栈与队列详细教学"
---

# 07 栈与队列详细教学

---

## 一、什么时候想到栈

```text
// 括号匹配
// 表达式求值
// 最近更大更小
// 等未来信息
```

---

## 二、代表题

### Valid Parentheses

**这个题型 / 算法点的总结**

`Valid Parentheses` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

这是最基础的栈题。  
遇到左括号就入栈，遇到右括号就检查栈顶是否是对应的左括号。

**代表 Python 代码**

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

先看题型识别里的信号：这题本质上就是 `括号匹配 / Parenthesis Matching`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：`s = "()[]{}"`
- 输出：`True`。每个右括号都能匹配最近的对应左括号。

**常见 Follow-up**

- 能不能把空间复杂度再压缩一层？
- 有没有另一种常见模板也能解决这题？

### Simplify Path

**这个题型 / 算法点的总结**

`Simplify Path` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

Unix 路径里：

- `.` 表示当前目录，忽略
- `..` 表示回到上一级，弹栈
- 普通字符串表示进入子目录，入栈

最后把栈里的目录重新拼起来即可。

**代表 Python 代码**

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for part in path.split("/"):
            if part == "" or part == ".":
                continue
            if part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(n)`。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `路径栈模拟 / Stack-based Path Simulation`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：一个最小可手算的样例
- 输出：先手推一遍算法流程，再对照代码中的循环、状态或数据结构变化。

**常见 Follow-up**

- 能不能把空间复杂度再压缩一层？
- 有没有另一种常见模板也能解决这题？

### Decode String

**这个题型 / 算法点的总结**

`Decode String` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

当遇到 `[` 时，说明当前字符串和重复次数要暂存起来，进入新层级。  
当遇到 `]` 时，从栈里弹出之前的状态，把当前字符串按次数展开再接回去。

**代表 Python 代码**

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

`O(n * expanded_length)`，通常记作 `O(n)` 到输出规模。

**空间复杂度**

`O(n)`。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `嵌套解码 / Nested Decoding with Stack`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：`s = "3[a2[c]]"`
- 输出：`accaccacc`。内层先展开，再乘上外层次数。

**常见 Follow-up**

- 能不能把空间复杂度再压缩一层？
- 有没有另一种常见模板也能解决这题？

### Basic Calculator / II / III

**这个题型 / 算法点的总结**

`Basic Calculator / II / III` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

这组题是在一条主线上递进的：`II` 先掌握乘除即时结算，`I` 和 `III` 再把括号嵌套加回来。核心仍然是把运算符优先级拆成可维护的状态。

**代表 Python 代码**

```python
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = "+"

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if ch in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                sign = ch
                num = 0

        return sum(stack)
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(n)`。

**怎么想到这个方法**

表达式题先别被细节吓到，先拆成两件事：数字怎么读完整，优先级怎样在扫描时局部结算。

**示例 case**

- 输入：一个最小可手算的样例
- 输出：先手推一遍算法流程，再对照代码中的循环、状态或数据结构变化。

**常见 Follow-up**

- 加入括号后，为什么通常需要额外栈或递归？
- 为什么除法要特别注意 Python 的取整方向？

### Longest Valid Parentheses

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

**代表 Python 代码**

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

先看题型识别里的信号：这题本质上就是 `栈 + 下标 / Stack with Indices`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：`s = ")()())"`
- 输出：`4`。最长合法括号子串是 `()()`。

**常见 Follow-up**

- 能不能把空间复杂度再压缩一层？
- 有没有另一种常见模板也能解决这题？

### Trapping Rain Water

**这个题型 / 算法点的总结**

`Trapping Rain Water` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

这题可以用单调栈，也可以用双指针。  
双指针更直观：

- 左边能装多少水取决于 `left_max`
- 右边能装多少水取决于 `right_max`

每次先处理较低的一边，因为它的装水上限已经确定。

**代表 Python 代码**

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

`O(1)` 双指针版。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `双指针 / Two Pointers`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：`height = [0,1,0,2,1,0,1,3,2,1,2,1]`
- 输出：`6`。每个位置的积水取决于左右最高板中的较小值。

**常见 Follow-up**

- 如果输入先排序或已经有序，能不能进一步简化？
- 如果要返回具体区间或下标，代码里要额外维护什么？

### Exclusive Time of Functions

**这个题型 / 算法点的总结**

`Exclusive Time of Functions` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

栈顶函数是当前正在运行的函数。  
当新函数开始时，之前的函数先累计运行时间。  
当函数结束时，把自己从栈里弹出，并更新结束时间。

**代表 Python 代码**

```python
from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        prev = 0

        for log in logs:
            fid, typ, time = log.split(":")
            fid, time = int(fid), int(time)

            if typ == "start":
                if stack:
                    ans[stack[-1]] += time - prev
                stack.append(fid)
                prev = time
            else:
                ans[stack.pop()] += time - prev + 1
                prev = time + 1

        return ans
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(n)`。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `调用栈模拟 / Call Stack Simulation`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：一个最小可手算的样例
- 输出：先手推一遍算法流程，再对照代码中的循环、状态或数据结构变化。

**常见 Follow-up**

- 能不能把空间复杂度再压缩一层？
- 有没有另一种常见模板也能解决这题？

