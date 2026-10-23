"""42. 接雨水。

维护从左侧、右侧扫描到的最高柱子，每轮结算较小最大值一侧的一列雨水。
另一侧已经存在足够高的边界，因此这一列的水面高度已经确定。
时间复杂度 O(n)，额外空间 O(1)，不修改输入数组。

原题链接：https://leetcode.cn/problems/trapping-rain-water/
"""

from __future__ import annotations


class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        pre_max = 0
        suf_max = 0
        ans = 0

        while left < right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if suf_max < pre_max:
                ans += suf_max - height[right]
                right -= 1
            else:
                # 每次只累加 left 或 right 这一列上方的全部雨水。
                ans += pre_max - height[left]
                left += 1

        return ans
