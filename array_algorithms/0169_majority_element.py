"""169. Majority Element.

Category: Array sorting and median selection.
Sort nums and return the element at the lower middle index, (n - 1) // 2.
A strict majority occupies more than half of the sorted array, so its
contiguous block must cover this index for both odd and even lengths.
The problem guarantees a nonempty array and an existing majority element.

Time: O(n log n) in the worst case, dominated by sorting.
Extra space: O(n) for Python's sorting workspace.
Computing the middle index and accessing the element each take O(1) time.
This solution sorts the input array in place.

Problem: https://leetcode.com/problems/majority-element/
"""

from __future__ import annotations


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        nums.sort()
        mid = (left + right) // 2
        return nums[mid]
