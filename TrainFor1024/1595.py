from typing import List
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        _max = self._max(cost)
        i = 0
        while i < len(cost):
            j = 0
            while j < len(cost[0]):
                if cost[i][j] == _max and self.remove(i, j, cost):
                    cost[i][j] = 0
                    _max = self._max(cost)
                j += 1
            i += 1
        print(233)
    
    def _max(self, cost):
        _all = []
        for ls in cost:
            _all.extend(ls)
        _max = max(_all)
        return _max

    def remove(self, i, j, cost):
        col = [ls[j] for ls in cost]
        if cost[i].count(0) == len(cost[i])-1 or col.count(0) == len(col)-1:
            return False
        else:
            return True

    

cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]

s = Solution()
print(s.connectTwoGroups(cost))
