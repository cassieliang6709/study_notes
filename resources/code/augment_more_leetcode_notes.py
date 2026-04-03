#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FULL_DIR = ROOT / "algorithms" / "extended_problem_full_solutions"
DETAILED_DIR = ROOT / "algorithms" / "extended_problem_detailed"


def parse_sections(text: str, pattern: str):
    matches = list(re.finditer(pattern, text, re.M))
    sections = []
    for i, match in enumerate(matches):
        title = match.group(1).strip()
        start = match.start()
        body_start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections.append((title, start, body_start, end))
    return sections


def normalize(title: str) -> str:
    title = title.strip()
    aliases = {
        "Construct Binary Tree from Preorder and Inorder": "Construct Binary Tree from Preorder and Inorder Traversal",
        "Remove Nth Node From End": "Remove Nth Node From End of List",
        "Lowest Common Ancestor": "Lowest Common Ancestor of a Binary Tree",
        "Course Schedule / II": "Course Schedule",
        "Climbing Stairs / Fibonacci": "Climbing Stairs",
        "Unique Paths / Unique Paths II": "Unique Paths",
        "Add Two Numbers / Add Two Numbers II": "Add Two Numbers",
        "Basic Calculator / II / III": "Basic Calculator",
        "Path Sum / Path Sum II / Path Sum III": "Path Sum III",
        "Serialize / Deserialize": "Serialize and Deserialize Binary Tree",
        "Regular Expression Matching / Wildcard Matching": "Regular Expression Matching",
    }
    return aliases.get(title, title)


