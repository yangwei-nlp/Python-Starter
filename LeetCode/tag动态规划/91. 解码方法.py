# class Solution:
#     def numDecodings(self, s: str) -> int:
#         if s == "0":return 0
#         if len(s) == 1 or len(s) == 0:
#             return 1
#         dp = [1] * (len(s)+1)
#         for i in range(1, len(s)):

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0
        dp = [1] * (len(s)+1)
        for i in range(1, len(s)):
            if s[i] == "0":
                # 等于零只有一种选择
                if s[i-1] != "1" and s[i-1] != "2":
                    return 0
                else:
                    dp[i+1] = dp[i-1]
            else:
                if s[i-1] != "0" and int(s[i-1:i+1]) <= 26:
                    dp[i+1] = dp[i] + dp[i-1]
                else:
                    dp[i+1] = dp[i]
        return dp[-1]

s = Solution()
print(s.numDecodings("226"))