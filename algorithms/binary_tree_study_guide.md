---
title: "Binary Tree 题目分类讲义"
---

# Binary Tree 题目分类讲义

这份笔记继续保持和链表讲义同样的风格：

- 先分类
- 再逐题整理
- Python 代码尽量简单直白
- 注释解释“为什么这样做”
- 不追求炫技

---

## 一、分类总表

先把你给出的题目去重后整理出来。

### 1. 基础遍历题

这类题先想“我到底要以前序、中序、后序还是层序来遍历”。

1. `Binary Tree Inorder Traversal`
2. `Binary Tree Level Order Traversal`
3. `Binary Tree Right Side View`

### 2. 树的基础性质判断

这类题的重点是：递归函数返回什么信息。

1. `Maximum Depth of Binary Tree`
2. `Symmetric Tree`
3. `Same Tree`
4. `Balanced Binary Tree`
5. `Subtree of Another Tree`
6. `Invert Binary Tree`
7. `Diameter of Binary Tree`

### 3. BST 专题

这类题一定要抓住二叉搜索树的性质：

- 左子树都比根小
- 右子树都比根大
- 中序遍历结果有序

1. `Validate Binary Search Tree`
2. `Kth Smallest Element in a BST`
3. `Convert Sorted Array to Binary Search Tree`
4. `Lowest Common Ancestor of a Binary Search Tree`

### 4. 路径 / 贡献值题

这类题的重点是：递归函数到底是在算“从当前节点往下的一条路”，还是“整棵子树里的最优答案”。

1. `Path Sum III`
2. `Count Good Nodes in Binary Tree`
3. `Binary Tree Maximum Path Sum`

### 5. 构造与变形

这类题重点是：如何拆分结构，或者如何原地改结构。

1. `Construct Binary Tree from Preorder and Inorder Traversal`
2. `Flatten Binary Tree to Linked List`
3. `Serialize and Deserialize Binary Tree`

### 6. 最近公共祖先

1. `Lowest Common Ancestor of a Binary Tree`

---

## 二、推荐刷题顺序

建议按这个顺序练：

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

## 三、二叉树常用方法总结

### 1. 前序 / 中序 / 后序

先记最重要的一件事：

- 前序：根 -> 左 -> 右
- 中序：左 -> 根 -> 右
- 后序：左 -> 右 -> 根

怎么选？

- 想先处理根，再处理子树：前序
- 想利用 BST 的有序性：中序
- 想先拿到左右子树结果，再决定当前节点：后序

### 2. 层序遍历

层序遍历一般配合队列。

常见用途：

- 一层一层看节点
- 求右视图
- 按层分组输出

### 3. 递归函数最关键的问题

写树题之前，先问自己：

“我的递归函数返回的到底是什么？”

例如：

- 返回子树高度
- 返回当前子树是不是平衡
- 返回从当前节点往下的最大贡献值
- 返回当前节点是不是找到了答案

很多树题难，不是难在代码，而是难在“递归定义没想清楚”。

### 4. BST 两个常见性质

1. 中序遍历有序
2. 查找时可以根据大小只走一边

### 5. 树题很适合画图

尤其是下面这些题，建议画图：

- `Diameter of Binary Tree`
- `Path Sum III`
- `Binary Tree Maximum Path Sum`
- `Construct Binary Tree from Preorder and Inorder Traversal`
- `Flatten Binary Tree to Linked List`
- `Lowest Common Ancestor`

---

## 四、逐题整理

---

## 1. Maximum Depth of Binary Tree

### 题目目标

求二叉树的最大深度。

### 这题属于哪一类

属于“树的基础性质判断”。

### 核心思路

一棵树的最大深度 = `max(左子树最大深度, 右子树最大深度) + 1`

### 分步骤理解

1. 如果节点为空，深度是 0
2. 递归求左子树最大深度
3. 递归求右子树最大深度
4. 取较大值再加上当前这一层

### Python 代码

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(h)`，`h` 是树高

### 易错点

- 空节点深度是 0，不是 1

---

## 2. Invert Binary Tree

### 题目目标

把一棵二叉树左右翻转。

### 这题属于哪一类

属于“树的基础性质判断”。

### 核心思路

每个节点都把左子树和右子树交换一下。

### 分步骤理解

1. 如果当前节点为空，直接返回
2. 交换 `root.left` 和 `root.right`
3. 再递归处理左右子树

### Python 代码

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

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(h)`

