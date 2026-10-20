"""1609. 奇偶树。

边层序遍历边检查：偶数下标层为奇数且严格递增；
奇数下标层为偶数且严格递减。根节点的层下标是 0。
时间复杂度 O(n)，额外空间 O(w)。
TreeNode 由力扣提供，包含 val、left、right。题目保证树非空。

原题链接：https://leetcode.cn/problems/even-odd-tree/
"""

from __future__ import annotations

from collections import deque


class Solution:
    def isEvenOddTree(self, root: TreeNode | None) -> bool:
        if root is None:
            return False

        q = deque([root])
        depth = 0

        while q:
            # 每层重新开始比较，第一个节点没有前驱值。
            previous = None
            even_level = depth % 2 == 0

            for _ in range(len(q)):
                node = q.popleft()
                value = node.val

                # 每个节点都检查奇偶性，单节点层也不会漏检。
                if even_level:
                    if value % 2 == 0:
                        return False
                    if previous is not None and value <= previous:
                        return False
                else:
                    if value % 2 != 0:
                        return False
                    if previous is not None and value >= previous:
                        return False

                previous = value

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            depth += 1

        # 所有层都通过检查后，才返回 True。
        return True
