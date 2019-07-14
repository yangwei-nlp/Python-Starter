class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 每有一个新的数字加入，最大值要么是当前最大值*新数，要么是
        # 当前最小值（负数）*新数（负数），要么是当前值。
        if len(nums) == 1:
            return nums[0]
        max_list = [0]*len(nums)
        min_list = [0]*len(nums)
        max_list[0] = nums[0]
        min_list[0] = nums[0]
        for i in range(1, len(nums)):
            max_list[i] = max(nums[i], max(nums[i]*max_list[i-1], nums[i]*min_list[i-1]))
            min_list[i] = min(nums[i], min(nums[i]*max_list[i-1], nums[i]*min_list[i-1]))
        return max(max_list)