### 易错点

- 别忘了最后返回 `root`

---

## 3. Same Tree

### 题目目标

判断两棵树是否完全相同。

### 这题属于哪一类

属于“树的基础性质判断”。

### 核心思路

两棵树相同，要求：

- 当前节点值相同
- 左子树相同
- 右子树相同

### Python 代码

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

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(h)`

---

## 4. Symmetric Tree

### 题目目标

判断一棵树是否左右对称。

### 这题属于哪一类

属于“树的基础性质判断”。

### 核心思路

不是判断“左子树和右子树一样”，而是判断“左子树和右子树镜像相同”。

### 分步骤理解

如果两棵镜像树对称，需要满足：

- 左边的根值 = 右边的根值
- 左边的左子树 和 右边的右子树 对称
- 左边的右子树 和 右边的左子树 对称

### Python 代码

```python
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True

            if not left or not right:
                return False

            if left.val != right.val:
                return False

            return (
                is_mirror(left.left, right.right)
                and is_mirror(left.right, right.left)
            )

        return is_mirror(root.left, root.right)
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(h)`

### 易错点

- 比较顺序是“左对右、右对左”，不是“左对左、右对右”

---

## 5. Binary Tree Inorder Traversal

### 题目目标

返回二叉树的中序遍历结果。

### 这题属于哪一类

属于“基础遍历题”。

### 核心思路

中序顺序是：

- 先左子树
- 再根节点
- 再右子树

### Python 代码

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return

            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)
        return result
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(h)`

---

## 6. Binary Tree Level Order Traversal

### 题目目标

按层返回二叉树节点值。

### 这题属于哪一类

属于“基础遍历题”。

### 核心思路

用队列做 BFS。

每次先记住当前层有多少个节点，这样就能把这一层单独收集出来。

### Python 代码

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

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(n)`

---

## 7. Binary Tree Right Side View

### 题目目标

从树的右侧看过去，返回每层能看到的节点。

### 这题属于哪一类

属于“基础遍历题”。

### 核心思路

还是层序遍历。

每层最后一个节点，就是右视图里能看到的节点。

### Python 代码

```python
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                # 每层最后一个节点，就是右视图看到的节点
                if i == level_size - 1:
                    result.append(node.val)

        return result
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(n)`

---

## 8. Diameter of Binary Tree

### 题目目标

求一棵树的直径，也就是任意两个节点之间最长路径的边数。

### 这题属于哪一类

属于“树的基础性质判断”。

### 核心思路

对于每个节点：

- 左子树高度
- 右子树高度

两者相加，就是“经过这个节点”的路径长度。

全局最大值就是答案。

### 分步骤理解

1. 写一个递归函数，返回当前节点的高度
2. 在递归过程中，顺便更新答案
3. 当前节点的高度 = `max(左高度, 右高度) + 1`

### Python 代码

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.answer = 0

        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            # 经过当前节点的最长路径
            self.answer = max(self.answer, left_height + right_height)

            return max(left_height, right_height) + 1

        height(root)
        return self.answer
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(h)`

### 易错点

- 题目要求的是边数，不是节点数

---

## 9. Balanced Binary Tree

### 题目目标

判断一棵树是否是平衡二叉树。

### 这题属于哪一类

属于“树的基础性质判断”。

### 核心思路

后序遍历。

因为要先知道左右子树高度，才能判断当前节点是否平衡。

### 分步骤理解

1. 递归函数返回当前子树高度
2. 如果发现某个子树已经不平衡，就一路返回特殊值
3. 当前节点左右高度差超过 1，就说明不平衡

### Python 代码

```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_height = height(node.left)
            if left_height == -1:
                return -1

            right_height = height(node.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            return max(left_height, right_height) + 1

        return height(root) != -1
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(h)`

---

## 10. Subtree of Another Tree

### 题目目标

判断 `subRoot` 是否是 `root` 的一棵子树。

### 这题属于哪一类

属于“树的基础性质判断”。

### 核心思路

