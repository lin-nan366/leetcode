"""2535. Difference Between Element Sum and Digit Sum of an Array.

Category: Math, array traversal, and simulation with digit extraction.
Accumulate each element, then use x % 10 to extract its last digit and
x //= 10 to remove that digit. Return the absolute difference of the sums.
Reassigning x does not modify the input array.

Time: O(n * d), where d is the maximum number of decimal digits per element.
Under the problem constraint nums[i] <= 2000, d <= 4, so time is O(n).
Extra space: O(1).

Problem: https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/
"""

from __future__ import annotations


class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        ans = 0
        res = 0
        for x in nums:
            ans += x
            while x:
                res += x % 10
                x //= 10
        return abs(ans - res)
