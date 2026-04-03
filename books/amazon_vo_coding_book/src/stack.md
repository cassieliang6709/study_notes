# 4. 栈 / 表达式解析

## 面试题目怎么问

- 计算包含 `+ -` 和括号的表达式
- 计算包含 `+ - * /` 的字符串表达式
- 求逆波兰表达式的值
- 解析字符串中的嵌套结构
- 给你一串日志或命令块，块之间可以嵌套，要求还原执行结果

## 识别信号

- 输入是字符串表达式
- 有括号
- 有运算优先级
- 有嵌套上下文
- 有 `start/end`、`BEGIN/END`、`(`/`)`

## Amazon 风格业务包装

- 解析定价公式
- 计算折扣规则表达式
- 解析带括号的配置规则
- 处理日志或命令中的嵌套结构

## 你该怎么想

- 只要字符串里有括号、优先级、嵌套，就先想 stack
- 看到“当前上下文”和“进入新层级”，就想到入栈
- 退出一层时，要把内层结果合并回外层

## 标准代码模板 1：Basic Calculator

```python
def calculate(s):
    stack = []
    res = 0
    num = 0
    sign = 1

    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch in '+-':
            res += sign * num
            num = 0
            sign = 1 if ch == '+' else -1
        elif ch == '(':
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
        elif ch == ')':
            res += sign * num
            num = 0
            res *= stack.pop()
            res += stack.pop()

    return res + sign * num
```

## 标准代码模板 2：逆波兰表达式

```python
def eval_rpn(tokens):
    stack = []
    for token in tokens:
        if token not in "+-*/":
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))
    return stack[-1]
```

## 标准代码模板 3：Decode String

```python
def decode_string(s):
    stack = []
    cur_num = 0
    cur_str = ""

    for ch in s:
        if ch.isdigit():
            cur_num = cur_num * 10 + int(ch)
        elif ch == '[':
            stack.append((cur_str, cur_num))
            cur_str = ""
            cur_num = 0
        elif ch == ']':
            prev_str, num = stack.pop()
            cur_str = prev_str + cur_str * num
        else:
            cur_str += ch

    return cur_str
```

## 标准代码模板 4：Exclusive Time of Functions

```python
def exclusive_time(n, logs):
    res = [0] * n
    stack = []
    prev_time = 0

    for log in logs:
        fn_id, typ, t = log.split(':')
        fn_id = int(fn_id)
        t = int(t)

        if typ == "start":
            if stack:
                res[stack[-1]] += t - prev_time
            stack.append(fn_id)
            prev_time = t
        else:
            res[stack.pop()] += t - prev_time + 1
            prev_time = t + 1

    return res
```

## 标准代码模板 5：Reverse Parentheses

```python
def reverse_parentheses(s):
    stack = [""]
    for ch in s:
        if ch == '(':
            stack.append("")
        elif ch == ')':
            cur = stack.pop()[::-1]
            stack[-1] += cur
        else:
            stack[-1] += ch
    return stack[0]
```

## 代码讲解

- Basic Calculator：栈保存的是括号外层的 `res` 和 `sign`
- Decode String：栈保存的是外层字符串和重复次数
- Exclusive Time：栈保存的是函数调用栈，栈顶就是当前执行函数
- Reverse Parentheses：栈保存每一层正在构造的字符串

## 面试时怎么讲

- 这类题本质是单次扫描 + 保存上下文
- 遇到数字就持续构造当前数
- 遇到运算符就结算前一个数
- 遇到括号或新作用域，就把当前层上下文压栈，退出时再合并

## 常见 follow-up 和回答

**Q1：为什么要用栈？**  
因为括号意味着多层上下文嵌套，栈最适合保存进入新层级前的状态。

**Q2：如果再加 `* /` 怎么办？**  
可以用当前层栈即时处理乘除，或者双栈通用解析。

**Q3：怎么处理多位数？**  
`num = num * 10 + int(ch)`。

**Q4：怎么处理空格？**  
扫描时直接跳过。

**Q5：日志 start / end 为什么也是栈？**  
因为函数调用天然就是调用栈，进入一个函数压栈，结束时弹栈。

## Amazon 风格完整题面

> You are given a pricing rule string.  
> The string may contain integers, `+`, `-`, and parentheses.  
> Return the final computed value after evaluating the rule.

## 可直接背的口语回答稿

“我会把它看成标准表达式解析问题。因为括号代表进入一个新的上下文，所以我会顺序扫描字符串，用栈保存进入括号前的外层结果和符号。遇到数字就构造当前数，遇到加减就先把前一个数字结算进结果里；遇到右括号时，先算出括号内部的值，再乘上外层符号并加回外层结果。”

## 推荐代表题

- Basic Calculator
- Evaluate Reverse Polish Notation
- Decode String
- Exclusive Time of Functions

