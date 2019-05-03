# class Solution:
#     def wordBreak(self, s: str, wordDict: 'List[str]') -> 'bool':
#         dp = [False] * (len(s) + 1)
#         dp[0] = True
#
#         for i in range(1, len(s)+1):
#             for j in range(i):  # 时间浪费主要在这里
#                 if dp[j] and s[j: i] in wordDict:
#                     dp[i] = True
#                     break
#         return dp[-1]


# 稍微能够快一点，因为将j做了调整
class Solution:
    def wordBreak(self, s: str, wordDict: 'List[str]') -> 'bool':
        inDict = [0]
        for i in range(len(s)+1):
            for j in inDict:
                if s[j: i] in wordDict:
                    inDict.append(i)
                    break
        return inDict[-1] == len(s)