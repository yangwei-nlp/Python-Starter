# class Solution:
#     def numSubarraysWithSum(self, A, S):
#         """
#         :type A: List[int]
#         :type S: int
#         :rtype: int
#         """
#         count = 0
#         for i in range(len(A)-S+1):
#             for j in range(i+S-1, len(A)):
#                 if A[i:j+1] == []:
#                     continue
#                 if sum(A[i:j+1]) == S:
#                     count += 1
#                 elif sum(A[i:j+1]) > S:
#                     break
#         return count


class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        result, cur_sum = 0, 0
        sum_dict = {0: 1}
        for num in A:
            cur_sum += num
            if cur_sum - S in sum_dict:
                result += sum_dict[cur_sum - S]
            if cur_sum in sum_dict:
                sum_dict[cur_sum] += 1
            else:
                sum_dict[cur_sum] = 1

        return result


s = Solution()
print(s.numSubarraysWithSum(A=[1,0,1,0,1], S=2))
