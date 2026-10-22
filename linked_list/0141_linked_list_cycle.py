"""141. 环形链表。

慢指针每轮走一步，快指针每轮走两步；移动后相遇，说明存在环。
时间复杂度 O(n)，额外空间 O(1)，不修改链表连接。
ListNode 由力扣提供；is 比较节点身份，不比较节点值。

原题链接：https://leetcode.cn/problems/linked-list-cycle/
"""

from __future__ import annotations


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 初始化时两者就相同，必须先移动再判断。
            if slow is fast:
                return True
        return False
