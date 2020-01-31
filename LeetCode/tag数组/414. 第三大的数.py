# -*- coding: utf-8 -*-
"""
Description :   
     Author :   Yang
       Date :   2020/1/31
"""
class Solution:
    def thirdMax(self, nums):
        ret = [float('-inf')] * 3
        for num in nums:
            if num in ret:
                continue
            if num > ret[0]:
                # 从大到小判断能够准确确定位置
                ret = [num, ret[0], ret[1]]
            elif num > ret[1]:
                ret = [ret[0], num, ret[1]]
            elif num > ret[2]:
                ret = [ret[0], ret[1], num]
        return ret[-1] if ret[-1] != float('-inf') else ret[0]



s = Solution()
print(s.thirdMax([3,2,1,4,1,54,2]))
