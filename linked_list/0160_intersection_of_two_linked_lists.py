"""160. 相交链表。

双指针分别从两条链表出发，到 None 后切换到另一条链表的头节点。
通过交换遍历顺序抵消长度差：相交时在公共部分起点相遇，否则同时为 None。
使用 is 比较节点身份，不能只比较 val；只移动变量，不修改 next。
时间复杂度 O(m + n)，额外空间 O(1)，m、n 为两条链表的长度。
ListNode 由力扣提供，题目保证两条链表无环。

原题链接：https://leetcode.cn/problems/intersection-of-two-linked-lists/
"""

from __future__ import annotations


class Solution:
    def getIntersectionNode(
        self, headA: ListNode | None, headB: ListNode | None
    ) -> ListNode | None:
        p = headA
        q = headB

        while q is not p:
            q = q.next if q else headA
            p = p.next if p else headB

        return q
