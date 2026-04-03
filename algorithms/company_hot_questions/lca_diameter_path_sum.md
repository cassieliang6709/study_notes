---
title: "LCA Diameter Path Sum"
---

# LCA + Diameter + Path Sum

这三类树题常被一起问，因为它们都在考“递归函数到底返回什么”。

## 1. Lowest Common Ancestor of a Binary Tree

### 题目含义

给两个节点 `p` 和 `q`，找它们的最近公共祖先。

### Python 代码

```python
from typing import Optional


class Solution:
    def lowestCommonAncestor(
        self,
        root: "TreeNode",
        p: "TreeNode",
        q: "TreeNode",
    ) -> Optional["TreeNode"]:
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left or right
```

### 时间复杂度

`O(n)`

### 空间复杂度

`O(h)`

### 怎么想到

如果左右子树分别找到了目标，当前节点就是分叉点。

## 2. Diameter of Binary Tree

### 题目含义

树的直径是任意两节点间最长路径长度。

### Python 代码

```python
from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional["TreeNode"]) -> int:
        ans = 0

        def depth(node):
            nonlocal ans
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            ans = max(ans, left + right)
            return 1 + max(left, right)

        depth(root)
        return ans
```

### 时间复杂度

`O(n)`

### 空间复杂度

`O(h)`

### 怎么想到

这类题常见套路是：

- 递归返回高度
- 在当前节点顺手更新全局答案

## 3. Path Sum III

### 题目含义

统计路径和等于 `targetSum` 的路径条数，路径可以从任意节点开始，但必须向下走。

### Python 代码

```python
from collections import defaultdict
from typing import Optional


class Solution:
    def pathSum(self, root: Optional["TreeNode"], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        ans = 0

        def dfs(node, cur_sum):
            nonlocal ans
            if not node:
                return

            cur_sum += node.val
            ans += prefix[cur_sum - targetSum]
            prefix[cur_sum] += 1

            dfs(node.left, cur_sum)
            dfs(node.right, cur_sum)

            prefix[cur_sum] -= 1

        dfs(root, 0)
        return ans
```

### 时间复杂度

`O(n)`

### 空间复杂度

`O(n)`

### 怎么想到

如果路径不一定从根开始，就不能只传“当前路径列表”；这时要联想到前缀和思想，把树路径问题转成“两个前缀和之差”。

## 常见 Follow-up

- 如果是 BST，LCA 如何利用有序性优化？
- 为什么 Diameter 的答案不一定经过根？
- 为什么 `Path Sum III` 不能简单暴力从每个点重新 DFS？
