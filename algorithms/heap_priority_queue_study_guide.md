---
title: "Heap / Priority Queue 题目分类讲义"
---

# Heap / Priority Queue 题目分类讲义

这份笔记的目标很简单：

- 用中文把堆题最常见的套路讲清楚
- 先理解“为什么要用堆”，再记模板
- 重点放在 Top K、合并有序结构、数据流中位数
- 默认以 Python `heapq` 思路为主

---

## 这个题型 / 算法点的总结

堆题最值得记住的一句话是：当你需要“反复拿当前最值”，而不是“一次性排序后看一眼”，就应该认真考虑堆。Top K、数据流、合并多个有序结构，本质上都在利用堆把“取最优元素”这件事压到 `O(log k)` 或 `O(log n)`。

## 题目含义

这份讲义是堆和优先队列的总览。为了让你先抓住最稳定的入门模板，下面用代表题 `Kth Largest Element in an Array` 演示：为什么维护一个大小为 `k` 的最小堆，就能得到第 `k` 大元素。

## Python 代码

```python
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap: list[int] = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]


print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
```

## 时间复杂度

一共处理 `n` 个元素，每次堆操作最多 `O(log k)`，所以时间复杂度是 `O(n log k)`。

## 空间复杂度

堆里最多保留 `k` 个元素，所以空间复杂度是 `O(k)`。

## 怎么想到

很多人一看到“第 k 大”就先想到排序，但排序其实做了很多题目不需要的工作。题目并不关心完整顺序，只关心最大的那 `k` 个元素里最小的是谁。这样一想，就会自然得到一个更节省的做法：只维护最大的 `k` 个候选值，堆顶就是答案。

## 示例 case

输入：`nums = [3, 2, 1, 5, 6, 4], k = 2`
输出：`5`
解释：从大到小排序后是 `[6, 5, 4, 3, 2, 1]`，第 2 大是 `5`。大小为 `2` 的最小堆最终会留下 `[5, 6]`，堆顶正好是答案。

边界 case：如果 `k = 1`，就等价于求最大值；如果 `k = len(nums)`，堆顶会变成整个数组最小值。

## 常见 Follow-up

- 如果题目变成“前 k 个高频元素”，堆里应该存什么？
- 如果数据是实时流进来的，为什么不能每次重新排序？
- 如果题目是合并多个有序链表，为什么堆里只需要放每条链表当前最前面的节点？

## 一、先记住什么时候该想到堆

看到下面这些描述时，优先往堆上想：

- 前 `k` 大 / 前 `k` 小
- 数据流里实时维护最值
- 不断取当前最小或最大
- 合并多个有序链表 / 有序数组
- 每次都要拿“当前最优选择”

一句话总结：

- `堆` 适合反复拿最值
- `最小堆` 默认拿最小
- `最大堆` 在 Python 里通常靠“取相反数”实现

---

## 二、分类总表

### 1. Top K 问题

核心是：

- 用大小为 `k` 的堆维护候选答案
- 超过 `k` 就弹掉不需要的那个

典型题：

1. `Kth Largest Element in an Array`
2. `Top K Frequent Elements`
3. `K Closest Points to Origin`

### 2. 合并多个有序结构

核心是：

- 每个有序结构只把“当前最前面那个元素”放进堆
- 每次弹出最小值，再把它后继补进堆

典型题：

1. `Merge k Sorted Lists`
2. `Find K Pairs with Smallest Sums`

### 3. 数据流实时维护答案

核心是：

- 数据一个一个进来
- 你不能每次都重新排序
- 要靠堆实时维护结构

典型题：

1. `Find Median from Data Stream`
2. `Kth Largest Element in a Stream`

### 4. 带优先级的图搜索

这类题更像“堆 + 图”。

典型题：

1. `Network Delay Time`
2. `Path With Minimum Effort`
3. `Dijkstra` 系列题

