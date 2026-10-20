"""117. 填充每个节点的下一个右侧节点指针 II。

沿当前层已连接好的 next 遍历，用 dummy 和 tail 串起下一层。
时间复杂度 O(n)，额外空间 O(1)。
Node 由力扣提供，包含 val、left、right、next；next 初始为 None。

原题链接：https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/
"""

from __future__ import annotations


class Solution:
    def connect(self, root: Node | None) -> Node | None:
        if root is None:
            return None

        cur = root

        while cur:
            # dummy.next 记录下一层的起点，tail 记录已连接部分的末尾。
            dummy = Node(0)
            tail = dummy

            while cur:
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next

                if cur.right:
                    tail.next = cur.right
                    tail = tail.next

                cur = cur.next

            tail.next = None
            cur = dummy.next

        return root
