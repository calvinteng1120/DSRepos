# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 16:22:58 2023

@author: wistronits
"""
nums = [1,2,3,4]
ans = []
prev = 0

for num in nums:
    #prev = prev + num
    prev += num
    ans.append(prev)
print(ans)
