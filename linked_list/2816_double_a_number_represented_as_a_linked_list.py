"""2816. 翻倍以链表形式表示的数字。

沿用反转链表的思路，从个位开始乘 2 并处理进位，再反转结果。
时间复杂度 O(n)；新结果链表占 O(n) 空间，其余额外空间 O(1)。
本解法会修改输入链表的连接；结果使用新建节点。
ListNode 由力扣提供，包含 val、next。

原题链接：https://leetcode.cn/problems/double-a-number-represented-as-a-linked-list/
"""

from __future__ import annotations


class Solution:
    def doubleIt(self, head: ListNode | None) -> ListNode | None:
        cur = self.reverseList(head)
        dummy = ListNode()
        tail = dummy
        carry = 0

        while cur or carry:
            # cur 可能已经为空，但仍有最后一个进位需要写入。
            x = cur.val * 2 if cur else 0
            total = x + carry
            digit = total % 10
            carry = total // 10

            tail.next = ListNode(digit)
            tail = tail.next
            if cur:
                cur = cur.next

        # dummy 保存结果入口，不能从已经移到末尾的 tail 开始反转。
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
