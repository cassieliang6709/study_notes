---
title: "Extended Problem List — Pattern Classification (English)"
lang: en
lang_pair: /algorithms/extended_problem_patterns_cn
---

# Extended Problem List — Pattern Classification

> Goal: Organize a large problem set by pattern, so you study by approach rather than by problem name.
> How to use: identify the pattern first, then work through problems in that group in order.

---

## Overall Learning Sequence

Work through topics in this order:

1. Arrays, Two Pointers, Sliding Window
2. Binary Search
3. Linked List
4. Trees and Recursion
5. DFS / Backtracking
6. BFS / Graph
7. Stack and Queue
8. Dynamic Programming
9. Heap / Top K
10. Design
11. Intervals, Math, and Miscellaneous

Reasoning: build foundational operations and pattern recognition first, then move to trees/graphs/backtracking templates, and finish with DP, design, and mixed problems.

---

## Section 1: Arrays, Two Pointers, Sliding Window

### Recognition Signals

```
complement / frequency / dedup                 → hash map
left-right squeeze, sorted, triplets           → two pointers
consecutive subarray / substring, min/max span → sliding window
in-place modification, preserve order          → slow/fast pointer
```

### Sub-categories

#### 1. Hash / Basic Array

- Two Sum
- Group Anagrams
- Intersection of Two Arrays
- Intersection of Two Arrays II
- Single Number
- Find All Duplicates in an Array
- Find the Duplicate Number

Key:
```
use dict/set to trade space for time
check before you store
```

#### 2. In-Place Array Operations

- Move Zeroes
- Sort Colors
- Merge Sorted Array
- String Compression
- Next Permutation

Key:
```
be very clear about what each pointer boundary means
the invariant: what has already been processed
```

#### 3. Two Pointers

- 3Sum
- 3Sum Closest
- Container With Most Water
- Squares of a Sorted Array
- Reverse String
- Valid Anagram

Key:
```
sort first, fix one element, then squeeze from both ends
or left-right squeeze directly
```

#### 4. Sliding Window

- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Longest Substring with At Most K Distinct Characters
- Max Consecutive Ones III
- Permutation in String
- Sliding Window Maximum

Key:
```
expand the window
when it becomes invalid, shrink from the left
update the answer after each valid window
```

### Recommended Order

1. Two Sum
2. Move Zeroes
3. Valid Anagram
4. Reverse String
5. Group Anagrams
6. Intersection of Two Arrays
7. Product of Array Except Self
8. Sort Colors
9. Merge Sorted Array
10. Container With Most Water
11. 3Sum
12. Longest Substring Without Repeating Characters
13. Permutation in String
14. Minimum Window Substring
15. Sliding Window Maximum
16. Next Permutation
17. Find the Duplicate Number

---

## Section 2: Binary Search

### Recognition Signals

```
sorted array
rotated sorted array
first / last occurrence
monotone condition
find minimum value satisfying a condition
```

### Basic Binary Search

- Search in Rotated Sorted Array
- Find First and Last Position of Element in Sorted Array
- Find Peak Element
- Single Element in a Sorted Array
- Search a 2D Matrix
- Find Minimum in Rotated Sorted Array
- Search in Rotated Sorted Array II
- Search a 2D Matrix II

### Advanced Binary Search / Binary Search on Answer

- Random Pick with Weight
- Kth Smallest Element in a Sorted Matrix
- Median of Two Sorted Arrays
- Closest Binary Search Tree Value
- Find the Celebrity

### Recommended Order

1. Search a 2D Matrix
2. Find First and Last Position of Element in Sorted Array
3. Search in Rotated Sorted Array
4. Find Minimum in Rotated Sorted Array
5. Find Peak Element
6. Single Element in a Sorted Array
7. Search a 2D Matrix II
8. Search in Rotated Sorted Array II
9. Kth Smallest Element in a Sorted Matrix
10. Random Pick with Weight
11. Median of Two Sorted Arrays

### Key Insight

```
Binary search is not just "halving a sorted array"
Its essence is exploiting monotonicity:
if a condition is true for X, it's true for all values above/below X
```

