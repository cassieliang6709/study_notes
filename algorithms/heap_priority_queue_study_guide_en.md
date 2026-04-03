---
title: "Heap / Priority Queue Study Guide (English)"
lang: en
lang_pair: /algorithms/heap_priority_queue_study_guide
---

# Heap / Priority Queue Study Guide

This guide covers when to use heaps, the key patterns, and the most important problems.

---

## Part 1: When to Reach for a Heap

Reach for a heap when you see:

- "Find the top K largest / smallest"
- "Return the Kth largest/smallest element"
- "Maintain a running max/min as data streams in"
- "Merge multiple sorted lists or arrays"
- "At each step, pick the current best option"

One-liner:
- **Heap** = efficiently get the min or max, repeatedly
- **Min-heap** = always pop the smallest element
- **Max-heap** = in Python, negate values to simulate one with `heapq`

---

## Part 2: Problem Categories

### 1. Top K Problems

Keep a heap of size k. Discard elements that don't belong in the top k.

1. `Kth Largest Element in an Array`
2. `Top K Frequent Elements`
3. `K Closest Points to Origin`

### 2. Merging Multiple Sorted Structures

Only push the "current front" of each structure into the heap. After popping the minimum, push its successor.

1. `Merge k Sorted Lists`
2. `Find K Pairs with Smallest Sums`

### 3. Real-Time Median / Data Streams

Data arrives one piece at a time; you can't sort everything from scratch each time.

1. `Find Median from Data Stream`
2. `Kth Largest Element in a Stream`

### 4. Heap + Graph (Dijkstra-style)

These are more advanced problems combining heaps with graph traversal.

1. `Network Delay Time`
2. `Path With Minimum Effort`

Master categories 1–3 before tackling category 4.

---

## Part 3: Recommended Practice Order

1. `Kth Largest Element in an Array`
2. `Top K Frequent Elements`
3. `K Closest Points to Origin`
4. `Merge k Sorted Lists`
5. `Kth Largest Element in a Stream`
6. `Find Median from Data Stream`
7. `Find K Pairs with Smallest Sums`
8. `Network Delay Time`

Reasoning: start with the purest Top K, then practice "what goes into the heap," then tackle the two-heap median problem.

---

## Part 4: Key Templates

### Template 1: Fixed-Size Min-Heap for Top K

Use this to find the Kth largest, or to maintain the top K elements.

```python
import heapq

heap = []

for x in nums:
    heapq.heappush(heap, x)
    if len(heap) > k:
        heapq.heappop(heap)

return heap[0]  # the Kth largest
```

Why this works: the heap keeps exactly `k` elements. The heap top is always the smallest among those `k` — i.e., the Kth largest globally.

**Key rule**: to keep the top K largest, use a min-heap of size k.

### Template 2: Frequency-Based Top K

```python
from collections import Counter
import heapq

count = Counter(nums)
heap = []

for x, freq in count.items():
    heapq.heappush(heap, (freq, x))
    if len(heap) > k:
        heapq.heappop(heap)
```

The key insight: frequency problems require two steps — count first, then heap. Decide what field to use as the heap key.

### Template 3: Merge k Sorted Structures

```python
import heapq

heap = []

for i, node in enumerate(lists):
    if node:
        heapq.heappush(heap, (node.val, i, node))

while heap:
    val, i, node = heapq.heappop(heap)
    # use node
    if node.next:
        heapq.heappush(heap, (node.next.val, i, node.next))
```

The `i` (index) is included so that when two values are equal, Python can compare tuples without reaching the `node` object (which isn't directly comparable). This prevents a `TypeError`.

### Template 4: Two-Heap Median

```python
import heapq

small = []   # max-heap (negate values): stores the smaller half
large = []   # min-heap: stores the larger half

def add_num(x):
    heapq.heappush(small, -x)
    # Balance: largest of small half must go to large half
    heapq.heappush(large, -heapq.heappop(small))

    # Keep sizes balanced: small can have at most 1 more than large
    if len(large) > len(small):
        heapq.heappush(small, -heapq.heappop(large))
```

Balance invariant:
- `small` holds the smaller half (max-heap)
- `large` holds the larger half (min-heap)
- `len(small) >= len(large)` at all times (differ by at most 1)

---

## Part 5: Problem Walkthroughs

## 1. Kth Largest Element in an Array

### Goal

Find the kth largest element in an unsorted array.

### Category

Top K problem.

### Core Idea

Maintain a min-heap of size k. The top of the heap is always the smallest of the k largest elements seen so far — which is exactly the kth largest.

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for x in nums:
            heapq.heappush(heap, x)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
```

**Remember**: to keep top K largest, use a **min**-heap.

---

## 2. Top K Frequent Elements

### Goal

Return the k most frequent elements.

### Core Idea

Step 1: Count frequencies with a hash map.
Step 2: Use a min-heap of size k, keyed by frequency.

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
```

Or the explicit heap version:

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]
```

### Common Mistake

Pushing raw elements into the heap instead of `(frequency, element)` tuples.

---

## 3. K Closest Points to Origin

### Goal

Find the k points closest to the origin (0, 0).

### Core Idea

Same as Top K, but the comparison key changes from "value" to "squared distance." Use a max-heap of size k to keep the k smallest distances.

```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = x * x + y * y
            heapq.heappush(heap, (-dist, x, y))  # max-heap via negation
            if len(heap) > k:
                heapq.heappop(heap)
        return [[x, y] for _, x, y in heap]
```

**Key insight**: the heap key doesn't have to be the value itself — it's whatever you're comparing by.

---

## 4. Merge k Sorted Lists

### Goal

Merge k sorted linked lists into one sorted list.

### Category

Merging multiple sorted structures.

### Core Idea

At any moment, each list's current front node is a candidate for the global minimum. Push all fronts into a heap. After popping the minimum, push its successor.

### Why the complexity is good

There are N total nodes. Each node is pushed and popped once. The heap size is at most k.

- Time: `O(N log k)`

---

## 5. Find Median from Data Stream

### Goal

Support two operations: add a number, and return the current median.

### Why one heap isn't enough

The median is the middle element, not a min or max. You need to track both halves of the data.

### Core Idea

Maintain two heaps:
- `small`: max-heap holding the smaller half
- `large`: min-heap holding the larger half

Median:
- If both halves are equal size: `(small_top + large_top) / 2`
- If `small` has one more: `small_top`

```python
class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap (negated)
        self.large = []  # min-heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
```

### The hardest part

Not finding the median — it's maintaining the balance invariant after each insertion.

---

## Part 6: Pre-Problem Checklist

Before writing heap code, answer:

1. Do I need repeated min or repeated max?
2. Should the heap store raw values or `(key, data)` tuples?
3. Do I need to control heap size at k?
4. Do I need lazy deletion?
5. Is this actually better solved with a bucket, sort, or deque?

---

## Part 7: Common Mistakes

- Confusing which heap type to use for "top K largest" vs "top K smallest"
- Wrong heap key — leading to incorrect ordering
- Comparing custom objects directly in Python — causes `TypeError`
- Forgetting to maintain heap size, causing O(n log n) instead of O(n log k)
- In `Find Median from Data Stream`, not rebalancing after each insertion

---

## Quick Reference

| Problem Type | Strategy |
|---|---|
| Top K largest/smallest | Fixed-size heap |
| Top K by frequency | Count first, then heap |
| Merge k sorted structures | Push only current fronts |
| Running median | Two heaps (small + large halves) |
