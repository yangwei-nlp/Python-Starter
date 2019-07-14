class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 贪心算法:https://www.youtube.com/watch?v=xV_AS08-OeA&index=4&list=PLLuMmzMTgVK5Igci8P3d88XpoyeIA1Fl-&t=0s
        # 本程序用动态规划方法实现
        dp = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
                    if dp[i] >= 3:
                        return True
        return False