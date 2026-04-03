---
title: "LeetCode Top 100 Pattern Roadmap"
---

# LeetCode Top 100 Pattern Roadmap

> Owner: cassie
> Goal: finish the full list by pattern, in a clean learning order
> Method: learn pattern -> memorize recognition signals -> use template -> solve grouped problems

---

## Pattern Summary

This roadmap teaches one core interview skill: classify first, code second. The goal is not to memorize 100 separate solutions, but to learn the recognition signals behind common patterns such as hashing, two pointers, sliding window, recursion, BFS/DFS, heap, and dynamic programming.

## Problem Meaning

This page is a learning roadmap rather than a single problem statement. To make the roadmap concrete, the representative code below uses `Two Sum`, because it is one of the cleanest examples of “see a signal, pick a pattern, apply a template.”

## Python Code

```python
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}

        for index, value in enumerate(nums):
            need = target - value
            if need in seen:
                return [seen[need], index]
            seen[value] = index

        return []


print(Solution().twoSum([2, 7, 11, 15], 9))
```

## Time Complexity

The representative solution scans the array once and uses constant-time hash lookups on average, so the time complexity is `O(n)`.

## Space Complexity

The hash map may store up to `n` elements, so the space complexity is `O(n)`.

## How To Think About It

The most important habit is to translate the wording into a pattern signal. `Two Sum` says “find a complement quickly,” which is a hash map signal. Once you notice that, the code is almost predetermined: for each number, check whether its complement has appeared before. This roadmap tries to build that recognition habit across the whole interview set.

## Example Case

Input: `nums = [2, 7, 11, 15], target = 9`
Output: `[0, 1]`
Explanation: when we reach `7`, we already saw `2`, and `2 + 7 = 9`.

Edge case: if no pair exists, the sample implementation returns `[]`; some interview versions guarantee that one answer always exists.

## Common Follow-up Questions

- If the array is sorted, when should you switch from hash map to two pointers?
- If the question asks for all triplets summing to zero, how does the pattern change into `3Sum`?
- If the target involves a continuous subarray instead of two values, when should you think about prefix sum or sliding window?

## How To Use This Document

For every problem, do this in order:

```text
// Step 1: classify the problem
// array? string? linked list? tree? graph? matrix?

// Step 2: identify the pattern
// hash? two pointers? sliding window? binary search?
// stack? backtracking? BFS/DFS? heap? DP?

// Step 3: state the core invariant before coding
// what does each pointer mean?
// what does dp[i] / dp[i][j] mean?
// what does the recursive function return?

// Step 4: hand-simulate a small example
// verify variable updates before writing code
```

Golden rule:

```text
// Do not memorize problem titles.
// Memorize recognition signals + solution templates.
```

---

## Suggested Learning Order

1. Arrays / Hashing / Basic scanning
2. Two pointers
3. Linked lists
4. Stack / Monotonic stack
5. Binary trees / BST
6. Binary search
7. Sliding window
8. Backtracking
9. Graph BFS / DFS
10. Heap / Priority queue
11. Dynamic programming
12. Hard mixed problems

Reason:

```text
// First build manipulation skills
// Then build pattern recognition
// Then build state-design ability for DP / hard problems
```

---

## Pattern 1: Arrays / Hashing / Basic Scanning

### Recognition Signals

```text
// "find if exists" / "count frequency" / "seen before"
=> think hash map / hash set

// "subarray sum" / "prefix relation"
=> think prefix sum + hash map

// "missing / duplicate / range 1..n"
=> think index mapping / in-place tricks / Floyd

// "best profit" / "maximum subarray" / "scan once"
=> think running state while traversing
```

### Core Templates

```text
// Hash lookup template
for x in nums:
    // check what you need first
    // then record current info
```

```text
// Prefix sum + hashmap
prefix = 0
count[0] = 1

for x in nums:
    prefix += x
    // if prefix - k appeared before,
    // that previous position forms a valid subarray
    ans += count[prefix - k]
    count[prefix] += 1
```

```text
// One-pass best state
for x in nums:
    // maintain "best so far"
    // update answer using current value + historical info
```

### Learning Order

