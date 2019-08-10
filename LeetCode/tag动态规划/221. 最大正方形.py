class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        result = [[0] * len(matrix[0])] * len(matrix)
        for i in range(len(matrix)-1, 0, -1):
            for j in range(len(matrix[0])-1, 0, -1):
                