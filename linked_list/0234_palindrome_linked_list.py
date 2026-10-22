"""234. 回文链表。

找中点并反转后半段，逐个比较节点值；判断结束后恢复原链表。
时间复杂度 O(n)，额外空间 O(1)。不相等时先退出比较，再恢复连接。
ListNode 由力扣提供，包含 val、next。

原题链接：https://leetcode.cn/problems/palindrome-linked-list/
"""

from __future__ import annotations


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        mid = self.middleNode(head)
        second_head = self.reverseList(mid)
        p1, p2 = head, second_head
        result = True

        while p2:
            if p1.val != p2.val:
                result = False
                break
            p1 = p1.next
            p2 = p2.next

        # second_head 保留反转起点；不能用已经移动过的 p2 来恢复。
        self.reverseList(second_head)
        return result

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
