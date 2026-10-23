"""16. 最接近的三数之和。

排序后固定一个数，另外两个数用相向双指针搜索。
res 保存最小绝对差，ans 保存对应的三数之和；和偏大移右指针，偏小移左指针。
时间复杂度 O(n^2)，双指针部分额外空间 O(1)；
Python 排序最坏需要 O(n) 辅助空间。本解法会排序输入数组。

原题链接：https://leetcode.cn/problems/3sum-closest/
"""

from __future__ import annotations


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        res = float("inf")

        for i in range(n - 2):
            x = nums[i]
            j = i + 1
            k = n - 1
            while j < k:
                s = x + nums[j] + nums[k]
                if s == target:
                    return s

                # 当前距离更小时，同时更新距离与答案。
                if abs(s - target) < res:
                    res = abs(s - target)
                    ans = s

                if s > target:
                    k -= 1
                else:
                    j += 1

        # 需要尝试所有固定位置，不能把返回写进 for 循环。
        return ans
