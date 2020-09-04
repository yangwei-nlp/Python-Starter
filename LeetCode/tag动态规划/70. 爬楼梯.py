class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        dp = [0]*n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

    def climbStairs2(self, n: int) -> int:
        """这里的处理更加简洁易懂，相比于上面方法"""
        if n == 1:
            return 1
        dp = [1, 1]
        
        for i in range(2, n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[-1]


s = Solution()
print(s.climbStairs2(3))