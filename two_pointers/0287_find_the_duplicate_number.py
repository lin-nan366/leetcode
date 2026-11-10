"""287. 寻找重复数。

把下标 i 看作节点，nums[i] 看作下一个节点编号。长度为 n + 1，
数值范围为 [1, n]，所以跳转始终合法，且没有任何节点指向起点 0。
从 0 出发必然先经过一段路径再进入环；入口同时被环外和环内的
两个不同节点指向，因此入口编号就是重复数字。

第一阶段快慢指针分别走一步、两步，找到环内相遇点。
第二阶段把一个指针放回 0，两个都改为每次走一步，再次相遇即为入口。
返回入口编号本身。时间复杂度 O(n)，额外空间 O(1)，不修改输入数组。

详细笔记：notes/2026-11-10_find_the_duplicate_number.md
原题链接：https://leetcode.cn/problems/find-the-duplicate-number/
"""

from __future__ import annotations


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = fast = 0

        # 先移动再比较，避免把初始的 0 == 0 当作环内相遇。
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # 一个回到起点，一个留在相遇点；之后两者都每次走一步。
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
