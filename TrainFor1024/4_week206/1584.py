class Solution:
    def minCostConnectPoints(self, points):
        cluster = {}  # key为类别
        for i in range(len(points)):
            cluster[i] = [i]
        



s = Solution()
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
s.minCostConnectPoints(points)

