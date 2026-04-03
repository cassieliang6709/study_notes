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


---

## Quiz

**Q1: `Binary Tree Right Side View` 用 BFS，每层取哪个节点？**

- [ ] 第一个节点
- [ ] 最后一个节点 ✅
- [ ] 最大值节点
- [ ] 中间节点

**Q2: `Diameter of Binary Tree` 的直径等于什么？**

- [ ] 根节点到最深叶子的路径
- [ ] 左子树深度 + 右子树深度（在任意节点处取最大值） ✅
- [ ] 节点总数
- [ ] 最深叶子的层数

**Q3: `Flatten Binary Tree to Linked List` 展开后的顺序是什么遍历顺序？**

- [ ] 中序
- [ ] 后序
- [ ] 前序 ✅
- [ ] 层序

**Q4: `Validate Binary Search Tree` 为什么不能只比较 node.val 和左右子节点？**

- [ ] 因为 BST 不要求左右子节点有序
- [ ] 因为整棵左子树都要小于根，单层比较会漏掉孙节点违规的情况 ✅
- [ ] 因为 Python 比较整数会出错
- [ ] 因为二叉树可能不平衡

**Q5: `Path Sum III`（路径不必从根开始）最优解法的核心思想是什么？**

- [ ] 暴力枚举所有路径
- [ ] 前缀和 + 哈希表，记录到当前节点的路径和出现次数 ✅
- [ ] DFS 只从根节点出发
- [ ] BFS 按层累加
