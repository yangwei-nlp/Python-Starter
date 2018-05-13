# coding=utf-8
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

s = "hello"
solver = Solution()
print solver.reverseString(s)
