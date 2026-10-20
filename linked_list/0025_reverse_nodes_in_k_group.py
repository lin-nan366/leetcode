"""25. K 个一组翻转链表。

先统计长度，只翻转节点数量达到 k 的完整分组。
每组内部反转后，再连接新尾、连接新头、移动组前驱。
时间复杂度 O(n)，额外空间 O(1)。
ListNode 由力扣提供，包含 val、next；题目保证 k >= 1。

原题链接：https://leetcode.cn/problems/reverse-nodes-in-k-group/
"""

from __future__ import annotations


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        dummy = ListNode(0, head)
        p0 = dummy
        cur = head

        while n >= k:
            n -= k
            # 每组独立反转，避免临时连接回已经处理过的部分。
            pre = None

            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            # pre：本组的新头；cur：下一组的起点。
            old_head = p0.next
            old_head.next = cur
            p0.next = pre
            p0 = old_head

        return dummy.next
