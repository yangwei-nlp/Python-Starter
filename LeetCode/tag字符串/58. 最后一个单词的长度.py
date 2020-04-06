# -*- coding: utf-8 -*-
"""
Description :   
     Author :   Yang
       Date :   2020/4/6
"""
class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()  # 变态的情况要处理
        if s == '':
            return 0
        length = 0
        for i in range(len(s)-1, -2, -1):
            if i >= 0 and s[i] != ' ':
                length += 1
            else:
                return length


s = Solution()
print(s.lengthOfLastWord("a "))
print(s.lengthOfLastWord("a asdfa"))