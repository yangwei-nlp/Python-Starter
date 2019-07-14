class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 思路:f(i,j)表示当s[i:j]子串是否是回文串(值为1或0)。当j-i<=1时，如果s[i] == s[j]则
        # 表示s[i:j]为回文串，及f(i,j) = true，否则f(i,j) = false。当j-i > 1时，则判断
        # s[i]、s[j]是否相等以及f(i+1, j-1)是否为true，即s[i+1:j-1]是否为回文串，如果为真，则
        # f(i,j) = true，反之为false
        k = len(s)  # 计算字符串的长度
        matrix = [[0 for i in range(k)] for i in range(k)]  # 初始化n*n的列表
        logestSubStr = ""  # 存储最长回文子串
        logestLen = 0  # 最长回文子串的长度

        for j in range(0, k):
            for i in range(0, j + 1):
                if j - i <= 1:
                    if s[i] == s[j]:
                        matrix[i][j] = 1  # 此时f(i,j)置为true
                        if logestLen < j - i + 1:  # 将s[i:j]的长度与当前的回文子串的最长长度相比 
                            logestSubStr = s[i:j + 1]  # 取当前的最长回文子串
                            logestLen = j - i + 1  # 当前最长回文子串的长度
                else:
                    if s[i] == s[j] and matrix[i + 1][j - 1]:  # 判断
                        matrix[i][j] = 1
                        if logestLen < j - i + 1:
                            logestSubStr = s[i:j + 1]
                            logestLen = j - i + 1
        return logestSubStr


s = Solution()
print(s.longestPalindrome("babad"))
