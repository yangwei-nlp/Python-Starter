class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        if target > nums[j]:
            return j + 1
        elif target <= nums[0]:
            return 0
        while j - i > 1:
            middle_index = (i + j) // 2
            if nums[middle_index] == target:
                return middle_index
            elif nums[middle_index] > target:
                j = middle_index
            else:
                i = middle_index
        return j