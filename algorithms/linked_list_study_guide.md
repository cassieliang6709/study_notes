---
title: "Linked List 题目分类讲义"
---

# Linked List 题目分类讲义

这份笔记的目标很简单：

- 先把常见链表题按方法分类
- 再用简单、直白、适合初学者的 Python 写法整理
- 注释尽量解释“为什么这样连指针”
- 不追求炫技，不追求最短代码

---

## 一、分类总表

### 1. 基础指针操作 / 虚拟头结点

这类题的核心是：`dummy` 节点、顺着链表往后连、避免头节点单独判断。

1. `Merge Two Sorted Lists`
2. `Add Two Numbers`
3. `Remove Nth Node From End of List`
4. `Swap Nodes in Pairs`

### 2. 反转与重连

这类题的核心是：先想清楚哪一段要反转，反转后怎么重新接回去。

1. `Reverse Linked List`
2. `Reorder List`
3. `Reverse Nodes in k-Group`

### 3. 快慢指针 / 找环

这类题的核心是：一个指针走得快，一个指针走得慢，通过它们的相遇或位置关系解决问题。

1. `Linked List Cycle`
2. `Linked List Cycle II`
3. `Palindrome Linked List`
4. `Find The Duplicate Number`

### 4. 分治 / 归并 / 排序

这类题的核心是：拆成小问题，再把有序结果合并回来。

1. `Merge k Sorted Lists`
2. `Sort List`

### 5. 特殊结构处理

这类题不是普通单链表，需要额外注意结构特点。

1. `Copy List with Random Pointer`
2. `Intersection of Two Linked Lists`

### 6. 链表设计题

这类题不只是“做一遍遍历”，而是要自己设计数据结构。

1. `LRU Cache`

---

## 二、推荐刷题顺序

建议按下面顺序练：

1. `Reverse Linked List`
2. `Merge Two Sorted Lists`
3. `Linked List Cycle`
4. `Add Two Numbers`
5. `Remove Nth Node From End of List`
6. `Swap Nodes in Pairs`
7. `Linked List Cycle II`
8. `Intersection of Two Linked Lists`
9. `Palindrome Linked List`
10. `Reorder List`
11. `Merge k Sorted Lists`
12. `Sort List`
13. `Copy List with Random Pointer`
14. `Reverse Nodes in k-Group`
15. `LRU Cache`
16. `Find The Duplicate Number`

说明：

- `Find The Duplicate Number` 严格来说不是链表题
- 但是它非常适合放在“快慢指针找环”这组里一起理解

---

## 三、常用链表小技巧

### 1. `dummy` 虚拟头结点

当题目可能会改动头节点时，优先考虑加一个 `dummy`。

好处：

- 不用单独处理“删的是头节点”
- 不用单独处理“新链表第一个节点是谁”

### 2. 反转链表的三指针

最常见写法：

- `prev`：已经反转好的前一段
- `curr`：当前要处理的节点
- `nxt`：提前保存下一个节点，避免断链

### 3. 快慢指针

常见用途：

- 找中点
- 判断有环
- 找环入口

### 4. 画图

链表题非常适合画图。

特别是下面这些题，一定建议边画边想：

- `Swap Nodes in Pairs`
- `Reorder List`
- `Reverse Nodes in k-Group`
- `Copy List with Random Pointer`
- `LRU Cache`

---

## 四、逐题整理

---

## 1. Reverse Linked List

### 题目目标

把一个单链表整个反转。

### 这题属于哪一类

属于“反转与重连”。

这是最基础的链表反转题，很多更难的链表题本质上都是“先切一段，再反转，再接回去”。

### 核心思路

每次把当前节点 `curr` 的指针方向改掉，让它指向前一个节点 `prev`。

处理完后整体方向就反过来了。

### 分步骤理解

1. 一开始 `prev = None`，因为反转后原来的头节点会变成尾节点，它后面应该接 `None`
2. `curr` 从头节点开始往后走
3. 先保存 `curr.next`，因为等会儿要改指针，改完就找不到后面了
4. 让 `curr.next = prev`
5. 再整体往前推进：`prev = curr`，`curr = nxt`
6. 最后 `prev` 就是新的头节点

