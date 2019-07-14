class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 和之前62题一样的，都是用动态规划思路
        m = len(grid)
        n = len(grid[0])
        matrix = [[0 for j in range(n)] for i in range(m)]
        matrix[0][0] = grid[0][0]
        for j in range(1, n):
            matrix[0][j] = matrix[0][j - 1] + grid[0][j]
        for i in range(1, m):
            matrix[i][0] = matrix[i - 1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1]) + grid[i][j]

        return matrix[m - 1][n - 1]