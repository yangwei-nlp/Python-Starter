# class Solution:
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         # 倒着遍历和正着遍历基本思想一样的
#         if len(nums) == 1:
#             return nums[0]
#         sum_list = [0] * len(nums)
#         sum_list[-1] = nums[-1]
#         for i in range(len(nums)-2, -1, -1):
#             sum_list[i] = max(nums[i], nums[i] + sum_list[i+1])
#         return max(sum_list)


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 倒着遍历和正着遍历基本思想一样的
        if len(nums) == 1:
            return nums[0]
        max_sum = [0]*len(nums)
        max_sum[0] = nums[0]
        for i in range(1, len(nums)):
            max_sum[i] = max(nums[i], max_sum[i-1]+nums[i])
        return max(max_sum)



s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(s.maxSubArray([-2,-1]))