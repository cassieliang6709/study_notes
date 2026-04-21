---
title: "Linked List Study Guide (English)"
lang: en
lang_pair: /algorithms/linked_list_study_guide
---

# Linked List Study Guide

This guide covers the most common linked list problem patterns. The goal is to build muscle memory for pointer manipulation — once you internalize the patterns, almost every linked list problem reduces to a combination of them.

---

## Pattern Summary

Linked list problems are mostly about reusing a few pointer patterns well: `dummy` head nodes, fast/slow pointers, local reversal, and reconnecting segments. If you can explain what each pointer means and which link changes next, most linked list questions stop feeling random.

## Problem Meaning

This guide is not one single LeetCode problem. It teaches you how linked list interview questions collapse into a small set of reusable templates. As a representative example, start with `Reverse Linked List`. Once that one is truly clear, harder problems like `Reorder List` and `Reverse Nodes in k-Group` become much more manageable.

## Python Code

```python
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    val: int
    next: Optional['ListNode'] = None


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


def build_list(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> list[int]:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


head = build_list([1, 2, 3, 4])
print(to_list(Solution().reverseList(head)))
```

## Time Complexity

The representative solution walks through the list once, so the time complexity is `O(n)`.

## Space Complexity

It only uses a few pointers, so the extra space complexity is `O(1)`.

## How To Think About It

Do not start from “what is the final head?” Start from a smaller invariant: at each step, make `curr` point backward to `prev`. If that local pointer flip is correct every round, the whole list becomes reversed by the end. That same mindset helps on many linked list problems.

## Example Case

Input list: `1 -> 2 -> 3 -> 4`
Output list: `4 -> 3 -> 2 -> 1`
Explanation: each step moves the current node to the front of the already-reversed part.

Edge case: `[]` stays empty, and `[7]` stays unchanged because there is nothing to reconnect.

## Common Follow-up Questions

- How would you reverse only positions `m` through `n`?
- How would you reverse every `k` nodes and leave the rest unchanged?
- Why do palindrome linked list solutions often find the middle first and reverse the second half?

## Part 1: Problem Categories

### 1. Basic Pointer Operations / Dummy Head

The core technique: use a `dummy` node to avoid special-casing the head, and use a `tail` pointer to build a new list.

1. `Merge Two Sorted Lists`
2. `Add Two Numbers`
3. `Remove Nth Node From End of List`
4. `Swap Nodes in Pairs`

### 2. Reversal and Reconnection

Figure out which segment to reverse, then reconnect it properly.

1. `Reverse Linked List`
2. `Reorder List`
3. `Reverse Nodes in k-Group`

### 3. Fast and Slow Pointers / Cycle Detection

One pointer moves faster than the other. Their relative positions solve problems about midpoints, cycles, and cycle entry points.

1. `Linked List Cycle`
2. `Linked List Cycle II`
3. `Palindrome Linked List`
4. `Find The Duplicate Number`

### 4. Divide and Conquer / Merge Sort

Split into smaller problems, solve each, then merge.

1. `Merge k Sorted Lists`
2. `Sort List`

### 5. Special Structures

These problems aren't standard singly-linked lists and require extra care.

1. `Copy List with Random Pointer`
2. `Intersection of Two Linked Lists`

### 6. Design Problems

Design a data structure, not just traverse a list.

1. `LRU Cache`

---

## Part 2: Recommended Practice Order

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

Note: `Find The Duplicate Number` is not strictly a linked list problem, but it fits naturally in the "fast/slow pointer + cycle detection" group.

---

## Part 3: Core Techniques

### 1. The Dummy Node

When a problem might modify the head, add a `dummy` node before the head.

Benefits:
- No special case needed for deleting the head
- No special case needed for identifying the new list's first node

```python
dummy = ListNode(0)
dummy.next = head
```

Always return `dummy.next` at the end.

### 2. Three-Pointer Reversal

The standard iterative reversal pattern:

- `prev`: the already-reversed segment
- `curr`: the node being processed
- `nxt`: save the next node before breaking the link

