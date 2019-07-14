# 动态规划的思路，但是没用列表来存储临时值，节省内存
# class Solution:
#     def countNumbersWithUniqueDigits(self, n: int) -> int:
#         if n == 0:
#             return 1
#         elif n == 1:
#             return 10
#         elif n == 2:
#             return 91
#         elif n > 10:
#             return 0
#         last = 91
#         temp = 9*9
#         k = 3
#         multi = 8
#         while k <= n:
#             temp *= multi
#             multi -= 1
#             k += 1
#             last += temp
#         return last


# 思路：https://blog.csdn.net/xiangwanpeng/article/details/53262383
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n > 10:
            return 0
        elif n == 1:
            return 10
        elif n == 0:
            return 1
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 10
        k = 2
        temp = 9
        multipy = 9
        while k <= n:
            temp *= multipy
            multipy -= 1
            dp[k] = dp[k-1] + temp
            k += 1
        return dp[-1]

s = Solution()
print(s.countNumbersWithUniqueDigits(4))