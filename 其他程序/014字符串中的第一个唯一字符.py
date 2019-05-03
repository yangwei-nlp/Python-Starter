# coding=utf-8
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(str(s)) == 0:
            return -1
        count = {}
        for i in range(len(s)):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
        flag = -1
        number = []
        for char, num in count.items():
            if num == 1:
                number.append(s.index(char))
        if len(number) > 0:
            ret = min(number)
        else:
            ret = -1
        if ret >= 0:
            return ret
        else:
            return flag

solver = Solution()
print solver.firstUniqChar("cc")
