# coding=utf-8
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t) or set(s) != set(t):
            return False
        num_s = {}
        for char in s:
            if char in num_s:
                num_s[char] += 1
            else:
                num_s[char] = 1
        num_t = {}
        for char in t:
            if char in num_t:
                num_t[char] += 1
            else:
                num_t[char] = 1
        if num_s == num_t:
            return True
        else:
            return False
        # 妈的，发现有s.count()这个函数，你再好好想想吧
s = "anagram"
t = "nagaram"

solver = Solution()
print solver.isAnagram(s, t)