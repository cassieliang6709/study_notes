---
title: "04 二叉树与 BST"
---

# 04 二叉树与 BST

树题不要一题一题背，要先统一成“遍历 + 返回值”的思路。

---

## 一、先记住四种遍历

```text
// 前序：中左右
// 中序：左中右
// 后序：左右中
// 层序：按层 BFS
```

如何选：

```text
// 构造 / 路径 => 前序
// BST 有序性 => 中序
// 子树向上返回信息 => 后序
// 每层信息 => 层序
```

---

## 二、DFS 统一模板

```text
def dfs(node):
    if not node:
        return base

    left = dfs(node.left)
    right = dfs(node.right)

    // 组合左右子树的信息
    return 给父节点的结果
```

关键问题：

```text
// 当前题里，dfs(node) 到底表示什么？
// 是高度？路径和？是否合法？还是某个最优值？
```

---

## 三、重点题

### 1. Maximum Depth of Binary Tree

**这个题型 / 算法点的总结**

`Maximum Depth of Binary Tree` 主要在练树的递归返回值设计。做这类题时先决定遍历方式，再决定递归函数返回什么。

**题目含义**

题目要你求二叉树的最大深度，也就是从根节点到最深叶子节点一共经过多少层。最自然的定义就是：`depth(root) = 1 + max(depth(left), depth(right))`。

**Python 代码**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(h)`，递归栈高度为树高。

**怎么想到这个方法**

树高题往往直接写递归定义最自然：当前节点的深度等于左右子树更深者加一。

**示例 case**

- 输入：一棵高度为 3 的二叉树
- 输出：`3`。递归返回左右子树更深者加一。

**常见 Follow-up**

- BFS 版怎么写？
- 平衡树和链式树的空间区别是什么？

### 2. Invert Binary Tree

**这个题型 / 算法点的总结**

`Invert Binary Tree` 主要在练树的递归返回值设计。做这类题时先决定遍历方式，再决定递归函数返回什么。

**题目含义**

这题就是把每个节点的左右子树交换。因为每个节点都做同一件事，所以非常适合 DFS 或递归。

**Python 代码**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(h)`。

**怎么想到这个方法**

每个节点都做同样的左右交换，所以递归是最顺手的表达方式。把这题想成“后序地返回交换后的子树”就很自然。

**示例 case**

- 输入：二叉树根节点
- 输出：左右子树全部镜像交换后的树。

**常见 Follow-up**

- 迭代版怎么写？
- 为什么这题特别适合解释递归框架？

### 3. Binary Tree Inorder Traversal

**这个题型 / 算法点的总结**

`Binary Tree Inorder Traversal` 主要在练树的递归返回值设计。做这类题时先决定遍历方式，再决定递归函数返回什么。

**题目含义**

题目要求中序遍历二叉树，也就是按 `left -> root -> right` 的顺序输出节点值。面试里通常会优先写迭代版，因为它能体现你真的理解栈是怎么模拟递归的。

**Python 代码**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        ans = []
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right

        return ans
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(h)`。

**怎么想到这个方法**

中序遍历的顺序固定是左根右。迭代版的重点是理解：一路向左压栈，相当于手动模拟递归调用栈。

**示例 case**

- 输入：`[1,null,2,3]`
- 输出：`[1,3,2]`。中序遍历顺序是左、根、右。

**常见 Follow-up**

- 前序和后序的迭代写法如何改？
- 如果是 BST，中序遍历有什么额外性质？

### 4. Symmetric Tree

**这个题型 / 算法点的总结**

`Symmetric Tree` 主要在练树的递归返回值设计。做这类题时先决定遍历方式，再决定递归函数返回什么。

**题目含义**

对称树的关键不是分别判断左右子树，而是判断：

- 左树的左子树 vs 右树的右子树
- 左树的右子树 vs 右树的左子树

**Python 代码**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional['TreeNode']) -> bool:
        def mirror(a, b):
            if not a and not b:
                return True
            if not a or not b or a.val != b.val:
                return False
            return mirror(a.left, b.right) and mirror(a.right, b.left)

        return mirror(root.left, root.right) if root else True
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(h)` 递归栈。

**怎么想到这个方法**

对称不是看单边，而是同时比较两棵镜像子树：左的左对右的右，左的右对右的左。

**示例 case**

- 输入：左右镜像的二叉树
- 输出：`True`。镜像比较要同时看左左对右右、左右对右左。

**常见 Follow-up**

- 迭代版怎么用队列成对比较？
- 如果是 `same tree`，条件怎么变化？

### 5. Binary Tree Level Order Traversal

**这个题型 / 算法点的总结**

`Binary Tree Level Order Traversal` 主要在练树的递归返回值设计。做这类题时先决定遍历方式，再决定递归函数返回什么。

**题目含义**

这是最标准的树 BFS 题。  
用队列一层一层处理，每次循环先记录当前层大小，然后把这一层所有节点弹出并把孩子加入队列。

**Python 代码**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import List, Optional


