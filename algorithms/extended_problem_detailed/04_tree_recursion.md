---
title: "04 树与递归详细教学"
---

# 04 树与递归详细教学

树题先决定遍历方式，再决定返回值。

---

## 一、遍历选择

```text
// 前序：构造
// 中序：BST
// 后序：子树信息
// 层序：每层统计
```

---

## 二、代表题

### Binary Tree Level Order Traversal

**这个题型 / 算法点的总结**

`Binary Tree Level Order Traversal` 主要在练树的递归返回值设计。做这类题时先决定遍历方式，再决定递归函数返回什么。

**题目含义**

这是最标准的树 BFS 题。  
用队列一层一层处理，每次循环先记录当前层大小，然后把这一层所有节点弹出并把孩子加入队列。

**代表 Python 代码**

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

先看题型识别里的信号：这题本质上就是 `层序遍历 / Level Order BFS`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：普通二叉树
- 输出：按层分组的节点值数组，例如 `[[3],[9,20],[15,7]]`。

**常见 Follow-up**

- 如果要返回具体路径而不是只判断可行性，额外记录什么？
- DFS、BFS、并查集三种解法分别适合什么场景？

### Binary Tree Right Side View

**这个题型 / 算法点的总结**

`Binary Tree Right Side View` 主要在练树的递归返回值设计。做这类题时先决定遍历方式，再决定递归函数返回什么。

**题目含义**

右视图的意思是：每一层只看最右边那个节点。  
最直接做法是层序遍历，每层最后访问到的节点加入答案。

**代表 Python 代码**

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

先看题型识别里的信号：这题本质上就是 `层序视图 / Level View`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：二叉树
- 输出：从右侧看到的节点列表，例如 `[1,3,4]`。

**常见 Follow-up**

- 如果要返回具体路径而不是只判断可行性，额外记录什么？
- DFS、BFS、并查集三种解法分别适合什么场景？

### Symmetric Tree

**这个题型 / 算法点的总结**

`Symmetric Tree` 主要在练树的递归返回值设计。做这类题时先决定遍历方式，再决定递归函数返回什么。

**题目含义**

对称树的关键不是分别判断左右子树，而是判断：

- 左树的左子树 vs 右树的右子树
- 左树的右子树 vs 右树的左子树

**代表 Python 代码**

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

`O(h)`。

**怎么想到这个方法**

先看题型识别里的信号：这题本质上就是 `镜像递归 / Mirror Recursion`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：左右镜像的二叉树
- 输出：`True`。镜像比较要同时看左左对右右、左右对右左。

**常见 Follow-up**

- 能不能把空间复杂度再压缩一层？
- 有没有另一种常见模板也能解决这题？

### Diameter of Binary Tree

**这个题型 / 算法点的总结**

`Diameter of Binary Tree` 主要在练树的递归返回值设计。做这类题时先决定遍历方式，再决定递归函数返回什么。

**题目含义**

对每个节点：

- 经过它的最长路径 = 左子树高度 + 右子树高度
- 返回给父节点的是自己的高度

所以这题是标准的“后序遍历 + 全局答案”。

**代表 Python 代码**

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

先看题型识别里的信号：这题本质上就是 `后序 DFS 求高度 / Postorder Height Computation`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：二叉树
- 输出：任意两节点间最长路径长度。答案不一定经过根。

**常见 Follow-up**

- 如果要返回具体路径而不是只判断可行性，额外记录什么？
- DFS、BFS、并查集三种解法分别适合什么场景？

### Path Sum / Path Sum II / Path Sum III

**这个题型 / 算法点的总结**

`Path Sum / Path Sum II / Path Sum III` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

这一组题都在问树上的路径问题：`Path Sum I` 判断是否存在，`II` 收集所有路径，`III` 统计路径条数。真正需要优先掌握的是“路径信息该怎么沿递归传下去”，以及 `Path Sum III` 的前缀和做法。

