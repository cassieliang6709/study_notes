#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TARGET_DIRS = [
    ROOT / "algorithms" / "company_hot_questions",
    ROOT / "algorithms" / "leetcode_100_detailed",
    ROOT / "algorithms" / "extended_problem_detailed",
    ROOT / "algorithms" / "extended_problem_full_solutions",
]


SECTION_PATTERNS = [
    r"^##\s+\d+\.\s+(.+)$",
    r"^###\s+\d+\.\s+(.+)$",
    r"^####\s+\d+\.\s+(.+)$",
    r"^###\s+(.+)$",
]


CASES = {
    "Two Sum": ("输入：`nums = [2, 7, 11, 15]`, `target = 9`", "输出：`[0, 1]`。因为 `2 + 7 = 9`，而且题目要返回原始下标。"),
    "Best Time to Buy and Sell Stock": ("输入：`prices = [7, 1, 5, 3, 6, 4]`", "输出：`5`。最优是在价格 `1` 买入、价格 `6` 卖出。"),
    "Maximum Subarray": ("输入：`nums = [-2,1,-3,4,-1,2,1,-5,4]`", "输出：`6`。最大连续子数组是 `[4,-1,2,1]`。"),
    "Move Zeroes": ("输入：`nums = [0,1,0,3,12]`", "输出：`[1,3,12,0,0]`。非零元素相对顺序保持不变。"),
    "Container With Most Water": ("输入：`height = [1,8,6,2,5,4,8,3,7]`", "输出：`49`。最优边界在下标 `1` 和 `8`。"),
    "3Sum": ("输入：`nums = [-1,0,1,2,-1,-4]`", "输出：`[[-1,-1,2],[-1,0,1]]`。排序后用双指针可以自然去重。"),
    "Subarray Sum Equals K": ("输入：`nums = [1,1,1]`, `k = 2`", "输出：`2`。满足条件的连续子数组是前两个 `1` 和后两个 `1`。"),
    "Product of Array Except Self": ("输入：`nums = [1,2,3,4]`", "输出：`[24,12,8,6]`。每个位置都等于左边乘积乘右边乘积。"),
    "Longest Consecutive Sequence": ("输入：`nums = [100,4,200,1,3,2]`", "输出：`4`。连续序列是 `1,2,3,4`。"),
    "Trapping Rain Water": ("输入：`height = [0,1,0,2,1,0,1,3,2,1,2,1]`", "输出：`6`。每个位置的积水取决于左右最高板中的较小值。"),
    "Reverse Linked List": ("输入链表：`1 -> 2 -> 3 -> 4 -> 5`", "输出链表：`5 -> 4 -> 3 -> 2 -> 1`。整个链表方向被反过来。"),
    "Merge Two Sorted Lists": ("输入：`1 -> 2 -> 4` 和 `1 -> 3 -> 4`", "输出：`1 -> 1 -> 2 -> 3 -> 4 -> 4`。每次接较小节点。"),
    "Remove Nth Node From End of List": ("输入：`head = [1,2,3,4,5]`, `n = 2`", "输出：`[1,2,3,5]`。倒数第二个节点 `4` 被删除。"),
    "Add Two Numbers": ("输入：`[2,4,3]` 和 `[5,6,4]`", "输出：`[7,0,8]`。因为它们表示 `342 + 465 = 807`。"),
    "Linked List Cycle / Cycle II": ("输入：链表尾部连回前面某个节点", "输出：`Cycle I` 判断是否有环，`Cycle II` 找到环入口。快慢指针相遇后可继续定位入口。"),
    "Palindrome Linked List": ("输入：`1 -> 2 -> 2 -> 1`", "输出：`True`。反转后半段后从两边向中间比较。"),
    "Intersection of Two Linked Lists": ("输入：两条链表在某个节点后共用尾部", "输出：返回第一个公共节点。双指针走 `A+B` 与 `B+A` 会自动对齐。"),
    "Swap Nodes in Pairs": ("输入：`1 -> 2 -> 3 -> 4`", "输出：`2 -> 1 -> 4 -> 3`。每两个节点交换一次。"),
    "Copy List with Random Pointer": ("输入：链表节点除 `next` 外还有 `random` 指针", "输出：一条深拷贝链表，`next` 和 `random` 关系都要复制。"),
    "Sort List": ("输入：`4 -> 2 -> 1 -> 3`", "输出：`1 -> 2 -> 3 -> 4`。链表排序通常用归并最稳定。"),
    "LRU Cache": ("操作：`put(1,1)`, `put(2,2)`, `get(1)`, `put(3,3)`", "结果：插入 `3` 时会淘汰 key `2`，因为它是最近最少使用。"),
    "Merge k Sorted Lists": ("输入：多个已排序链表", "输出：合并后的有序链表。最常见做法是最小堆，每次拿当前最小头节点。"),
    "Reverse Nodes in k-Group": ("输入：`1 -> 2 -> 3 -> 4 -> 5`, `k = 2`", "输出：`2 -> 1 -> 4 -> 3 -> 5`。不足 `k` 个的尾段保持不变。"),
    "Valid Parentheses": ("输入：`s = \"()[]{}\"`", "输出：`True`。每个右括号都能匹配最近的对应左括号。"),
    "Min Stack": ("操作：`push(-2)`, `push(0)`, `push(-3)`, `getMin()`", "输出：`-3`。最小值要和主栈同步维护。"),
    "Decode String": ("输入：`s = \"3[a2[c]]\"`", "输出：`accaccacc`。内层先展开，再乘上外层次数。"),
    "Daily Temperatures": ("输入：`[73,74,75,71,69,72,76,73]`", "输出：`[1,1,4,2,1,1,0,0]`。每个位置等到更高温度需要几天。"),
    "Largest Rectangle in Histogram": ("输入：`heights = [2,1,5,6,2,3]`", "输出：`10`。最大矩形由高度 `5,6` 这段组成。"),
    "Longest Valid Parentheses": ("输入：`s = \")()())\"`", "输出：`4`。最长合法括号子串是 `()()`。"),
    "Maximum Depth of Binary Tree": ("输入：一棵高度为 3 的二叉树", "输出：`3`。递归返回左右子树更深者加一。"),
    "Invert Binary Tree": ("输入：二叉树根节点", "输出：左右子树全部镜像交换后的树。"),
    "Binary Tree Inorder Traversal": ("输入：`[1,null,2,3]`", "输出：`[1,3,2]`。中序遍历顺序是左、根、右。"),
    "Symmetric Tree": ("输入：左右镜像的二叉树", "输出：`True`。镜像比较要同时看左左对右右、左右对右左。"),
    "Binary Tree Level Order Traversal": ("输入：普通二叉树", "输出：按层分组的节点值数组，例如 `[[3],[9,20],[15,7]]`。"),
    "Diameter of Binary Tree": ("输入：二叉树", "输出：任意两节点间最长路径长度。答案不一定经过根。"),
    "Validate Binary Search Tree": ("输入：一棵二叉树", "输出：判断是否满足 BST 全局有序约束，而不是只比较父子节点。"),
    "Kth Smallest Element in a BST": ("输入：BST 和 `k = 3`", "输出：中序遍历第 3 个节点值。"),
    "Lowest Common Ancestor of a Binary Tree": ("输入：二叉树中的两个节点", "输出：它们最近的公共祖先节点。"),
    "Binary Tree Right Side View": ("输入：二叉树", "输出：从右侧看到的节点列表，例如 `[1,3,4]`。"),
    "Path Sum III": ("输入：二叉树和 `targetSum`", "输出：所有向下路径中和等于目标值的条数。"),
    "Flatten Binary Tree to Linked List": ("输入：二叉树", "输出：原地拉平成先序遍历顺序的右链表。"),
    "Construct Binary Tree from Preorder and Inorder": ("输入：前序和中序遍历数组", "输出：还原出的原始二叉树。"),
    "Binary Tree Maximum Path Sum": ("输入：可能包含负数的二叉树", "输出：任意路径的最大路径和。"),
    "Longest Substring Without Repeating Characters": ("输入：`s = \"abcabcbb\"`", "输出：`3`。最长无重复子串是 `abc`。"),
    "Find All Anagrams in a String": ("输入：`s = \"cbaebabacd\"`, `p = \"abc\"`", "输出：`[0,6]`。这两个起点对应的窗口都是 `abc` 的异位词。"),
    "Minimum Window Substring": ("输入：`s = \"ADOBECODEBANC\"`, `t = \"ABC\"`", "输出：`\"BANC\"`。它是覆盖 `ABC` 的最短窗口。"),
    "Sliding Window Maximum": ("输入：`nums = [1,3,-1,-3,5,3,6,7]`, `k = 3`", "输出：`[3,3,5,5,6,7]`。每个长度为 3 的窗口都要取最大值。"),
    "Jump Game": ("输入：`nums = [2,3,1,1,4]`", "输出：`True`。维护最远可达位置就能判断能否到终点。"),
    "Jump Game II": ("输入：`nums = [2,3,1,1,4]`", "输出：`2`。最少跳两次即可到末尾。"),
    "Partition Labels": ("输入：`s = \"ababcbacadefegdehijhklij\"`", "输出：`[9,7,8]`。每段内部完整包含各字符的全部出现位置。"),
    "Climbing Stairs": ("输入：`n = 4`", "输出：`5`。到第 4 阶的方法数等于到第 3 阶和第 2 阶的方法数之和。"),
    "House Robber": ("输入：`nums = [1,2,3,1]`", "输出：`4`。最优是偷第 1 和第 3 间房。"),
    "Unique Paths": ("输入：`m = 3`, `n = 7`", "输出：`28`。每格只依赖上方和左方。"),
    "Minimum Path Sum": ("输入：`grid = [[1,3,1],[1,5,1],[4,2,1]]`", "输出：`7`。最优路径是 `1→3→1→1→1`。"),
    "Coin Change": ("输入：`coins = [1,2,5]`, `amount = 11`", "输出：`3`。最优组合是 `5 + 5 + 1`。"),
    "Word Break": ("输入：`s = \"leetcode\"`, `wordDict = [\"leet\",\"code\"]`", "输出：`True`。可以切成 `leet + code`。"),
    "Partition Equal Subset Sum": ("输入：`nums = [1,5,11,5]`", "输出：`True`。可以分成和都为 `11` 的两个子集。"),
    "Longest Common Subsequence": ("输入：`text1 = \"abcde\"`, `text2 = \"ace\"`", "输出：`3`。最长公共子序列是 `ace`。"),
    "Longest Increasing Subsequence": ("输入：`nums = [10,9,2,5,3,7,101,18]`", "输出：`4`。一个最长递增子序列是 `2,3,7,101`。"),
    "Longest Palindromic Substring": ("输入：`s = \"babad\"`", "输出：`\"bab\"` 或 `\"aba\"`。中心扩展能自然找到答案。"),
    "Maximum Product Subarray": ("输入：`nums = [2,3,-2,4]`", "输出：`6`。最大乘积来自连续子数组 `[2,3]`。"),
    "Edit Distance": ("输入：`word1 = \"horse\"`, `word2 = \"ros\"`", "输出：`3`。三步操作可完成转换。"),
    "Median of Two Sorted Arrays": ("输入：`nums1 = [1,3]`, `nums2 = [2]`", "输出：`2.0`。总长度是奇数时取左半最大值。"),
    "Find Median from Data Stream": ("操作：持续插入数字后随时查询中位数", "结果：通常用一个最大堆和一个最小堆平衡左右两半。"),
    "First Missing Positive": ("输入：`nums = [3,4,-1,1]`", "输出：`2`。原地放置后第一个不匹配的位置就是答案。"),
    "N-Queens": ("输入：`n = 4`", "输出：两种合法摆法。回溯时每层放一行并检查列与对角线。"),
    "Word Ladder": ("输入：`beginWord = \"hit\"`, `endWord = \"cog\"`", "输出：`5`。最短路径是 `hit -> hot -> dot -> dog -> cog`。"),
    "Word Search": ("输入：网格和单词 `ABCCED`", "输出：`True`。路径可以上下左右走，但同格不能重复用。"),
    "Insert Delete GetRandom O(1)": ("操作：`insert(1)`, `insert(2)`, `remove(1)`, `getRandom()`", "结果：插入、删除、随机取值都要做到均摊 `O(1)`。"),
    "Search in Sorted Array of Unknown Size": ("输入：只能通过 `reader.get(i)` 访问的有序数组", "输出：先翻倍扩边界，再在区间内二分查找目标值。"),
}


