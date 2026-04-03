---
title: "LFU Cache"
---

# LFU Cache

## 这个题型 / 算法点的总结

这题本质是“设计类 + 频率分桶 + 同频下再按 LRU 处理”。和 LRU 相比，它多了一层频率维度，所以要维护 `freq -> keys` 这层结构。

## 题目含义

设计一个缓存，支持 `get` / `put`，容量满时淘汰访问频次最低的元素；如果多个元素频次相同，淘汰其中最久未使用的。

这题本质上是在 LRU 的基础上多加了一层“频率分桶”。

## Python 代码

```python
from collections import defaultdict, OrderedDict


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val_freq = {}
        self.freq_to_keys = defaultdict(OrderedDict)

    def _bump(self, key: int) -> None:
        value, freq = self.key_to_val_freq[key]
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        self.key_to_val_freq[key] = (value, freq + 1)
        self.freq_to_keys[freq + 1][key] = None

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        value, _ = self.key_to_val_freq[key]
        self._bump(key)
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_val_freq:
            _, freq = self.key_to_val_freq[key]
            self.key_to_val_freq[key] = (value, freq)
            self._bump(key)
            return

        if len(self.key_to_val_freq) == self.capacity:
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val_freq[evict_key]
            if not self.freq_to_keys[self.min_freq]:
                del self.freq_to_keys[self.min_freq]

        self.key_to_val_freq[key] = (value, 1)
        self.freq_to_keys[1][key] = None
        self.min_freq = 1
```

## 时间复杂度

- `get`: `O(1)` 均摊
- `put`: `O(1)` 均摊

## 空间复杂度

`O(capacity)`

## 怎么想到这个方法

这题相比 LRU 多了一个维度：

- 不仅要知道最近是否使用
- 还要知道使用了多少次

所以要从一层顺序变成两层结构：

- `key -> (value, freq)`
- `freq -> ordered keys`
- `min_freq` 记录当前最小频次

## 示例 case

- 输入操作：`put(1,1)`, `put(2,2)`, `get(1)`, `put(3,3)`
- 输出行为：插入 `3` 时会淘汰 key `2`
- 为什么：key `1` 被访问后频次更高，key `2` 仍处于最低频次

## 常见 Follow-up

- 为什么需要 `min_freq`，不维护它会怎样？
- 同频次下为什么还要按 LRU 淘汰？
- 如果频率特别大，是否需要做老化或衰减？

## 常见易错点

- 频率升级后忘了更新 `min_freq`
- 淘汰元素后频率桶为空没有清理
- 更新已有 key 的 value 时忘了同时 bump 频率
