"""24. 两两交换链表中的节点。

每轮把 node0 -> node1 -> node2 -> node3
改成 node0 -> node2 -> node1 -> node3，再移动到下一组。
时间复杂度 O(n)，额外空间 O(1)。
ListNode 由力扣提供，包含 val、next；只交换节点，不修改节点值。

原题链接：https://leetcode.cn/problems/swap-nodes-in-pairs/
"""

from __future__ import annotations


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        node0 = dummy  # 当前这一组前面的节点。
        node1 = head   # 当前这一组的第一个节点。

        while node1 and node1.next:  # 至少还剩两个节点才能交换。
            node2 = node1.next
            node3 = node2.next      # 提前保存后续链表。

            node0.next = node2
            node2.next = node1
            node1.next = node3

            # 变量名表示当前角色，不是固定的节点编号。
            node0 = node1
            node1 = node3

        return dummy.next
