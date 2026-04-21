---
title: "Binary Tree Study Guide (English)"
lang: en
lang_pair: /algorithms/binary_tree_study_guide
---

# Binary Tree Study Guide

This guide covers the most common binary tree problem patterns for interviews. The focus is on building intuition for recursion, not memorizing every solution.

---

## Pattern Summary

The real key to binary tree problems is defining exactly what your recursive function returns. Many questions look different on the surface, but underneath they all ask you to gather information from the left subtree, gather information from the right subtree, and combine the two at the current node.

## Problem Meaning

This guide is a tree-pattern overview rather than one specific LeetCode problem. To anchor the pattern, the representative example below uses `Maximum Depth of Binary Tree`, because it is the cleanest entry point into postorder recursion.

## Python Code

```python
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


root = TreeNode(
    3,
    left=TreeNode(9),
    right=TreeNode(20, TreeNode(15), TreeNode(7)),
)
print(Solution().maxDepth(root))
```

## Time Complexity

Each node is visited once, so the time complexity is `O(n)`.

## Space Complexity

The recursion stack is at most the height of the tree, so the space complexity is `O(h)`, or `O(n)` in the worst case.

## How To Think About It

Do not try to solve “the whole tree” all at once. Ask a smaller question first: if I already know the answer for the left subtree and the right subtree, how do I combine them at the current node? For max depth, the combination rule is just “take the larger depth and add one.” That same mindset scales to balanced tree, diameter, and path-sum problems.

## Example Case

Input tree: `[3,9,20,null,null,15,7]`
Output: `3`
Explanation: the longest root-to-leaf path has three nodes, such as `3 -> 20 -> 15`.

Edge case: an empty tree returns `0` because there are no levels at all.

## Common Follow-up Questions

- Why does minimum depth need more care than simply replacing `max` with `min`?
- How would you return both “height” and “balanced or not” from one recursive call?
- In path-sum style problems, should the return value mean the best answer in the whole subtree or the best downward path starting here?

## Part 1: Problem Categories

### 1. Traversal Problems

Pick your traversal method first, then write the code.

1. `Binary Tree Inorder Traversal`
2. `Binary Tree Level Order Traversal`
3. `Binary Tree Right Side View`

### 2. Tree Property Problems

The key question here is: what does your recursive function need to return?

1. `Maximum Depth of Binary Tree`
2. `Symmetric Tree`
3. `Same Tree`
4. `Balanced Binary Tree`
5. `Subtree of Another Tree`
6. `Invert Binary Tree`
7. `Diameter of Binary Tree`

### 3. BST Problems

Always exploit the BST property: left subtree < root < right subtree. Inorder traversal of a BST yields a sorted sequence.

1. `Validate Binary Search Tree`
2. `Kth Smallest Element in a BST`
3. `Convert Sorted Array to Binary Search Tree`
4. `Lowest Common Ancestor of a Binary Search Tree`

### 4. Path / Contribution Problems

The key question: is my recursive function computing "the best path going downward from this node" or "the global best answer within this subtree"? These are different things.

1. `Path Sum III`
2. `Count Good Nodes in Binary Tree`
3. `Binary Tree Maximum Path Sum`

### 5. Construction and Transformation

How do you split structure, or modify structure in-place?

1. `Construct Binary Tree from Preorder and Inorder Traversal`
2. `Flatten Binary Tree to Linked List`
3. `Serialize and Deserialize Binary Tree`

### 6. Lowest Common Ancestor

1. `Lowest Common Ancestor of a Binary Tree`

---

## Part 2: Recommended Practice Order

1. `Maximum Depth of Binary Tree`
2. `Invert Binary Tree`
3. `Same Tree`
4. `Symmetric Tree`
5. `Binary Tree Inorder Traversal`
6. `Binary Tree Level Order Traversal`
7. `Binary Tree Right Side View`
8. `Diameter of Binary Tree`
9. `Balanced Binary Tree`
10. `Subtree of Another Tree`
11. `Validate Binary Search Tree`
12. `Kth Smallest Element in a BST`
13. `Lowest Common Ancestor of a Binary Search Tree`
14. `Convert Sorted Array to Binary Search Tree`
15. `Lowest Common Ancestor of a Binary Tree`
16. `Path Sum III`
17. `Count Good Nodes in Binary Tree`
18. `Binary Tree Maximum Path Sum`
19. `Construct Binary Tree from Preorder and Inorder Traversal`
20. `Flatten Binary Tree to Linked List`
21. `Serialize and Deserialize Binary Tree`

---

## Part 3: Core Techniques

### 1. Choosing a Traversal Order

- **Preorder** (root → left → right): Use when you need to process the root before children. Good for construction and path-tracking problems.
- **Inorder** (left → root → right): Use when you need BST sorted order. Almost every BST problem benefits from inorder.
- **Postorder** (left → right → root): Use when you need information from both children before deciding what to return at the current node. Great for "combine results from subtrees" problems.
- **Level order** (BFS): Use when you need per-layer information — right side view, layer-by-layer output, etc.

### 2. The Most Important Question in Tree Recursion

Before writing any tree solution, ask yourself:

> "What does my recursive function return at each node?"

Examples of what it might return:
- The height of the subtree
- Whether the subtree is balanced
- The maximum "gain" going downward from this node
- Whether the target was found

Many tree problems aren't hard because of code complexity — they're hard because you haven't clearly defined what the recursion means.

### 3. Two Key BST Properties

1. Inorder traversal produces a sorted sequence
2. You can prune the search to one side based on value comparison

