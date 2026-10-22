"""2130. 链表最大孪生和。

反转后半段，将前面的节点与原来倒数的节点逐对相加，记录最大值。
题目保证节点数为不小于 2 的偶数；第二个指针先走到 None 时停止。
时间复杂度 O(n)，额外空间 O(1)。本解法会修改输入链表的连接。
ListNode 由力扣提供，包含 val、next。

原题链接：https://leetcode.cn/problems/maximum-twin-sum-of-a-linked-list/
"""

from __future__ import annotations


class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        mid = self.middleNode(head)
        head2 = self.reverseList(mid)
        ans = head.val + head2.val

        while head2:
            ans = max(ans, head.val + head2.val)
            head = head.next
            head2 = head2.next

        return ans

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
