# -*- coding: utf-8 -*-
"""
Description :   
     Author :   Yang
       Date :   2020/4/6
"""
class Solution:
    def romanToInt(self, s):
        num_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)-1):
            if num_dict[s[i]] > num_dict[s[i+1]]:
                result += num_dict[s[i]]
            else:
                result -= num_dict[s[i]]
        return result + num_dict[s[-1]]


s = Solution()
print(s.romanToInt('IV'))