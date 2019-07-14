class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        # 动态规划方案，时间复杂度为O(n^2)
        # 首先得到差序列
        diff = [0 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            diff[i] = nums[i] - nums[i-1]
        for i in range(len(nums)):
            if diff[i] == 0:
                continue
            else:
                diff[i-1] = -1*diff[i]
                break

        dp = [1 for _ in range(len(nums))]
        for j in range(1, len(nums)):
            for k in range(j-1, -1, -1):
                if diff[j]*diff[k] < 0:
                    dp[j] = dp[k] +1
                    break
                elif diff[j]*diff[k] == 0:
                    dp[j] = dp[k]
        return dp[-1]

s = Solution()
print(s.wiggleMaxLength([3,3,3,2,5]))