1. Two Sum
2. Majority Element
3. Single Number
4. Best Time to Buy and Sell Stock
5. Maximum Subarray
6. Move Zeroes
7. Rotate Array
8. Product of Array Except Self
9. Group Anagrams
10. Longest Consecutive Sequence
11. Subarray Sum Equals K
12. Merge Intervals
13. Sort Colors
14. Find the Duplicate Number
15. First Missing Positive
16. Next Permutation

### Problem Notes

- `Two Sum`
  ```text
  // store value -> index
  // before inserting current value, check whether target - x already exists
  ```

- `Majority Element`
  ```text
  // Boyer-Moore voting
  // maintain a candidate and a counter
  // same value => counter++
  // different value => counter--
  ```

- `Single Number`
  ```text
  // XOR property:
  // a ^ a = 0
  // a ^ 0 = a
  // duplicates cancel out
  ```

- `Best Time to Buy and Sell Stock`
  ```text
  // maintain the minimum price seen so far
  // profit at day i = price[i] - min_price
  ```

- `Maximum Subarray`
  ```text
  // Kadane's algorithm
  // current best ending here:
  // either extend previous subarray or restart at current number
  ```

- `Product of Array Except Self`
  ```text
  // prefix product from left
  // suffix product from right
  // answer[i] = left product * right product
  ```

- `Group Anagrams`
  ```text
  // same sorted string => same group
  // key can be sorted(word) or 26-count tuple
  ```

- `Longest Consecutive Sequence`
  ```text
  // put all numbers into a set
  // only start counting from numbers whose predecessor does not exist
  ```

- `Subarray Sum Equals K`
  ```text
  // prefix sum difference
  // count how many previous prefixes equal current_prefix - k
  ```

- `Merge Intervals`
  ```text
  // interval problems almost always start with sorting by start
  // merge if current.start <= last.end
  ```

- `Sort Colors`
  ```text
  // Dutch National Flag
  // maintain boundaries for 0-region and 2-region
  ```

- `Find the Duplicate Number`
  ```text
  // values behave like next pointers
  // use Floyd cycle detection
  ```

- `First Missing Positive`
  ```text
  // put each valid value x into index x - 1
  // then scan for first mismatch
  ```

- `Next Permutation`
  ```text
  // from right, find first descending pivot
  // swap with next larger element on the right
  // reverse the suffix
  ```

### Common Mistakes

- Using sorting when the problem requires original index
- Forgetting to initialize prefix hash with `0 -> 1`
- Confusing subarray with subsequence
- Writing an `O(n^2)` scan when a hash or single pass is enough

---

## Pattern 2: Two Pointers

### Recognition Signals

```text
// sorted array
// opposite ends moving inward
// remove / compact in-place
// palindrome / pair sum / triplets
// linked list slow-fast behavior
```

### Core Templates

```text
// opposite-direction pointers
left = 0
right = n - 1

while left < right:
    // update answer
    // move the side that cannot help more
```

```text
// slow-fast pointers
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

### Learning Order

1. Move Zeroes
2. Container With Most Water
3. 3Sum
4. Trapping Rain Water
5. Linked List Cycle
6. Linked List Cycle II
7. Palindrome Linked List

### Problem Notes

- `Move Zeroes`
  ```text
  // slow pointer = next position to place a non-zero
  // fast pointer scans every element
  ```

- `Container With Most Water`
  ```text
  // area depends on shorter side
  // move the shorter side because the taller side is not the bottleneck
  ```

- `3Sum`
  ```text
  // sort first
  // fix one number, then solve two-sum with left/right pointers
  // skip duplicates carefully
  ```

- `Trapping Rain Water`
  ```text
  // water at each side depends on smaller max boundary
  // maintain left_max and right_max
  ```

- `Linked List Cycle`
  ```text
  // if slow and fast meet, there is a cycle
  ```

- `Linked List Cycle II`
  ```text
  // after slow meets fast,
  // reset one pointer to head
  // move both one step at a time
  // their next meeting point is the cycle entrance
  ```

---

## Pattern 3: Linked Lists

### Recognition Signals

```text
// reverse / merge / delete / swap
// nth from end
// middle of list
// cycle or intersection
```

### Core Templates

```text
// dummy node for deletion / insertion / swap
dummy.next = head
prev = dummy
```

```text
// reverse a list
prev = None
cur = head

