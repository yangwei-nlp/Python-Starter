class Solution:
    def containsCycle(self, grid):
        rows = len(grid)
        columns = len(grid[0])
        this_mask_num = 0
        last_mask_num = 0
        while True:
            for i in range(rows):
                for j in range(columns):
                    if self.if_mask(grid, i, j, rows, columns):
                        if grid[i][j] != -1:
                            grid[i][j] = -1
                            this_mask_num += 1
            if this_mask_num == rows * columns:
                return False
            if last_mask_num == this_mask_num:
                return True
            else:
                last_mask_num = this_mask_num


    def if_mask(self, grid, i, j, rows, columns):
        equals = 0
        if 0 <= i + 1 < rows:
            # 右移
            if grid[i][j] == grid[i+1][j]:
                equals += 1
        if 0 <= i - 1 < rows:
            if grid[i][j] == grid[i-1][j]:
                equals += 1
        if 0 <= j + 1 < columns:
            if grid[i][j] == grid[i][j+1]:
                equals += 1
        if 0 <= j - 1 < rows:
            if grid[i][j] == grid[i][j-1]:
                equals += 1
        if equals >= 2:
            # 应该保留
            return False
        else:
            return True


grid = [["g","c","d","h","c","f","g","b","d","d","a","d","f","e","h","f","d","h","d","b"],["g","b","c","c","d","g","h","h","b","b","b","g","e","b","h","b","c","g","g","h"],["e","d","f","f","g","g","b","a","h","g","g","f","g","h","c","d","h","g","g","a"],["c","h","c","b","c","a","a","h","f","c","c","f","f","a","g","a","e","g","e","a"],["c","c","a","c","b","c","h","a","g","b","a","a","d","f","e","h","a","f","h","b"],["c","g","b","d","a","c","d","b","e","d","a","c","e","f","b","f","b","f","b","a"],["g","h","d","d","b","f","h","c","f","b","c","d","d","d","c","d","d","g","c","d"],["a","a","b","c","f","e","g","e","h","e","f","c","b","c","a","c","b","b","h","g"],["e","a","g","f","f","f","d","g","c","a","f","c","f","e","c","g","d","e","h","h"],["c","a","e","c","d","g","e","c","d","h","a","g","e","e","f","h","e","g","g","g"]]

s = Solution()
s.containsCycle(grid)


