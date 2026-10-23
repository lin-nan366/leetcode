"""125. 验证回文串。

用 isalnum() 保留字母和数字，用 lower() 转为小写，再从两端比较。
isalnum() 只返回判断结果，真正的过滤由 if 完成；过滤后为空也是回文串。
时间复杂度 O(n)，额外空间 O(n)，用于保存清理后的字符串。

原题链接：https://leetcode.cn/problems/valid-palindrome/
"""

from __future__ import annotations


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
        left = 0
        right = len(cleaned) - 1

        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1

        return True
