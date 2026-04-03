# 10. 有序映射 / TreeMap

## 面试题目怎么问

- 给你一些时间点和对应值，查询某个时间最近的历史值
- 找不大于 `x` 的最大 key
- 找不小于 `x` 的最小 key
- 动态插入和查询最近元素

## 识别信号

- “最近的但不超过”
- “第一个大于等于”
- “前驱 / 后继”
- 需要动态维护有序性

## Amazon 风格业务包装

- 查询某个时间点最近一次生效的价格
- 查询某个订单时间之前最近一次库存状态
- 找距离某个邮编最近的可用配送站
- 动态维护按时间排序的事件并做前驱后继查询

## 你该怎么想

- 看到“最近但不超过”“第一个不小于”，马上想有序结构
- 哈希表只适合精确查找，不适合前驱后继

## 标准代码模板 1：floor

```python
import bisect

def floor_value(keys, values, target):
    idx = bisect.bisect_right(keys, target) - 1
    if idx < 0:
        return None
    return values[idx]
```

## 标准代码模板 2：ceiling

```python
import bisect

def ceiling_value(keys, values, target):
    idx = bisect.bisect_left(keys, target)
    if idx == len(keys):
        return None
    return values[idx]
```

## 面试时怎么讲

- 这类题核心不是哈希，而是有序查询
- Java 里会优先想到 `TreeMap`
- Python 里如果不能用第三方库，常见做法是排序数组加二分

## 常见 follow-up 和回答

**Q1：为什么哈希表不适合这类题？**  
哈希表不维护顺序，无法高效回答 `floor` / `ceiling`。

**Q2：Python 没有 TreeMap 怎么办？**  
离线查询可用排序加二分；高频动态插入时要和面试官说明语言限制。

**Q3：如果既要动态插入又要频繁查询最近值怎么办？**  
理想结构是平衡树，比如 Java `TreeMap`。

## Amazon 风格完整题面

> You are given historical price updates `(timestamp, price)`.  
> For a query timestamp `t`, return the latest price that became effective at or before `t`.

## 可直接背的口语回答稿

“这个问题的关键不是查某个 key 是否存在，而是找不超过 `target` 的最近一个 key，也就是 `floor` 查询。所以我会优先想到 ordered map；在 Python 里如果不使用第三方库，可以先把时间戳排序，再用二分找到 `bisect_right(target) - 1` 的位置。”

## 推荐代表题

- Time Based Key-Value Store
- Find Right Interval
- 各类 floor / ceiling 查询题

