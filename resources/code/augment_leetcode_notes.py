#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TARGET_DIR = ROOT / "algorithms" / "leetcode_100_detailed"
SOURCE_DIR = ROOT / "algorithms" / "extended_problem_full_solutions"


def parse_sections(text: str, heading_pattern: str):
    matches = list(re.finditer(heading_pattern, text, re.M))
    sections = {}
    for i, match in enumerate(matches):
        title = match.group(1).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections[title] = text[start:end].strip()
    return sections


def extract_between(section: str, label: str, next_labels: list[str]) -> str:
    pattern = re.escape(label)
    match = re.search(pattern, section)
    if not match:
        return ""
    start = match.end()
    end = len(section)
    for next_label in next_labels:
        next_match = re.search(re.escape(next_label), section[start:])
        if next_match:
            end = min(end, start + next_match.start())
    return section[start:end].strip()


def extract_code(section: str) -> str:
    match = re.search(r"\*\*Python 标准解法\*\*\s*```python\n(.*?)```", section, re.S)
    return match.group(1).strip() if match else ""


def clean_paragraph(text: str) -> str:
    text = text.strip()
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


ALIAS = {
    "Construct Binary Tree from Preorder and Inorder": "Construct Binary Tree from Preorder and Inorder Traversal",
}


FALLBACK = {
    "Maximum Depth of Binary Tree": {
        "meaning": "题目要你求二叉树的最大深度，也就是从根节点到最深叶子节点一共经过多少层。最自然的定义就是：`depth(root) = 1 + max(depth(left), depth(right))`。",
        "code": """from typing import Optional\n\n\nclass Solution:\n    def maxDepth(self, root: Optional[TreeNode]) -> int:\n        if not root:\n            return 0\n        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))""",
    },
    "Invert Binary Tree": {
        "meaning": "这题就是把每个节点的左右子树交换。因为每个节点都做同一件事，所以非常适合 DFS 或递归。",
        "code": """from typing import Optional\n\n\nclass Solution:\n    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:\n        if not root:\n            return None\n        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)\n        return root""",
    },
    "Binary Tree Inorder Traversal": {
        "meaning": "题目要求中序遍历二叉树，也就是按 `left -> root -> right` 的顺序输出节点值。面试里通常会优先写迭代版，因为它能体现你真的理解栈是怎么模拟递归的。",
        "code": """from typing import List, Optional\n\n\nclass Solution:\n    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:\n        stack = []\n        ans = []\n        cur = root\n\n        while stack or cur:\n            while cur:\n                stack.append(cur)\n                cur = cur.left\n\n            cur = stack.pop()\n            ans.append(cur.val)\n            cur = cur.right\n\n        return ans""",
    },
    "Daily Temperatures": {
        "meaning": "对每一天，题目要你找后面第一个更高温度出现的天数差。关键词是“下一个更大元素”，所以单调栈最合适。",
        "code": """from typing import List\n\n\nclass Solution:\n    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:\n        ans = [0] * len(temperatures)\n        stack = []\n\n        for i, temp in enumerate(temperatures):\n            while stack and temperatures[stack[-1]] < temp:\n                j = stack.pop()\n                ans[j] = i - j\n            stack.append(i)\n\n        return ans""",
    },
    "Largest Rectangle in Histogram": {
        "meaning": "题目要你在柱状图里找到最大矩形面积。关键在于固定某根柱子当最矮高度，然后往左右找到第一个更矮的位置，所以这是单调栈的经典题。",
        "code": """from typing import List\n\n\nclass Solution:\n    def largestRectangleArea(self, heights: List[int]) -> int:\n        stack = []\n        ans = 0\n        heights.append(0)\n\n        for i, h in enumerate(heights):\n            while stack and heights[stack[-1]] > h:\n                height = heights[stack.pop()]\n                left = stack[-1] if stack else -1\n                width = i - left - 1\n                ans = max(ans, height * width)\n            stack.append(i)\n\n        heights.pop()\n        return ans""",
    },
    "House Robber": {
        "meaning": "每个房子都有钱，但相邻房子不能同时偷。题目本质是在每个位置做“偷 / 不偷”的最优选择，是一维 DP 模板题。",
        "code": """from typing import List\n\n\nclass Solution:\n    def rob(self, nums: List[int]) -> int:\n        prev2 = 0\n        prev1 = 0\n\n        for x in nums:\n            prev2, prev1 = prev1, max(prev1, prev2 + x)\n\n        return prev1""",
    },
    "Minimum Path Sum": {
        "meaning": "从左上角走到右下角，每次只能向右或向下，求路径和最小值。因为当前格子的最优值只依赖上方和左方，所以是标准网格 DP。",
        "code": """from typing import List\n\n\nclass Solution:\n    def minPathSum(self, grid: List[List[int]]) -> int:\n        m, n = len(grid), len(grid[0])\n        dp = [[0] * n for _ in range(m)]\n        dp[0][0] = grid[0][0]\n\n        for i in range(1, m):\n            dp[i][0] = dp[i - 1][0] + grid[i][0]\n        for j in range(1, n):\n            dp[0][j] = dp[0][j - 1] + grid[0][j]\n\n        for i in range(1, m):\n            for j in range(1, n):\n                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]\n\n        return dp[-1][-1]""",
    },
    "Coin Change": {
        "meaning": "给硬币面额和目标金额，求凑出目标金额的最少硬币数。因为目标金额可以由更小金额推出来，所以是完全背包 / 一维 DP。",
        "code": """from typing import List\n\n\nclass Solution:\n    def coinChange(self, coins: List[int], amount: int) -> int:\n        dp = [amount + 1] * (amount + 1)\n        dp[0] = 0\n\n        for a in range(1, amount + 1):\n            for coin in coins:\n                if coin <= a:\n                    dp[a] = min(dp[a], dp[a - coin] + 1)\n\n        return dp[amount] if dp[amount] != amount + 1 else -1""",
    },
    "Longest Common Subsequence": {
        "meaning": "题目要你求两个字符串的最长公共子序列长度。典型状态是 `dp[i][j]` 表示前 `i` 个字符和前 `j` 个字符的答案。",
        "code": """class Solution:\n    def longestCommonSubsequence(self, text1: str, text2: str) -> int:\n        m, n = len(text1), len(text2)\n        dp = [[0] * (n + 1) for _ in range(m + 1)]\n\n        for i in range(1, m + 1):\n            for j in range(1, n + 1):\n                if text1[i - 1] == text2[j - 1]:\n                    dp[i][j] = dp[i - 1][j - 1] + 1\n                else:\n                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])\n\n        return dp[m][n]""",
    },
    "Partition Equal Subset Sum": {
        "meaning": "这题是把数组分成两个和相等的子集，等价于看能不能选出一部分数，和恰好是总和的一半，所以直接转成 0-1 背包。",
        "code": """from typing import List\n\n\nclass Solution:\n    def canPartition(self, nums: List[int]) -> bool:\n        total = sum(nums)\n        if total % 2 == 1:\n            return False\n\n        target = total // 2\n        dp = [False] * (target + 1)\n        dp[0] = True\n\n        for num in nums:\n            for s in range(target, num - 1, -1):\n                dp[s] = dp[s] or dp[s - num]\n\n        return dp[target]""",
    },
    "Edit Distance": {
        "meaning": "题目要求把 `word1` 变成 `word2` 的最少操作数。每一步只有插入、删除、替换三种操作，所以状态转移非常标准。",
        "code": """class Solution:\n    def minDistance(self, word1: str, word2: str) -> int:\n        m, n = len(word1), len(word2)\n        dp = [[0] * (n + 1) for _ in range(m + 1)]\n\n        for i in range(m + 1):\n            dp[i][0] = i\n        for j in range(n + 1):\n            dp[0][j] = j\n\n        for i in range(1, m + 1):\n            for j in range(1, n + 1):\n                if word1[i - 1] == word2[j - 1]:\n                    dp[i][j] = dp[i - 1][j - 1]\n                else:\n                    dp[i][j] = 1 + min(\n                        dp[i - 1][j],\n                        dp[i][j - 1],\n                        dp[i - 1][j - 1],\n                    )\n\n        return dp[m][n]""",
    },
    "Min Stack": {
        "meaning": "设计一个栈，同时支持 `getMin()` 返回当前最小值。关键是让最小值也跟着栈同步维护，而不是每次现扫一遍。",
        "code": """class MinStack:\n    def __init__(self):\n        self.stack = []\n        self.min_stack = []\n\n    def push(self, val: int) -> None:\n        self.stack.append(val)\n        if not self.min_stack or val <= self.min_stack[-1]:\n            self.min_stack.append(val)\n\n    def pop(self) -> None:\n        val = self.stack.pop()\n        if val == self.min_stack[-1]:\n            self.min_stack.pop()\n\n    def top(self) -> int:\n        return self.stack[-1]\n\n    def getMin(self) -> int:\n        return self.min_stack[-1]""",
    },
    "Find All Anagrams in a String": {
        "meaning": "题目让你找出 `s` 中所有和 `p` 互为字母异位词的子串起点。因为窗口长度固定为 `len(p)`，所以这是固定滑窗。",
        "code": """from collections import Counter\nfrom typing import List\n\n\nclass Solution:\n    def findAnagrams(self, s: str, p: str) -> List[int]:\n        need = Counter(p)\n        window = Counter()\n        left = 0\n        ans = []\n\n        for right, ch in enumerate(s):\n            window[ch] += 1\n\n            if right - left + 1 > len(p):\n                left_ch = s[left]\n                window[left_ch] -= 1\n                if window[left_ch] == 0:\n                    del window[left_ch]\n                left += 1\n\n            if right - left + 1 == len(p) and window == need:\n                ans.append(left)\n\n        return ans""",
    },
    "Jump Game": {
        "meaning": "数组中每个位置给出你最多能跳多远，问能否到达终点。贪心的核心是维护当前能到达的最远位置。",
        "code": """from typing import List\n\n\nclass Solution:\n    def canJump(self, nums: List[int]) -> bool:\n        farthest = 0\n        for i, step in enumerate(nums):\n            if i > farthest:\n                return False\n            farthest = max(farthest, i + step)\n        return True""",
    },
    "Jump Game II": {
        "meaning": "和 `Jump Game` 不同，这次要你求最少跳跃次数。仍然是贪心，但多维护一层当前步数能覆盖的边界。",
        "code": """from typing import List\n\n\nclass Solution:\n    def jump(self, nums: List[int]) -> int:\n        steps = 0\n        end = 0\n        farthest = 0\n\n        for i in range(len(nums) - 1):\n            farthest = max(farthest, i + nums[i])\n            if i == end:\n                steps += 1\n                end = farthest\n\n        return steps""",
    },
    "Partition Labels": {
        "meaning": "你要把字符串切成尽量多段，并保证同一个字符只出现在一段里。关键是先知道每个字符最后一次出现的位置，然后贪心切段。",
        "code": """from typing import List\n\n\nclass Solution:\n    def partitionLabels(self, s: str) -> List[int]:\n        last = {ch: i for i, ch in enumerate(s)}\n        ans = []\n        start = 0\n        end = 0\n\n        for i, ch in enumerate(s):\n            end = max(end, last[ch])\n            if i == end:\n                ans.append(end - start + 1)\n                start = i + 1\n\n        return ans""",
    },
    "Linked List Cycle / Cycle II": {
        "meaning": "这一组题的目标分别是：判断链表是否有环，以及找出环的入口。核心都是 Floyd 快慢指针。",
        "code": """from typing import Optional\n\n\nclass Solution:\n    def hasCycle(self, head: Optional[ListNode]) -> bool:\n        slow = head\n        fast = head\n\n        while fast and fast.next:\n            slow = slow.next\n            fast = fast.next.next\n            if slow == fast:\n                return True\n\n        return False""",
    },
    "Palindrome Linked List": {
        "meaning": "判断链表是否为回文。标准做法是找中点、反转后半段，再从两头往中间比。",
        "code": """from typing import Optional\n\n\nclass Solution:\n    def isPalindrome(self, head: Optional[ListNode]) -> bool:\n        slow = head\n        fast = head\n\n        while fast and fast.next:\n            slow = slow.next\n            fast = fast.next.next\n\n        prev = None\n        while slow:\n            nxt = slow.next\n            slow.next = prev\n            prev = slow\n            slow = nxt\n\n        left = head\n        right = prev\n        while right:\n            if left.val != right.val:\n                return False\n            left = left.next\n            right = right.next\n\n        return True""",
    },
    "Swap Nodes in Pairs": {
        "meaning": "每两个相邻节点交换一次，本质是链表局部重连。`dummy` 节点能让头结点交换也保持统一写法。",
        "code": """from typing import Optional\n\n\nclass Solution:\n    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:\n        dummy = ListNode(0, head)\n        prev = dummy\n\n        while prev.next and prev.next.next:\n            a = prev.next\n            b = a.next\n\n            prev.next = b\n            a.next = b.next\n            b.next = a\n            prev = a\n\n        return dummy.next""",
    },
    "Reverse Nodes in k-Group": {
        "meaning": "链表每 `k` 个节点翻转一次，不足 `k` 个保持不变。面试重点在于分组、断开、反转、再接回。",
        "code": """from typing import Optional\n\n\nclass Solution:\n    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:\n        dummy = ListNode(0, head)\n        group_prev = dummy\n\n        while True:\n            kth = group_prev\n            for _ in range(k):\n                kth = kth.next\n                if not kth:\n                    return dummy.next\n\n            group_next = kth.next\n            prev = group_next\n            cur = group_prev.next\n\n            while cur != group_next:\n                nxt = cur.next\n                cur.next = prev\n                prev = cur\n                cur = nxt\n\n            tmp = group_prev.next\n            group_prev.next = kth\n            group_prev = tmp""",
    },
    "N-Queens": {
        "meaning": "在 `n x n` 棋盘上放 `n` 个皇后，要求互不攻击。典型回溯题，关键是列、主对角线、副对角线的冲突判断。",
        "code": """from typing import List\n\n\nclass Solution:\n    def solveNQueens(self, n: int) -> List[List[str]]:\n        cols = set()\n        diag1 = set()\n        diag2 = set()\n        board = [['.'] * n for _ in range(n)]\n        ans = []\n\n        def dfs(r: int) -> None:\n            if r == n:\n                ans.append([''.join(row) for row in board])\n                return\n\n            for c in range(n):\n                if c in cols or r - c in diag1 or r + c in diag2:\n                    continue\n                cols.add(c)\n                diag1.add(r - c)\n                diag2.add(r + c)\n                board[r][c] = 'Q'\n                dfs(r + 1)\n                board[r][c] = '.'\n                cols.remove(c)\n                diag1.remove(r - c)\n                diag2.remove(r + c)\n\n        dfs(0)\n        return ans""",
    },
}


