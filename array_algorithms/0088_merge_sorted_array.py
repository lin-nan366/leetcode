"""88. Merge Sorted Array.

Category: Array traversal and sorting.
Copy nums2 into the reserved positions of nums1, then sort nums1 in place.
Only the first m positions of nums1 contain valid input elements; zero can
also be a valid value, so identify reserved positions by index, not value.
Use enumerate to obtain both an index and a value while traversing a list.

General sorting bound: O(k log k) time, where k = m + n.
Python's sort may use O(k) temporary space.
Modifies nums1 in place, leaves nums2 unchanged, and returns None.

Problem: https://leetcode.com/problems/merge-sorted-array/
"""

from __future__ import annotations


class Solution:
    def merge(
        self, nums1: list[int], m: int, nums2: list[int], n: int
    ) -> None:
        n = len(nums2)
        index = 0
        for i, x in enumerate(nums1):
            if i >= m:
                nums1[i] = nums2[index]
                index += 1
        nums1.sort()
