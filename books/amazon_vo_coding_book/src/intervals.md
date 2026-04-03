# 8. 区间 / 扫描线

## 面试题目怎么问

- 合并重叠区间
- 判断是否有区间冲突
- 需要多少个会议室
- 某一时刻最大并发量是多少

## 识别信号

- 输入是一组 `[start, end]`
- 问是否重叠
- 问最大同时存在多少个
- 问合并后的区间

## Amazon 风格业务包装

- 配送车辆占用 loading dock 的时间区间是否冲突
- warehouse station / packing station / loading bay 需要多少个
- 多个订单在时间轴上同时活跃，求峰值并发
- 合并重叠的 delivery time slots

## 标准代码模板 1：合并区间

```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    res = []

    for start, end in intervals:
        if not res or res[-1][1] < start:
            res.append([start, end])
        else:
            res[-1][1] = max(res[-1][1], end)

    return res
```

## 标准代码模板 2：Meeting Rooms II

```python
import heapq

def min_meeting_rooms(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])
    heap = []
    ans = 0

    for start, end in intervals:
        while heap and heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
        ans = max(ans, len(heap))

    return ans
```

## 标准代码模板 3：扫描线求最大并发

```python
def max_overlap(intervals):
    events = []
    for start, end in intervals:
        events.append((start, 1))
        events.append((end, -1))

    events.sort(key=lambda x: (x[0], x[1]))

    cur = 0
    best = 0
    for _, delta in events:
        cur += delta
        best = max(best, cur)

    return best
```

## 面试时怎么讲

- 区间题第一步通常是排序
- 合并区间时，只需要和结果数组最后一个区间比较
- 如果是求同时进行的数量，用最小堆维护当前最早结束的区间

## 常见 follow-up 和回答

**Q1：为什么要先排序？**  
不排序就无法在线性扫描时只和前一个相关区间比较。

**Q2：区间端点相等算不算重叠？**  
要先确认题意；会议室问题通常 `end <= next_start` 视为不冲突。

**Q3：会议室题为什么堆里放结束时间？**  
因为我们只关心哪个区间最早结束。

**Q4：什么时候用堆，什么时候用扫描线？**  
资源分配更适合堆；只求并发峰值时扫描线更直接。

## Amazon 风格完整题面

> Delivery trucks occupy loading docks over time intervals.  
> Return the minimum number of loading docks needed so that no truck has to wait.

## 可直接背的口语回答稿

“这题本质是区间重叠和资源分配问题。我会先按开始时间排序，然后用一个最小堆维护当前所有正在占用资源的结束时间。每来一个新区间，就看最早结束的那个能不能释放。如果能释放就弹掉，再把当前区间压入堆。堆大小的峰值就是最少需要的资源数。”

## 推荐代表题

- Merge Intervals
- Meeting Rooms
- Meeting Rooms II