**代表 Python 代码**

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
        prefix = defaultdict(int)
        prefix[0] = 1
        ans = 0

        def dfs(node, cur):
            nonlocal ans
            if not node:
                return
            cur += node.val
            ans += prefix[cur - targetSum]
            prefix[cur] += 1
            dfs(node.left, cur)
            dfs(node.right, cur)
            prefix[cur] -= 1

        dfs(root, 0)
        return ans
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(n)`。

**怎么想到这个方法**

如果只是根到叶，普通 DFS 就够了；一旦题目允许路径从中间开始，就该联想到“路径和 = 两个前缀和之差”。

**示例 case**

- 输入：一个最小可手算的样例
- 输出：先手推一遍算法流程，再对照代码中的循环、状态或数据结构变化。

**常见 Follow-up**

- `Path Sum I / II / III` 的状态传递分别有什么不同？
- 如果树节点值可能是负数，为什么不能直接剪枝？

### Flatten Binary Tree to Linked List

**这个题型 / 算法点的总结**

`Flatten Binary Tree to Linked List` 主要在练链表指针操作，重点是想清楚节点之间该怎么断开、反转和接回去。

**题目含义**

目标是把树变成前序遍历顺序的链表。  
对当前节点：

1. 先拍平左右子树
2. 如果有左子树，就把左子树插到右边
3. 再把原右子树接到左子树尾部

**代表 Python 代码**

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

先看题型识别里的信号：这题本质上就是 `树结构重连 / Tree Rewiring`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：二叉树
- 输出：原地拉平成先序遍历顺序的右链表。

**常见 Follow-up**

- 能不能把空间复杂度再压缩一层？
- 有没有另一种常见模板也能解决这题？

### Construct Binary Tree from Preorder and Inorder

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

**代表 Python 代码**

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

先看题型识别里的信号：这题本质上就是 `递归构造 / Recursive Tree Construction`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：前序和中序遍历数组
- 输出：还原出的原始二叉树。

**常见 Follow-up**

- 能不能把空间复杂度再压缩一层？
- 有没有另一种常见模板也能解决这题？

### Lowest Common Ancestor

**这个题型 / 算法点的总结**

`Lowest Common Ancestor` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

如果：

- 左子树找到了一个目标
- 右子树也找到了另一个目标

那么当前节点就是最近公共祖先。  
否则，把找到的那个节点往上返回。

**代表 Python 代码**

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

先看题型识别里的信号：这题本质上就是 `后序递归判断 / Postorder Recursive Search`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：一个最小可手算的样例
- 输出：先手推一遍算法流程，再对照代码中的循环、状态或数据结构变化。

**常见 Follow-up**

- 能不能把空间复杂度再压缩一层？
- 有没有另一种常见模板也能解决这题？

### Validate Binary Search Tree

**这个题型 / 算法点的总结**

`Validate Binary Search Tree` 主要在练树的递归返回值设计。做这类题时先决定遍历方式，再决定递归函数返回什么。

**题目含义**

不能只检查：

```text
node.left < node < node.right
```

因为 BST 的约束是整棵子树范围。  
所以递归时要传入合法区间 `(low, high)`。

**代表 Python 代码**

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

先看题型识别里的信号：这题本质上就是 `BST 上下界检查 / BST Range Validation`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：一棵二叉树
- 输出：判断是否满足 BST 全局有序约束，而不是只比较父子节点。

**常见 Follow-up**

- 能不能把空间复杂度再压缩一层？
- 有没有另一种常见模板也能解决这题？

### Kth Smallest Element in a BST

**这个题型 / 算法点的总结**

`Kth Smallest Element in a BST` 主要在练树的递归返回值设计。做这类题时先决定遍历方式，再决定递归函数返回什么。

**题目含义**

BST 中序遍历结果是递增的。  
所以只要中序遍历到第 `k` 个节点，返回它的值即可。

**代表 Python 代码**

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

先看题型识别里的信号：这题本质上就是 `BST 中序遍历 / Inorder Traversal of BST`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。

**示例 case**

- 输入：BST 和 `k = 3`
- 输出：中序遍历第 3 个节点值。

**常见 Follow-up**

- 能不能把空间复杂度再压缩一层？
- 有没有另一种常见模板也能解决这题？

### Serialize / Deserialize

**这个题型 / 算法点的总结**

`Serialize / Deserialize` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。

**题目含义**

这类题的本质是给树定义一个可逆编码。普通二叉树最稳的是前序遍历配合 `null` 标记；BST 则有机会进一步利用有序性压缩信息。

**代表 Python 代码**

```python
class Codec:
    def serialize(self, root):
        vals = []

        def dfs(node):
            if not node:
                vals.append("null")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(vals)

    def deserialize(self, data):
        vals = iter(data.split(","))

        def dfs():
            val = next(vals)
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
```

**时间复杂度**

`O(n)`。

**空间复杂度**

`O(n)`。

**怎么想到这个方法**

先别急着写代码，先想清楚“我打算按什么遍历顺序编码，空节点怎么表示，解码时怎样唯一还原”。

**示例 case**

- 输入：一个最小可手算的样例
- 输出：先手推一遍算法流程，再对照代码中的循环、状态或数据结构变化。

**常见 Follow-up**

- 如果是 BST，怎样减少 `null` 标记？
- 如果要按层序序列化，代码结构会怎样变化？