while cur:
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
```

```text
// merge two sorted lists
dummy = ListNode(0)
tail = dummy

while l1 and l2:
    // append smaller node

// append remainder
```

### Learning Order

1. Reverse Linked List
2. Merge Two Sorted Lists
3. Remove Nth Node From End of List
4. Add Two Numbers
5. Intersection of Two Linked Lists
6. Swap Nodes in Pairs
7. Copy List with Random Pointer
8. Sort List
9. LRU Cache
10. Merge k Sorted Lists
11. Reverse Nodes in k-Group

### Problem Notes

- `Remove Nth Node From End of List`
  ```text
  // move fast pointer n steps first
  // then move slow and fast together
  // slow stops right before node to delete
  ```

- `Add Two Numbers`
  ```text
  // digit-by-digit simulation with carry
  // keep going while l1 or l2 or carry exists
  ```

- `Intersection of Two Linked Lists`
  ```text
  // pointer A goes A->B
  // pointer B goes B->A
  // equalized path lengths make them meet
  ```

- `Copy List with Random Pointer`
  ```text
  // either hashmap old->new
  // or interleave copied nodes between original nodes
  ```

- `Sort List`
  ```text
  // linked list merge sort
  // split by middle, sort recursively, merge
  ```

- `LRU Cache`
  ```text
  // hashmap for O(1) lookup
  // doubly linked list for O(1) remove / move-to-front
  ```

- `Reverse Nodes in k-Group`
  ```text
  // identify a block of k nodes
  // reverse that block
  // reconnect to previous and next parts
  ```

---

## Pattern 4: Stack / Monotonic Stack

### Recognition Signals

```text
// matching pairs
// nested expressions
// nearest greater / smaller
// histogram / temperatures / waiting days
```

### Core Templates

```text
// standard stack
for ch in s:
    // push opening info
    // on closing symbol, pop and validate
```

```text
// monotonic stack usually stores indices
for i, x in enumerate(nums):
    while stack and nums[stack[-1]] < x:
        idx = stack.pop()
        // current i is the next greater element for idx
    stack.append(i)
```

### Learning Order

1. Valid Parentheses
2. Min Stack
3. Decode String
4. Daily Temperatures
5. Largest Rectangle in Histogram
6. Longest Valid Parentheses

### Problem Notes

- `Min Stack`
  ```text
  // either keep a second stack of minima
  // or store pairs: (value, current_min)
  ```

- `Decode String`
  ```text
  // push previous string and repeat count when seeing '['
  // build current segment until ']'
  ```

- `Daily Temperatures`
  ```text
  // maintain decreasing temperature stack
  // when a warmer day arrives, resolve previous days
  ```

- `Largest Rectangle in Histogram`
  ```text
  // when a bar is popped,
  // it becomes the limiting height of the maximal rectangle
  // width comes from current index and new stack top
  ```

---

## Pattern 5: Binary Trees / BST

### Recognition Signals

```text
// tree path, depth, diameter, balance
// BST ordering
// layer-by-layer view
// subtree information
```

### Traversal Selection

```text
// preorder: build / serialize / path construction
// inorder: BST sorted order
// postorder: combine left and right subtree info
// level order: BFS by layers
```

### Core Template

```text
def dfs(node):
    if not node:
        return base_value

    left = dfs(node.left)
    right = dfs(node.right)

    // combine subtree answers here
    return something_for_parent