def clean(text: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", text.strip())


def strip_fence(text: str) -> str:
    text = clean(text)
    text = text.replace("```text", "")
    text = text.replace("```", "")
    return clean(text)


def get_block(section: str, label: str, next_labels: list[str]) -> str:
    m = re.search(re.escape(label), section)
    if not m:
        return ""
    start = m.end()
    end = len(section)
    for next_label in next_labels:
        n = re.search(re.escape(next_label), section[start:])
        if n:
            end = min(end, start + n.start())
    return clean(section[start:end])


def get_code(section: str) -> str:
    m = re.search(r"\*\*Python 标准解法\*\*\s*```python\n(.*?)```", section, re.S)
    return clean(m.group(1)) if m else ""


def infer_complexity(title: str, pattern: str, meaning: str, code: str) -> tuple[str, str]:
    exact = {
        "Two Sum": ("`O(n)`。", "`O(n)`。"),
        "Product of Array Except Self": ("`O(n)`。", "`O(1)` 额外空间；如果把输出数组算上则是 `O(n)`。"),
        "Move Zeroes": ("`O(n)`。", "`O(1)`。"),
        "Next Permutation": ("`O(n)`。", "`O(1)`。"),
        "Merge Sorted Array": ("`O(m+n)`。", "`O(1)`。"),
        "Sort Colors": ("`O(n)`。", "`O(1)`。"),
        "Group Anagrams": ("若排序键值，通常是 `O(n * k log k)`。", "`O(nk)`。"),
        "Find the Duplicate Number": ("`O(n)`。", "`O(1)`。"),
        "Single Number": ("`O(n)`。", "`O(1)`。"),
        "3Sum": ("`O(n^2)`。", "排序外额外 `O(1)`；计入排序栈常写 `O(log n)`。"),
        "3Sum Closest": ("`O(n^2)`。", "`O(1)`。"),
        "Container With Most Water": ("`O(n)`。", "`O(1)`。"),
        "Longest Substring Without Repeating Characters": ("`O(n)`。", "`O(k)`，`k` 为窗口字符种类。"),
        "Minimum Window Substring": ("`O(m+n)`。", "`O(k)`。"),
        "Sliding Window Maximum": ("`O(n)`。", "`O(k)`。"),
        "Search in Rotated Sorted Array": ("`O(log n)`。", "`O(1)`。"),
        "Find First and Last Position of Element in Sorted Array": ("`O(log n)`。", "`O(1)`。"),
        "Find Peak Element": ("`O(log n)`。", "`O(1)`。"),
        "Single Element in a Sorted Array": ("`O(log n)`。", "`O(1)`。"),
        "Search a 2D Matrix": ("`O(log(mn))`。", "`O(1)`。"),
        "Find Minimum in Rotated Sorted Array": ("`O(log n)`。", "`O(1)`。"),
        "Kth Smallest Element in a Sorted Matrix": ("若按值域二分，`O(n log(range))`。", "`O(1)` 或 `O(n)`，取决于计数实现。"),
        "Random Pick with Weight": ("预处理 `O(n)`，每次查询 `O(log n)`。", "`O(n)`。"),
        "Median of Two Sorted Arrays": ("`O(log(min(m,n)))`。", "`O(1)`。"),
        "Reverse Linked List": ("`O(n)`。", "`O(1)`。"),
        "Reverse Linked List II": ("`O(n)`。", "`O(1)`。"),
        "Reorder List": ("`O(n)`。", "`O(1)`。"),
        "Remove Nth Node From End of List": ("`O(n)`。", "`O(1)`。"),
        "Add Two Numbers": ("`O(max(m,n))`。", "`O(1)` 额外空间，不计答案链表。"),
        "Add Two Numbers II": ("`O(m+n)`。", "`O(m+n)`。"),
        "Merge Two Sorted Lists": ("`O(m+n)`。", "`O(1)`。"),
        "Merge k Sorted Lists": ("`O(N log k)`。", "`O(k)`。"),
        "Sort List": ("`O(n log n)`。", "`O(log n)` 递归栈。"),
        "Copy List with Random Pointer": ("`O(n)`。", "`O(n)`。"),
        "Binary Tree Level Order Traversal": ("`O(n)`。", "`O(n)`。"),
        "Binary Tree Right Side View": ("`O(n)`。", "`O(n)`。"),
        "Symmetric Tree": ("`O(n)`。", "`O(h)`。"),
        "Diameter of Binary Tree": ("`O(n)`。", "`O(h)`。"),
        "Path Sum": ("`O(n)`。", "`O(h)`。"),
        "Path Sum II": ("`O(n)` 到 `O(n^2)`，取决于拷贝路径的代价。", "`O(h)`，不计答案。"),
        "Path Sum III": ("`O(n)`。", "`O(n)`。"),
        "Flatten Binary Tree to Linked List": ("`O(n)`。", "`O(h)`。"),
        "Construct Binary Tree from Preorder and Inorder Traversal": ("`O(n)`。", "`O(n)`。"),
        "Lowest Common Ancestor of a Binary Tree": ("`O(n)`。", "`O(h)`。"),
        "Validate Binary Search Tree": ("`O(n)`。", "`O(h)`。"),
        "Kth Smallest Element in a BST": ("`O(h+k)`，最坏 `O(n)`。", "`O(h)`。"),
        "Serialize and Deserialize Binary Tree": ("`O(n)`。", "`O(n)`。"),
        "Subsets": ("`O(n * 2^n)`。", "`O(n)`，不计答案。"),
        "Permutations": ("`O(n * n!)`。", "`O(n)`，不计答案。"),
        "Combination Sum": ("最坏指数级。", "`O(target)` 量级递归深度，不计答案。"),
        "Generate Parentheses": ("Catalan 数量级。", "`O(n)`，不计答案。"),
        "Restore IP Addresses": ("常数上界内枚举，通常写 `O(1)`。", "`O(1)`，不计答案。"),
        "Word Break II": ("最坏指数级，`memo` 可显著剪枝。", "`O(n + 输出规模)`。"),
        "Partition to K Equal Sum Subsets": ("最坏指数级。", "`O(n)` 到 `O(2^n)`，取决于状态表示。"),
        "Word Ladder": ("经典写法约 `O(N * L * 26)`。", "`O(N * L)`。"),
        "Number of Islands": ("`O(mn)`。", "`O(mn)` 最坏递归栈或队列。"),
        "Max Area of Island": ("`O(mn)`。", "`O(mn)` 最坏递归栈。"),
        "Course Schedule": ("`O(V+E)`。", "`O(V+E)`。"),
        "Course Schedule II": ("`O(V+E)`。", "`O(V+E)`。"),
        "Clone Graph": ("`O(V+E)`。", "`O(V)`。"),
        "Accounts Merge": ("约 `O(N alpha(N) + M log M)`。", "`O(N)`。"),
        "Alien Dictionary": ("`O(C)` 到 `O(C + V + E)`。", "`O(V+E)`。"),
        "Valid Parentheses": ("`O(n)`。", "`O(n)`。"),
        "Simplify Path": ("`O(n)`。", "`O(n)`。"),
        "Decode String": ("`O(n * expanded_length)`，通常记作 `O(n)` 到输出规模。", "`O(n)`。"),
        "Basic Calculator": ("`O(n)`。", "`O(n)`。"),
        "Basic Calculator II": ("`O(n)`。", "`O(n)` 或 `O(1)` 额外，取决于实现。"),
        "Basic Calculator III": ("`O(n)`。", "`O(n)`。"),
        "Longest Valid Parentheses": ("`O(n)`。", "`O(n)`。"),
        "Trapping Rain Water": ("`O(n)`。", "`O(1)` 双指针版。"),
        "Exclusive Time of Functions": ("`O(n)`。", "`O(n)`。"),
        "Climbing Stairs": ("`O(n)`。", "`O(1)`。"),
        "Fibonacci Number": ("`O(n)`。", "`O(1)`。"),
        "Best Time to Buy and Sell Stock": ("`O(n)`。", "`O(1)`。"),
        "Longest Increasing Subsequence": ("二分优化版 `O(n log n)`。", "`O(n)`。"),
        "Maximum Product Subarray": ("`O(n)`。", "`O(1)`。"),
        "Word Break": ("`O(n^2)`。", "`O(n)`。"),
        "Decode Ways": ("`O(n)`。", "`O(1)` 或 `O(n)`。"),
        "Maximum Subarray": ("`O(n)`。", "`O(1)`。"),
        "Unique Paths": ("`O(mn)`。", "`O(n)` 或 `O(mn)`。"),
        "Unique Paths II": ("`O(mn)`。", "`O(n)` 或 `O(mn)`。"),
        "Continuous Subarray Sum": ("`O(n)`。", "`O(min(n,k))` 到 `O(n)`。"),
        "Longest Palindromic Substring": ("`O(n^2)`。", "`O(1)` 中心扩展版。"),
        "Regular Expression Matching": ("`O(mn)`。", "`O(mn)`。"),
        "Wildcard Matching": ("`O(mn)`。", "`O(mn)`。"),
        "Longest Increasing Path in a Matrix": ("`O(mn)`。", "`O(mn)`。"),
        "Kth Largest Element in an Array": ("`O(n log k)` 用堆；Quickselect 平均 `O(n)`。", "`O(k)`。"),
        "K Closest Points to Origin": ("`O(n log k)`。", "`O(k)`。"),
        "Top K Frequent Elements": ("`O(n log k)`。", "`O(n)`。"),
        "Top K Frequent Words": ("`O(n log k)`。", "`O(n)`。"),
        "Find Median from Data Stream": ("插入 `O(log n)`，查询 `O(1)`。", "`O(n)`。"),
        "LRU Cache": ("`O(1)` 均摊完成 `get/put`。", "`O(capacity)`。"),
        "Insert Delete GetRandom O(1)": ("`O(1)` 均摊。", "`O(n)`。"),
        "Implement Trie (Prefix Tree)": ("每次操作 `O(L)`。", "`O(total_chars)`。"),
        "Add and Search Word - Data structure design": ("普通查找 `O(L)`，带通配符最坏指数级。", "`O(total_chars)`。"),
        "Binary Search Tree Iterator": ("`next/hasNext` 均摊 `O(1)`。", "`O(h)`。"),
        "Merge Intervals": ("`O(n log n)`。", "`O(n)`。"),
        "Insert Interval": ("`O(n)`。", "`O(n)`。"),
        "Meeting Rooms II": ("`O(n log n)`。", "`O(n)`。"),
        "Pow(x, n)": ("`O(log n)`。", "`O(log n)` 递归版或 `O(1)` 迭代版。"),
        "Divide Two Integers": ("`O(log(dividend))`。", "`O(1)`。"),
        "Rotate Image": ("`O(n^2)`。", "`O(1)`。"),
        "Spiral Matrix": ("`O(mn)`。", "`O(1)` 额外，不计答案。"),
        "Set Matrix Zeroes": ("`O(mn)`。", "`O(1)`。"),
        "String to Integer (atoi)": ("`O(n)`。", "`O(1)`。"),
        "Roman to Integer": ("`O(n)`。", "`O(1)`。"),
        "First Missing Positive": ("`O(n)`。", "`O(1)`。"),
        "Longest Consecutive Sequence": ("`O(n)` 平均。", "`O(n)`。"),
        "Task Scheduler": ("`O(n)` 到 `O(n log k)`，取决于实现。", "`O(1)` 到 `O(k)`。"),
        "Sudoku Solver": ("最坏指数级回溯。", "`O(81)` 递归深度上界。"),
    }
    if title in exact:
        return exact[title]

    if "Binary Search" in pattern or "二分" in pattern:
        return ("通常是 `O(log n)`。", "`O(1)`。")
    if "BFS" in pattern or "层序" in pattern or "Topological" in pattern:
        return ("通常是遍历所有点边或网格单元，常见写法为 `O(V+E)` 或 `O(mn)`。", "通常是 `O(V+E)` 或队列规模。")
    if "DFS" in pattern or "Backtracking" in pattern or "回溯" in pattern:
        return ("通常取决于搜索树大小，常见为指数级。", "递归栈加辅助状态，通常 `O(depth)` 到指数级状态空间。")
    if "Hash" in pattern or "哈希" in pattern:
        return ("通常是 `O(n)`。", "通常是 `O(n)`。")
    if "Two Pointers" in pattern or "双指针" in pattern:
        return ("通常是 `O(n)`。", "通常是 `O(1)`。")
    if "Heap" in pattern or "堆" in pattern or "Priority" in pattern:
        return ("常见是 `O(n log k)` 或单次 `O(log n)`。", "通常是堆大小 `O(k)` 或 `O(n)`。")
    if "Trie" in pattern:
        return ("通常与字符串总长度线性相关。", "通常是 Trie 总节点数。")
    return ("请结合这题使用的主循环、排序、堆或递归分支来记忆复杂度。", "请结合辅助数据结构与递归深度来判断空间复杂度。")


def infer_think(title: str, pattern: str, meaning: str) -> str:
    key = pattern.replace("\n", " ").strip()
    if key:
        return f"先看题型识别里的信号：这题本质上就是 `{key}`。把题目翻译成这个模板后，再去套对应的不变量、状态定义或数据结构，就会更容易写出来。"
    return f"先把 `{title}` 还原成你熟悉的主模板，再去想代码。大多数面试题真正考的是识别题型，而不是临场发明新算法。"


def infer_follow_up(title: str, pattern: str) -> str:
    if "Binary Search" in pattern or "二分" in pattern:
        return "- 如果数组里有重复元素，边界条件怎么改？\n- 如果不能直接按下标访问，还适合二分吗？"
    if "BFS" in pattern or "DFS" in pattern or "图" in pattern:
        return "- 如果要返回具体路径而不是只判断可行性，额外记录什么？\n- DFS、BFS、并查集三种解法分别适合什么场景？"
    if "Backtracking" in pattern or "回溯" in pattern:
        return "- 哪些剪枝最值得优先做？\n- 如果只要求返回数量而不是全部方案，代码能如何简化？"
    if "Heap" in pattern or "堆" in pattern:
        return "- 如果 `k` 很小，为什么堆通常比全排序更合适？\n- 如果数据流持续到来，解法要怎么调整？"
    if "Two Pointers" in pattern or "双指针" in pattern or "滑窗" in pattern:
        return "- 如果输入先排序或已经有序，能不能进一步简化？\n- 如果要返回具体区间或下标，代码里要额外维护什么？"
    if "Hash" in pattern or "哈希" in pattern:
        return "- 如果空间受限，能不能改成排序或双指针？\n- 如果要返回所有答案而不是一个答案，如何去重？"
    return "- 能不能把空间复杂度再压缩一层？\n- 有没有另一种常见模板也能解决这题？"


def build_full_block(title: str, pattern: str, meaning: str, code: str) -> str:
    time_text, space_text = infer_complexity(title, pattern, meaning, code)
    think_text = infer_think(title, pattern, meaning)
    follow_text = infer_follow_up(title, pattern)
    return f"""**题型识别**

```text
{pattern}
```

**题目含义**

{meaning}

**Python 代码**

```python
{code}
```

**时间复杂度**

{time_text}

**空间复杂度**

{space_text}

**怎么想到这个方法**

{think_text}

**常见 Follow-up**

{follow_text}"""


def build_source_map():
    source = {}
    for path in sorted(FULL_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        for title, _, body_start, end in parse_sections(text, r"^##\s+\d+\.\s+(.+)$"):
            section = text[body_start:end]
            pattern = strip_fence(get_block(section, "**题型识别**", ["**中文解释**", "**English Explanation**", "**Python 标准解法**"]))
            meaning = get_block(section, "**中文解释**", ["**English Explanation**", "**Python 标准解法**"])
            code = get_code(section)
            if pattern and meaning and code:
                source[title] = {"pattern": pattern, "meaning": meaning, "code": code}
    return source


SOURCE = build_source_map()


def augment_full_solutions():
    for path in sorted(FULL_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        matches = parse_sections(text, r"^##\s+\d+\.\s+(.+)$")
        if not matches:
            continue
        new_text = []
        cursor = 0
        for title, start, body_start, end in matches:
            new_text.append(text[cursor:body_start])
            section = text[body_start:end]
            pattern = strip_fence(get_block(section, "**题型识别**", ["**中文解释**", "**English Explanation**", "**Python 标准解法**"]))
            meaning = get_block(section, "**中文解释**", ["**English Explanation**", "**Python 标准解法**"])
            code = get_code(section)
            if pattern and meaning and code:
                new_text.append("\n\n" + build_full_block(title, pattern, meaning, code) + "\n\n")
            else:
                new_text.append(section)
            cursor = end
        new_text.append(text[cursor:])
        path.write_text("".join(new_text), encoding="utf-8")


DETAIL_OVERRIDES = {
    "Path Sum / Path Sum II / Path Sum III": {
        "pattern": "递归 / DFS / 前缀和",
        "meaning": "这一组题都在问树上的路径问题：`Path Sum I` 判断是否存在，`II` 收集所有路径，`III` 统计路径条数。真正需要优先掌握的是“路径信息该怎么沿递归传下去”，以及 `Path Sum III` 的前缀和做法。",
        "code": """from collections import defaultdict
from typing import Optional


class Solution:
    def pathSum(self, root: Optional['TreeNode'], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        ans = 0

        def dfs(node, cur):
            nonlocal ans
            if not node:
                return
            cur += node.val
            ans += prefix[cur - targetSum]
            prefix[cur] += 1
            dfs(node.left, cur)
            dfs(node.right, cur)
            prefix[cur] -= 1

        dfs(root, 0)
        return ans""",
        "time": "`O(n)`。",
        "space": "`O(n)`。",
        "think": "如果只是根到叶，普通 DFS 就够了；一旦题目允许路径从中间开始，就该联想到“路径和 = 两个前缀和之差”。",
        "follow": "- `Path Sum I / II / III` 的状态传递分别有什么不同？\n- 如果树节点值可能是负数，为什么不能直接剪枝？",
    },
    "Serialize / Deserialize": {
        "pattern": "树的构造与还原",
        "meaning": "这类题的本质是给树定义一个可逆编码。普通二叉树最稳的是前序遍历配合 `null` 标记；BST 则有机会进一步利用有序性压缩信息。",
        "code": """class Codec:
    def serialize(self, root):
        vals = []

        def dfs(node):
            if not node:
                vals.append("null")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(vals)

    def deserialize(self, data):
        vals = iter(data.split(","))

        def dfs():
            val = next(vals)
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()""",
        "time": "`O(n)`。",
        "space": "`O(n)`。",
        "think": "先别急着写代码，先想清楚“我打算按什么遍历顺序编码，空节点怎么表示，解码时怎样唯一还原”。",
        "follow": "- 如果是 BST，怎样减少 `null` 标记？\n- 如果要按层序序列化，代码结构会怎样变化？",
    },
    "Course Schedule / II": {
        "pattern": "拓扑排序 / 有向图判环",
        "meaning": "这组题都在处理课程依赖。`Course Schedule I` 问有没有合法顺序，本质是看图里有没有环；`II` 进一步要求你返回一种可行顺序。",
        "code": """from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        q = deque(i for i in range(numCourses) if indegree[i] == 0)
        order = []

        while q:
            node = q.popleft()
            order.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return order if len(order) == numCourses else []""",
        "time": "`O(V+E)`。",
        "space": "`O(V+E)`。",
        "think": "一看到“依赖关系”和“能不能安排顺序”，就该把题目翻译成有向图，再决定是 DFS 判环还是 BFS 拓扑排序。",
        "follow": "- 如果只判断能否完成，和返回顺序相比代码差在哪？\n- DFS 判环法和 Kahn 算法怎么选？",
    },
    "Basic Calculator / II / III": {
        "pattern": "栈模拟表达式求值",
        "meaning": "这组题是在一条主线上递进的：`II` 先掌握乘除即时结算，`I` 和 `III` 再把括号嵌套加回来。核心仍然是把运算符优先级拆成可维护的状态。",
        "code": """class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = "+"

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if ch in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                sign = ch
                num = 0

        return sum(stack)""",
        "time": "`O(n)`。",
        "space": "`O(n)`。",
        "think": "表达式题先别被细节吓到，先拆成两件事：数字怎么读完整，优先级怎样在扫描时局部结算。",
        "follow": "- 加入括号后，为什么通常需要额外栈或递归？\n- 为什么除法要特别注意 Python 的取整方向？",
    },
    "Regular Expression Matching / Wildcard Matching": {
        "pattern": "二维字符串 DP",
        "meaning": "这两题都属于双串匹配 DP。难点不在代码量，而在于你能不能清楚写出 `dp[i][j]` 的含义，并按字符类别列转移。",
        "code": """class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(2, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] in {s[i - 1], "."}:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] in {s[i - 1], "."}:
                        dp[i][j] |= dp[i - 1][j]

        return dp[m][n]""",
        "time": "`O(mn)`。",
        "space": "`O(mn)`。",
        "think": "只要是两个字符串的匹配关系，就先考虑二维 DP；然后把每种特殊字符看成不同的转移分支。",
        "follow": "- `regex` 里的 `*` 和 `wildcard` 里的 `*` 语义有什么区别？\n- 这种二维 DP 能不能压缩空间？",
    },
    "Climbing Stairs / Fibonacci": {
        "pattern": "一维线性 DP",
        "meaning": "这两个问题本质一样：当前位置的答案只依赖前面很少几个状态，是最适合入门 DP 的模板。",
        "code": """class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b""",
        "time": "`O(n)`。",
        "space": "`O(1)`。",
        "think": "当题目满足“当前答案只依赖固定几个更小子问题”时，就该想到线性 DP 和状态压缩。",
        "follow": "- 如果一次可以走 1/2/3 步，状态转移如何改？\n- 为什么这类题常常可以压到 `O(1)` 空间？",
    },
    "Unique Paths / Unique Paths II": {
        "pattern": "网格 DP",
        "meaning": "这两题都在问从左上走到右下，只是第二题多了障碍物。共同核心是：当前格子的答案来自上方和左方。",
        "code": """from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]

        return dp[-1]""",
        "time": "`O(mn)`。",
        "space": "`O(n)`。",
        "think": "题目一旦限制只能向右或向下移动，网格 DP 基本就是默认答案。",
        "follow": "- 没有障碍物时为什么还能用组合数学？\n- 如果要求最小路径和，状态如何变化？",
    },
}


def build_detailed_block(title: str, src: dict) -> str:
    pattern = src["pattern"]
    meaning = src["meaning"]
    code = src["code"]
    time_text = src.get("time") or infer_complexity(normalize(title), pattern, meaning, code)[0]
    space_text = src.get("space") or infer_complexity(normalize(title), pattern, meaning, code)[1]
    think_text = src.get("think") or infer_think(normalize(title), pattern, meaning)
    follow_text = src.get("follow") or infer_follow_up(normalize(title), pattern)
    return f"""**题目含义**

{meaning}

**代表 Python 代码**

```python
{code}
```

**时间复杂度**

{time_text}

**空间复杂度**

{space_text}

**怎么想到这个方法**

{think_text}

**常见 Follow-up**

{follow_text}"""


def source_for_detailed(title: str):
    if title in DETAIL_OVERRIDES:
        return DETAIL_OVERRIDES[title]
    key = normalize(title)
    return SOURCE.get(key)


def augment_detailed():
    skip_titles = {"识别信号", "代表题", "核心方法", "核心原则", "提醒", "精确查找", "左边界", "1. DFS 染色", "2. BFS 按层", "3. 拓扑排序"}
    for path in sorted(DETAILED_DIR.glob("*.md")):
        if path.name in {"README.md", "index.md", "01_array_two_pointers_sliding_window.md"}:
            continue
        text = path.read_text(encoding="utf-8")
        matches = parse_sections(text, r"^###\s+(.+)$")
        if not matches:
            continue
        out = []
        cursor = 0
        for title, start, body_start, end in matches:
            out.append(text[cursor:body_start])
            plain = title.strip()
            if plain in skip_titles:
                out.append(text[body_start:end])
            else:
                src = source_for_detailed(plain)
                if src:
                    out.append("\n\n" + build_detailed_block(plain, src) + "\n\n")
                else:
                    out.append(text[body_start:end])
            cursor = end
        out.append(text[cursor:])
        path.write_text("".join(out), encoding="utf-8")


def main():
    augment_full_solutions()
    augment_detailed()


if __name__ == "__main__":
    main()
