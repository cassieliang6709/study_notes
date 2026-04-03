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

```text
// dfs(node) = 以 node 为根的最大深度
// return 1 + max(left, right)
```

### 2. Invert Binary Tree

```text
// 交换左右子树即可
// 这是练递归手感的模板题
```

### 3. Binary Tree Inorder Traversal

```text
// 记住中序遍历顺序
// 左 -> 中 -> 右
```

### 4. Symmetric Tree

```text
// 判断两棵树是否镜像
// 左树的左 对 右树的右
// 左树的右 对 右树的左
```

### 5. Binary Tree Level Order Traversal

```text
// BFS
// 每次取一整层
```

### 6. Diameter of Binary Tree

```text
// 每个节点都试一次：
// 左高度 + 右高度
// 返回给父节点的是当前高度
```

### 7. Validate Binary Search Tree

```text
// 不能只比较父子
// 要维护上下界
```

### 8. Kth Smallest Element in a BST

```text
// BST 中序有序
// 中序遍历计数
```

### 9. Lowest Common Ancestor of a Binary Tree

```text
// 左右都找到了，当前就是 LCA
// 只一边找到，就把那一边结果往上返回
```

### 10. Binary Tree Right Side View

```text
// 层序遍历每层最后一个
// 或 DFS 先右后左
```

### 11. Path Sum III

```text
// 根到当前路径上的前缀和
// 和数组里的 subarray sum equals k 是同一模式
```

### 12. Flatten Binary Tree to Linked List

```text
// 拍平后要求变成前序顺序
// 所以思路要围绕前序结构来想
```

### 13. Construct Binary Tree from Preorder and Inorder

```text
// preorder 第一个是根
// inorder 里根左边是左子树，右边是右子树
```

### 14. Binary Tree Maximum Path Sum

```text
// 全局答案：left + node + right
// 返回给父节点：node + max(left, right)
// 注意负贡献直接舍弃
```

---

## 四、树题统一自检

```text
// 递归函数返回什么？
// 这是经过当前节点的答案，还是返回给父节点的答案？
// 要不要全局变量？
// 是 DFS 还是 BFS 更自然？
```

---

## 五、推荐刷题顺序

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

