class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 很简单的题目，采用双指针就可以实现，复杂度o(n)
        if len(s) == 0:
            return True
        elif len(t) == 0:
            return False
        i = 0
        j = 0
        while j <= len(t)-1:
            if t[j] == s[i]:
                i += 1
                if i == len(s):
                    return True
            j += 1
        return False