def normalize(title: str) -> str:
    aliases = {
        "Construct Binary Tree from Preorder and Inorder": "Construct Binary Tree from Preorder and Inorder",
        "Construct Binary Tree from Preorder and Inorder Traversal": "Construct Binary Tree from Preorder and Inorder",
        "Search in Sorted Array of Unknown Size": "Search in Sorted Array of Unknown Size",
        "LCA Diameter Path Sum": "Lowest Common Ancestor of a Binary Tree",
    }
    return aliases.get(title.strip(), title.strip())


def find_sections(text: str):
    best = []
    for pattern in SECTION_PATTERNS:
        matches = list(re.finditer(pattern, text, re.M))
        if len(matches) > len(best):
            best = matches
    return best


def add_helper_definitions(code: str) -> str:
    if "class Solution" not in code:
        return code
    prefix = []
    if "from typing import" not in code and ("List[" in code or "Optional[" in code):
        names = []
        if "List[" in code:
            names.append("List")
        if "Optional[" in code:
            names.append("Optional")
        prefix.append(f"from typing import {', '.join(names)}")
    if "ListNode" in code and "class ListNode" not in code:
        prefix.append(
            "class ListNode:\n"
            "    def __init__(self, val=0, next=None):\n"
            "        self.val = val\n"
            "        self.next = next\n"
        )
    if "TreeNode" in code and "class TreeNode" not in code:
        prefix.append(
            "class TreeNode:\n"
            "    def __init__(self, val=0, left=None, right=None):\n"
            "        self.val = val\n"
            "        self.left = left\n"
            "        self.right = right\n"
        )
    if not prefix:
        return code
    return "\n\n".join(prefix) + "\n\n" + code


