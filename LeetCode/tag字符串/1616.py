class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        pass


    def check(self, s="ulaalu"):
        # 回文串判断
        return s == s[::-1]




a = "ulacfd"
b = "jizalu"

s = Solution()
s.checkPalindromeFormation(a, b)
print(s.check("abcba"))
