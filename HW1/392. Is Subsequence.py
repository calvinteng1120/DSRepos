# -*- coding: utf-8 -*-
"""
給定兩個字符串 s 和 t，如果 s 是 t 的子序列則返回 true，否則返回 false。
字符串的子序列是通過刪除一些（可以不刪除）字符而不打亂其餘字符的相對位置
而從原始字符串形成的新字符串。 （即，“ace”是“abcde”的子序列，而“aec”不是）。
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # 用來遍歷 s 的指標
        j = 0  # 用來遍歷 t 的指標
        
        while i < len(s) and j < len(t):
            print(s[i]);
            print(t[j]);
            if s[i] == t[j]:  # 如果 s[i] 和 t[j] 相等
                i += 1  # 前進到下一個字元
            j += 1  # 無論如何都要前進到 t 的下一個字元
        
        return i == len(s)  # 如果 s 中的所有字元都被找到了，就返回 True，否則返回 False

# 建立 Solution 的實例
solution = Solution()


# Example 1:
s = "abc"
t = "ahbgdc"
result = solution.isSubsequence(s, t)
print(result)  # 印出 "True"

# Example 2:
s = "axc"
t = "ahbgdc"
result = solution.isSubsequence(s, t)
print(result)  # 印出 "False"



