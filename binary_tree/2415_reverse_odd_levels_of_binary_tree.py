"""2415. 反转二叉树的奇数层。

每层开始时，交换奇数层左右对称节点的值，再收集下一层。
时间复杂度 O(n)，额外空间 O(w)。
TreeNode 由力扣提供，包含 val、left、right。题目给定完美二叉树。

原题链接：https://leetcode.cn/problems/reverse-odd-levels-of-binary-tree/
"""

from __future__ import annotations

from collections import deque


class Solution:
    def reverseOddLevels(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None

        q = deque([root])
        depth = 0

        while q:
            # 此时 q 中只有当前层的节点，每层只交换一次。
            if depth % 2 == 1:
                # 列表中仍是原节点的引用，下标访问为 O(1)。
                nodes = list(q)
                size = len(nodes)

                for i in range(size // 2):
                    j = size - 1 - i
                    nodes[i].val, nodes[j].val = (
                        nodes[j].val,
                        nodes[i].val,
                    )

            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            depth += 1

        return root
