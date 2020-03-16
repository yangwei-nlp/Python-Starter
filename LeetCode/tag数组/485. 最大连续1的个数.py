# -*- coding: utf-8 -*-
"""
Description :   
     Author :   Yang
       Date :   2020/2/1
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_len = 0
        temp_len = 0
        for num in nums:
            if num == 1:
                temp_len += 1
            else:
                if temp_len > max_len:
                    max_len = temp_len
                temp_len = 0  # 注意，如果当前数是0，需要将当前计数重置为0
        return max(max_len, temp_len)
