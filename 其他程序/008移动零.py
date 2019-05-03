# coding=utf-8
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 第一种方法有问题
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         nums.append(0)
        #         nums.remove(0)

        # 第二种方法
        zeros = 0 # 记录某个元素之前(紧邻的)零的个数
        for i in range(len(nums)):
            if nums[i] != 0:
                if zeros != 0:
                    nums[i-zeros], nums[i] = nums[i], nums[i-zeros]
            else:
                zeros += 1
        return nums
solver = Solution()
print solver.moveZeroes([1,3,12,0,0,1,4,0,1])