class Solution:
    def levelOrder(self, root: Optional['TreeNode']) -> List[List[int]]:
        if not root:
            return []

        ans = []
        q = deque([root])

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)

        return ans
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(n)`。

**怎么想到这个方法**

只要题目要求“按层输出”，那就是 BFS 队列模板。队列长度天然告诉你这一层有几个节点。

**示例 case**

- 输入：普通二叉树
- 输出：按层分组的节点值数组，例如 `[[3],[9,20],[15,7]]`。

**常见 Follow-up**

- 如果改成自底向上输出怎么做？
- DFS 能不能写出层序遍历？

### 6. Diameter of Binary Tree

**这个题型 / 算法点的总结**

`Diameter of Binary Tree` 主要在练树的递归返回值设计。做这类题时先决定遍历方式，再决定递归函数返回什么。

**题目含义**

对每个节点：

- 经过它的最长路径 = 左子树高度 + 右子树高度
- 返回给父节点的是自己的高度

所以这题是标准的“后序遍历 + 全局答案”。

**Python 代码**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional['TreeNode']) -> int:
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

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(h)`。

**怎么想到这个方法**

树的直径题通常不是在每个点向外暴力扩，而是后序遍历时顺便拿到左右子树高度，再更新答案。

**示例 case**

- 输入：二叉树
- 输出：任意两节点间最长路径长度。答案不一定经过根。

**常见 Follow-up**

- 为什么答案不一定经过根？
- 如果要求输出路径本身，还要额外记录什么？

### 7. Validate Binary Search Tree

**这个题型 / 算法点的总结**

`Validate Binary Search Tree` 主要在练树的递归返回值设计。做这类题时先决定遍历方式，再决定递归函数返回什么。

**题目含义**

不能只检查：

```text
node.left < node < node.right
```

因为 BST 的约束是整棵子树范围。  
所以递归时要传入合法区间 `(low, high)`。

