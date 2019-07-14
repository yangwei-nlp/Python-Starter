class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        count = 0
        kids = sorted(g)
        cookies = sorted(s)

        for sj in cookies:
            judge = [True if gi <= sj else False for gi in kids]
            if True in judge:
                del kids[judge.index(True)]
                count += 1
        return count

# 本题的思路简单，但是如何用python实现却是考验基本功的一件事情

class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        len1 = len(g)
        len2 = len(s)
        i = 0
        j = 0
        num = 0
        while i < len1 and j < len2:
            if g[i] <= s[j]:
                num += 1
                i += 1
            j += 1
        return num
