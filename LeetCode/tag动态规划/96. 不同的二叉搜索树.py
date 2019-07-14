class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # https://blog.csdn.net/OneDeveloper/article/details/80016857
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for k in range(1, i+1):
                dp[i] += dp[k-1] * dp[i-k]
        return dp[-1]

s = Solution()
print(s.numTrees(4))