# coding=utf-8
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        nums = sorted(nums)
        flag = 0
        length = len(nums)
        while k<length-1:
            if nums[0] == nums[1]:
                nums.remove(nums[0])
                nums.remove(nums[0])
            else:
                flag = nums[0]
                break
            k += 2
        if len(nums) == 1:
           flag, = nums
        return flag

solver = Solution()
print solver.singleNumber([4,1,2,1,2])
print solver.singleNumber([2,2,1])

