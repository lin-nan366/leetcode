"""15. 三数之和。

排序后固定第一个数，在右侧用相向双指针寻找和为 0 的组合。
找到答案后移动两个指针，并跳过重复值；固定的第一个数也要去重。
时间复杂度 O(n^2)，双指针部分额外空间 O(1)，不含答案；
Python 排序最坏需要 O(n) 辅助空间。本解法会排序输入数组。

原题链接：https://leetcode.cn/problems/3sum/
"""

from __future__ import annotations


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n - 2):
            x = nums[i]
            if i > 0 and x == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1
            while j < k:
                s = x + nums[j] + nums[k]
                if s == 0:
                    ans.append([x, nums[j], nums[k]])
                    # 找到答案也必须前进，否则会无限追加同一个组合。
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1

        return ans
