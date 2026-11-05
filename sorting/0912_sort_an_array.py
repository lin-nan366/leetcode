"""912. 排序数组：随机三路快速排序。

随机选择基准值 pivot，将当前区间划分为小于、等于和大于 pivot 的三段。
等于 pivot 的部分无需继续处理，只递归排序左右两段。
大于 pivot 时，从右侧交换过来的元素还没有检查，因此 i 不前进。

时间复杂度：平均 O(n log n)，最坏 O(n²)。
额外空间：递归栈平均 O(log n)，最坏 O(n)。
直接修改输入数组，并返回同一个数组；不使用内置排序函数。

原题：https://leetcode.cn/problems/sort-an-array/
"""

from __future__ import annotations

from random import randint


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def quick_sort(left: int, right: int) -> None:
            if left >= right:
                return

            # 随机选择基准值。
            pivot = nums[randint(left, right)]
            lt, i, gt = left, left, right

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                    # 换过来的数还没检查，所以 i 不动。
                else:
                    i += 1

            # 三段依次为：小于、等于、大于 pivot。
            # 等于的部分无需再处理，只递归左右两段。
            quick_sort(left, lt - 1)
            quick_sort(gt + 1, right)

        quick_sort(0, len(nums) - 1)
        return nums
