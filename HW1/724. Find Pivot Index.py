# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #self：代表類別的實例。
        #在類別的方法中，通常需要使用self來訪問或修改實例的屬性和方法。
        #List[int]是Python的類型提示（Type Hint），表示nums是一個包含整數的列表。
        #int:：這部分是函數的返回類型提示   
        total_sum = sum(nums)
        left_sum = 0
    
        # 使用enumerate函數遍歷nums列表的索引和對應的元素。
        for index, num in enumerate(nums):
            total_sum -= num
            if left_sum == total_sum:
                return index
            left_sum += num
    
        return -1

# 建立 Solution 的實例
solution = Solution()

# 呼叫 pivotIndex 方法，並傳入一個整數列表作為參數
nums = [1, 7, 3, 6, 5, 6]
result = solution.pivotIndex(nums)

# 印出結果
print(result)