---

## Section 3: Linked List

### Recognition Signals

```
reverse
remove nth from end
merge sorted lists
random pointer
reorder / partial reversal
```

### Sub-categories

#### 1. Reversal and Basic Operations

- Reverse Linked List
- Reverse Linked List II
- Reorder List
- Remove Nth Node From End of List

#### 2. Merging and Arithmetic

- Add Two Numbers
- Add Two Numbers II
- Merge Two Sorted Lists
- Merge k Sorted Lists
- Sort List

#### 3. Special Structures

- Intersection of Two Linked Lists
- Copy List with Random Pointer

### Recommended Order

1. Reverse Linked List
2. Merge Two Sorted Lists
3. Remove Nth Node From End of List
4. Add Two Numbers
5. Intersection of Two Linked Lists
6. Reorder List
7. Reverse Linked List II
8. Copy List with Random Pointer
9. Sort List
10. Merge k Sorted Lists
11. Add Two Numbers II

### Key Patterns

```
dummy node
fast/slow pointers
reversal
merge
cut and reattach
```

---

## Section 4: Trees and Recursion

### Recognition Signals

```
depth, height, path, ancestor, construction, serialization
BST ordering properties
per-level information
```

### Sub-categories

#### 1. Traversal / Views

- Binary Tree Level Order Traversal
- Binary Tree Right Side View
- Binary Tree Vertical Order Traversal
- Vertical Order Traversal of a Binary Tree
- Find Largest Value in Each Tree Row
- Maximum Width of Binary Tree
- Populating Next Right Pointers in Each Node
- Populating Next Right Pointers in Each Node II

#### 2. Paths and Sums

- Binary Tree Maximum Path Sum
- Path Sum
- Path Sum II
- Path Sum III
- Sum Root to Leaf Numbers

#### 3. Properties and Transformations

- Symmetric Tree
- Diameter of Binary Tree
- Flatten Binary Tree to Linked List
- Construct Binary Tree from Preorder and Inorder Traversal
- Lowest Common Ancestor of a Binary Tree

#### 4. BST and Serialization

- Validate Binary Search Tree
- Lowest Common Ancestor of a Binary Search Tree
- Convert Sorted Array to Binary Search Tree
- Convert Binary Search Tree to Sorted Doubly Linked List
- Kth Smallest Element in a BST
- Range Sum of BST
- Serialize and Deserialize Binary Tree
- Serialize and Deserialize BST

### Recommended Order

1. Symmetric Tree
2. Binary Tree Level Order Traversal
3. Binary Tree Right Side View
4. Diameter of Binary Tree
5. Path Sum
6. Path Sum II
7. Sum Root to Leaf Numbers
8. Lowest Common Ancestor of a Binary Tree
9. Flatten Binary Tree to Linked List
10. Construct Binary Tree from Preorder and Inorder Traversal
11. Validate Binary Search Tree
12. Kth Smallest Element in a BST
13. Lowest Common Ancestor of a Binary Search Tree
14. Convert Sorted Array to Binary Search Tree
15. Path Sum III
16. Binary Tree Maximum Path Sum
17. Serialize and Deserialize Binary Tree
18. Serialize and Deserialize BST

### Key Patterns

```
choose traversal first:
  preorder   → construction
  inorder    → BST
  postorder  → aggregate subtree info
  level-order → per-level views
```

---

## Section 5: DFS / Backtracking

### Recognition Signals

```
all combinations
all permutations
all valid arrangements
try a choice, undo if it doesn't work
```

### Problems

- Subsets
- Permutations
- Combination Sum
- Generate Parentheses
- Letter Combinations of a Phone Number
- Restore IP Addresses
- Binary Tree Paths
- Word Break II
- Partition to K Equal Sum Subsets

### Recommended Order

1. Letter Combinations of a Phone Number
2. Subsets
3. Permutations
4. Combination Sum
5. Generate Parentheses
6. Restore IP Addresses
7. Binary Tree Paths
8. Word Break II
9. Partition to K Equal Sum Subsets

### Key Questions