META = {
    "Two Sum": ("`O(n)`，每个元素查一次哈希表。", "`O(n)`，字典存历史元素。", "看到“找两数和为 target”，先把它翻译成“当前数需要一个补数”。只要题目允许用额外空间，`hash map` 往往就是第一反应。", "- 如果数组已排序，能不能改成双指针？\n- 如果要返回所有不重复配对，如何避免重复？"),
    "Best Time to Buy and Sell Stock": ("`O(n)`，单次扫描。", "`O(1)`。", "一旦题目限制只能买卖一次，就不要去想区间枚举，而是问自己：如果今天卖，最好的买入价是谁？于是自然会维护历史最小值。", "- 如果可以交易多次怎么改？\n- 如果有冷冻期或手续费，为什么会变成 DP？"),
    "Maximum Subarray": ("`O(n)`。", "`O(1)`。", "关键词是“连续子数组最大和”。这种题先问“以当前位置结尾的最优值是什么”，就会走到 Kadane 的状态转移。", "- 如果还要返回具体区间，怎么记录起点终点？\n- 如果数组是环形，思路怎么改？"),
    "Move Zeroes": ("`O(n)`。", "`O(1)` 原地。", "题目要求原地、稳定地把非零元素往前放，这就是典型快慢指针信号。`slow` 负责放置位置，`fast` 负责扫描。", "- 如果不能交换、只能覆盖写，怎么实现？\n- 如果要把指定值移到末尾，模板是否相同？"),
    "Container With Most Water": ("`O(n)`。", "`O(1)`。", "题目同时给你左右边界和面积公式，通常就该考虑双指针。因为面积瓶颈由短板决定，所以每次移动更短的一边才有希望变优。", "- 为什么移动更高的一边没有意义？\n- 如果需要输出具体下标，代码怎么保留答案？"),
    "3Sum": ("`O(n^2)`，排序后枚举一个数再双指针。", "排序开销外额外 `O(1)`；若计入排序栈通常写 `O(log n)`。", "看到“三元组 + 去重 + 和为 0”，就要想到先排序，把问题降成固定一个数后的 `Two Sum`。", "- 如果是 `3Sum Closest` 怎么改？\n- 如果是 `4Sum`，思路如何继续套？"),
    "Subarray Sum Equals K": ("`O(n)`。", "`O(n)`，前缀和计数表。", "只要题目问“连续子数组和为 k 的个数”，先把区间和写成两个前缀和之差，问题就能转成哈希计数。", "- 如果数组都是非负数，能不能改滑窗？\n- 如果要找最长而不是个数，哈希表存什么？"),
    "Product of Array Except Self": ("`O(n)`。", "额外空间 `O(1)`；如果把输出数组也算上则是 `O(n)`。", "不能用除法时，最自然的拆法就是“左边乘积 * 右边乘积”。这类题一般都会想到前缀/后缀信息预处理。", "- 如果数组有 0，用除法法为什么麻烦？\n- 能否只用一个输出数组完成？"),
    "Longest Consecutive Sequence": ("`O(n)` 平均。", "`O(n)`。", "题目要的是“连续值”，不是连续下标，所以别急着排序。哈希集合更适合做“某个数是不是序列起点”的判断。", "- 如果要求输出序列本身怎么做？\n- 排序做法为什么是 `O(n log n)`？"),
    "Trapping Rain Water": ("`O(n)`。", "`O(1)` 双指针版；单调栈版是 `O(n)` 空间。", "题目本质是每个位置能装多少水取决于左右最高板。你可以从“预处理左右最大值”出发，再进一步优化成双指针。", "- 你能讲单调栈解法吗？\n- 如果要输出每格积水量，需要额外存什么？"),
    "Reverse Linked List": ("`O(n)`。", "`O(1)`。", "链表反转的核心不是背代码，而是每次改指针前先保住 `next`。面试里只要能稳定说清 `prev / cur / nxt` 三个角色就够了。", "- 递归版怎么写？\n- 如果只反转区间 `[left, right]` 呢？"),
    "Merge Two Sorted Lists": ("`O(m+n)`。", "`O(1)` 额外空间。", "两个有序结构合并时，几乎总是双指针。链表版再加一个 `dummy` 节点，就能少掉大量头节点特判。", "- 如果是数组合并为什么常从后往前？\n- 如果是 `k` 个有序链表怎么办？"),
    "Remove Nth Node From End of List": ("`O(n)`。", "`O(1)`。", "“倒数第 n 个”是快慢指针的经典信号，让 `fast` 先走 `n` 步，就把“倒数”翻译成了“相隔固定距离的同向移动”。", "- 如果要求只遍历一遍，为什么快慢指针正合适？\n- 为什么最好总是加 `dummy`？"),
    "Add Two Numbers": ("`O(max(m,n))`。", "`O(1)` 额外空间，不计答案链表。", "逐位相加、带进位，这和手算加法完全一致。题目把数字倒着存，其实就是在帮你从低位开始处理。", "- 如果链表是正序存储怎么办？\n- 如果不能改原链表，如何处理？"),
    "Linked List Cycle / Cycle II": ("`O(n)`。", "`O(1)`。", "只要问链表里有没有环，快慢指针几乎就是默认答案。进一步找入口时，记住“相遇点再和头节点同步走”这个结论。", "- 为什么相遇后从头和相遇点一起走会在入口相遇？\n- 用哈希表也能做，差别是什么？"),
    "Palindrome Linked List": ("`O(n)`。", "`O(1)`。", "回文判断通常需要双端比较，但链表不能从尾往前走，所以要先把后半段反转，手动造出两个方向。", "- 比完之后要不要恢复链表？\n- 如果只能用递归，空间代价是什么？"),
    "Intersection of Two Linked Lists": ("`O(m+n)`。", "`O(1)`。", "两个指针分别走 `A+B` 和 `B+A`，总路程对齐后就能在交点相遇。这题的关键是把长度差自动抵消掉。", "- 为什么走完自己链表后切到另一条链表就能对齐？\n- 哈希表写法和双指针写法怎么比较？"),
    "Swap Nodes in Pairs": ("`O(n)`。", "`O(1)`。", "看到“成对交换节点”，要想到这不是换值，而是换指针。`dummy + prev + a + b` 这四个指针关系最稳定。", "- 如果每 `k` 个交换一次，就是哪道题？\n- 交换节点值和交换节点本身有什么区别？"),
    "Copy List with Random Pointer": ("`O(n)`。", "`O(n)` 哈希表版。", "这题的难点不是遍历，而是节点之间有额外的 `random` 关系。最稳的思路是先建立旧节点到新节点的映射。", "- 你能讲 `O(1)` 额外空间的穿插复制法吗？\n- 为什么要分两遍构造？"),
    "Sort List": ("`O(n log n)`。", "`O(log n)` 递归栈；自底向上可做到 `O(1)` 额外空间。", "链表不适合随机访问，所以别想快速排序那套。面试默认答案是链表归并排序：找中点、拆开、递归合并。", "- 为什么链表排序更偏向归并而不是快排？\n- 你能写 bottom-up 版吗？"),
    "LRU Cache": ("`O(1)` 均摊完成 `get/put`。", "`O(capacity)`。", "一旦题目同时要“按 key 快速找”和“按最近使用顺序快速删”，就该想到 `HashMap + Doubly Linked List` 的双结构组合。", "- 如果变成 LFU，该多维护什么状态？\n- 为什么必须是双向链表？"),
    "Merge k Sorted Lists": ("`O(N log k)`。", "`O(k)`。", "多个有序链表合并，本质就是反复拿当前最小值。只要 `k` 大于 2，最自然的优化就是最小堆。", "- 分治合并和堆解法怎么比较？\n- 如果链表数量很少，是否直接两两合并更简单？"),
    "Reverse Nodes in k-Group": ("`O(n)`。", "`O(1)`。", "这题是在局部反转基础上再加“按组处理”。真正的面试重点是把一组的边界找出来，再把反转后的头尾接回原链表。", "- 如果最后不足 `k` 个也要反转，哪里改？\n- 你会写递归版吗？"),
    "Valid Parentheses": ("`O(n)`。", "`O(n)`。", "看到括号匹配、嵌套结构、最近未匹配元素，这三个信号基本就能直接想到栈。", "- 如果括号种类变多，代码需要变吗？\n- 如果要求返回第一个非法位置怎么办？"),
    "Min Stack": ("`O(1)` 每次操作。", "`O(n)`。", "设计题里一旦某个查询要做到 `O(1)`，就要问自己能不能在写入时把未来查询需要的信息一并维护起来。这里就是同步维护最小值栈。", "- 如果要支持 `getMax()` 呢？\n- 能不能每个栈节点直接存当前最小值？"),
    "Decode String": ("`O(n)`。", "`O(n)`。", "字符串解码一看到嵌套括号，就要想到用栈保存“进入括号之前”的状态。每遇到 `]` 就把当前片段弹出并展开。", "- 如果出现多位数字，为什么当前写法依然对？\n- 递归下降也能做，优缺点是什么？"),
    "Daily Temperatures": ("`O(n)`。", "`O(n)`。", "“下一个更大元素”就是单调栈最经典的识别信号。栈里存还没找到答案的位置，并保持对应值单调。", "- 如果问的是前一个更大元素呢？\n- 如果不返回天数差，只返回温度值，怎么改？"),
    "Largest Rectangle in Histogram": ("`O(n)`。", "`O(n)`。", "看到“每根柱子向左右扩展到哪里”，就要想到找左右第一个更小元素，这正是单调栈的拿手戏。", "- 如果是二维 `maximal rectangle`，怎么降维？\n- 为什么结尾常常补一个 0？"),
    "Longest Valid Parentheses": ("`O(n)`。", "`O(n)`。", "这题表面像括号匹配，实际上是“最长合法区间”。栈里放下标而不是字符，才能顺手算长度。", "- DP 解法也能做吗？\n- 为什么栈里常先压入 `-1`？"),
    "Binary Tree Level Order Traversal": ("`O(n)`。", "`O(n)`。", "只要题目要求“按层输出”，那就是 BFS 队列模板。队列长度天然告诉你这一层有几个节点。", "- 如果改成自底向上输出怎么做？\n- DFS 能不能写出层序遍历？"),
    "Maximum Depth of Binary Tree": ("`O(n)`。", "`O(h)`，递归栈高度为树高。", "树高题往往直接写递归定义最自然：当前节点的深度等于左右子树更深者加一。", "- BFS 版怎么写？\n- 平衡树和链式树的空间区别是什么？"),
    "Invert Binary Tree": ("`O(n)`。", "`O(h)`。", "每个节点都做同样的左右交换，所以递归是最顺手的表达方式。把这题想成“后序地返回交换后的子树”就很自然。", "- 迭代版怎么写？\n- 为什么这题特别适合解释递归框架？"),
    "Binary Tree Inorder Traversal": ("`O(n)`。", "`O(h)`。", "中序遍历的顺序固定是左根右。迭代版的重点是理解：一路向左压栈，相当于手动模拟递归调用栈。", "- 前序和后序的迭代写法如何改？\n- 如果是 BST，中序遍历有什么额外性质？"),
    "Symmetric Tree": ("`O(n)`。", "`O(h)` 递归栈。", "对称不是看单边，而是同时比较两棵镜像子树：左的左对右的右，左的右对右的左。", "- 迭代版怎么用队列成对比较？\n- 如果是 `same tree`，条件怎么变化？"),
    "Diameter of Binary Tree": ("`O(n)`。", "`O(h)`。", "树的直径题通常不是在每个点向外暴力扩，而是后序遍历时顺便拿到左右子树高度，再更新答案。", "- 为什么答案不一定经过根？\n- 如果要求输出路径本身，还要额外记录什么？"),
    "Validate Binary Search Tree": ("`O(n)`。", "`O(h)`。", "BST 校验容易掉进“只比父节点”的坑。正确思路是给每个节点传可取值范围，或者用中序递增性质。", "- 为什么只比较父子节点不够？\n- 中序遍历版怎么写？"),
    "Kth Smallest Element in a BST": ("`O(h+k)`，最坏 `O(n)`。", "`O(h)`。", "BST 的中序遍历天然有序，所以这题最直接的思路就是中序走到第 `k` 个就停。", "- 如果树频繁更新、频繁查询第 k 小，怎么优化？\n- 如果要求第 k 大呢？"),
    "Lowest Common Ancestor of a Binary Tree": ("`O(n)`。", "`O(h)`。", "LCA 的递归核心是：如果左右子树分别找到了不同目标，那么当前节点就是分叉点。", "- 如果是 BST，如何利用有序性优化？\n- 如果节点有父指针，能不能换思路？"),
    "Binary Tree Right Side View": ("`O(n)`。", "`O(n)`。", "题目按层看每层最右边节点，所以最自然还是层序遍历，只记录每层最后一个出队节点。", "- DFS 也能做吗？\n- 如果要左视图，只改哪一行？"),
    "Path Sum III": ("`O(n)`。", "`O(n)`。", "这题虽然在树上，但问的是“路径和为 target 的条数”，所以要联想到数组里的前缀和计数，再把它搬到 DFS 路径上。", "- 为什么不能只从根开始算？\n- 如果路径必须从根到叶，思路怎么简化？"),
    "Flatten Binary Tree to Linked List": ("`O(n)`。", "`O(h)`。", "题目要原地把树拉平成先序链表，所以你需要保住左右子树的连接关系。后序返回尾节点会写得更稳。", "- 你能讲 Morris 风格的 `O(1)` 空间做法吗？\n- 为什么要先处理右子树再处理左子树？"),
    "Construct Binary Tree from Preorder and Inorder": ("`O(n)`。", "`O(n)`。", "前序给根，中序帮你切左右子树。只要你能说清“根是谁、左右范围怎么切”，这题就已经过半了。", "- 为什么需要 `value -> index` 哈希表？\n- 如果改成中序 + 后序呢？"),
    "Binary Tree Maximum Path Sum": ("`O(n)`。", "`O(h)`。", "最大路径和的难点是区分“往上返回给父节点的值”和“当前节点内部更新答案的值”。这通常是树 DP 的标志。", "- 为什么返回值不能同时带左右两边？\n- 如果节点值全负，初始化要注意什么？"),
    "Longest Substring Without Repeating Characters": ("`O(n)`。", "`O(k)`，`k` 为窗口内字符种类。", "题目是典型的“最长 + 子串 + 无重复”，三个关键词凑在一起几乎就是可变滑窗。", "- 如果字符集固定，能不能用数组替代哈希表？\n- 如果允许最多重复一次，窗口条件怎么改？"),
    "Find All Anagrams in a String": ("`O(n)`。", "`O(1)` 或 `O(k)`，取决于字符集实现。", "因为窗口长度固定为 `len(p)`，所以它不是可变滑窗，而是固定滑窗加频次比较。", "- 如果字符集特别大，频次数组还合适吗？\n- 能不能维护一个 `matches` 计数避免整张表比较？"),
    "Minimum Window Substring": ("`O(m+n)`。", "`O(k)`。", "题目要最短合法窗口，固定窗口不适合，应该想到可变滑窗。关键是先定义什么叫“窗口已经覆盖了 t”。", "- 如果 `t` 中有重复字符，为什么需要计数而不是集合？\n- 如果要返回长度而不是子串，代码怎么简化？"),
    "Sliding Window Maximum": ("`O(n)`。", "`O(k)`。", "窗口里既要滑动，又要随时拿最大值，这类题最常见的组合就是单调队列。", "- 为什么普通队列不够？\n- 如果还要拿窗口最小值，能不能一起维护？"),
    "Jump Game": ("`O(n)`。", "`O(1)`。", "题目不是问具体路径，只问能不能到，所以没必要做 DP。贪心维护“目前最远能到哪”就足够了。", "- 如果要求最少步数，怎么升级成 `Jump Game II`？\n- 为什么当 `i > farthest` 时就能提前返回？"),
    "Jump Game II": ("`O(n)`。", "`O(1)`。", "最少步数版可以把每一步看成一层区间扩展，和 BFS 分层很像，但可以压缩成贪心边界写法。", "- 为什么不需要真的把每个位置入队？\n- 如果还要返回路径，数据结构怎么变？"),
    "Partition Labels": ("`O(n)`。", "`O(1)` 或 `O(k)`。", "先预处理每个字符最后出现位置，然后一遍扫描动态扩展当前段的右边界。这是很典型的区间贪心。", "- 如果字符集不是小写字母，写法要改吗？\n- 为什么在 `i == end` 时就能安全切段？"),
    "Climbing Stairs": ("`O(n)`。", "`O(1)`。", "每一步只能由前两步转移而来，所以本质就是 Fibonacci。只要能写出状态转移，这题就很顺。", "- 如果一次能爬 1/2/3 阶，转移怎么改？\n- 为什么可以把 DP 数组压缩成两个变量？"),
    "House Robber": ("`O(n)`。", "`O(1)`。", "每个位置只有“抢 / 不抢”两种选择，而且会影响下一个位置，所以非常适合一维 DP。", "- 如果房子围成一圈怎么办？\n- 如果是二叉树版为什么会变成树 DP？"),
    "Unique Paths": ("`O(mn)`。", "`O(mn)`；可压缩到 `O(n)`。", "只能向右或向下，所以到达当前格子的路径数只来自上方和左方，这是最标准的网格 DP 信号。", "- 如果有障碍物怎么办？\n- 组合数学解法为什么也成立？"),
    "Minimum Path Sum": ("`O(mn)`。", "`O(mn)`；可压缩到 `O(n)`。", "和 `Unique Paths` 相比，这题只是把“路径条数”换成了“最小路径和”。网格 DP 模板完全一致。", "- 如何原地修改 `grid` 省空间？\n- 如果允许对角线移动，状态要怎么改？"),
    "Coin Change": ("`O(amount * len(coins))`。", "`O(amount)`。", "问最少硬币数时，先想“凑出金额 `a` 的答案能不能由更小金额推出来”。这就是完全背包 / 一维 DP。", "- 如果问方案数而不是最少个数，转移怎么改？\n- 如果每种硬币只能用一次，会变成什么模型？"),
    "Word Break": ("`O(n^2)`，若切片和集合查找都算上通常这样写。", "`O(n)`。", "题目问字符串能不能被字典切开，最自然的状态是：前 `i` 个字符能不能被拆分。", "- 如果要输出所有方案，就变成哪道题？\n- `Trie + DFS + memo` 为什么有时更快？"),
    "Partition Equal Subset Sum": ("`O(n * target)`。", "`O(target)`。", "一看到“能不能选一些数凑出某个和”，就要往 0-1 背包上靠。这里目标值正好是总和的一半。", "- 为什么内层循环要倒序？\n- 如果要输出具体子集，如何回溯路径？"),
    "Longest Common Subsequence": ("`O(mn)`。", "`O(mn)`；可压缩到 `O(n)`。", "两个字符串问题优先想二维 DP。LCS 的关键是明确字符相等和不等时分别继承哪个子问题。", "- 如果要恢复出子序列本身，需要怎么做？\n- 和最长公共子串有什么区别？"),
    "Longest Increasing Subsequence": ("`O(n log n)`。", "`O(n)`。", "这题有 `O(n^2)` DP，但面试里经常追问更优解。想到“维护每个长度的最小结尾”后，就能配合二分优化。", "- 你也能讲 `O(n^2)` 版本吗？\n- 如果要恢复具体序列，需额外存什么？"),
    "Longest Palindromic Substring": ("`O(n^2)`。", "`O(1)` 中心扩展版。", "子串回文题最先想到的通常是“以某个中心向两边扩”。这样既好写，也容易现场讲清楚。", "- DP 版怎么定义状态？\n- 为什么奇数长度和偶数长度都要枚举？"),
    "Maximum Product Subarray": ("`O(n)`。", "`O(1)`。", "乘积题和加法题不同，负数会让最大最小互换，所以你要同时维护当前位置结尾的最大值和最小值。", "- 为什么只维护最大值不够？\n- 如果数组里有 0，会发生什么？"),
    "Edit Distance": ("`O(mn)`。", "`O(mn)`；可压缩到 `O(n)`。", "操作只有插入、删除、替换三种，所以二维 DP 非常自然。想清楚 `dp[i][j]` 的含义就能稳住。", "- 如果替换代价不是 1，状态怎么改？\n- 如何压缩空间？"),
    "Median of Two Sorted Arrays": ("`O(log(min(m,n)))`。", "`O(1)`。", "这题难在把“求中位数”转成“找一个合法切分”。只要切分左边元素个数正确，再保证左半最大值不超过右半最小值即可。", "- 为什么要优先在更短数组上二分？\n- 如果总长度是奇数和偶数，答案如何取？"),
    "Find Median from Data Stream": ("`O(log n)` 插入，`O(1)` 查询。", "`O(n)`。", "数据流中位数一看到“动态插入 + 随时查询中位数”，就该想到两个堆维持左右两半。", "- 为什么一个最大堆一个最小堆？\n- 如果要删除元素，还能怎么设计？"),
    "First Missing Positive": ("`O(n)`。", "`O(1)` 原地。", "数组值域落在 `1..n` 时，面试高频套路是把值尽量放回它应该在的位置，再扫描第一个不匹配的位置。", "- 为什么答案一定在 `1..n+1`？\n- 用哈希集合能做，但为什么不是最优？"),
    "N-Queens": ("`O(n!)` 量级，精确值取决于剪枝。", "`O(n)` 递归栈加集合。", "题目让你枚举所有合法摆法，而且每行只能放一个皇后，这就是标准回溯。列和对角线冲突检查是剪枝重点。", "- 如果只要求返回解的数量，怎么改？\n- 位运算优化为什么会更快？"),
}


