"""2583. 二叉树中的第 K 大层和。

层序遍历收集每层的和，遍历全部结束后降序排序一次。
时间复杂度 O(n + h log h)，额外空间 O(w + h)，h 为层数。
TreeNode 由力扣提供，包含 val、left、right。

原题链接：https://leetcode.cn/problems/kth-largest-sum-in-a-binary-tree/
"""

from __future__ import annotations

from collections import deque


class Solution:
    def kthLargestLevelSum(self, root: TreeNode | None, k: int) -> int:
        if root is None:
            return -1

        q = deque([root])
        level_sums = []

        while q:
            level_sum = 0

            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level_sums.append(level_sum)

        if k > len(level_sums):
            return -1

        # 排序放在 while 外面；相同的层和也要保留。
        level_sums.sort(reverse=True)
        return level_sums[k - 1]