def infer_summary(title: str, section: str) -> str:
    m = re.search(r"\*\*题型识别\*\*\s*```text\n(.*?)```", section, re.S)
    if m:
        pattern = " / ".join(x.strip() for x in m.group(1).splitlines() if x.strip())
        return f"这题最重要的不是记答案，而是识别信号。看到 `{title}` 时，优先把它归到 `{pattern}` 这类模板，再去套对应的不变量、状态定义或数据结构。"
    if "链表" in title or "List" in title:
        return f"`{title}` 主要在练链表指针操作，重点是想清楚节点之间该怎么断开、反转和接回去。"
    if "Tree" in title or "BST" in title:
        return f"`{title}` 主要在练树的递归返回值设计。做这类题时先决定遍历方式，再决定递归函数返回什么。"
    if "Window" in title or "Substring" in title:
        return f"`{title}` 属于滑动窗口类问题，关键是想清楚窗口什么时候合法、什么时候需要收缩。"
    return f"`{title}` 的核心是先识别它最像哪种经典题型，再把题目翻译成那个模板。"


def infer_case(title: str) -> tuple[str, str]:
    title = normalize(title)
    if title in CASES:
        return CASES[title]
    if "Tree" in title or "BST" in title:
        return ("输入：一棵小型二叉树样例", "输出：根据题意返回遍历结果、布尔判断或某个树上统计值。树题重点是手动画出左右子树的递归关系。")
    if "List" in title or "Linked" in title:
        return ("输入：长度较短的链表样例", "输出：按题目要求返回重排、反转、合并或判断结果。链表题建议先画指针再写代码。")
    if "Matrix" in title or "Grid" in title:
        return ("输入：一个小矩阵或网格", "输出：按题意返回路径、搜索结果或区间统计。建议先手推 2x2 或 3x3 的最小样例。")
    return ("输入：一个最小可手算的样例", "输出：先手推一遍算法流程，再对照代码中的循环、状态或数据结构变化。")


