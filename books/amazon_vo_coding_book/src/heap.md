# 3. 堆 / 多路归并

## 面试题目怎么问

- 合并 `k` 个有序链表
- 合并多个有序数组
- 找前 `k` 个高频元素
- 找距离原点最近的 `k` 个点
- 实时维护第 `k` 大 / 第 `k` 小元素

## 识别信号

- 多个有序输入流
- 每次只需要最小或最大
- `Top K`
- 数据不断进来，要动态维护答案

## Amazon 风格业务包装

- 多个 warehouse 各自产生有序事件流，要合并成一个全局时间线
- 多条配送线路各自按时间排序，要求输出整体最早事件
- 电商商品里找 Top K 热门商品
- 找离某个配送站最近的 K 个司机 / K 个仓库

## 你该怎么想

- 多个输入源都已经有序，就想多路归并
- 只关心当前最小 / 最大，就想 heap
- 只要看到 `Top K`，先把堆当默认选项

## 标准代码模板 1：合并 k 个有序数组

```python
import heapq

def merge_k_sorted_arrays(arrays):
    heap = []
    res = []

    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))

    while heap:
        val, row, idx = heapq.heappop(heap)
        res.append(val)

        if idx + 1 < len(arrays[row]):
            heapq.heappush(heap, (arrays[row][idx + 1], row, idx + 1))

    return res
```

## 标准代码模板 2：合并 k 个有序链表

```python
import heapq

def merge_k_sorted_lists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode(0)
    cur = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        cur.next = node
        cur = cur.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next
```

## 标准代码模板 3：Top K 高频

```python
from collections import Counter
import heapq

def top_k_frequent(nums, k):
    count = Counter(nums)
    heap = []

    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for freq, num in heap]
```

## 标准代码模板 4：K Closest

```python
import heapq

def k_closest(points, k):
    heap = []

    for x, y in points:
        dist = x * x + y * y
        heapq.heappush(heap, (-dist, x, y))
        if len(heap) > k:
            heapq.heappop(heap)

    return [(x, y) for neg_dist, x, y in heap]
```

## 代码讲解

- 多路归并时，堆里只维护每个流当前头部候选
- Top K 时，常见做法是大小为 `k` 的小顶堆
- `K closest` 常用大小为 `k` 的“伪大顶堆”

## 面试时怎么讲

- 只要问题核心是“随时拿到当前最小/最大”，就优先考虑堆
- 多路归并时，堆里维护每个流当前最小候选
- 每弹出一个值，再推进这个流的下一个候选

## 常见 follow-up 和回答

**Q1：为什么是 `log k`，不是 `log n`？**  
因为堆里同时最多只维护 `k` 个候选。

**Q2：Top K 高频能不能比堆更快？**  
能，频率范围合适时可以用 bucket sort。

**Q3：为什么不把所有元素拉平后排序？**  
可以，但通常是 `O(N log N)`；多路归并能做到 `O(N log k)`。

**Q4：如果数据流特别大，不能一次性放进内存怎么办？**  
有序流合并时仍然只维护每个流的当前指针。

## Amazon 风格完整题面

> Each warehouse produces a sorted stream of shipping events ordered by timestamp.  
> Merge all streams into one globally sorted timeline.

## 可直接背的口语回答稿

“题面虽然在讲多个仓库的事件流，但本质是多路归并。每个流本身已经有序，所以我不需要把所有元素一次性拉平排序。我会用一个最小堆，堆里只维护每个流当前最小的那个事件。每次弹出堆顶加入结果，再把该流的下一个事件压回堆。这样总复杂度是 `O(N log k)`。”

## 推荐代表题

- Merge K Sorted Lists
- Top K Frequent Elements
- K Closest Points to Origin
- Kth Largest Element in a Stream