枚举 `root` 中的每一个节点，看它作为根时，整棵子树是否和 `subRoot` 完全相同。

### Python 代码

```python
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False

            return same_tree(a.left, b.left) and same_tree(a.right, b.right)

        if not root:
            return False

        if same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
```

### 复杂度

- 时间复杂度：最坏 `O(m * n)`
- 空间复杂度：`O(h)`

### 易错点

- 不是只比较节点值，而是整棵结构都要一样

---

## 11. Validate Binary Search Tree

### 题目目标

判断一棵树是否是合法 BST。

### 这题属于哪一类

属于“BST 专题”。

### 核心思路

不能只看“左孩子小于根、右孩子大于根”。

因为 BST 要求的是：

- 左子树所有节点都小于根
- 右子树所有节点都大于根

最稳妥写法是给每个节点一个合法范围。

### 分步骤理解

1. 根节点一开始范围是 `(-inf, inf)`
2. 走到左子树时，上界变成当前节点值
3. 走到右子树时，下界变成当前节点值
4. 只要节点值不在范围内，就不是 BST

### Python 代码

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True

            if not (low < node.val < high):
                return False

            return (
                dfs(node.left, low, node.val)
                and dfs(node.right, node.val, high)
            )

        return dfs(root, float("-inf"), float("inf"))
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(h)`

### 易错点

- 不能只检查当前节点和左右孩子
- BST 一般要求严格小于和严格大于

---

## 12. Kth Smallest Element in a BST

### 题目目标

找到 BST 中第 `k` 小的元素。

### 这题属于哪一类

属于“BST 专题”。

### 核心思路

BST 的中序遍历结果是有序的。

所以只要做中序遍历，数到第 `k` 个即可。

### Python 代码

```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.answer = 0

        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return

            inorder(node.left)

            self.count += 1
            if self.count == k:
                self.answer = node.val
                return

            inorder(node.right)

        inorder(root)
        return self.answer
```

### 复杂度

- 时间复杂度：`O(h + k)` 到 `O(n)`
- 空间复杂度：`O(h)`

### 易错点

- 这题利用的是“中序有序”

---

## 13. Lowest Common Ancestor of a Binary Search Tree

### 题目目标

找 BST 中两个节点的最近公共祖先。

### 这题属于哪一类

属于“BST 专题”。

### 核心思路

利用 BST 性质：

- 如果 `p` 和 `q` 都小于当前节点，往左走
- 如果都大于当前节点，往右走
- 否则当前节点就是分叉点，也就是答案

### Python 代码

```python
class Solution:
    def lowestCommonAncestor(
        self,
        root: 'TreeNode',
        p: 'TreeNode',
        q: 'TreeNode'
    ) -> 'TreeNode':
        curr = root

        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr
```

### 复杂度

- 时间复杂度：`O(h)`
- 空间复杂度：`O(1)`

---

## 14. Convert Sorted Array to Binary Search Tree

### 题目目标

把有序数组转换成高度平衡 BST。

### 这题属于哪一类

属于“BST 专题”。

### 核心思路

每次取中间元素做根节点。

这样左右两边数量尽量接近，树就更平衡。

### Python 代码

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(nums) - 1)
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(h)`

---

## 15. Lowest Common Ancestor of a Binary Tree

### 题目目标

找普通二叉树中两个节点的最近公共祖先。

### 这题属于哪一类

属于“最近公共祖先”。

### 核心思路

后序递归。

因为要先知道左边有没有、右边有没有，再决定当前节点是不是答案。

### 分步骤理解

1. 如果当前节点为空，返回空
2. 如果当前节点就是 `p` 或 `q`，直接返回当前节点
3. 递归找左子树
4. 递归找右子树
5. 如果左右都找到了，当前节点就是最近公共祖先
6. 如果只有一边找到，就把那一边往上返回

### Python 代码

```python
class Solution:
    def lowestCommonAncestor(
        self,
        root: 'TreeNode',
        p: 'TreeNode',
        q: 'TreeNode'
    ) -> 'TreeNode':
        if not root:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        if left:
            return left

        return right
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(h)`

### 易错点

- 普通二叉树不能用 BST 的大小关系去判断

---

## 16. Path Sum III