### 4. Draw It Out

These problems are much easier with a diagram:

- `Diameter of Binary Tree`
- `Path Sum III`
- `Binary Tree Maximum Path Sum`
- `Construct Binary Tree from Preorder and Inorder Traversal`
- `Flatten Binary Tree to Linked List`
- `Lowest Common Ancestor`

---

## Part 4: Problem Walkthroughs

---

## 1. Maximum Depth of Binary Tree

### Goal

Find the maximum depth (number of nodes along the longest root-to-leaf path).

### Category

Tree property — basic recursion.

### Core Idea

`max_depth(node) = max(max_depth(left), max_depth(right)) + 1`

### Step-by-Step

1. Base case: if node is `None`, depth is 0
2. Recursively get depth of left subtree
3. Recursively get depth of right subtree
4. Return the larger of the two, plus 1 for the current level

### Python Code

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1
```

### Complexity

- Time: `O(n)` — every node visited once
- Space: `O(h)` — h is the height of the tree (call stack)

### Common Mistake

An empty node has depth 0, not 1.

---

## 2. Invert Binary Tree

### Goal

Mirror a binary tree (swap left and right children at every node).

### Core Idea

At every node, swap its left and right children, then recurse into both.

### Python Code

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
```

### Common Mistake

Don't forget to return `root` at the end.

---

## 3. Same Tree

### Goal

Check whether two binary trees are identical in structure and values.

### Core Idea

Two trees are the same if:
- Their root values are equal
- Their left subtrees are the same
- Their right subtrees are the same

### Python Code

```python
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

---

## 4. Symmetric Tree

### Goal

Check whether a binary tree is symmetric (mirror of itself).

### Core Idea

A tree is symmetric if its left subtree is a mirror of its right subtree. Write a helper that compares two nodes mirrored across the center.

### Python Code

```python
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return mirror(left.left, right.right) and mirror(left.right, right.left)

        return mirror(root.left, root.right)
```

---

## 5. Binary Tree Level Order Traversal

### Goal

Return nodes grouped by level (BFS).

### Core Idea

Use a queue. At each step, process all nodes at the current level, collect their values, and enqueue their children for the next level.

### Python Code

```python
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result
```

---

## 6. Diameter of Binary Tree

### Goal

Find the length of the longest path between any two nodes. The path doesn't need to go through the root.

### Core Idea

At each node, the diameter passing through it equals `left_height + right_height`. But the function that recurses upward should return the height, not the diameter. Track the global maximum separately.

### Python Code

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def height(node):
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            # Diameter at this node
            self.max_diameter = max(self.max_diameter, left + right)

            # Return height to parent
            return max(left, right) + 1

        height(root)
        return self.max_diameter
```

### Key Insight

The return value of `height()` (used by the parent) and the answer update `(left + right)` are two different things. Don't conflate them.

---

## 7. Validate Binary Search Tree

### Goal

Determine whether a binary tree satisfies BST constraints.

### Core Idea

Pass upper and lower bounds down the recursion. Every node must satisfy `min_val < node.val < max_val`.

### Python Code

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val, max_val):
            if not node:
                return True
            if node.val <= min_val or node.val >= max_val:
                return False
            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))

        return validate(root, float('-inf'), float('inf'))
```

### Common Mistake

Checking only `left.val < root.val < right.val` is not enough. You need to verify the constraint holds for the entire subtree, not just the immediate children.

---

## 8. Lowest Common Ancestor of a Binary Tree

### Goal

Find the lowest common ancestor (LCA) of two given nodes in a binary tree.

### Core Idea

During postorder recursion:
- If the current node is `None`, return `None`
- If the current node is `p` or `q`, return it
- If both left and right subtrees return non-None, the current node is the LCA
- Otherwise, return whichever subtree returned non-None

### Python Code

```python
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right
```

---

## 9. Binary Tree Maximum Path Sum

### Goal

Find the maximum path sum in a binary tree. A path can start and end at any node.

### Core Idea

At each node, compute the maximum "gain" from going left or right (take 0 if the subtree is negative). The maximum path through this node is `left_gain + node.val + right_gain`. Track the global max separately, and return only `node.val + max(left_gain, right_gain)` to the parent (you can only extend the path in one direction from a parent's perspective).

### Python Code

```python
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def gain(node):
            if not node:
                return 0

            left_gain = max(gain(node.left), 0)
            right_gain = max(gain(node.right), 0)

            # Path through this node
            self.max_sum = max(self.max_sum, node.val + left_gain + right_gain)

            # Can only extend one side to parent
            return node.val + max(left_gain, right_gain)

        gain(root)
        return self.max_sum
```

---

## 10. Serialize and Deserialize Binary Tree

### Goal

Convert a binary tree to a string and reconstruct it from that string.

### Core Idea

Use preorder traversal for serialization. Record `None` nodes as `"#"`. During deserialization, reconstruct using the same preorder, consuming values from a queue.

### Python Code

```python
from collections import deque

class Codec:
    def serialize(self, root):
        result = []

        def preorder(node):
            if not node:
                result.append('#')
                return
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ','.join(result)

    def deserialize(self, data):
        vals = deque(data.split(','))

        def build():
            val = vals.popleft()
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node

        return build()
```

---

## Summary Checklist

Before writing any tree solution, answer these questions:

1. Which traversal order fits this problem?
2. What does my recursive function return at each node?
3. Is the answer the return value, or do I need a global variable?
4. What is my base case (usually `None`)?
5. Did I draw a diagram?
