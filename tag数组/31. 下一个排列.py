class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # https://blog.csdn.net/guoziqing506/article/details/51787763
        # https://www.youtube.com/watch?v=9mdoM2dVid8
        if nums is None or len(nums) == 0:
            return

        firstSmall = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i+1]:
                firstSmall = i
                break

        if firstSmall == -1:
            nums.sort()
            return

        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[firstSmall]:
                nums[firstSmall], nums[i] = nums[i], nums[firstSmall]
                break

        i = firstSmall + 1
        if i < len(nums) - 1:
            j = len(nums) - 1
            while i != j:
                if j - i == 1:
                    nums[i], nums[j] = nums[j], nums[i]
                    return
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

            return
        else:
            return