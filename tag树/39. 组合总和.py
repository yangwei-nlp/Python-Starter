class Solution:
    def combinationSum(self, candidates: 'List[int]', target: int) -> 'List[List[int]]':
        candidates.sort()
        Solution.res = []
        path = []
        self.dfs(candidates, target, 0, path)
        return Solution.res

    def dfs(self, candidates, target, idx, path):
        if target == 0:
            Solution.res.append(path)
        for i in range(idx, len(candidates)):
            if candidates[i] > target:
                return
            self.dfs(candidates, target-candidates[i], i, path+[candidates[i]])

s = Solution()
print(s.combinationSum([2,3], 5))