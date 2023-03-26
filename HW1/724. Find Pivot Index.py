# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 20:18:04 2023

@author: wistronits
"""

def find_pivot_index(nums):
    total_sum = sum(nums)
    left_sum = 0

    for index, num in enumerate(nums):
        total_sum -= num
        if left_sum == total_sum:
            return index
        left_sum += num

    return -1

# Example usage:
nums1 = [1, 7, 3, 6, 5, 6]
result1 = find_pivot_index(nums1)
print(result1)

nums2 = [1, 2, 3]
result2 = find_pivot_index(nums2)
print(result2)

nums3 = [2, 1, -1]
result3 = find_pivot_index(nums3)
print(result3)
