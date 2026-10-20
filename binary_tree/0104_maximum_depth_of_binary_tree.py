"""104. 二叉树的最大深度。

层序遍历，每处理完一层，深度加一。
时间复杂度 O(n)，额外空间 O(w)，w 为树的最大层宽。
TreeNode 由力扣提供，包含 val、left、right。

原题链接：https://leetcode.cn/problems/maximum-depth-of-binary-tree/
"""

from __future__ import annotations

from collections import deque


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        q = deque([root])
        depth = 0

        while q:
            # range(len(q)) 固定本层的节点数量。
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            depth += 1

        return depth