### Python 代码

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            # 先保存下一个节点，避免改完指针后找不到后面
            nxt = curr.next

            # 当前节点反过来指向前一个节点
            curr.next = prev

            # 两个指针一起往前走
            prev = curr
            curr = nxt

        # 循环结束后，prev 就是新的头节点
        return prev
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

### 容易错的点

- 忘记先保存 `curr.next`
- 最后返回的是 `prev`，不是 `curr`

### 边界情况

- 空链表
- 只有一个节点

---

## 2. Merge Two Sorted Lists

### 题目目标

把两个有序链表合并成一个新的有序链表。

### 这题属于哪一类

属于“基础指针操作 / 虚拟头结点”。

### 核心思路

用一个 `dummy` 节点作为新链表的开头，再用 `tail` 一直往后接较小的那个节点。

### 分步骤理解

1. 建一个 `dummy`，方便最后返回结果
2. 用 `tail` 表示“新链表当前最后一个节点”
3. 比较 `list1.val` 和 `list2.val`
4. 谁小就把谁接到 `tail.next`
5. 被接走的那个链表往后走一步
6. `tail` 也往后走一步
7. 其中一个链表走完后，另一个链表剩下的部分直接接上

### Python 代码

```python
class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            # 新链表的尾巴往后走
            tail = tail.next

        # 把剩下没走完的链表直接接上
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next
```

### 复杂度

- 时间复杂度：`O(m + n)`
- 空间复杂度：`O(1)`

### 容易错的点

- 忘记写 `dummy`
- 循环结束后忘记把剩余链表接上

### 边界情况

- 一个链表为空
- 两个链表都为空

---

## 3. Linked List Cycle

### 题目目标

判断链表里是否有环。

### 这题属于哪一类

属于“快慢指针 / 找环”。

### 核心思路

慢指针每次走一步，快指针每次走两步。

如果有环，它们迟早会相遇；如果没有环，快指针会先走到空。

### 分步骤理解

1. `slow` 和 `fast` 都从头节点开始
2. `slow` 每轮走一步
3. `fast` 每轮走两步
4. 如果某一时刻 `slow == fast`，说明有环
5. 如果 `fast` 或 `fast.next` 是空，说明走到头了，没有环

### Python 代码

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

### 容易错的点

- 循环条件必须写成 `while fast and fast.next`
- 不要写成只判断 `fast`

### 边界情况

- 空链表
- 一个节点自己指向自己

---

## 4. Add Two Numbers

### 题目目标

两个链表分别表示两个非负整数，每个节点存一位，按倒序存储。求它们的和。

### 这题属于哪一类

属于“基础指针操作 / 虚拟头结点”。

### 核心思路

像手算加法一样，一位一位相加，同时维护进位 `carry`。

### 分步骤理解

1. 用 `dummy` 和 `tail` 维护结果链表
2. 只要 `l1`、`l2`、`carry` 有任何一个还没结束，就继续
3. 当前位的和 = `x + y + carry`
4. 当前节点保存 `total % 10`
5. 新的进位是 `total // 10`
6. 两个链表分别往后走

### Python 代码

```python
class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10
            digit = total % 10

            tail.next = ListNode(digit)
            tail = tail.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
```

### 复杂度

- 时间复杂度：`O(max(m, n))`
- 空间复杂度：`O(max(m, n))`

### 容易错的点

- 最后可能还有一个进位，不能漏
- 短链表走完后，当前位要按 `0` 处理

### 边界情况

- 两个链表长度不同
- 最后一位还要继续进位，比如 `9 + 1`

---

## 5. Remove Nth Node From End of List

### 题目目标

删除链表的倒数第 `n` 个节点。

### 这题属于哪一类

属于“基础指针操作 / 虚拟头结点”。

### 核心思路

用快慢指针保持固定距离。

让 `fast` 先走 `n + 1` 步，这样当 `fast` 到头时，`slow` 正好停在待删除节点的前一个位置。

### 分步骤理解

1. 建 `dummy`，让删除头节点也变成普通情况
2. `slow` 和 `fast` 都从 `dummy` 开始
3. 先让 `fast` 走 `n + 1` 步
4. 然后 `slow` 和 `fast` 一起走
5. 当 `fast` 走到空时，`slow.next` 就是要删除的节点
6. 让 `slow.next = slow.next.next`

