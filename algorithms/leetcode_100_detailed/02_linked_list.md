# 02 链表

链表题的本质只有几种操作：找中点、反转、删除、合并、断开再接回去。

---

## 一、先背这 5 个动作

```text
// 1. dummy 节点
// 2. 反转链表
// 3. 快慢指针找中点
// 4. 合并两个有序链表
// 5. 局部区间反转
```

---

## 二、必背模板

### 1. dummy 节点

```text
dummy = ListNode(0)
dummy.next = head
prev = dummy

// 删除、插入、交换节点时都更稳
```

### 2. 反转链表

```text
prev = None
cur = head

while cur:
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
```

### 3. 找中点

```text
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

### 4. 合并有序链表

```text
dummy = ListNode(0)
tail = dummy

while l1 and l2:
    // 接较小者

tail.next = l1 or l2
```

---

## 三、重点题详细讲

### 1. Reverse Linked List

识别：

```text
// 经典反转模板题
```

核心：

```text
// 每次先保存下一节点
// 再把当前 next 指回 prev
```

---

### 2. Merge Two Sorted Lists

识别：

```text
// 两个有序结构合并
=> 双指针 + dummy
```

注释模板：

```text
dummy = ListNode(0)
tail = dummy

while l1 and l2:
    if l1.val <= l2.val:
        tail.next = l1
        l1 = l1.next
    else:
        tail.next = l2
        l2 = l2.next
    tail = tail.next

tail.next = l1 or l2
```

---

### 3. Remove Nth Node From End of List

识别：

```text
// 倒数第 n 个
=> 快慢指针
```

核心：

```text
// fast 先走 n 步
// 然后 slow 和 fast 一起走
// fast 到尾时，slow 在待删节点前面
```

易错点：

- 删除头节点时没有 dummy

---

### 4. Add Two Numbers

识别：

```text
// 链表表示大整数，逐位相加
=> 模拟加法
```

模板：

```text
carry = 0

while l1 or l2 or carry:
    x = l1.val if l1 else 0
    y = l2.val if l2 else 0
    s = x + y + carry

    当前位 = s % 10
    carry = s // 10
```

---

### 5. Linked List Cycle / Cycle II

识别：

```text
// 有环
=> Floyd 快慢指针
```

记忆法：

```text
// 判环：能否相遇
// 找入口：一个回头，一个从相遇点出发，再次相遇即入口
```

---

### 6. Palindrome Linked List

思路：

```text
// 1. 找中点
// 2. 反转后半段
// 3. 前后比较
```

---

### 7. Intersection of Two Linked Lists

思路：

```text
// A 走完走 B
// B 走完走 A
// 两人路径长度被拉齐后会在交点相遇
```

---

### 8. Swap Nodes in Pairs

思路：

```text
// 每次操作两个节点
// dummy + prev 最方便
```

---

### 9. Copy List with Random Pointer

两种解法：

```text
// 解法 1：哈希表 old -> new
// 解法 2：节点穿插复制，空间 O(1)
```

建议：

```text
// 先会哈希表版本
// 再学穿插版本
```

---

### 10. Sort List

识别：

```text
// 链表排序
=> 归并排序
```

为什么不是快排：

```text
// 链表不适合随机访问
// 归并更自然
```

---

### 11. LRU Cache

识别：

```text
// O(1) get / put
=> 哈希表 + 双向链表
```

核心设计：

```text
// map[key] -> node
// 双向链表维护最近使用顺序
// 头部最新，尾部最旧
```

---

### 12. Merge k Sorted Lists

识别：

```text
// 多个有序链表合并
=> 堆
```

---

### 13. Reverse Nodes in k-Group

识别：

```text
// 局部反转 + 分组
=> 链表综合题
```

步骤：

```text
// 1. 看是否够 k 个
// 2. 记录下一段起点
// 3. 反转当前 k 段
// 4. 接回原链表
```

---

## 四、链表题复盘标准

每做一题都问自己：

```text
// 需不需要 dummy？
// 需不需要找中点？
// 需不需要反转？
// 要不要断开再接回去？
```

---

## 五、推荐刷题顺序

1. Reverse Linked List
2. Merge Two Sorted Lists
3. Linked List Cycle
4. Remove Nth Node From End of List
5. Add Two Numbers
6. Intersection of Two Linked Lists
7. Palindrome Linked List
8. Linked List Cycle II
9. Swap Nodes in Pairs
10. Copy List with Random Pointer
11. Sort List
12. LRU Cache
13. Merge k Sorted Lists
14. Reverse Nodes in k-Group

