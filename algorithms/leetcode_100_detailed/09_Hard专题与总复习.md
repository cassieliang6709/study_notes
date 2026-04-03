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

```text
// 难点：不是合并
// 本质：partition 二分
```

### 2. Binary Tree Maximum Path Sum

```text
// 难点：返回值和全局答案不是一回事
```

### 3. Longest Valid Parentheses

```text
// 难点：状态设计不直观
```

### 4. Find Median from Data Stream

```text
// 难点：两个堆的平衡维护
```

### 5. Reverse Nodes in k-Group

```text
// 难点：分段 + 反转 + 接回去
```

### 6. Sliding Window Maximum

```text
// 难点：滑窗 + 单调队列
```

### 7. Largest Rectangle in Histogram

```text
// 难点：弹栈时宽度怎么计算
```

### 8. Trapping Rain Water

```text
// 难点：左右边界思维
```

### 9. First Missing Positive

```text
// 难点：原地映射
```

### 10. N-Queens

```text
// 难点：剪枝设计
```

### 11. Edit Distance

```text
// 难点：二维状态 + 三种操作
```

### 12. Minimum Window Substring

```text
// 难点：窗口合法条件维护
```

---

## 三、总复习方法

### 第 1 轮

```text
// 只追求做过
// 建立 pattern 感觉
```

### 第 2 轮

```text
// 同类题一起做
// 建立模板记忆
```

### 第 3 轮

```text
// 重做之前错题和慢题
// 训练无提示写出模板
```

---

## 四、最终检查清单

做题前问自己：

```text
// 这题最像哪个 pattern？
// 暴力为什么慢？
// 最优解的关键不变量是什么？
```

做题后问自己：

```text
// 这题以后遇到什么信号时我应该立刻想到？
// 我是不会模板，还是不会识别题型？
```

---

## 五、最后推荐的总顺序

如果你要真的把 Top 100 完整刷完，建议最终总顺序还是：

1. 数组 / 哈希 / 双指针
2. 链表
3. 栈 / 单调栈
4. 树 / BST
5. 二分 / 滑窗
6. 回溯 / 图
7. 堆 / Trie / 贪心
8. 动态规划
9. Hard 专题复刷

---

## 六、你下一步怎么用这套文档

最合理的方式：

1. 先刷 [01_数组哈希双指针.md](./01_数组哈希双指针.md)
2. 刷完一组后，把错题单独记到一个错题本
3. 每周回来看一次总路线图和 Hard 专题
