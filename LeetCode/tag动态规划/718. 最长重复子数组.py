# 暴力解法，没什么技术含量，但是超时了
# from collections import defaultdict
# class Solution:
#     def findLength(self, A, B):
#         B_dict = defaultdict(list)
#         for i_B, num_B in enumerate(B):
#             for i_A, num_A in enumerate(A):
#                 if num_A == num_B:
#                     B_dict[i_B].append(i_A)
#         ret = []
#         i = 0
#         while i < len(B):
#             if i in B_dict:
#                 for start in B_dict[i]:
#                     j = i
#                     while start < len(A) and j < len(B) and B[j] == A[start]:
#                         j += 1
#                         start += 1
#                     ret.append(j-i)
#             i += 1
#         return 0 if not ret else max(ret)

# s = Solution()
# print(s.findLength([3, 0, 4, 5, 6, 9, 10, 12, 4, 5, 6, 7, 8],
#              [1, 2, 3, 4, 5, 8, 4, 5, 6, 7, 8, 9, 13]))

# print(s.findLength([0,0,0,0,0],
#                    [0,0,0,0,0]))

# print(s.findLength([70,39,25,40,7], [52,20,67,5,31]))


# 这道题其实是动态规划的题目，so：
# https://blog.csdn.net/m0_37477175/article/details/80273231
class Solution:
    def findLength(self, A, B):
        len_A, len_B = len(A), len(B)
        dp = [[0 for i in range(len_B+1)] for j in range(len_A+1)]
        for i in range(1, len_A+1):
            for j in range(1, len_B+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0
        return max([max(row) for row in dp])