如果你现在还在基础阶段，可以先把前 3 类吃透。

---

## 三、推荐刷题顺序

建议按下面顺序练：

1. `Kth Largest Element in an Array`
2. `Top K Frequent Elements`
3. `K Closest Points to Origin`
4. `Merge k Sorted Lists`
5. `Kth Largest Element in a Stream`
6. `Find Median from Data Stream`
7. `Find K Pairs with Smallest Sums`
8. `Network Delay Time`

原因：

- 先学最纯的 Top K
- 再学“堆里放什么”
- 然后再做两个堆维护中位数

---

## 四、堆题最常用模板

### 1. 大小为 k 的最小堆

适合：

- 求第 `k` 大
- 维护前 `k` 大元素

```python
import heapq

heap = []

for x in nums:
    heapq.heappush(heap, x)
    if len(heap) > k:
        heapq.heappop(heap)

return heap[0]
```

这段模板的本质是：

- 堆里永远只留 `k` 个元素
- 最后堆顶就是这 `k` 个元素里最小的那个
- 也就是全局第 `k` 大

### 2. 频率题模板

```python
from collections import Counter
import heapq

count = Counter(nums)
heap = []

for x, freq in count.items():
    heapq.heappush(heap, (freq, x))
    if len(heap) > k:
        heapq.heappop(heap)
```

重点不是死记代码，而是记住：

- 频率题先统计
- 再决定堆里存什么

### 3. 合并 k 个有序结构模板

```python
import heapq

heap = []

for i, node in enumerate(lists):
    if node:
        heapq.heappush(heap, (node.val, i, node))

while heap:
    val, i, node = heapq.heappop(heap)
    # 使用当前最小节点
    if node.next:
        heapq.heappush(heap, (node.next.val, i, node.next))
```

这里多放一个 `i`，是为了：

- 当 `val` 相等时，仍然能比较元组
- 避免直接比较链表节点对象报错

### 4. 两个堆维护中位数

```python
import heapq

small = []   # max heap，用相反数模拟
large = []   # min heap

def add_num(x):
    heapq.heappush(small, -x)
    heapq.heappush(large, -heapq.heappop(small))

    if len(large) > len(small):
        heapq.heappush(small, -heapq.heappop(large))
```

核心平衡规则：

- `small` 保存较小的一半
- `large` 保存较大的一半
- 两边大小差不能超过 `1`

---

## 五、逐题核心思路

## 1. Kth Largest Element in an Array

### 题目目标

找数组中第 `k` 大元素。

### 这题属于哪一类

属于“Top K 问题”。

### 核心思路

维护一个大小为 `k` 的最小堆。

为什么是最小堆？

因为你想保留“最大的 k 个元素”，那这批元素里最容易被淘汰的，就是其中最小的那个。

### 最关键的一句话

- `保留前 k 大，用最小堆`

---

## 2. Top K Frequent Elements

### 题目目标

找出现频率最高的前 `k` 个元素。

### 核心思路

分两步：

1. 先用哈希表统计频率
2. 再用堆维护前 `k` 个高频元素

### 这题真正练的东西

- 学会先做统计，再上堆
- 学会决定“堆里放什么字段”

### 容易错的点

- 直接把原数组元素塞进堆，忘了频率才是排序依据

---

## 3. K Closest Points to Origin

### 题目目标

找离原点最近的 `k` 个点。

### 核心思路

本质仍然是 Top K。

只是排序依据从“数值大小”换成了“距离平方”。

### 最关键的一句话

- `堆里存的是比较标准，不一定是原值本身`

比如可以存：

```python
(-dist, x, y)
```

或者直接用最小堆后一次性取前 `k`。

---

## 4. Merge k Sorted Lists

### 题目目标

合并 `k` 个有序链表。

### 这题属于哪一类

属于“合并多个有序结构”。

### 核心思路

每条链表当前最前面的节点都可能成为全局最小值，所以把它们都放进堆里。