### 题目目标

统计路径和等于 `targetSum` 的路径数。

路径必须从上往下走，但不一定从根开始，也不一定在叶子结束。

### 这题属于哪一类

属于“路径 / 贡献值题”。

### 核心思路

最容易理解的做法：

- 枚举每个节点作为起点
- 再从这个起点往下找，看看有多少条路径和等于目标值

不是最花哨的写法，但很适合先学清楚。

### Python 代码

```python
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def count_from(node: Optional[TreeNode], target: int) -> int:
            if not node:
                return 0

            total = 0

            if node.val == target:
                total += 1

            total += count_from(node.left, target - node.val)
            total += count_from(node.right, target - node.val)

            return total

        if not root:
            return 0

        # 以当前节点为起点的路径数
        count_at_root = count_from(root, targetSum)

        # 再去左子树和右子树继续枚举起点
        count_left = self.pathSum(root.left, targetSum)
        count_right = self.pathSum(root.right, targetSum)

        return count_at_root + count_left + count_right
```

### 复杂度

- 时间复杂度：最坏 `O(n^2)`
- 空间复杂度：`O(h)`

### 易错点

- 路径必须向下，但可以从任意节点开始

---

## 17. Count Good Nodes in Binary Tree

### 题目目标

从根到当前节点这条路径上，如果当前节点的值不小于之前所有节点值，它就是 good node。

求 good node 的数量。

### 这题属于哪一类

属于“路径 / 贡献值题”。

### 核心思路

递归过程中一路带着“当前路径上的最大值”。

### Python 代码

```python
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: Optional[TreeNode], path_max: int) -> int:
            if not node:
                return 0

            count = 0
            if node.val >= path_max:
                count = 1

            new_max = max(path_max, node.val)

            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)

            return count

        return dfs(root, root.val)
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(h)`

---

## 18. Binary Tree Maximum Path Sum

### 题目目标

求树中任意路径的最大路径和。

路径不一定经过根节点，但路径必须连续。

### 这题属于哪一类

属于“路径 / 贡献值题”。

### 核心思路

这题最关键的是分清楚两个量：

1. 递归函数返回给父节点的值：
   - 只能选一边
   - 因为路径往上延伸时不能分叉
2. 经过当前节点的完整路径值：
   - 可以同时选左边和右边
   - 用它来更新全局答案

### 分步骤理解

1. 递归求左子树最大贡献值
2. 递归求右子树最大贡献值
3. 如果某边贡献是负数，就不要它，按 0 处理
4. 经过当前节点的路径和 =
   `node.val + left_gain + right_gain`
5. 用它更新全局答案
6. 返回给父节点的只能是：
   `node.val + max(left_gain, right_gain)`

### Python 代码

```python
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.answer = float("-inf")

        def max_gain(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # 经过当前节点的完整路径
            current_path_sum = node.val + left_gain + right_gain
            self.answer = max(self.answer, current_path_sum)

            # 返回给父节点时，只能选一边继续往上
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return self.answer
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(h)`

### 易错点

- 返回给父节点时，不能左右两边一起返回

---

## 19. Construct Binary Tree from Preorder and Inorder Traversal

### 题目目标

根据前序遍历和中序遍历构造二叉树。

### 这题属于哪一类

属于“构造与变形”。

### 核心思路

前序遍历的第一个值一定是根节点。

找到它在中序遍历中的位置后：

- 左边是左子树
- 右边是右子树

### 分步骤理解

1. 前序第一个元素是根
2. 在中序中找到根的位置
3. 这个位置左边那一段是左子树
4. 右边那一段是右子树
5. 递归继续构造

