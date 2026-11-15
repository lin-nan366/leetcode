"""1524. 和为奇数的子数组数目。

前缀和之差是子数组和；差为奇数，当且仅当两个前缀和奇偶性不同。
sums[i] 只保存前 i 个元素之和的奇偶性，0 为偶数，1 为奇数。
按下标顺序扫描，cnt[0]、cnt[1] 记录此前两类前缀的数量；
当前奇偶性为 s 时，新增的奇数和子数组数量为 cnt[s ^ 1]。

保留截图中的前缀数组写法。sums 包含空前缀 0，所以 cnt 从 [0, 0]
开始，遍历空前缀时自然把偶数前缀数量加一。时间 O(n)，额外空间 O(n)。
不修改输入数组，结果对 1_000_000_007 取模。

详细笔记：notes/2026-11-15_number_of_sub_arrays_with_odd_sum.md
原题链接：https://leetcode.cn/problems/number-of-sub-arrays-with-odd-sum/
"""

from __future__ import annotations


class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        sums = [0] * (len(arr) + 1)
        for i, x in enumerate(arr):
            sums[i + 1] = (sums[i] + x) % 2

        # 两个桶分别记录此前偶数、奇数前缀的数量。
        cnt = [0] * 2
        ans = 0
        for s in sums:
            # s 只有 0、1，异或 1 得到相反的奇偶性。
            ans += cnt[s ^ 1]
            cnt[s] += 1

        return ans % 1_000_000_007
