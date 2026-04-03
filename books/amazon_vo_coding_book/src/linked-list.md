# 9. 链表基础操作

## 面试题目怎么问

- 反转链表
- 合并两个有序链表
- `k` 个一组翻转链表
- 找链表中点
- 判断链表是否有环

## 识别信号

- 单链表
- 修改指针
- 找中点 / 判环
- 原地操作

## Amazon 风格业务包装

- 一个 order processing pipeline 用链式节点表示处理阶段
- 多条有序事件链需要合并
- 需要原地重排任务节点顺序

## 标准代码模板 1：反转链表

```python
def reverse_list(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev
```

## 标准代码模板 2：合并两个有序链表

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    cur = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next

    cur.next = l1 if l1 else l2
    return dummy.next
```

## 标准代码模板 3：快慢指针找中点 / 判环

```python
def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

## 面试时怎么讲

- 链表题的核心是指针操作顺序
- 我会优先考虑是否需要 `dummy head`
- 如果是反转，用 `prev / curr / next` 三指针
- 如果是找中点或判环，用快慢指针

## 常见 follow-up 和回答

**Q1：为什么很多链表题都建议用 `dummy head`？**  
因为它能统一处理头节点变化的情况。

**Q2：反转链表最容易错在哪里？**  
最容易错在改指针后丢失后续节点，所以一定先保存 `next`。

**Q3：快慢指针为什么能判环？**  
如果有环，快指针最终一定会追上慢指针。

## Amazon 风格完整题面

> A workflow is represented as a singly linked list of task nodes.  
> Reverse the order of the tasks in place.

## 可直接背的口语回答稿

“题目给的是链表结构，所以我会直接做指针操作而不是先转数组。反转链表时，我用三个指针：`prev`、`curr`、`next`。每一步先保存后继，再反转当前指针方向，然后整体向前推进。这样时间 `O(n)`，空间 `O(1)`。”

## 推荐代表题

- Reverse Linked List
- Merge Two Sorted Lists
- Linked List Cycle
- Middle of the Linked List

