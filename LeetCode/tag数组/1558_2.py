class Solution:
    def containsCycle(self, grid):
        new_dic = []
        for i in range(len(grid)-1, -1, -1):
            row = grid[i]
            in_out = []
            for j in range(len(row)):
                while j < len(row) - 1:
                    _in = j
                    if row[j] == row[j+1]:
                        for dic in in_out:
                            _in, _out = dic.items()
                            if j == _in:
                                new_dic.append({j: _out})
                        _out = j + 1
                        in_out.append({_in: _out})
                        
                    print(new_dic)
                    j += 1
                
                if grid[i+1][j] == grid[i][j] and j in in_out.keys():
                    for dic in in_out:
                        _in, _out = dic.items()
                        if j == _in:
                            new_dic.append({j: _out})


    # def move(self, grid, in_out, tmp_idx):




grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
s = Solution()
s.containsCycle(grid)
