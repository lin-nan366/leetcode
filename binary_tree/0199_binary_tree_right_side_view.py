"""199. 二叉树的右视图。

从左到右进行层序遍历，记录每层最后一个节点的值。
时间复杂度 O(n)，额外空间 O(w)，不计返回结果。
TreeNode 由力扣提供，包含 val、left、right。

原题链接：https://leetcode.cn/problems/binary-tree-right-side-view/
"""

from __future__ import annotations

from collections import deque


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        q = deque([root])
        ans = []

        while q:
            size = len(q)

            for i in range(size):
                node = q.popleft()

                # range(size) 的最后一个下标是 size - 1。
                if i == size - 1:
                    ans.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return ans
