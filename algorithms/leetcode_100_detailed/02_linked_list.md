---
title: "02 链表"
---

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

**题目含义**

反转链表的标准做法是维护两个指针：

- `prev`：已经反转好的部分头节点
- `cur`：当前要处理的节点

每一步都先保存 `next`，再把当前节点指向 `prev`。

**Python 代码**

```python
from typing import Optional


class Solution:
    def reverseList(self, head: Optional['ListNode']) -> Optional['ListNode']:
        prev = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(1)`。

**怎么想到这个方法**

链表反转的核心不是背代码，而是每次改指针前先保住 `next`。面试里只要能稳定说清 `prev / cur / nxt` 三个角色就够了。

**常见 Follow-up**

- 递归版怎么写？
- 如果只反转区间 `[left, right]` 呢？

### 2. Merge Two Sorted Lists

**题目含义**

这题是链表里的最基础模板题。  
维护一个 `tail` 指针，每次把较小节点接到结果链表后面。

**Python 代码**

```python
from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional['ListNode'], list2: Optional['ListNode']) -> Optional['ListNode']:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2
        return dummy.next
```

**时间复杂度**

`O(m+n)`。

**空间复杂度**

`O(1)` 额外空间。

**怎么想到这个方法**

两个有序结构合并时，几乎总是双指针。链表版再加一个 `dummy` 节点，就能少掉大量头节点特判。

**常见 Follow-up**

- 如果是数组合并为什么常从后往前？
- 如果是 `k` 个有序链表怎么办？

### 3. Remove Nth Node From End of List

**题目含义**

让 `fast` 先走 `n` 步，然后 `slow` 和 `fast` 一起走。  
这样当 `fast` 到达末尾时，`slow` 正好在待删除节点前一个位置。

为什么要用 `dummy`：

- 如果删除的是头节点，`dummy` 能统一处理

**Python 代码**

```python
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional['ListNode'], n: int) -> Optional['ListNode']:
        dummy = ListNode(0, head)
        fast = slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(1)`。

**怎么想到这个方法**

“倒数第 n 个”是快慢指针的经典信号，让 `fast` 先走 `n` 步，就把“倒数”翻译成了“相隔固定距离的同向移动”。

**常见 Follow-up**

- 如果要求只遍历一遍，为什么快慢指针正合适？
- 为什么最好总是加 `dummy`？

### 4. Add Two Numbers

**题目含义**

这题和手算加法完全一样：

- 当前位 = 两个节点值 + 进位
- 结果节点保存 `total % 10`
- 新进位是 `total // 10`

因为输入本身是逆序，所以我们直接从头往后加。

**Python 代码**

```python
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional['ListNode'], l2: Optional['ListNode']) -> Optional['ListNode']:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + carry

            carry = total // 10
            cur.next = ListNode(total % 10)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
```

**时间复杂度**

`O(max(m,n))`。

**空间复杂度**

`O(1)` 额外空间，不计答案链表。

**怎么想到这个方法**

逐位相加、带进位，这和手算加法完全一致。题目把数字倒着存，其实就是在帮你从低位开始处理。

**常见 Follow-up**

- 如果链表是正序存储怎么办？
- 如果不能改原链表，如何处理？

### 5. Linked List Cycle / Cycle II

**题目含义**

这一组题的目标分别是：判断链表是否有环，以及找出环的入口。核心都是 Floyd 快慢指针。

**Python 代码**

```python
from typing import Optional


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

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(1)`。

**怎么想到这个方法**

只要问链表里有没有环，快慢指针几乎就是默认答案。进一步找入口时，记住“相遇点再和头节点同步走”这个结论。

**常见 Follow-up**

- 为什么相遇后从头和相遇点一起走会在入口相遇？
- 用哈希表也能做，差别是什么？

### 6. Palindrome Linked List

**题目含义**

判断链表是否为回文。标准做法是找中点、反转后半段，再从两头往中间比。

**Python 代码**

```python
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(1)`。

**怎么想到这个方法**

回文判断通常需要双端比较，但链表不能从尾往前走，所以要先把后半段反转，手动造出两个方向。

**常见 Follow-up**

- 比完之后要不要恢复链表？
- 如果只能用递归，空间代价是什么？

### 7. Intersection of Two Linked Lists

**题目含义**

让两个指针分别走：

- `A -> B`
- `B -> A`

这样走完以后，两者总路程相同，就会在交点相遇；如果没有交点，就一起走到 `None`。

**Python 代码**

```python
from typing import Optional


class Solution:
    def getIntersectionNode(self, headA: 'ListNode', headB: 'ListNode') -> Optional['ListNode']:
        a, b = headA, headB

        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a
```

**时间复杂度**

`O(m+n)`。

**空间复杂度**

`O(1)`。

**怎么想到这个方法**

