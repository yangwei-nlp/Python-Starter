# coding=utf-8
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 方法一：--->超时了
        # flag = False
        # for i in range(len(nums)):
        #     if nums[i] in nums[i+1:]:
        #         flag = True
        #         break
        # return flag
        # 方法二：
        flag = False
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                flag = True
        return flag
        # 方法三：
        # 使用set，自己想

solver = Solution()
print solver.containsDuplicate([1,2,3,0])