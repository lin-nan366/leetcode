"""27. Remove Element.

Category: Array traversal and sorting with a sentinel value.
Replace every occurrence of val with positive infinity and count the other
elements. Sort nums so the retained integers occupy the first count positions.
Only that prefix matters to the judge; the suffix may contain infinities.
The input contains finite integers, so infinity sorts after every valid value.

Time: O(n log n) in the worst case.
Extra space: O(n) for Python's sorting workspace.
Modifies nums in place and returns the number of retained elements.

Problem: https://leetcode.com/problems/remove-element/
"""

from __future__ import annotations

from math import inf


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        ans = 0
        for i, x in enumerate(nums):
            if x == val:
                nums[i] = inf
            else:
                ans += 1
        nums.sort()
        return ans
