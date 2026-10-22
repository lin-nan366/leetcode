"""876. 链表的中间结点。

慢指针每轮走一步，快指针每轮走两步；快指针到末尾时返回慢指针。
偶数长度返回第二个中间节点。时间复杂度 O(n)，额外空间 O(1)。
ListNode 由力扣提供，包含 val、next。

原题链接：https://leetcode.cn/problems/middle-of-the-linked-list/
"""

from __future__ import annotations


class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
