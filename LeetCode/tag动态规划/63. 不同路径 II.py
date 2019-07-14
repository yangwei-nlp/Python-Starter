class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if not obstacleGrid[i][j]:  # 如果ij位置不是障碍
                    if i or j:  # 如果不是00位置
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                    else:  # 是00位置
                        dp[i][j] = 1
                # 如果是障碍物就跳走了，当前位置可到达路径数位0，仍然满足那个式子
        return dp[-1][-1]