### Python 代码

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {}
        for i, value in enumerate(inorder):
            index_map[value] = i

        self.preorder_index = 0

        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            root_value = preorder[self.preorder_index]
            self.preorder_index += 1

            root = TreeNode(root_value)
            inorder_index = index_map[root_value]

            root.left = build(left, inorder_index - 1)
            root.right = build(inorder_index + 1, right)

            return root

        return build(0, len(inorder) - 1)
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(n)`

### 易错点

- 一定要先建左子树，再建右子树，因为前序是“根左右”

---

## 20. Flatten Binary Tree to Linked List

### 题目目标

把二叉树原地展开成链表，顺序要和前序遍历一致。

### 这题属于哪一类

属于“构造与变形”。

### 核心思路

后序思路更稳。

先把左右子树都处理好，再把：

- 左子树接到右边
- 原来的右子树接到左子树展开后的尾部

### 分步骤理解

1. 先递归展开左子树
2. 再递归展开右子树
3. 如果左子树为空，不用处理
4. 如果左子树不为空：
   - 找到左子树最右边那个节点
   - 把原来的右子树接到它后面
   - 再把左子树整体搬到右边
   - `root.left = None`

### Python 代码

```python
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        if not root.left:
            return

        left_subtree = root.left
        right_subtree = root.right

        # 找到左子树展开后最右边的节点
        tail = left_subtree
        while tail.right:
            tail = tail.right

        # 把原来的右子树接到左子树尾部
        tail.right = right_subtree

        # 把左子树整体移到右边
        root.right = left_subtree
        root.left = None
```

### 复杂度

- 时间复杂度：最坏 `O(n^2)`
- 空间复杂度：`O(h)`

### 说明

这不是最优写法，但更容易理解。

如果你后面要，我可以再单独给你补一版 `O(n)` 的后序写法。

---

## 21. Serialize and Deserialize Binary Tree

### 题目目标

把树编码成字符串，再把字符串还原成原来的树。

### 这题属于哪一类

属于“构造与变形”。

### 核心思路

最容易理解的方式是前序遍历 + 空节点标记。

例如：

- 遇到节点，记录它的值
- 遇到空节点，记录 `"null"`

这样反序列化时就能按同样顺序还原回来。

### Python 代码

```python
class Codec:
    def serialize(self, root):
        values = []

        def dfs(node):
            if not node:
                values.append("null")
                return

            values.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(values)

    def deserialize(self, data):
        values = data.split(",")
        self.index = 0

        def build():
            if values[self.index] == "null":
                self.index += 1
                return None

            node = TreeNode(int(values[self.index]))
            self.index += 1

            node.left = build()
            node.right = build()

            return node

        return build()
```

### 复杂度

- 序列化时间复杂度：`O(n)`
- 反序列化时间复杂度：`O(n)`
- 空间复杂度：`O(n)`

### 易错点

- 空节点一定要记下来，否则树结构还原不出来

---

## 五、最后做一遍方法总结

### 1. 遍历题先想什么

先问自己：

- 我要按什么顺序访问节点？
- 结果是一维列表，还是按层二维列表？

代表题：

- `Binary Tree Inorder Traversal`
- `Binary Tree Level Order Traversal`
- `Binary Tree Right Side View`

### 2. 性质判断题先想什么

先问自己：

- 递归函数返回的是高度？
- 还是布尔值？
- 还是别的信息？

代表题：

- `Maximum Depth of Binary Tree`
- `Balanced Binary Tree`
- `Diameter of Binary Tree`
- `Symmetric Tree`

### 3. BST 题先想什么

先问自己：

- 能不能利用中序有序？
- 能不能利用大小关系只走一边？

代表题：

- `Validate Binary Search Tree`
- `Kth Smallest Element in a BST`
- `Lowest Common Ancestor of a Binary Search Tree`

### 4. 路径题先想什么

先问自己：

- 我的递归返回的是“单边路径值”还是“整条路径值”？
- 是不是要维护全局答案？

代表题：

- `Path Sum III`
- `Binary Tree Maximum Path Sum`

### 5. 构造题先想什么

先问自己：

- 根节点是谁？
- 左子树和右子树范围怎么切？
- 还原结构时，空节点要不要保留？

代表题：

- `Construct Binary Tree from Preorder and Inorder Traversal`
- `Serialize and Deserialize Binary Tree`

---

## 六、复习建议

复习树题时，建议每次都强迫自己先说出下面两件事：

1. 这题属于哪一类
2. 递归函数返回的是什么

很多树题一旦这两点想清楚，代码其实并不复杂。

如果你愿意，我下一步可以继续给你补：

- 一份 `Tree` 考前速记版
- 每题的小样例手推过程
- `DFS / BFS / BST / LCA` 四大模板总结