```

### Learning Order

1. Maximum Depth of Binary Tree
2. Invert Binary Tree
3. Binary Tree Inorder Traversal
4. Symmetric Tree
5. Binary Tree Level Order Traversal
6. Diameter of Binary Tree
7. Validate Binary Search Tree
8. Convert Sorted Array to Binary Search Tree
9. Kth Smallest Element in a BST
10. Lowest Common Ancestor of a Binary Tree
11. Binary Tree Right Side View
12. Path Sum III
13. Flatten Binary Tree to Linked List
14. Construct Binary Tree from Preorder and Inorder Traversal
15. Binary Tree Maximum Path Sum

### Problem Notes

- `Symmetric Tree`
  ```text
  // compare left subtree of one side with right subtree of the other side
  ```

- `Diameter of Binary Tree`
  ```text
  // for each node:
  // longest path through node = left_height + right_height
  // return height to parent
  ```

- `Validate Binary Search Tree`
  ```text
  // BST is not just local left < root < right
  // every node must satisfy global lower and upper bounds
  ```

- `Kth Smallest Element in a BST`
  ```text
  // inorder traversal of BST is sorted
  // count visited nodes
  ```

- `Lowest Common Ancestor of a Binary Tree`
  ```text
  // if left and right both return non-null,
  // current node is the LCA
  ```

- `Path Sum III`
  ```text
  // same pattern as subarray sum equals k
  // prefix sum on a root-to-current path
  ```

- `Flatten Binary Tree to Linked List`
  ```text
  // reconnect left flattened subtree between root and right subtree
  // reverse preorder thinking is also common
  ```

- `Binary Tree Maximum Path Sum`
  ```text
  // return only one-side gain to parent
  // but update global answer using left + node + right
  ```

---

## Pattern 6: Binary Search

### Recognition Signals

```text
// sorted input
// first / last occurrence
// minimum valid answer
// rotated sorted array
// monotonic condition
```

### Core Templates

```text
// exact match
left = 0
right = n - 1

while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

```text
// left boundary search
while left <= right:
    mid = (left + right) // 2
    if nums[mid] >= target:
        right = mid - 1
    else:
        left = mid + 1
```

### Learning Order

1. Search Insert Position
2. Find First and Last Position of Element in Sorted Array
3. Search a 2D Matrix
4. Find Minimum in Rotated Sorted Array
5. Search in Rotated Sorted Array
6. Search a 2D Matrix II
7. Median of Two Sorted Arrays

### Problem Notes

- `Find First and Last Position of Element`
  ```text
  // run binary search twice:
  // once for left boundary
  // once for right boundary
  ```

- `Find Minimum in Rotated Sorted Array`
  ```text
  // compare nums[mid] with nums[right]
  // decide which half must contain the minimum
  ```

- `Search in Rotated Sorted Array`
  ```text
  // one half is always sorted
  // determine whether target lies inside that sorted half
  ```

- `Median of Two Sorted Arrays`
  ```text
  // binary search partition, not actual merge
  // make left partition size fixed
  // ensure maxLeft <= minRight on both arrays
  ```

---

## Pattern 7: Sliding Window

### Recognition Signals

```text
// substring / subarray
// longest or shortest valid contiguous segment
// no repeated chars
// cover all required chars
// fixed-size window
```

### Core Templates

```text
// variable-size window
left = 0

for right in range(n):
    // expand window by including nums[right]

    while window is invalid:
        // shrink from left
        left += 1

    // update answer
```

```text
// fixed-size window
// initialize first k elements
// then slide:
// add right, remove left, update answer
```

### Learning Order

1. Longest Substring Without Repeating Characters
2. Find All Anagrams in a String
3. Minimum Window Substring
4. Sliding Window Maximum

### Problem Notes

- `Longest Substring Without Repeating Characters`
  ```text
  // maintain a window with all unique chars
  // if duplicate appears, move left until valid again
  ```

- `Find All Anagrams in a String`
  ```text
  // fixed-size frequency window
  // compare counts against target pattern
  ```

- `Minimum Window Substring`
  ```text
  // expand until all required chars are covered
  // then shrink as much as possible while still valid
  ```

- `Sliding Window Maximum`
  ```text
  // use deque, not heap, for O(n)
  // maintain decreasing values in deque
  ```

---

## Pattern 8: Backtracking

### Recognition Signals

```text
// all combinations
// all permutations
// all partitions
// search every valid choice
// place / remove / undo
```

### Core Template

```text
path = []

def backtrack(state):
    if reach_goal:
        ans.append(path copy)
        return

    for choice in available choices:
        if choice is invalid:
            continue

        // choose
        path.append(choice)

        // explore
        backtrack(next_state)

        // unchoose
        path.pop()
```

### Learning Order

1. Letter Combinations of a Phone Number
2. Subsets
3. Permutations
4. Combination Sum
5. Generate Parentheses
6. Palindrome Partitioning
7. Word Search
8. N-Queens

### Problem Notes

