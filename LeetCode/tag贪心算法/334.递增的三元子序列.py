class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 贪心算法:https://www.youtube.com/watch?v=xV_AS08-OeA&index=4&list=PLLuMmzMTgVK5Igci8P3d88XpoyeIA1Fl-&t=0s
        if len(nums) <= 2:
            return False
        # 由于是3元子序列，所以我们只需要建立两个变量就好，所以空间复杂度o(1)
        min1 = max(nums)
        min2 = max(nums)
        for i in range(len(nums)):
            if nums[i] > min2:
                return True
            elif nums[i] < min1:
                min1 = nums[i]
                # 注意，min1只要更新了就说明找到了二元子序列了，再来一个比min2大就可以了
                # 但是，由于现在min2是最大值，所以需要更新min2，更新规则是：
                # 新数比min1大，但是比现min2小
            elif nums[i] > min1 and nums[i] < min2:
                min2 = nums[i]
        return False