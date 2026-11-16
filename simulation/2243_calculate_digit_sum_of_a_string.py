"""2243. 计算字符串的数字和。

按题意模拟：每 k 个字符分为一组，逐位求和，再把各组的和转成字符串拼接。
每一轮先处理完旧字符串的所有组，再统一替换 s；长度不超过 k 时结束。
保留截图中的提前返回与 if/else 结构，长度恰好为 k 时会跳过 while。

设原始长度为 n、执行轮数为 T，每轮耗时与当前串长成正比，
时间上界为 O(1 + nT)，额外空间 O(n)。每轮长度不一定严格缩短。

详细笔记：notes/2026-11-16_calculate_digit_sum_of_a_string.md
原题链接：https://leetcode.cn/problems/calculate-digit-sum-of-a-string/
"""

from __future__ import annotations


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        n = len(s)
        if n < k:
            return s
        else:
            while len(s) > k:
                t = []
                for i in range(0, len(s), k):
                    # 切片取一组，map 逐位转成整数，sum 累加。
                    total = sum(map(int, s[i : i + k]))
                    t.append(str(total))
                # 完成本轮全部分组后，统一生成下一轮的字符串。
                s = "".join(t)
        return s