- `Subsets`
  ```text
  // classic choose / skip pattern
  // usually use start index to avoid revisiting previous positions
  ```

- `Permutations`
  ```text
  // order matters
  // use used[] to mark chosen elements
  ```

- `Combination Sum`
  ```text
  // order does not matter
  // reuse of same element allowed
  // recursive call often keeps same index
  ```

- `Generate Parentheses`
  ```text
  // left_count <= n
  // right_count <= left_count
  ```

- `Palindrome Partitioning`
  ```text
  // choose a substring cut
  // continue only if chosen substring is a palindrome
  ```

- `Word Search`
  ```text
  // DFS on matrix
  // mark visited during current path
  // restore after backtracking
  ```

- `N-Queens`
  ```text
  // track used columns, diag1, diag2
  // prune invalid queen placements early
  ```

---

## Pattern 9: Graph BFS / DFS

### Recognition Signals

```text
// islands / connected components
// dependencies / prerequisites
// spread over time
// shortest number of steps in unweighted graph
```

### Core Templates

```text
// DFS flood fill
def dfs(r, c):
    if out of bounds or invalid:
        return
    mark visited
    dfs in four directions
```

```text
// BFS by levels
queue = all starting states
steps = 0

while queue:
    for _ in range(len(queue)):
        process one node
        push next nodes
    steps += 1
```

### Learning Order

1. Number of Islands
2. Rotting Oranges
3. Course Schedule

### Problem Notes

- `Number of Islands`
  ```text
  // count components
  // once land is found, flood-fill the whole island
  ```

- `Rotting Oranges`
  ```text
  // all rotten oranges are simultaneous BFS sources
  // each BFS layer represents one minute
  ```

- `Course Schedule`
  ```text
  // detect cycle in a directed graph
  // topological sort using indegree
  ```

---

## Pattern 10: Heap / Priority Queue

### Recognition Signals

```text
// top k
// streaming median
// repeatedly take smallest / largest
// merge many sorted structures
```

### Core Templates

```text
// keep size-k min heap for k largest elements
for x in nums:
    push x
    if heap size > k:
        pop smallest
```

```text
// two heaps for median
// left heap: max heap
// right heap: min heap
// rebalance sizes after each insert
```

### Learning Order

1. Kth Largest Element in an Array
2. Top K Frequent Elements
3. Merge k Sorted Lists
4. Find Median from Data Stream

### Problem Notes

- `Top K Frequent Elements`
  ```text
  // count frequencies first
  // then use heap or bucket sort
  ```

- `Merge k Sorted Lists`
  ```text
  // heap stores current node from each list
  // repeatedly pop smallest node and push its next
  ```

- `Find Median from Data Stream`
  ```text
  // maintain lower half and upper half
  // balance sizes so median is always available
  ```

---

## Pattern 11: Dynamic Programming

### DP Checklist

```text
// 1. What does dp state mean?
// 2. What is the transition?
// 3. What is the base case?
// 4. What traversal order is valid?
```

### Recognition Signals

```text
// optimal value
// counting ways
// choose or skip
// overlapping subproblems
// "minimum steps", "maximum length", "can we form"
```

### Learning Order

1. Climbing Stairs
2. Pascal's Triangle
3. House Robber
4. Unique Paths
5. Minimum Path Sum
6. Coin Change
7. Perfect Squares
8. Word Break
9. Partition Equal Subset Sum
10. Longest Common Subsequence
11. Longest Increasing Subsequence
12. Longest Palindromic Substring
13. Maximum Product Subarray
14. Edit Distance
15. Longest Valid Parentheses

### Core Templates

```text
// 1D DP
dp[i] = answer for prefix / first i positions
```

```text
// 2D grid DP
dp[r][c] = answer up to cell (r, c)
// usually from top / left
```

```text
// string pair DP
dp[i][j] = answer for s1[:i], s2[:j]
```

### Problem Notes

- `Climbing Stairs`
  ```text
  // Fibonacci-style DP
  // dp[i] = dp[i-1] + dp[i-2]
  ```

- `House Robber`
  ```text
  // rob current => cannot rob previous
  // skip current => inherit previous answer
  ```

- `Unique Paths`
  ```text
  // paths to current cell = from top + from left
  ```

