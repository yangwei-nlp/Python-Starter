class Solution:
    def containsCycle(self, grid):
        row = grid[-1]
        init = self.get_in_outs_based_this_row(row)
        self.in_outs_based_last_row = init
        for i in range(len(grid)-2, -1, -1):
            row = grid[i]
            in_outs_based_this_row = self.get_in_outs_based_this_row(row)
            in_outs_based_last_row = self.get_in_outs_based_last_row(grid, i)
            
            # 将两行融合
            new_in_outs = {}
            new_in_outs.update(in_outs_based_last_row)
            for this_k, this_vals in in_outs_based_this_row.items():
                if this_k in in_outs_based_last_row:
                    new_corres_out = list(set(new_in_outs[this_k]).union(set(this_vals)))
                    if this_k in new_corres_out:
                        return True
                    new_in_outs[this_k] = new_corres_out
                else:
                    new_in_outs[this_k] = this_vals
            self.in_outs_based_last_row = new_in_outs

        return False


    def get_in_outs_based_last_row(self, grid, i):
        in_out = {}
        for j in range(len(grid[0])):
            corresponding_out = []
            if grid[i][j] == grid[i+1][j]:
                if j in self.in_outs_based_last_row:
                    tmp_out = self.in_outs_based_last_row[j]
                    for tmp_idx in tmp_out:
                        if grid[i][tmp_idx] == grid[i][j]:
                            corresponding_out.append(tmp_idx)
                    new_corres_out = corresponding_out[:]
                    for corrs_out in corresponding_out:
                        for _idx in range(corrs_out-1, -1, -1):
                            if grid[i][_idx] == grid[i][corrs_out]:
                                new_corres_out.append(_idx)
                            else:
                                break
                        for _idx in range(corrs_out+1, len(grid[0])):
                            if grid[i][_idx] == grid[i][corrs_out]:
                                new_corres_out.append(_idx)
                            else:
                                break
                    if new_corres_out:
                        in_out[j] = new_corres_out
        return in_out

    def get_in_outs_based_this_row(self, row):
        # 该行的进出点
        in_out = {}
        for j in range(len(row)):
            corresponding_out = []
            for col in range(j+1, len(row)):
                if row[col] == row[j]:
                    corresponding_out.append(col)
                else:
                    break
            if corresponding_out:
                in_out[j] = corresponding_out
        return in_out


grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
s = Solution()
print(s.containsCycle(grid))
# s.row_in_out(["c","c","c","a"])

