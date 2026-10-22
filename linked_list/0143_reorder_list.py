"""143. 重排链表。

找中点，反转后半段，再将后半段的节点交替插到前面的节点后面。
本写法两段共享原中间节点；用 while head2.next 跳过最后的共享节点。
时间复杂度 O(n)，额外空间 O(1)。原地修改，返回 None。
ListNode 由力扣提供，包含 val、next。

原题链接：https://leetcode.cn/problems/reorder-list/
"""

from __future__ import annotations


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        if head is None:
            return

        mid = self.middleNode(head)
        head2 = self.reverseList(mid)
        while head2.next:
            nxt = head.next
            nxt2 = head2.next

            head.next = head2
            head2.next = nxt

            head = nxt
            head2 = nxt2

    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: ListNode | None) -> ListNode | None:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
