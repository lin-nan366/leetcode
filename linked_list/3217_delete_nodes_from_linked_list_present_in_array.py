"""3217. 从链表中移除在数组中存在的节点。

先将 nums 转成集合，再遍历一次链表；集合成员查询平均 O(1)。
平均时间复杂度 O(m + n)，额外空间 O(m)，m 为数组长度，n 为节点数。
不能直接用列表做每次成员查询，否则最坏时间仍为 O(m * n)。
ListNode 由力扣提供，包含 val、next。

原题链接：https://leetcode.cn/problems/delete-nodes-from-linked-list-present-in-array/
"""

from __future__ import annotations


class Solution:
    def modifiedList(self, nums: list[int], head: ListNode | None) -> ListNode | None:
        to_remove = set(nums)  # 集合只创建一次，必须放在遍历循环外。
        dummy = ListNode(next=head)
        cur = dummy

        while cur.next:
            if cur.next.val in to_remove:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next
