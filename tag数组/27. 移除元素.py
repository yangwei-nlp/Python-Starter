class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # https://www.cnblogs.com/cloud-ken/p/10021266.html
        length = len(nums)
        for i in range(length-1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)