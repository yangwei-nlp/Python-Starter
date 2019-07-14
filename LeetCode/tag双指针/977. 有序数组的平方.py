# class Solution:
#     def sortedSquares(self, A):
#         """
#         :type A: List[int]
#         :rtype: List[int]
#         """
#         result = [num**2 for num in A]
#         return sorted(result)
#         # 投机取巧的方法，完全没有用到算法


# class Solution:
#     def sortedSquares(self, A):
#         """
#         :type A: List[int]
#         :rtype: List[int]
#         """
#         if len(A) == 1:
#             return [A[0]**2]
#         if A[0] >= 0:
#             # 没有负数
#             return [num**2 for num in A]
#         if A[-1] < 0:
#             # 全为负数
#             return [A[i]**2 for i in range(len(A)-1, -1, -1)]
#         result = []
#         i = 0
#         j = 0
#         for k in range(len(A)-1):
#             if A[k] < 0 and A[k+1] >= 0:
#                 i = k
#                 j = k + 1
#         while i >= 0 and j <= len(A) - 1:
#             if abs(A[i]) < A[j]:
#                 result.append(A[i]**2)
#                 i -= 1
#             elif A[j] < abs(A[i]):
#                 result.append(A[j]**2)
#                 j += 1
#             elif abs(A[i]) == A[j]:
#                 result.append(A[i]**2)
#                 result.append(A[i]**2)
#                 i -= 1
#                 j += 1
#         if i < 0:
#             for m in range(j, len(A)):
#                 result.append(A[m]**2)
#         elif j > len(A) - 1:
#             for m in range(i, -1, -1):
#                 result.append(A[m]**2)
#         return result


# s = Solution()
# print(s.sortedSquares([-7, -3, 2, 3, 11]))
# print(s.sortedSquares([-4, -1, 0, 3, 10]))


# 法三：更简洁
# 通过建立左右两个指针，i = 0, j = len(A)-1
# 然后比较左右两个指针所指向的值的绝对值那个更大，
# 更大的那个显然就应该放到后面，然后接着比较即可。


class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, len(A)-1
        result = [0] * len(A)
        for k in range(len(A)-1, -1, -1):
            if abs(A[i]) < abs(A[j]):
                result[k] = A[j]**2
                j -= 1
            else:
                result[k] = A[i]**2
                i += 1
        return result


s = Solution()
print(s.sortedSquares([-7, -3, 2, 3, 11]))
print(s.sortedSquares([-4, -1, 0, 3, 10]))
