"""116. 填充每个节点的下一个右侧节点指针。

层序遍历，将当前节点连接到队首的下一个同层节点。
时间复杂度 O(n)，额外空间 O(w)。此队列解法不满足常数空间进阶要求。
Node 由力扣提供，包含 val、left、right、next。

原题链接：https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/
"""

from __future__ import annotations

from collections import deque


class Solution:
    def connect(self, root: Node | None) -> Node | None:
        if root is None:
            return None

        q = deque([root])

        while q:
            size = len(q)

            for i in range(size):
                node = q.popleft()

                # 最后一个节点必须先单独处理，不能直接访问 q[0]。
                if i == size - 1:
                    node.next = None
                else:
                    node.next = q[0]

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root
