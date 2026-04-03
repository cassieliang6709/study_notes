# 07 堆、Trie、贪心

---

## 第一部分：堆

### 识别信号

```text
// top k
// 数据流
// 不断取最小 / 最大
// 合并多个有序结构
```

### 模板

```text
// 保留前 k 大
for x in nums:
    heappush(heap, x)
    if len(heap) > k:
        heappop(heap)
```

重点题：

- `Kth Largest Element in an Array`
- `Top K Frequent Elements`
- `Merge k Sorted Lists`
- `Find Median from Data Stream`

---

## 第二部分：Trie

### 识别信号

```text
// 前缀
// 字典树
// 单词搜索 / 前缀匹配
```

### 模板

```text
class TrieNode:
    children = {}
    is_end = False
```

重点：

```text
// insert
// search
// startsWith
```

---

## 第三部分：贪心

### 识别信号

```text
// 局部最优能推出全局最优
// 维护最远覆盖
// 按最后出现位置切分
```

重点题：

### 1. Jump Game

```text
// 维护最远可达位置
```

### 2. Jump Game II

```text
// 当前步能覆盖到哪里
// 下一步最远能扩到哪里
```

### 3. Partition Labels

```text
// 当前段必须扩到段内所有字符最后出现位置的最远处
```

---

## 四、推荐刷题顺序

1. Kth Largest Element in an Array
2. Top K Frequent Elements
3. Merge k Sorted Lists
4. Find Median from Data Stream
5. Implement Trie
6. Jump Game
7. Jump Game II
8. Partition Labels

