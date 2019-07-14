# coding=utf-8
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for num in nums[0: len(nums)-k]:
            nums.append(num)
            nums.remove(num)
        return nums

solver = Solution()
print solver.rotate([0,1,2,3,4,5,6,7,8,9], 3)