class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 妈的，我这个代码写得太好了
        i = len(nums) - 1
        j = i - 1
        while j >= 0:
            if nums[j] >= i - j:
                i = j
            j -= 1

        return True if i == 0 else False