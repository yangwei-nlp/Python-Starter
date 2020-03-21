# -*- coding: utf-8 -*-
"""
Description :   
     Author :   Yang
       Date :   2020/3/21
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        """动态规划：每个字符的最长子串取决于：
        1.该字符和前面所有字符组合得到最长子串
        2.不含该字符的前面最长子串
        1,2比较得到最长子串
        """
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        def get_len(s, i):
            longest_str = ""
            for j in range(i - 1, -1, -1):
                if j < 0 or s[i] in longest_str:
                    return len(longest_str) + 1
                else:
                    longest_str += s[j]

        length = 1
        for i in range(1, len(s)):
            # get_len，得到i字符前面
            length = max(length, get_len(s, i))  # 保存当前步的最大长度

        return length

# "abcabcbb"
