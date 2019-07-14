class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 动态规划的思路，具体思路见《数据结构与算法-笔记》各个算法击破之 一，动态规划
        matrix = [[0 for i in range(n)] for j in range(m)]
        matrix[0] = [1] * n
        for i in range(m):
            matrix[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        return matrix[m - 1][n - 1]