- `Minimum Path Sum`
  ```text
  // min cost to current cell = cell value + min(top, left)
  ```

- `Coin Change`
  ```text
  // minimum number of coins to make amount
  // dp[a] = min(dp[a], dp[a - coin] + 1)
  ```

- `Perfect Squares`
  ```text
  // same shape as coin change
  // available "coins" are square numbers
  ```

- `Word Break`
  ```text
  // dp[i] means s[:i] can be segmented
  // try all split points j < i
  ```

- `Partition Equal Subset Sum`
  ```text
  // subset-sum / 0-1 knapsack
  // target is total_sum / 2
  ```

- `Longest Common Subsequence`
  ```text
  // if chars match:
  // dp[i][j] = dp[i-1][j-1] + 1
  // else take max of top / left
  ```

- `Longest Increasing Subsequence`
  ```text
  // classic O(n^2) DP first
  // then learn patience sorting + binary search
  ```

- `Longest Palindromic Substring`
  ```text
  // interval DP or expand-around-center
  // center expansion is often simpler
  ```

- `Maximum Product Subarray`
  ```text
  // track both max_here and min_here
  // negative number can swap their roles
  ```

- `Edit Distance`
  ```text
  // operations: insert / delete / replace
  // pick min among those transitions
  ```

- `Longest Valid Parentheses`
  ```text
  // either stack solution or DP
  // good problem for understanding "ends-at-i" state
  ```

### Common Mistakes

- Writing a recurrence before defining state clearly
- Wrong base cases
- Wrong iteration order
- Mixing "exactly i" with "up to i"

---

## Pattern 12: Matrix Problems

### Recognition Signals

```text
// 2D traversal
// in-place transform
// search in rows/cols
// DFS/BFS on grid
```

### Learning Order

1. Rotate Image
2. Spiral Matrix
3. Set Matrix Zeroes
4. Search a 2D Matrix
5. Search a 2D Matrix II
6. Number of Islands
7. Rotting Oranges
8. Word Search

### Matrix Checklist

```text
// 1. what are the valid neighbors?
// 2. do I need visited?
// 3. can I modify the matrix in place?
// 4. will a cell be processed multiple times?
// 5. where are the boundary checks?
```

---

## Pattern 13: Trie

### Problem

1. Implement Trie (Prefix Tree)

### Core Idea

```text
// Trie stores characters level by level
// node.children[ch]
// node.is_end marks complete words
```

### Use Cases

- Prefix search
- Dictionary lookups
- Word search extensions

---

## Pattern 14: Greedy

### Recognition Signals

```text
// local best choice seems to preserve global optimality
// jump coverage
// interval-like cutting
// maximize reach / minimize steps with current best boundary
```

### Learning Order

1. Best Time to Buy and Sell Stock
2. Jump Game
3. Jump Game II
4. Partition Labels

### Problem Notes

- `Jump Game`
  ```text
  // maintain farthest reachable index
  // if current index exceeds it, fail
  ```

- `Jump Game II`
  ```text
  // current_end = boundary of current jump
  // farthest = best next boundary
  // when reaching current_end, commit one jump
  ```

- `Partition Labels`
  ```text
  // a segment must extend to the last occurrence of every char inside it
  ```

---

## Hard Problems To Leave For The End

- Median of Two Sorted Arrays
- Binary Tree Maximum Path Sum
- Longest Valid Parentheses
- Find Median from Data Stream
- Merge k Sorted Lists
- Reverse Nodes in k-Group
- Sliding Window Maximum
- Largest Rectangle in Histogram
- Trapping Rain Water
- First Missing Positive
- N-Queens
- Edit Distance
- Minimum Window Substring

Reason:

```text
// these are not random hard problems
// they are combinations of earlier core patterns
```

---

## 6-Phase Completion Plan

### Phase 1: Build Core Reflexes

- Two Sum
- Best Time to Buy and Sell Stock
- Maximum Subarray
- Move Zeroes
- Reverse Linked List
- Merge Two Sorted Lists
- Valid Parentheses
- Maximum Depth of Binary Tree
- Invert Binary Tree
- Binary Tree Inorder Traversal
- Search Insert Position
- Climbing Stairs
- House Robber
- Longest Substring Without Repeating Characters
- Number of Islands