for title in FALLBACK:
    META.setdefault(
        title,
        ("见该题代码对应的主循环或递归规模分析。", "见该题使用的数据结构与递归深度。", "先识别这道题属于哪种经典模板，再把问题翻译成那个模板的标准状态或不变量。", "- 面试里常见追问是能不能优化空间。\n- 也常会问有没有另一种模板写法。"),
    )


def build_standard_block(title: str, meaning: str, code: str, time_text: str, space_text: str, think_text: str, follow_text: str) -> str:
    return f"""**题目含义**

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
    source_map = {}
    for path in sorted(SOURCE_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        for title, section in parse_sections(text, r"^##\s+\d+\.\s+(.+)$").items():
            meaning = extract_between(section, "**中文解释**", ["**English Explanation**", "**Python 标准解法**"])
            code = extract_code(section)
            source_map[title] = {
                "meaning": clean_paragraph(meaning),
                "code": code,
            }
    return source_map


SOURCE_MAP = build_source_map()


def content_for_title(title: str):
    source_title = ALIAS.get(title, title)
    if source_title in SOURCE_MAP:
        data = SOURCE_MAP[source_title]
        return data["meaning"], data["code"]
    if title in FALLBACK:
        data = FALLBACK[title]
        return data["meaning"], data["code"]
    return "", ""


def replace_problem_sections(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    matches = list(re.finditer(r"^###\s+\d+\.\s+(.+)$", text, re.M))
    if not matches:
        return

    new_parts = []
    cursor = 0

    for i, match in enumerate(matches):
        title = match.group(1).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        new_parts.append(text[cursor:start])

        if title in META:
            meaning, code = content_for_title(title)
            if meaning and code:
                time_text, space_text, think_text, follow_text = META[title]
                new_section = "\n\n" + build_standard_block(
                    title,
                    meaning,
                    code,
                    time_text,
                    space_text,
                    think_text,
                    follow_text,
                ) + "\n\n"
                new_parts.append(new_section)
            else:
                new_parts.append(text[start:end])
        else:
            new_parts.append(text[start:end])
        cursor = end

    new_parts.append(text[cursor:])
    path.write_text("".join(new_parts), encoding="utf-8")


def main() -> None:
    for path in sorted(TARGET_DIR.glob("[0-9][0-9]_*.md")):
        replace_problem_sections(path)


if __name__ == "__main__":
    main()