每次弹出最小节点后，只需要把这个节点的下一个再放进堆。

### 最关键的一句话

- `堆里永远只放每条链表当前的候选头`

### 为什么复杂度好

总共有 `N` 个节点，每个节点只进堆出堆一次，堆大小最多 `k`。

所以复杂度是：

- 时间复杂度：`O(N log k)`

---

## 5. Kth Largest Element in a Stream

### 题目目标

数据一边进来，一边返回当前第 `k` 大。

### 核心思路

和静态数组版完全一样，依然维护大小为 `k` 的最小堆。

每插入一个新数：

- 先进堆
- 如果堆太大，就弹出最小值
- 堆顶就是答案

这题练的是：

- “一次建好” 和 “持续更新” 的思维一致

---

## 6. Find Median from Data Stream

### 题目目标

数据流里实时返回中位数。

### 为什么一个堆不够

因为中位数在中间，不是单纯最小或最大。

所以你要把数据分成两半：

- 左边一半
- 右边一半

### 核心思路

用两个堆维护：

- `small`：较小的一半，最大堆
- `large`：较大的一半，最小堆

这样：

- 如果总数是奇数，中位数就是某一边堆顶
- 如果总数是偶数，中位数就是两个堆顶平均值

### 这题最难的地方

不是取中位数，而是“插入后怎么重新平衡”

---

## 六、堆题统一检查清单

写堆题前，先问自己这 5 个问题：

1. 我到底要反复拿最小，还是反复拿最大
2. 堆里应该存原值，还是存 `(关键字, 数据)` 这样的元组
3. 需要维护大小为 `k` 吗
4. 需要懒删除吗
5. 这题是不是其实该用桶、排序或双端队列，而不是堆

---

## 七、最常见错误

- 搞反“前 k 大”和“前 k 小”该用什么堆
- 堆里字段设计错，导致排序依据不对
- Python 里直接把自定义对象放堆里比较，报错
- 忘记堆大小控制，复杂度退化
- `Find Median from Data Stream` 里两个堆没平衡好

---

## 八、一句话速记

- `Top K`：固定大小堆
- `频率题`：先统计，再入堆
- `合并有序结构`：堆里只放每路当前候选
- `中位数数据流`：两个堆分左右两半

---

## 九、建议下一步

最好的继续方式是：

1. 先手写 `Kth Largest Element in an Array`
2. 再手写 `Top K Frequent Elements`
3. 再手写 `Merge k Sorted Lists`
4. 最后挑战 `Find Median from Data Stream`

因为它们正好覆盖：

- Top K
- 频率统计 + 堆
- 合并多路有序结构
- 双堆维护数据流

这四题打通之后，绝大多数基础堆题就有框架了。

---

## Quiz

**Q1: Python `heapq` 默认是最小堆还是最大堆？**

- [ ] 最大堆
- [ ] 最小堆 ✅
- [ ] 随机
- [ ] 取决于元素类型

**Q2: 要用 Python 实现最大堆，最简单的办法是什么？**

- [ ] 用 `heapq.nlargest`
- [ ] 存入元素时取负值 ✅
- [ ] 重写比较函数
- [ ] 导入 `maxheap` 库

**Q3: "维护数据流中的中位数"需要用几个堆？**

- [ ] 1 个最小堆
- [ ] 1 个最大堆
- [ ] 2 个堆：一个最大堆 + 一个最小堆 ✅
- [ ] 3 个堆

**Q4: `Top K Frequent Elements` 用堆解法，堆的大小应该控制在多少？**

- [ ] 等于数组长度
- [ ] 等于不同元素的数量
- [ ] k ✅
- [ ] log(n)

**Q5: Dijkstra 最短路径算法为什么要用堆？**

- [ ] 因为图中有负权边
- [ ] 每次快速取出当前距离最小的节点 ✅
- [ ] 防止重复访问
- [ ] 减少空间复杂度