```
what goes in the path?
where does start begin?
do I need a used[] array?
when do I prune?
```

---

## Section 6: BFS / Graph

### Recognition Signals

```
shortest path
layer-by-layer spreading
islands / connected components
dependency relationships / topological sort
```

### Sub-categories

#### 1. BFS / Shortest Path

- Word Ladder
- Word Ladder II
- Walls and Gates
- Shortest Distance from All Buildings
- The Maze

#### 2. Connected Components / Islands / Search

- Number of Islands
- Max Area of Island
- Island Perimeter
- Battleships in a Board
- Is Graph Bipartite?
- Word Search
- Word Search II

#### 3. Topological Sort / Dependencies

- Course Schedule
- Course Schedule II
- Alien Dictionary

#### 4. Other Graph Problems

- Clone Graph
- Reconstruct Itinerary
- Pacific Atlantic Water Flow
- Accounts Merge
- All Nodes Distance K in Binary Tree
- Number of Connected Components in an Undirected Graph
- Minesweeper

### Recommended Order

1. Number of Islands
2. Max Area of Island
3. Island Perimeter
4. Word Search
5. Is Graph Bipartite?
6. Course Schedule
7. Course Schedule II
8. Clone Graph
9. Walls and Gates
10. Pacific Atlantic Water Flow
11. Word Ladder
12. Word Ladder II
13. Word Search II
14. Accounts Merge
15. Alien Dictionary
16. Reconstruct Itinerary

### Key Patterns

```
DFS flood-fill for connected components
BFS by layer for shortest path
topological sort for dependency ordering
union-find / graph mapping for grouping
```

---

## Section 7: Stack and Queue

### Recognition Signals

```
bracket matching
expression parsing
monotone relationships (next greater / previous smaller)
call stack simulation / time-slice modeling
```

### Sub-categories

#### 1. Monotone Stack / Structural Stack

- Trapping Rain Water
- Longest Valid Parentheses

#### 2. Brackets / Calculators / Parsing

- Valid Parentheses
- Simplify Path
- Basic Calculator
- Basic Calculator II
- Basic Calculator III
- Decode String

#### 3. Queue / Stack Simulation

- Design Circular Queue
- Exclusive Time of Functions

### Recommended Order

1. Valid Parentheses
2. Simplify Path
3. Decode String
4. Basic Calculator II
5. Basic Calculator
6. Longest Valid Parentheses
7. Trapping Rain Water
8. Design Circular Queue
9. Exclusive Time of Functions
10. Basic Calculator III

### Key Questions

```
do I store values or indices in the stack?
how do I compute the answer when popping?
for calculator problems: when do I "settle" the preceding expression?
```

---

## Section 8: Dynamic Programming

### Recognition Signals

```
optimal value
number of ways
can this be formed?
overlapping subproblems
```

### Sub-categories

#### 1. Sequence DP

- Climbing Stairs
- Fibonacci Number
- Best Time to Buy and Sell Stock
- Longest Increasing Subsequence
- Maximum Product Subarray
- Word Break
- Decode Ways
- Longest Palindromic Subsequence

#### 2. Paths and Subarrays

- Maximum Subarray
- Unique Paths
- Unique Paths II
- Subarray Sum Equals K
- Continuous Subarray Sum

#### 3. String / Pattern Matching

- Longest Palindromic Substring
- Regular Expression Matching
- Wildcard Matching
- Longest Increasing Path in a Matrix

### Recommended Order

1. Fibonacci Number
2. Climbing Stairs
3. Best Time to Buy and Sell Stock
4. Maximum Subarray
5. Unique Paths
6. Unique Paths II
7. Decode Ways
8. Word Break
9. Longest Increasing Subsequence
10. Maximum Product Subarray
11. Longest Palindromic Substring
12. Longest Palindromic Subsequence
13. Continuous Subarray Sum
14. Longest Increasing Path in a Matrix
15. Regular Expression Matching
16. Wildcard Matching

### Four-Step DP Framework

```
1. Define the state
2. Write the transition
3. Set base cases
4. Determine iteration order
```