### Phase 2: Consolidate Mid-Level Templates

- 3Sum
- Product of Array Except Self
- Merge Intervals
- Linked List Cycle
- Remove Nth Node From End of List
- Add Two Numbers
- Diameter of Binary Tree
- Validate Binary Search Tree
- Binary Tree Level Order Traversal
- Kth Smallest Element in a BST
- Search in Rotated Sorted Array
- Find First and Last Position of Element
- Subsets
- Permutations
- Combination Sum
- Course Schedule
- Rotting Oranges
- Daily Temperatures
- Top K Frequent Elements
- Coin Change
- Word Break
- Unique Paths
- Minimum Path Sum

### Phase 3: Trees / Window / Backtracking Strength

- Lowest Common Ancestor of a Binary Tree
- Path Sum III
- Binary Tree Right Side View
- Flatten Binary Tree to Linked List
- Letter Combinations of a Phone Number
- Generate Parentheses
- Palindrome Partitioning
- Word Search
- Find All Anagrams in a String
- Partition Equal Subset Sum
- Longest Common Subsequence
- Implement Trie

### Phase 4: Data Structures and Advanced Array Work

- Group Anagrams
- Longest Consecutive Sequence
- Subarray Sum Equals K
- Sort Colors
- Rotate Array
- Next Permutation
- Find the Duplicate Number
- Copy List with Random Pointer
- Sort List
- LRU Cache
- Kth Largest Element in an Array
- Search a 2D Matrix
- Search a 2D Matrix II
- Find Minimum in Rotated Sorted Array

### Phase 5: Controlled Hard Problems

- Trapping Rain Water
- Largest Rectangle in Histogram
- Sliding Window Maximum
- Minimum Window Substring
- Edit Distance
- Binary Tree Maximum Path Sum
- Merge k Sorted Lists
- Reverse Nodes in k-Group
- Find Median from Data Stream
- First Missing Positive
- N-Queens

### Phase 6: Final Bosses

- Median of Two Sorted Arrays
- Longest Valid Parentheses

---

## Daily Practice Format

Use this every day:

1. One new template problem
2. One same-pattern medium problem
3. One review problem from the last 3 days

### Example

```text
// Day structure
// Problem A: learn template
// Problem B: apply template
// Problem C: re-solve from memory
```

Why this works:

```text
// random solving builds familiarity
// grouped repetition builds pattern memory
```

---

## Review Rules

If you cannot solve a problem:

```text
// do not just read and move on
// instead write:
// 1. pattern
// 2. key invariant
// 3. why your attempt failed
// 4. the reusable template
```

If you solved it but slowly:

```text
// mark it as "redo in 2 days"
```

If you solved it cleanly:

```text
// mark it as "review in 1 week"
```

---

## One-Line Pattern Summary

- `Hashing`: use memory to remove repeated searching
- `Two pointers`: use relative position to shrink work
- `Sliding window`: maintain a valid contiguous range
- `Linked list`: dummy node + pointer rewiring
- `Stack`: process nested or nearest relationships
- `Monotonic stack`: solve next greater/smaller efficiently
- `Tree DFS`: ask each subtree to return useful information
- `BFS`: expand level by level
- `Binary search`: cut by monotonicity
- `Backtracking`: try, recurse, undo
- `Heap`: keep top-k or next-best candidates
- `DP`: define state and build from smaller subproblems

---

## Recommended Next Step

Start with this exact block:

1. Two Sum
2. Best Time to Buy and Sell Stock
3. Maximum Subarray
4. Move Zeroes
5. Reverse Linked List
6. Merge Two Sorted Lists
7. Valid Parentheses
8. Maximum Depth of Binary Tree
9. Search Insert Position
10. Climbing Stairs

Goal of this block:

```text
// build confidence fast
// cover the most reusable basic templates
// make later medium problems much easier
```

---

## After This File

Best continuation:

1. Make a second document: `pattern_1_arrays_hashing_detailed.md`
2. Teach each problem with:
   - recognition signal
   - brute force idea
   - optimal idea
   - commented template
   - common mistakes
   - mini checklist

That is the right next move if you want a true guided path instead of only a roadmap.
