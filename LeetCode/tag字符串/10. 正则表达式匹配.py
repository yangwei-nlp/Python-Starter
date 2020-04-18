"""
DP的话，肯定要用空间换时间了，这里用 monkeyGoCrazy 的思路：用2维布尔数组，dp[i][j]的含义是s[0-i] 与 s[0-j]是否匹配。

1.p.charAt(j) == s.charAt(i) : dp[i][j] = dp[i-1][j-1]
2.If p.charAt(j) == ‘.’ : dp[i][j] = dp[i-1][j-1];
3.If p.charAt(j) == ‘*’:
    here are two sub conditions:
        1.if p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2] //in this case, a* only counts as empty
        2.if p.charAt(i-1) == s.charAt(i) or p.charAt(i-1) == ‘.’:
            dp[i][j] = dp[i-1][j] //in this case, a* counts as multiple a
            dp[i][j] = dp[i][j-1] // in this case, a* counts as single a
            dp[i][j] = dp[i][j-2] // in this case, a* counts as empty
"""
class Solution:
    def isMatch(self, s, p):
        pass


s = Solution()
print(s.isMatch('mississippi', 'mis*is*p*.'))
print(s.isMatch('aa', 'a'))
print(s.isMatch("ab", ".*"))
print(s.isMatch("aab", "c*a*b"))