Never skip step 1. If you don't know what `dp[i]` means, everything else will be wrong.

---

## Section 9: Heap / Top K

### Recognition Signals

```
top k
running maximum / minimum
data stream
pop by priority
```

### Problems

- Kth Largest Element in an Array
- K Closest Points to Origin
- Top K Frequent Elements
- Top K Frequent Words
- Reorganize String
- Find Median from Data Stream
- Kth Largest Element in a Stream

### Recommended Order

1. Kth Largest Element in an Array
2. K Closest Points to Origin
3. Top K Frequent Elements
4. Kth Largest Element in a Stream
5. Top K Frequent Words
6. Reorganize String
7. Find Median from Data Stream

### Key Patterns

```
min-heap of size k → keep top k largest
max-heap → process highest priority first
two heaps → maintain running median
```

---

## Section 10: Design

### Recognition Signals

```
design a data structure
multiple operations must all be efficient
insert / delete / get / iterator
```

### Problems

- LRU Cache
- Insert Delete GetRandom O(1)
- Implement Trie (Prefix Tree)
- Add and Search Word
- Design Tic-Tac-Toe
- Binary Search Tree Iterator

### Recommended Order

1. Implement Trie
2. Binary Search Tree Iterator
3. Design Tic-Tac-Toe
4. Insert Delete GetRandom O(1)
5. LRU Cache
6. Add and Search Word

### Key Steps

```
1. list all required operations
2. define the time complexity target for each
3. pick the combination of data structures that achieves it
```

---

## Section 11: Intervals, Math, and Miscellaneous

### Sub-categories

#### 1. Intervals

- Merge Intervals
- Insert Interval
- Meeting Rooms II

Key: almost every interval problem starts with sorting by start time.

#### 2. Math / Matrix

- Pow(x, n)
- Divide Two Integers
- Rotate Image
- Spiral Matrix
- Set Matrix Zeroes

#### 3. Miscellaneous

- String to Integer (atoi)
- Roman to Integer
- First Missing Positive
- Longest Consecutive Sequence
- Palindrome Permutation
- Integer to English Words
- First Unique Character in a String
- Validate IP Address
- Task Scheduler
- Pancake Sorting
- Sudoku Solver

### Recommended Order

1. Merge Intervals
2. Insert Interval
3. Meeting Rooms II
4. Rotate Image
5. Spiral Matrix
6. Set Matrix Zeroes
7. Roman to Integer
8. String to Integer (atoi)
9. First Unique Character in a String
10. Validate IP Address
11. Longest Consecutive Sequence
12. First Missing Positive
13. Pow(x, n)
14. Divide Two Integers
15. Task Scheduler
16. Sudoku Solver
17. Integer to English Words

---

## How to Use This List Effectively

Don't grind problems in platform order. Use this approach instead:

### Round 1: Build Templates

Do the first 3–5 problems in each section. Focus on understanding the template, not just getting AC.

### Round 2: Reinforce by Pattern

Do 5–10 problems in the same pattern back-to-back. This builds automatic recognition.

### Round 3: Hard Problems

Pull out the hardest problems from each section and tackle them together.

---

## Self-Assessment System

Label each problem:

- `A`: saw the pattern immediately, wrote it cleanly
- `B`: got it, but not confident
- `C`: needed hints or couldn't solve it

Review order:
1. Clear all `C` problems first
2. Convert `B` to `A`
3. Maintain `A` problems with occasional review

---

## Must-Do Core Problems (If Time Is Limited)

If you don't want to get overwhelmed by volume, nail these first:

- Two Sum
- Move Zeroes
- Product of Array Except Self
- 3Sum
- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Search in Rotated Sorted Array
- Reverse Linked List
- Add Two Numbers
- Binary Tree Level Order Traversal
- Lowest Common Ancestor of a Binary Tree
- Subsets
- Permutations
- Number of Islands
- Course Schedule
- Valid Parentheses
- Decode String
- Climbing Stairs
- Word Break
- Kth Largest Element in an Array
- LRU Cache
- Merge Intervals

These 22 problems cover all the core templates.
