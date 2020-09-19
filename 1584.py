class Solution:
    def minCostConnectPoints(self, points):
        
        total_cost = 0
        costs = {}
        for i in range(len(points)):
            cost_i = {}
            for j in range(len(points)):
                if i == j:
                    continue
                else:
                    cost_i[j] = self.compute_dist(points[i], points[j])
            costs[i] = cost_i



    def compute_dist(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])


s = Solution()
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
s.minCostConnectPoints(points)
