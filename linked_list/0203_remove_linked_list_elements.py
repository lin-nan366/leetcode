"""203. 移除链表元素。

使用哨兵统一处理头节点删除，始终检查 cur.next 是否需要删除。
删除时 cur 不移动，保留节点时才向后移动，避免漏掉连续目标节点。
时间复杂度 O(n)，额外空间 O(1)。
ListNode 由力扣提供，包含 val、next。

原题链接：https://leetcode.cn/problems/remove-linked-list-elements/
"""

from __future__ import annotations


class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        dummy = ListNode(next=head)
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