两个指针分别走 `A+B` 和 `B+A`，总路程对齐后就能在交点相遇。这题的关键是把长度差自动抵消掉。

**常见 Follow-up**

- 为什么走完自己链表后切到另一条链表就能对齐？
- 哈希表写法和双指针写法怎么比较？

### 8. Swap Nodes in Pairs

**题目含义**

每两个相邻节点交换一次，本质是链表局部重连。`dummy` 节点能让头结点交换也保持统一写法。

**Python 代码**

```python
from typing import Optional


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            a = prev.next
            b = a.next

            prev.next = b
            a.next = b.next
            b.next = a
            prev = a

        return dummy.next
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(1)`。

**怎么想到这个方法**

看到“成对交换节点”，要想到这不是换值，而是换指针。`dummy + prev + a + b` 这四个指针关系最稳定。

**常见 Follow-up**

- 如果每 `k` 个交换一次，就是哪道题？
- 交换节点值和交换节点本身有什么区别？

### 9. Copy List with Random Pointer

**题目含义**

这题难点在于除了 `next` 之外还有 `random` 指针。  
最稳的写法是：

1. 第一遍创建所有新节点，建立 `旧节点 -> 新节点` 的映射
2. 第二遍连接 `next` 和 `random`

**Python 代码**

```python
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {}
        cur = head

        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            old_to_new[cur].next = old_to_new.get(cur.next)
            old_to_new[cur].random = old_to_new.get(cur.random)
            cur = cur.next

        return old_to_new[head]
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(n)` 哈希表版。

**怎么想到这个方法**

这题的难点不是遍历，而是节点之间有额外的 `random` 关系。最稳的思路是先建立旧节点到新节点的映射。

**常见 Follow-up**

- 你能讲 `O(1)` 额外空间的穿插复制法吗？
- 为什么要分两遍构造？

### 10. Sort List

**题目含义**

链表不适合快速排序，因为随机访问不方便。  
归并排序更自然：

1. 找中点拆成两半
2. 递归排序左右两半
3. 再合并两个有序链表

**Python 代码**

```python
from typing import Optional


class Solution:
    def sortList(self, head: Optional['ListNode']) -> Optional['ListNode']:
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def merge(self, a: Optional['ListNode'], b: Optional['ListNode']) -> Optional['ListNode']:
        dummy = ListNode()
        tail = dummy

        while a and b:
            if a.val <= b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a or b
        return dummy.next
```

**时间复杂度**

`O(n log n)`。

**空间复杂度**

`O(log n)` 递归栈；自底向上可做到 `O(1)` 额外空间。

**怎么想到这个方法**

链表不适合随机访问，所以别想快速排序那套。面试默认答案是链表归并排序：找中点、拆开、递归合并。

**常见 Follow-up**

- 为什么链表排序更偏向归并而不是快排？
- 你能写 bottom-up 版吗？

### 11. LRU Cache

**题目含义**

这题要求：

- `get` O(1)
- `put` O(1)

所以需要两部分：

- 哈希表：`key -> node`
- 双向链表：维护最近使用顺序

最近使用的放尾部，最久未使用的在头部后面。

**Python 代码**

```python
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])

        node = Node(key, value)
        self.map[key] = node
        self.insert(node)

        if len(self.map) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.map[lru.key]
```

**时间复杂度**

`O(1)` 均摊完成 `get/put`。

**空间复杂度**

`O(capacity)`。

**怎么想到这个方法**

一旦题目同时要“按 key 快速找”和“按最近使用顺序快速删”，就该想到 `HashMap + Doubly Linked List` 的双结构组合。

**常见 Follow-up**

- 如果变成 LFU，该多维护什么状态？
- 为什么必须是双向链表？

### 12. Merge k Sorted Lists

**题目含义**

合并两个有序链表可以双指针，但合并 `k` 个时最自然的是堆。  
堆里维护每条链表当前头节点：

- 每次弹出最小节点接到答案后面
- 再把它的 `next` 放回堆中

**Python 代码**

```python
import heapq
from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional['ListNode']]) -> Optional['ListNode']:
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        tail = dummy

        while heap:
            _, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
```

**时间复杂度**

`O(N log k)`。

**空间复杂度**

`O(k)`。

**怎么想到这个方法**

多个有序链表合并，本质就是反复拿当前最小值。只要 `k` 大于 2，最自然的优化就是最小堆。

**常见 Follow-up**

- 分治合并和堆解法怎么比较？
- 如果链表数量很少，是否直接两两合并更简单？

### 13. Reverse Nodes in k-Group

**题目含义**

链表每 `k` 个节点翻转一次，不足 `k` 个保持不变。面试重点在于分组、断开、反转、再接回。

**Python 代码**

```python
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

**常见 Follow-up**

- 如果最后不足 `k` 个也要反转，哪里改？
- 你会写递归版吗？