def enhance_section(title: str, section: str) -> str:
    for label in ("**Python 代码**", "**代表 Python 代码**"):
        section = re.sub(
            re.escape(label) + r"\s*```python\n(.*?)```",
            lambda m: f"{label}\n\n```python\n{add_helper_definitions(m.group(1).strip())}\n```",
            section,
            flags=re.S,
        )
    if "**这个题型 / 算法点的总结**" not in section:
        summary = infer_summary(title, section)
        if "**题目含义**" in section:
            section = section.replace("**题目含义**", f"**这个题型 / 算法点的总结**\n\n{summary}\n\n**题目含义**", 1)
    if "**示例 case**" not in section:
        case_in, case_out = infer_case(title)
        insert = f"**示例 case**\n\n- {case_in}\n- {case_out}\n\n"
        if "**常见 Follow-up**" in section:
            section = section.replace("**常见 Follow-up**", insert + "**常见 Follow-up**", 1)
        elif "**怎么想到这个方法**" in section:
            section = section + "\n\n" + insert.rstrip()
    return section


def process_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    matches = find_sections(text)
    if not matches:
        return
    out = []
    cursor = 0
    for i, m in enumerate(matches):
        title = m.group(1).strip()
        start = m.start()
        body_start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out.append(text[cursor:body_start])
        body = text[body_start:end]
        if ("**Python 代码**" in body or "**代表 Python 代码**" in body) and "**题目含义**" in body:
            out.append("\n\n" + enhance_section(title, body).strip() + "\n\n")
        else:
            out.append(body)
        cursor = end
    out.append(text[cursor:])
    path.write_text("".join(out), encoding="utf-8")


def main() -> None:
    for directory in TARGET_DIRS:
        for path in sorted(directory.glob("*.md")):
            if path.name.lower().startswith("readme") or path.name == "index.md":
                continue
            process_file(path)


if __name__ == "__main__":
    main()