### Python 代码

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # fast 先走 n + 1 步，这样 slow 才能停在待删除节点的前一个位置
        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        # 删除 slow 后面的那个节点
        slow.next = slow.next.next

        return dummy.next
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

### 容易错的点

- `fast` 要先走 `n + 1` 步，不是 `n` 步
- 一定要用 `dummy`，不然删头节点不好处理

### 边界情况

- 删除头节点
- 链表长度刚好等于 `n`

---

## 6. Swap Nodes in Pairs

### 题目目标

每两个节点交换一次位置。

例如：`1->2->3->4` 变成 `2->1->4->3`

### 这题属于哪一类

属于“基础指针操作 / 虚拟头结点”。

### 核心思路

每次抓出两个节点，手动重新连边。

### 分步骤理解

假设当前要交换的两个节点是：

- `first`
- `second`

前面那个节点记作 `prev`

原来是：

`prev -> first -> second -> next_pair`

交换后要变成：

`prev -> second -> first -> next_pair`

### Python 代码

```python
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            # 第一步：让 first 指向下一组的开头
            first.next = second.next

            # 第二步：让 second 指回 first
            second.next = first

            # 第三步：让前面的部分接上 second
            prev.next = second

            # prev 往后跳到这一组交换后的尾巴
            prev = first

        return dummy.next
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

### 容易错的点

- 三条边的连接顺序不能乱
- 交换完之后，`prev` 要走到 `first`

### 边界情况

- 空链表
- 只有一个节点
- 节点个数是奇数

---

## 7. Linked List Cycle II

### 题目目标

如果链表有环，返回入环的第一个节点；如果没有环，返回 `None`。

### 这题属于哪一类

属于“快慢指针 / 找环”。

### 核心思路

第一步先判断会不会相遇。

如果相遇了，再让一个指针回到头节点，然后两个指针都每次走一步，它们再次相遇的地方就是环入口。

### 分步骤理解

1. 用快慢指针找第一次相遇点
2. 如果没有相遇，直接返回 `None`
3. 相遇后，让一个指针回到 `head`
4. 两个指针都改成每次走一步
5. 它们再次相遇的位置就是入环点

### Python 代码

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # 一个指针回到头节点
                ptr = head

                # ptr 和 slow 再次相遇的位置就是环入口
                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next

                return ptr

        return None
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

### 容易错的点

- 相遇后不是直接返回相遇点
- 要让一个指针回到头节点，再一起一步一步走

### 边界情况

- 无环
- 环从头节点开始

---

## 8. Intersection of Two Linked Lists

### 题目目标

找到两个单链表相交的起点。

### 这题属于哪一类

属于“特殊结构处理”。

### 核心思路

让两个指针分别走两条链表。

一个走完 A 就去走 B，另一个走完 B 就去走 A。

这样两人走过的总长度一样，最终会在相交点相遇；如果不相交，就一起走到 `None`。

### 分步骤理解

1. `pA` 从 `headA` 出发
2. `pB` 从 `headB` 出发
3. 走到空后，不停止，而是跳到另一条链表头部
4. 最终：
   - 相交：在相交点相遇
   - 不相交：在 `None` 相遇

### Python 代码

```python
class Solution:
    def getIntersectionNode(
        self,
        headA: ListNode,
        headB: ListNode
    ) -> Optional[ListNode]:
        pA = headA
        pB = headB

        while pA != pB:
            if pA:
                pA = pA.next
            else:
                pA = headB

            if pB:
                pB = pB.next
            else:
                pB = headA

        return pA
```

### 复杂度

- 时间复杂度：`O(m + n)`
- 空间复杂度：`O(1)`

### 容易错的点

- 比较的是节点本身，不是节点值
- 不相交时，最后返回的是 `None`

### 边界情况

- 两个链表不相交
- 相交点就是头节点

---

## 9. Palindrome Linked List

### 题目目标

判断链表是不是回文。

### 这题属于哪一类

属于“快慢指针 / 找环”这一组里的“快慢指针找中点”。

### 核心思路

1. 找到链表中点
2. 反转后半段
3. 比较前半段和后半段是否一样

### 分步骤理解

1. 用快慢指针找中点
2. 把从 `slow` 开始的后半段反转
3. 用两个指针分别从头部和后半段头部出发比较
4. 只要有一个值不同，就不是回文

### Python 代码

```python
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # 找到中点
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 反转后半段
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # prev 现在是反转后半段的头节点
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

