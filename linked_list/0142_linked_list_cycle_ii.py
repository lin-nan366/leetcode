"""142. 环形链表 II。

快慢指针先在环内相遇，再从链表头和相遇点分别每轮走一步。
第二次相遇的节点就是环入口，第一次相遇的位置不一定是入口。
时间复杂度 O(n)，额外空间 O(1)，不修改链表连接。
ListNode 由力扣提供，包含 val、next。

原题链接：https://leetcode.cn/problems/linked-list-cycle-ii/
"""

from __future__ import annotations


class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                p = head
                while p is not slow:
                    p = p.next
                    slow = slow.next
                return p
        return None
