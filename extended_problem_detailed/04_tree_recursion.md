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

```text
// BFS 分层
```

### Binary Tree Right Side View

```text
// 每层最后一个
```

### Symmetric Tree

```text
// 比较镜像子树
```

### Diameter of Binary Tree

```text
// 当前直径 = 左高度 + 右高度
// 返回高度给父节点
```

### Path Sum / Path Sum II / Path Sum III

```text
// I：是否存在
// II：收集路径
// III：前缀和思想
```

### Flatten Binary Tree to Linked List

```text
// 前序结构重连
```

### Construct Binary Tree from Preorder and Inorder

```text
// preorder 定根
// inorder 切左右子树
```

### Lowest Common Ancestor

```text
// 左右都返回非空时，当前即祖先
```

### Validate Binary Search Tree

```text
// 上下界约束
```

### Kth Smallest Element in a BST

```text
// 中序有序
```

### Serialize / Deserialize

```text
// Binary Tree 常用前序 + null
// BST 可利用 BST 性质，但先会普通版
```

---

## 建议顺序

1. Symmetric Tree
2. Binary Tree Level Order Traversal
3. Binary Tree Right Side View
4. Diameter of Binary Tree
5. Path Sum
6. Path Sum II
7. Validate Binary Search Tree
8. Lowest Common Ancestor of a Binary Tree
9. Kth Smallest Element in a BST
10. Flatten Binary Tree to Linked List
11. Construct Binary Tree from Preorder and Inorder Traversal
12. Path Sum III
13. Binary Tree Maximum Path Sum
14. Serialize and Deserialize Binary Tree

