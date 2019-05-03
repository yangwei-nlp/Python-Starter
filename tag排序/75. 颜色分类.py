# 直接判断有几个0，几个1，几个2，然后将列表改成需要的样子，一次遍历即可
# class Solution:
#     def sortColors(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         count_0 = 0
#         count_1 = 0
#         count_2 = 0
#         for num in nums:
#             if num == 0:
#                 count_0 += 1
#             elif num == 1:
#                 count_1 += 1
#             elif num == 2:
#                 count_2 += 1
#         nums[:count_0] = [0]*count_0
#         nums[count_0:(count_0+count_1)] = [1]*count_1
#         nums[(count_0+count_1):] = [2]*count_2


# 除了上述那种方法还有其他巧妙的方法，比如三个指针来辅助排序
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j, k, m = -1, -1, -1, 0
        while m < len(nums):
            if nums[m] == 0:
                k += 1
                nums[k] = 2
                j += 1
                nums[j] = 1
                i += 1
                nums[i] = 0
            elif nums[m] == 1:
                k += 1
                nums[k] = 2
                j += 1
                nums[j] = 1
            elif nums[m] == 2:
                k += 1
                nums[k] = 2
            m += 1


# [2,0,2,1,1,0]