```python
prev = None
curr = head

while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt

return prev
```

### 3. Fast and Slow Pointers

Common uses:
- Find the middle of a list (slow ends at middle when fast reaches end)
- Detect a cycle (they meet if a cycle exists)
- Find cycle entry point (Floyd's algorithm)

### 4. Draw It Out

These problems almost require diagrams to get right:

- `Swap Nodes in Pairs`
- `Reorder List`
- `Reverse Nodes in k-Group`
- `Copy List with Random Pointer`
- `LRU Cache`

---

## Part 4: Problem Walkthroughs

---

## 1. Reverse Linked List

### Goal

Reverse a singly-linked list in place.

### Category

Reversal and reconnection — the foundational template.

### Core Idea

Iterate through the list. At each node, flip its pointer to point backward.

### Step-by-Step

1. Start with `prev = None` (the original head will become the tail, pointing to `None`)
2. `curr` starts at `head`
3. Save `curr.next` before overwriting it
4. Set `curr.next = prev`
5. Advance both: `prev = curr`, `curr = nxt`
6. When done, `prev` is the new head

### Python Code

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next      # save next before overwriting
            curr.next = prev     # flip pointer
            prev = curr          # advance prev
            curr = nxt           # advance curr

        return prev              # prev is the new head
```

### Complexity

- Time: `O(n)`
- Space: `O(1)`

### Common Mistakes

- Forgetting to save `curr.next` before overwriting it
- Returning `curr` instead of `prev` at the end

---

## 2. Merge Two Sorted Lists

### Goal

Merge two sorted linked lists into one sorted linked list.

### Core Idea

Use a `dummy` node to start the new list. Use a `tail` pointer to track where to attach the next smaller node.

### Python Code

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
            tail = tail.next

        # Attach any remaining nodes
        tail.next = list1 if list1 else list2

        return dummy.next
```

### Complexity

- Time: `O(m + n)`
- Space: `O(1)`

### Common Mistakes

- Forgetting the `dummy` node
- Forgetting to attach the remaining list after the loop

---

## 3. Linked List Cycle

### Goal

Detect whether a linked list has a cycle.

### Core Idea

Fast pointer moves 2 steps, slow pointer moves 1 step. If there's a cycle, they will eventually meet. If fast reaches `None`, there's no cycle.

### Python Code

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

---

## 4. Remove Nth Node From End of List

### Goal

Remove the nth node from the end of the list in one pass.

### Core Idea

Use two pointers with a gap of n. Move the fast pointer n steps ahead. Then move both together until fast reaches the end — slow will be just before the node to remove.

### Python Code

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy

        # Move fast n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        # slow is just before the node to remove
        slow.next = slow.next.next

        return dummy.next
```

### Why dummy helps here

If the node to remove is the head, you need a node before it to relink. The dummy handles this naturally.

---

## 5. Reorder List

### Goal

Given list `L0 → L1 → ... → Ln`, reorder it to `L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...`

### Core Idea

Three steps:
1. Find the middle of the list (fast/slow pointers)
2. Reverse the second half
3. Interleave the two halves

### Python Code

```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: reverse second half
        prev = None
        curr = slow.next
        slow.next = None  # cut the list
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: merge
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
```

---

## 6. LRU Cache

### Goal

Design a data structure that supports `get(key)` and `put(key, value)` both in O(1) time, evicting the least recently used item when over capacity.

### Core Idea

Combine a hash map (for O(1) lookup) with a doubly-linked list (for O(1) move-to-front and eviction from the tail).

### Python Code

```python
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # Sentinel head and tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._insert_front(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
```

### Why sentinel nodes?

Using dummy head and tail sentinels means you never have to special-case edge conditions when the list is nearly empty.

---

## Summary Checklist

Before writing any linked list solution, ask:

1. Will the head ever change? → Use a `dummy` node
2. Do I need to reverse something? → Use the three-pointer pattern
3. Do I need the middle or need to detect a cycle? → Use fast/slow pointers
4. Is this a k-sorted-lists merge problem? → Use a heap
5. Did I draw the pointer changes before coding?
