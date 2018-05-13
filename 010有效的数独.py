# coding=utf-8
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        import numpy as np
        board = np.array(board)
        flag = True
        for c in range(0, 7, 3):
            for r in range(0, 7, 3):
                row_col = board[c:c+3, r:r+3][board[c:c+3, r:r+3] != '.']
                if len(row_col) != len(set(row_col)):
                    flag = False
                    break
        for i in range(9):
            row = board[i, :][board[i, :] != '.']
            if len(row) != len(set(row)):
                flag = False
                break
        for j in range(9):
            col = board[:, j][board[:, j] != '.']
            if len(col) != len(set(col)):
                flag = False
                break
        return flag

solver = Solution()
print solver.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
])

print solver.isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
])