**Python 代码**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isValidBST(self, root: Optional['TreeNode']) -> bool:
        def valid(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return valid(node.left, low, node.val) and valid(node.right, node.val, high)

        return valid(root, float("-inf"), float("inf"))
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(h)`。

**怎么想到这个方法**

BST 校验容易掉进“只比父节点”的坑。正确思路是给每个节点传可取值范围，或者用中序递增性质。

**示例 case**

- 输入：一棵二叉树
- 输出：判断是否满足 BST 全局有序约束，而不是只比较父子节点。

**常见 Follow-up**

- 为什么只比较父子节点不够？
- 中序遍历版怎么写？

### 8. Kth Smallest Element in a BST

**这个题型 / 算法点的总结**

`Kth Smallest Element in a BST` 主要在练树的递归返回值设计。做这类题时先决定遍历方式，再决定递归函数返回什么。

**题目含义**

BST 中序遍历结果是递增的。  
所以只要中序遍历到第 `k` 个节点，返回它的值即可。

**Python 代码**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def kthSmallest(self, root: Optional['TreeNode'], k: int) -> int:
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val

            root = root.right
```

**时间复杂度**

`O(h+k)`，最坏 `O(n)`。

**空间复杂度**

`O(h)`。

**怎么想到这个方法**

BST 的中序遍历天然有序，所以这题最直接的思路就是中序走到第 `k` 个就停。

**示例 case**

- 输入：BST 和 `k = 3`
- 输出：中序遍历第 3 个节点值。

**常见 Follow-up**

- 如果树频繁更新、频繁查询第 k 小，怎么优化？
- 如果要求第 k 大呢？

### 9. Lowest Common Ancestor of a Binary Tree

**这个题型 / 算法点的总结**

`Lowest Common Ancestor of a Binary Tree` 主要在练树的递归返回值设计。做这类题时先决定遍历方式，再决定递归函数返回什么。

**题目含义**

如果：

- 左子树找到了一个目标
- 右子树也找到了另一个目标

那么当前节点就是最近公共祖先。  
否则，把找到的那个节点往上返回。

**Python 代码**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(h)`。

**怎么想到这个方法**

LCA 的递归核心是：如果左右子树分别找到了不同目标，那么当前节点就是分叉点。

**示例 case**

- 输入：二叉树中的两个节点
- 输出：它们最近的公共祖先节点。

**常见 Follow-up**

- 如果是 BST，如何利用有序性优化？
- 如果节点有父指针，能不能换思路？

### 10. Binary Tree Right Side View

**这个题型 / 算法点的总结**

`Binary Tree Right Side View` 主要在练树的递归返回值设计。做这类题时先决定遍历方式，再决定递归函数返回什么。

**题目含义**

右视图的意思是：每一层只看最右边那个节点。  
最直接做法是层序遍历，每层最后访问到的节点加入答案。

**Python 代码**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import List, Optional


class Solution:
    def rightSideView(self, root: Optional['TreeNode']) -> List[int]:
        if not root:
            return []

        ans = []
        q = deque([root])

        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if i == size - 1:
                    ans.append(node.val)

        return ans
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(n)`。

**怎么想到这个方法**

题目按层看每层最右边节点，所以最自然还是层序遍历，只记录每层最后一个出队节点。

**示例 case**

- 输入：二叉树
- 输出：从右侧看到的节点列表，例如 `[1,3,4]`。

**常见 Follow-up**

- DFS 也能做吗？
- 如果要左视图，只改哪一行？

### 11. Path Sum III

**这个题型 / 算法点的总结**

`Path Sum III` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

这题和数组里的 `Subarray Sum Equals K` 很像。  
我们维护从根到当前节点的前缀和 `prefix`。  
如果之前出现过某个前缀和 `prefix - targetSum`，说明中间这一段路径和正好等于目标值。

**Python 代码**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import defaultdict
from typing import Optional


class Solution:
    def pathSum(self, root: Optional['TreeNode'], targetSum: int) -> int:
        count = defaultdict(int)
        count[0] = 1

        def dfs(node, prefix):
            if not node:
                return 0

            prefix += node.val
            ans = count[prefix - targetSum]
            count[prefix] += 1

            ans += dfs(node.left, prefix)
            ans += dfs(node.right, prefix)

            count[prefix] -= 1
            return ans

        return dfs(root, 0)
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(n)`。

**怎么想到这个方法**

这题虽然在树上，但问的是“路径和为 target 的条数”，所以要联想到数组里的前缀和计数，再把它搬到 DFS 路径上。

**示例 case**

- 输入：二叉树和 `targetSum`
- 输出：所有向下路径中和等于目标值的条数。

**常见 Follow-up**

- 为什么不能只从根开始算？
- 如果路径必须从根到叶，思路怎么简化？

### 12. Flatten Binary Tree to Linked List

**这个题型 / 算法点的总结**

`Flatten Binary Tree to Linked List`` 主要在练链表指针操作，重点是想清楚节点之间该怎么断开、反转和接回去。

**题目含义**

目标是把树变成前序遍历顺序的链表。  
对当前节点：

1. 先拍平左右子树
2. 如果有左子树，就把左子树插到右边
3. 再把原右子树接到左子树尾部

**Python 代码**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def flatten(self, root: Optional['TreeNode']) -> None:
        def dfs(node):
            if not node:
                return None

            left_tail = dfs(node.left)
            right_tail = dfs(node.right)

            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None

            return right_tail or left_tail or node

        dfs(root)
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(h)`。

**怎么想到这个方法**

题目要原地把树拉平成先序链表，所以你需要保住左右子树的连接关系。后序返回尾节点会写得更稳。

**示例 case**

- 输入：二叉树
- 输出：原地拉平成先序遍历顺序的右链表。

**常见 Follow-up**

- 你能讲 Morris 风格的 `O(1)` 空间做法吗？
- 为什么要先处理右子树再处理左子树？

### 13. Construct Binary Tree from Preorder and Inorder

**这个题型 / 算法点的总结**

`Construct Binary Tree from Preorder and Inorder` 主要在练树的递归返回值设计。做这类题时先决定遍历方式，再决定递归函数返回什么。

**题目含义**

关键性质：

- 前序第一个元素一定是根
- 中序中根左边是左子树，右边是右子树

所以每次递归：

1. 从前序取根
2. 在中序定位根
3. 递归构建左右子树

**Python 代码**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional['TreeNode']:
        pos = {value: i for i, value in enumerate(inorder)}
        pre_idx = 0

        def build(left, right):
            nonlocal pre_idx
            if left > right:
                return None

            root_val = preorder[pre_idx]
            pre_idx += 1

            root = TreeNode(root_val)
            mid = pos[root_val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(n)`。

**怎么想到这个方法**

前序给根，中序帮你切左右子树。只要你能说清“根是谁、左右范围怎么切”，这题就已经过半了。

**示例 case**

- 输入：前序和中序遍历数组
- 输出：还原出的原始二叉树。

**常见 Follow-up**

- 为什么需要 `value -> index` 哈希表？
- 如果改成中序 + 后序呢？

### 14. Binary Tree Maximum Path Sum

**这个题型 / 算法点的总结**

`Binary Tree Maximum Path Sum` 主要在练树的递归返回值设计。做这类题时先决定遍历方式，再决定递归函数返回什么。

**题目含义**

这题最容易混淆的点是：

- 返回给父节点的值
- 全局最大路径值

不是一回事。

对每个节点：

- 向父节点返回：`node.val + max(left_gain, right_gain)`
- 更新全局答案：`node.val + left_gain + right_gain`

负贡献要直接丢掉，所以要和 `0` 比较。

**Python 代码**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def maxPathSum(self, root: Optional['TreeNode']) -> int:
        ans = float("-inf")

        def dfs(node):
            nonlocal ans
            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            ans = max(ans, node.val + left + right)
            return node.val + max(left, right)

        dfs(root)
        return ans
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(h)`。

**怎么想到这个方法**

最大路径和的难点是区分“往上返回给父节点的值”和“当前节点内部更新答案的值”。这通常是树 DP 的标志。

**示例 case**

- 输入：可能包含负数的二叉树
- 输出：任意路径的最大路径和。

**常见 Follow-up**

- 为什么返回值不能同时带左右两边？
- 如果节点值全负，初始化要注意什么？

