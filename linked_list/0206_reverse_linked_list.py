"""206. 反转链表。

先保存原来的下一个节点，再把当前节点接到已经反转的部分前面。
时间复杂度 O(n)，额外空间 O(1)。
ListNode 由力扣提供，包含 val、next。

原题链接：https://leetcode.cn/problems/reverse-linked-list/
"""

from __future__ import annotations


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        pre = None
        cur = head

        while cur:
            nxt = cur.next  # 修改连接之前，先保存后续链表。
            cur.next = pre  # 指向前一个节点，不能指向 cur 自己。
            pre = cur
            cur = nxt      # 沿原来的链表前进，不能写成 cur = pre。

        return pre
