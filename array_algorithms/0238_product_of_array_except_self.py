"""238. 除自身以外数组的乘积。

答案等于当前位置左侧所有元素的乘积乘以右侧所有元素的乘积。
第一轮把不含当前位置的左侧乘积写入 ans，复用输出数组。
第二轮从右向左扫描，用 right 保存不含当前位置的右侧乘积；
先执行 ans[i] *= right，再执行 right *= nums[i]，以排除自身。

不建立独立的前缀积、后缀积辅助数组，仍然使用左右乘积组合的思路。
时间复杂度 O(n)，额外空间 O(1)，按题意不计输出数组 ans 的空间。
不使用除法，不修改 nums，包含零或负数时也能直接计算。

详细笔记：notes/2026-11-13_product_of_array_except_self.md
原题链接：https://leetcode.cn/problems/product-of-array-except-self/
"""

from __future__ import annotations


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [1] * n

        # ans[i] 保存下标 i 左侧所有元素的乘积，不包含 nums[i]。
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]

        right = 1
        for i in range(n - 1, -1, -1):
            # 此时 right 只包含 i 右侧的元素，先计算当前答案。
            ans[i] *= right
            # 加入当前元素，供下一轮下标 i - 1 使用。
            right *= nums[i]

        return ans
