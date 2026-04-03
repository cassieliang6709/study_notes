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

```text
// 看到括号匹配，第一反应就是栈
// 遇到右括号，就检查栈顶是否是对应左括号
```

### 2. Min Stack

```text
// 栈里每个位置额外记住当前最小值
// 这样 getMin 才能 O(1)
```

### 3. Decode String

```text
// 处理嵌套结构
// 每遇到 '['，把之前状态压栈
// 每遇到 ']'，把当前段展开回去
```

### 4. Daily Temperatures

```text
// 单调递减栈
// 当前更高温一出现，就把前面等待它的天数全部结算
```

### 5. Largest Rectangle in Histogram

核心理解：

```text
// 每个柱子都可能成为某个最大矩形的最矮柱
// 一旦它右边遇到更矮柱，它的“扩张边界”就确定了
```

### 6. Longest Valid Parentheses

两种方式：

```text
// 栈解法
// DP 解法
```

建议先学：

```text
// 先学栈解法，更直观
```

---

## 六、做题时的自检

```text
// 栈里存值，还是存下标？
// 是要找“下一个更大”，还是“上一个更小”？
// 弹栈时答案如何计算？
```

---

## 七、推荐刷题顺序

1. Valid Parentheses
2. Min Stack
3. Decode String
4. Daily Temperatures
5. Largest Rectangle in Histogram
6. Longest Valid Parentheses

