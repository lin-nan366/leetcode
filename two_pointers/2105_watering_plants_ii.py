"""2105. 给植物浇水 II。

两人分别从两端浇水，每轮都完成当前植物；水不足时先补满，再立即浇水。
剩下中间一株时，由剩余水更多的人处理，只在两人都不够时增加一次补水。
时间复杂度 O(n)，额外空间 O(1)，不修改输入数组。

原题链接：https://leetcode.cn/problems/watering-plants-ii/
"""

from __future__ import annotations


class Solution:
    def minimumRefill(
        self, plants: list[int], capacityA: int, capacityB: int
    ) -> int:
        left = 0
        right = len(plants) - 1
        ans = 0
        pre_A = capacityA
        pre_B = capacityB

        while left < right:
            if capacityA < plants[left]:
                capacityA = pre_A
                ans += 1
            # 是否补水都要完成浇水与前进，不能留到下一轮。
            capacityA -= plants[left]
            left += 1

            if capacityB < plants[right]:
                capacityB = pre_B
                ans += 1
            capacityB -= plants[right]
            right -= 1

        if left == right and max(capacityA, capacityB) < plants[left]:
            ans += 1

        return ans
