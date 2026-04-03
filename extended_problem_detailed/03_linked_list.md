---
title: "03 链表详细教学"
---

# 03 链表详细教学

链表题的核心动作：

```text
// dummy
// 找中点
// 反转
// 合并
// 局部断开再接回
```

---

## 代表题

### Reverse Linked List

```text
// 先记最标准反转模板
```

### Reverse Linked List II

```text
// 局部区间反转
// 常用 dummy + pre + 头插法
```

### Reorder List

```text
// 找中点
// 反转后半段
// 两段交错合并
```

### Remove Nth Node From End

```text
// 快慢指针
// fast 先走 n 步
```

### Add Two Numbers / Add Two Numbers II

```text
// 前者逆序模拟加法
// 后者通常用栈或先反转
```

### Merge k Sorted Lists

```text
// 堆
// 或分治归并
```

### Sort List

```text
// 链表归并排序
```

### Copy List with Random Pointer

```text
// 哈希表 old -> new
// 或穿插复制
```

---

## 建议顺序

1. Reverse Linked List
2. Remove Nth Node From End of List
3. Merge Two Sorted Lists
4. Add Two Numbers
5. Intersection of Two Linked Lists
6. Reorder List
7. Reverse Linked List II
8. Copy List with Random Pointer
9. Sort List
10. Merge k Sorted Lists
11. Add Two Numbers II


---

## Quiz

**Q1: `Reverse Linked List II`（反转 [left, right] 段），关键操作是什么？**

- [ ] 先找到 left 位置，再整段截出来反转后拼回
- [ ] 使用 dummy 节点，记录 left 前一个节点，局部反转后重新连接 ✅
- [ ] 把链表转成数组再操作
- [ ] 用递归反转整条链表

**Q2: `Reorder List`（L0→Ln→L1→Ln-1…）需要哪几步？**

- [ ] 直接遍历重排
- [ ] 找中点 → 反转后半段 → 交叉合并 ✅
- [ ] 转成栈再重建
- [ ] 用双端队列

**Q3: `Copy List with Random Pointer` 的关键挑战是什么？**

- [ ] 深拷贝普通 next 指针
- [ ] 在没有原节点地址的情况下设置 random 指针
- [ ] random 指针可能指向任意节点，需要先建立旧→新节点的映射 ✅
- [ ] 链表本身是循环的

**Q4: `Sort List` 的最优解法是什么，时间复杂度多少？**

- [ ] 冒泡排序，O(n²)
- [ ] 把链表转成数组排序，O(n log n) 但空间 O(n)
- [ ] 链表归并排序，O(n log n)，空间 O(log n) ✅
- [ ] 快速排序，O(n log n) 平均

**Q5: 找链表倒数第 k 个节点，双指针法怎么设置间距？**

- [ ] 两个指针同时出发
- [ ] 让快指针先走 k 步，再同时走 ✅
- [ ] 先求链表长度再计算
- [ ] 快指针走 k-1 步
