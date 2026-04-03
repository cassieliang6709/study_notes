# 5. 数组 + HashSet / HashMap

## 面试题目怎么问

- 找最长连续序列长度
- 统计每个元素频率
- 按某个规则分组，比如字母异位词
- 两数之和、元素映射、出现次数统计

## 识别信号

- 快速查找某个元素是否存在
- 频率统计
- 去重
- 建立值到信息的映射

## Amazon 风格业务包装

- inventory item IDs 里找最长连续编号区间
- 统计每种商品出现次数
- 把商品按某种属性分组
- 订单号或用户 ID 做快速查重、去重、映射

## 你该怎么想

- 看到“存在性判断”就想 set
- 看到“频次”就想 map / Counter
- 看到“最长连续”就想 Longest Consecutive Sequence

## 标准代码模板 1：Longest Consecutive Sequence

```python
def longest_consecutive(nums):
    num_set = set(nums)
    best = 0

    for x in num_set:
        if x - 1 not in num_set:
            y = x
            while y in num_set:
                y += 1
            best = max(best, y - x)

    return best
```

## 标准代码模板 2：频次统计

```python
from collections import Counter

def count_freq(nums):
    return Counter(nums)
```

## 标准代码模板 3：分组

```python
from collections import defaultdict

def group_by_first_letter(words):
    groups = defaultdict(list)
    for w in words:
        groups[w[0]].append(w)
    return groups
```

## 标准代码模板 4：Two Sum

```python
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []
```

## 代码讲解

- `set` 用来做高效存在性判断
- `map` 用来记录频率、位置、分组、状态
- 最长连续序列的关键是只从“没有前驱的点”开始扩展

## 面试时怎么讲

- 如果题目核心是“某个元素在不在”，我优先考虑 `set`
- 如果题目核心是“某个元素对应什么信息”，我优先考虑 `map`
- 最长连续序列用 `set`，并只从连续段起点扩展

## 常见 follow-up 和回答

**Q1：最长连续序列为什么是 `O(n)`？**  
每个元素最多只会在某个连续段扩展中被访问一次。

**Q2：什么时候用 `set`，什么时候用 `map`？**  
只关心“在不在”用 `set`；需要记录频率、位置、分组时用 `map`。

**Q3：如果数组特别大，空间不够怎么办？**  
可以先排序再线性扫描，时间 `O(n log n)`，空间更省。

## Amazon 风格完整题面

> You are given a list of inventory item IDs.  
> Return the length of the longest consecutive ID range that appears in the list.

## 可直接背的口语回答稿

“这里业务背景可以先忽略，本质上就是数组里找最长连续序列。因为核心操作是高效判断某个数在不在，所以我会先把所有元素放进 `set`。然后只从连续段起点开始向后扩展，也就是只处理那些 `x - 1` 不在集合里的数。这样避免重复扫描，整体时间复杂度是 `O(n)`。”

## 推荐代表题

- Longest Consecutive Sequence
- Two Sum
- Group Anagrams
- Top K Frequent Elements

