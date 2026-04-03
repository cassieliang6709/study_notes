---
title: "LRU Cache"
---

# LRU Cache

## 题目含义

设计一个缓存，支持：

- `get(key)`：如果 key 存在，返回值；否则返回 `-1`
- `put(key, value)`：插入或更新
- 当容量满时，淘汰最近最少使用的元素

这题的重点不是代码量，而是你能不能稳定讲清楚为什么操作都能做到 `O(1)`。

## Python 代码

```python
class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert_front(self, node: Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._insert_front(node)
            return

        node = Node(key, value)
        self.cache[key] = node
        self._insert_front(node)

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
```

## 时间复杂度

- `get`: `O(1)`
- `put`: `O(1)`

## 空间复杂度

`O(capacity)`

## 怎么想到这个方法

题目同时要求两件事：

- 按 key 快速查
- 按“最近使用顺序”快速删

单靠哈希表不够，因为它不会维护顺序；单靠链表也不够，因为查找太慢。于是自然想到：

- `hash map` 负责 `key -> node`
- 双向链表负责维护最近使用顺序

## 常见 Follow-up

- 为什么必须是双向链表，单链表哪里不够？
- 如果 interviewer 继续追问 LFU，数据结构要怎么升级？
- 如果要支持 TTL 或并发，额外需要维护什么？

## 常见易错点

- 更新已有 key 后忘了移动到链表头部
- 淘汰尾节点时忘了同步从哈希表删除
- `capacity = 0` 时没有单独想清楚行为
