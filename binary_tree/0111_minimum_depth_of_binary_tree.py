"""111. 二叉树的最小深度。

层序遍历，第一次遇到叶子节点时，当前层数就是最小深度。
最坏时间复杂度 O(n)，额外空间 O(w)。
TreeNode 由力扣提供，包含 val、left、right。

原题链接：https://leetcode.cn/problems/minimum-depth-of-binary-tree/
"""

from __future__ import annotations

from collections import deque


class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        q = deque([root])
        depth = 1

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                # 左右孩子都不存在，才是叶子节点。
                if node.left is None and node.right is None:
                    return depth

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            depth += 1
