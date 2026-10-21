"""92. 反转链表 II。

找到第 left 个节点的前驱，只反转 [left, right] 区间，再接回两端。
时间复杂度 O(n)，额外空间 O(1)。
ListNode 由力扣提供；题目保证 1 <= left <= right <= 链表长度。

原题链接：https://leetcode.cn/problems/reverse-linked-list-ii/
"""

from __future__ import annotations


class Solution:
    def reverseBetween(
        self, head: ListNode | None, left: int, right: int
    ) -> ListNode | None:
        if left == right:
            return head

        dummy = ListNode(0, head)
        p0 = dummy
        for _ in range(left - 1):
            p0 = p0.next

        old_head = p0.next  # 区间的旧头，反转后成为区间的尾节点。
        pre = None
        cur = old_head

        # 左右端点都包含在内，一共反转 right - left + 1 个节点。
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        old_head.next = cur  # 区间的新尾接到后续链表。
        p0.next = pre        # 区间前驱接到区间的新头。
        return dummy.next
