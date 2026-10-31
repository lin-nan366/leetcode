"""80. Remove Duplicates from Sorted Array II.

Category: Two pointers (read/write) with an implicit stack.
The retained prefix acts as a stack. stack_size is both its length and the
next write position, while i scans the remaining elements from left to right.
The first two elements can always be retained. For each later element,
compare it with nums[stack_size - 2], the second-to-last retained element.
Because nums is sorted, equality means two copies are already retained;
otherwise, copy the current element into the prefix and advance stack_size.
The write position never exceeds the read position, preserving unread values.

Only the prefix up to the returned length matters; the suffix is ignored.
The final min handles arrays shorter than two elements.
Time: O(n). Extra space: O(1); no separate stack or array is allocated.
Modifies nums in place and returns the retained length.

Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"""

from __future__ import annotations


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        stack_size = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[stack_size - 2]:
                nums[stack_size] = nums[i]
                stack_size += 1
        return min(stack_size, len(nums))
