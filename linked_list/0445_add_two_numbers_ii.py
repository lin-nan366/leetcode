"""445. 两数相加 II。

反转两个输入链表，从个位开始相加，最后把结果链表反转回来。
时间复杂度 O(m + n)，除结果链表外额外空间 O(1)。
结果链表空间 O(max(m, n))，m、n 分别为两个输入链表的长度。
本解法会修改输入链表的连接；不反转输入的进阶要求可使用两个栈。
ListNode 由力扣提供，包含 val、next。

原题链接：https://leetcode.cn/problems/add-two-numbers-ii/
"""

from __future__ import annotations


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        # l1、l2 本身就是头节点，不需要访问 .head。
        p1 = self.reverseList(l1)
        p2 = self.reverseList(l2)

        dummy = ListNode()
        tail = dummy
        carry = 0

        # 输入结束后，如果还有进位，也要继续生成一个节点。
        while p1 or p2 or carry:
            x = p1.val if p1 else 0
            y = p2.val if p2 else 0
            total = x + y + carry  # 加上上一轮留下的进位。
            digit = total % 10
            carry = total // 10   # 新进位留给下一轮。

            tail.next = ListNode(digit)
            tail = tail.next      # 移动尾指针，避免覆盖已有结果。

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        return self.reverseList(dummy.next)

    def reverseList(self, head: ListNode | None) -> ListNode | None:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
