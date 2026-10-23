"""611. 有效三角形的个数。

排序后固定 nums[i] 为最长边，另外两个指针都在 i 左边。
两条短边之和大于最长边时，一次计入 k - j 个组合，再缩小右指针。
本题按不同下标计数，相同边长也要保留，不做三数之和式的答案去重。
时间复杂度 O(n^2)，双指针部分额外空间 O(1)；
Python 排序最坏需要 O(n) 辅助空间。本解法会排序输入数组。

原题链接：https://leetcode.cn/problems/valid-triangle-number/
"""

from __future__ import annotations


class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)

        for i in range(2, n):
            x = nums[i]
            j = 0
            k = i - 1
            while j < k:
                if nums[j] + nums[k] > x:
                    # j 到 k - 1 的任意位置，都能与 k、i 构成三角形。
                    ans += k - j
                    k -= 1
                else:
                    j += 1

        return ans
