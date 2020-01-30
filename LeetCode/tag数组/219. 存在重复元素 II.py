# -*- coding: utf-8 -*-
"""
Description :   
     Author :   Yang
       Date :   2020/1/15
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        num_index = {}
        for i, num in enumerate(nums):
            if num in num_index:
                if i - num_index[num] <= k:
                    return True
                else:
                    num_index[num] = i  # 需要将索引更新到最近位置
            else:
                num_index[num] = i
        return False



nums = [1, 2, 3, 1]
k = 3
s = Solution()
print(s.containsNearbyDuplicate(nums, k))