### 容易错的点

- 比较时只需要比较后半段长度
- 奇数长度时，中间那个节点自然可以跳过，不需要额外处理

### 边界情况

- 单节点
- 偶数长度回文
- 奇数长度回文

---

## 10. Reorder List

### 题目目标

把链表从：

`L0 -> L1 -> ... -> Ln`

改成：

`L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 ...`

### 这题属于哪一类

属于“反转与重连”。

### 核心思路

这题经典三步：

1. 找中点
2. 反转后半段
3. 两段交替合并

### 分步骤理解

1. 用快慢指针找中点
2. 把后半段切下来
3. 反转后半段
4. 前半段和后半段轮流取节点拼起来

### Python 代码

```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 第一步：找中点
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 第二步：反转后半段
        second = slow.next
        slow.next = None

        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 第三步：合并前半段和反转后的后半段
        first = head
        second = prev

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

### 容易错的点

- 一定要先 `slow.next = None` 把前后两段断开
- 合并时要先保存两个“下一步”节点

### 边界情况

- 只有 1 个或 2 个节点
- 奇数长度
- 偶数长度

---

## 11. Merge k Sorted Lists

### 题目目标

合并 `k` 个有序链表。

### 这题属于哪一类

属于“分治 / 归并 / 排序”。

### 核心思路

如果一个一个合并，会比较慢。

更好的办法是像归并排序那样，两两合并。

### 分步骤理解

1. 把 `lists` 看成一个数组
2. 每轮把它们两两合并
3. 合并完后，链表总数减半
4. 最后只剩一个链表，就是答案

### Python 代码

```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                if i + 1 < len(lists):
                    list2 = lists[i + 1]
                else:
                    list2 = None

                merged_lists.append(self.merge_two_lists(list1, list2))

            lists = merged_lists

        return lists[0]

    def merge_two_lists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next
