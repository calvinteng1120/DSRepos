# -*- coding: utf-8 -*-
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):  # 長度不同必定不同構
            return False
        
        s_map = {}  # s 中每個字元對應到 t 中的字元的 mapping
        t_set = set()  # t 中出現過的字元集合
        
        for i in range(len(s)):
            if s[i] in s_map:  # 如果 s[i] 已經對應到某個字元
                if s_map[s[i]] != t[i]:  # 檢查對應的字元是否相同
                    return False
            else:  # 如果 s[i] 尚未對應到任何字元
                if t[i] in t_set:  # 檢查 t[i] 是否已經被映射過
                    return False
                s_map[s[i]] = t[i]  # 建立 s[i] 對應到 t[i] 的 mapping
                t_set.add(t[i])  # 將 t[i] 加入 t_set 中
        
        return True

# 建立 Solution 的實例
solution = Solution()

# Example 1:
s = "egg"
t = "add"
result = solution.isIsomorphic(s, t)
print(result)  # 印出 "True"

# Example 2:
s = "foo"
t = "bar"
result = solution.isIsomorphic(s, t)
print(result)  # 印出 "False"

# Example 3:
s = "paper"
t = "title"
result = solution.isIsomorphic(s, t)
print(result)  # 印出 "True"

