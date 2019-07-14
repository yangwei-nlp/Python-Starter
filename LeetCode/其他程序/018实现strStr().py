# coding=utf-8
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        return haystack.find(needle)

solver = Solution()
print solver.strStr(haystack = "hello", needle = "ll")