```

### 复杂度

- 时间复杂度：`O(N log k)`
  - `N` 是所有节点总数
- 空间复杂度：`O(1)` 或 `O(log k)` 取决于你是否把辅助数组算进去

### 容易错的点

- `k` 是奇数时，最后一个链表要原样留下来参与下一轮
- 不要一个一个顺序合并，那样效率更低

### 边界情况

- `lists` 为空
- 只有一个链表
- 某些链表为空

---

## 12. Sort List

### 题目目标

对链表进行排序，要求时间复杂度尽量好。

### 这题属于哪一类

属于“分治 / 归并 / 排序”。

### 核心思路

链表最适合用归并排序。

因为：

- 数组适合随机访问，所以常用快排或归并
- 链表不适合随机访问，但特别适合从中间切开，再合并两个有序链表

### 分步骤理解

1. 如果链表长度是 0 或 1，直接返回
2. 用快慢指针找中点，把链表切成两半
3. 分别排序左半边和右半边
4. 再把两个有序链表合并起来

### Python 代码

```python
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 找中点，并把链表切成两半
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        left = self.sortList(head)
        right = self.sortList(slow)

        return self.merge(left, right)

    def merge(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next
```

### 复杂度

- 时间复杂度：`O(n log n)`
- 空间复杂度：`O(log n)`，主要来自递归栈

### 容易错的点

- 找到中点后一定要断开：`prev.next = None`
- 不断开的话，递归会陷入死循环

### 边界情况

- 空链表
- 单节点
- 已经有序
- 含重复值

---

## 13. Copy List with Random Pointer

### 题目目标

复制一个带有 `next` 和 `random` 指针的链表。

### 这题属于哪一类

属于“特殊结构处理”。

### 核心思路

最容易理解的方法是：用哈希表记录“原节点 -> 新节点”的对应关系。

第一遍先把所有新节点创建出来。

第二遍再把 `next` 和 `random` 连好。

### 分步骤理解

1. 第一遍遍历：
   - 每看到一个旧节点，就创建一个对应的新节点
   - 存到字典里
2. 第二遍遍历：
   - 新节点的 `next` 指向“旧节点的 next 对应的新节点”
   - 新节点的 `random` 指向“旧节点的 random 对应的新节点”

### Python 代码

```python
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {}

        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            new_node = old_to_new[curr]

            if curr.next:
                new_node.next = old_to_new[curr.next]
            else:
                new_node.next = None

            if curr.random:
                new_node.random = old_to_new[curr.random]
            else:
                new_node.random = None

            curr = curr.next

        return old_to_new[head]
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(n)`

### 容易错的点

- 复制的不是值，而是整个节点关系
- `random` 可能是 `None`

### 边界情况

- 空链表
- `random` 全是 `None`
- `random` 指向自己

---

## 14. Reverse Nodes in k-Group

### 题目目标

每 `k` 个节点为一组进行反转；如果最后剩下的节点不足 `k` 个，就保持不变。

### 这题属于哪一类

属于“反转与重连”。

### 核心思路

这题可以理解成：

- 不断找到一段长度刚好为 `k` 的区间
- 把这段反转
- 再接回原链表

### 分步骤理解

1. 用 `dummy` 统一处理头节点
2. `group_prev` 表示“这一组前面的那个节点”
3. 先检查从 `group_prev.next` 开始，后面够不够 `k` 个节点
4. 如果不够，直接结束
5. 如果够，就把这一组反转
6. 反转后再把前后接起来
7. `group_prev` 跳到这一组反转后的尾巴，准备处理下一组

### Python 代码

```python
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = group_prev

            # 先找到这一组的第 k 个节点
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next

            # 反转这一组
            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # 反转前，group_prev.next 是这一组的头
            # 反转后，它变成这一组的尾
            old_group_head = group_prev.next

            # 把前面的部分接到反转后的新头
            group_prev.next = kth

            # group_prev 移动到这一组新的尾巴
            group_prev = old_group_head
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

### 容易错的点

- 不足 `k` 个时不要反转
- 反转时让 `prev` 从 `group_next` 开始，这样尾巴才能自动接回去

### 边界情况

- `k = 1`
- 链表长度小于 `k`
- 链表长度不是 `k` 的整数倍

---

## 15. LRU Cache

### 题目目标

设计一个数据结构，支持：

- `get(key)`：查询 key
- `put(key, value)`：插入或更新 key

并且要求最近最少使用的数据优先被淘汰。

### 这题属于哪一类

属于“链表设计题”。

### 核心思路

这是标准组合：

- 哈希表：负责 `O(1)` 找到节点
- 双向链表：负责 `O(1)` 删除节点、移动节点、插入到头部

为什么要双向链表？

因为要把任意节点快速删掉，只用单链表不方便。

### 设计思路

我们维护一个双向链表，表示“使用顺序”：

- 链表头部：最近刚使用的
- 链表尾部：最久没使用的

同时维护一个字典：

- `key -> 对应的链表节点`

### 需要的辅助操作

1. `remove(node)`：把一个节点从双向链表里删掉
2. `insert_to_front(node)`：把节点插到头部
3. `move_to_front(node)`：先删再插，表示它刚被使用过
4. `remove_lru()`：删除尾部前面的那个真实节点

### Python 代码

```python
class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # 用两个哨兵节点，避免头尾插入删除时写很多特殊判断
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert_to_front(self, node: Node) -> None:
        first_real_node = self.head.next

        node.next = first_real_node
        node.prev = self.head

        self.head.next = node
        first_real_node.prev = node

    def move_to_front(self, node: Node) -> None:
        self.remove(node)
        self.insert_to_front(node)

    def remove_lru(self) -> Node:
        # tail 前面的那个节点，就是最久没使用的节点
        lru_node = self.tail.prev
        self.remove(lru_node)
        return lru_node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # 被访问过，就要移动到最前面
        self.move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_front(node)
            return

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert_to_front(new_node)

        if len(self.cache) > self.capacity:
            lru_node = self.remove_lru()
            del self.cache[lru_node.key]
```

### 复杂度

- `get` 时间复杂度：`O(1)`
- `put` 时间复杂度：`O(1)`
- 空间复杂度：`O(capacity)`

### 容易错的点

- 用的是双向链表，不是单链表
- 更新已有 key 时，不是新增，而是改值并移动到头部
- 淘汰的是尾部前面的真实节点，不是尾哨兵

### 边界情况

- 容量为 1
- 重复 `put` 同一个 key
- `get` 一个不存在的 key

---

## 16. Find The Duplicate Number

### 题目目标

给定一个长度为 `n + 1` 的数组，数字范围是 `1` 到 `n`，其中只有一个数字重复，找出这个重复数字。

### 这题属于哪一类

严格来说它不是链表题。

但它非常适合和“链表找环”一起学，因为它本质上用了同一个思想。

### 为什么能当成找环

把数组下标当成节点，把“值”当成下一跳的位置：

- 从下标 `0` 出发
- 下一步去 `nums[0]`
- 再下一步去 `nums[nums[0]]`

因为数字范围是 `1` 到 `n`，而数组长度是 `n + 1`，所以一定会形成环。

那个重复数字，就对应环的入口。

### 核心思路

和 `Linked List Cycle II` 完全同款：

1. 先用快慢指针找到相遇点
2. 再让一个指针回到起点
3. 两个指针每次都走一步
4. 再次相遇的位置就是重复数字

### Python 代码

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        # 第一步：先找到相遇点
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # 第二步：一个指针回到起点
        ptr = nums[0]

        while ptr != slow:
            ptr = nums[ptr]
            slow = nums[slow]

        return ptr
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

### 容易错的点

- 这题不能排序后直接改数组，也不能用额外哈希表
- 它的重点正是“把数组想成链表上的 next 指针”

### 边界情况

- 重复数字出现多次
- 重复数字刚好较小或较大

---

## 五、最后做一遍方法总结

### 1. 什么时候先想 `dummy`

出现下面情况时，优先考虑 `dummy`：

- 可能删头节点
- 可能换头节点
- 需要构造新链表

代表题：

- `Merge Two Sorted Lists`
- `Add Two Numbers`
- `Remove Nth Node From End of List`
- `Swap Nodes in Pairs`

### 2. 什么时候先想快慢指针

出现下面情况时，优先考虑快慢指针：

- 找中点
- 判断有环
- 找环入口
- 结构上需要“一前一后”关系

代表题：

- `Linked List Cycle`
- `Linked List Cycle II`
- `Palindrome Linked List`
- `Find The Duplicate Number`

### 3. 什么时候先想“切开 + 反转 + 合并”

代表题：

- `Reorder List`
- `Reverse Nodes in k-Group`

### 4. 什么时候先想归并

代表题：

- `Merge k Sorted Lists`
- `Sort List`

### 5. 什么时候需要“哈希表 + 链表”

代表题：

- `Copy List with Random Pointer`
- `LRU Cache`

---

## 六、复习建议

如果你想真正把这些题做熟，建议每次复习时不要只是看答案，而是按下面顺序练：

1. 先口头说出这题属于哪一类
2. 先不写代码，只画图说清楚指针怎么走
3. 再写代码
4. 写完后自己检查：
   - 有没有断链
   - 有没有漏掉头节点情况
   - 有没有漏掉空链表
   - 有没有把最后一段正确接回去

如果你愿意，我下一步可以继续把这份笔记升级成更适合背诵的版本，比如：

- 每题再补一个“小例子手推过程”
- 每题再补“面试时怎么口述思路”
- 再单独整理一份“链表万能模板总结”

---

## Quiz

**Q1: 为什么链表题经常需要 `dummy` 虚拟头节点？**

- [ ] 为了节省空间
- [ ] 让代码更慢
- [ ] 避免处理头节点为空或头节点被删除的边界情况 ✅
- [ ] Python 语法要求

**Q2: 快慢指针找链表中点，慢指针每次走 1 步，快指针走几步？**

- [ ] 1 步
- [ ] 2 步 ✅
- [ ] 3 步
- [ ] 跳到末尾

**Q3: 反转链表的三指针法，`prev` 初始值应该是什么？**

- [ ] `head`
- [ ] `head.next`
- [ ] `None` ✅
- [ ] 链表尾节点

**Q4: 判断链表是否有环，快指针追上慢指针说明什么？**

- [ ] 链表长度为偶数
- [ ] 链表没有环
- [ ] 链表有环 ✅
- [ ] 快慢指针同时到达尾节点

**Q5: `Merge k Sorted Lists` 最优解法是什么？**

- [ ] 暴力拼接后排序
- [ ] 两两合并，时间复杂度 O(kN)
- [ ] 用最小堆维护 k 个指针，时间复杂度 O(N log k) ✅
- [ ] 递归合并
