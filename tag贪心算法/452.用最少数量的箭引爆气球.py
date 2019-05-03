class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # tag双指针: 区间，合并区间
        # 思路来源：https://www.youtube.com/watch?v=DguJN47_mSg&index=3&list=PLLuMmzMTgVK5Igci8P3d88XpoyeIA1Fl-&t=0s
        if len(points) == 0:
            return 0
        points = sorted(points, key=lambda x: x[1])
        count = 1
        cur = points[0]
        for point in points:
            if point[0] <= cur[1]:
                continue
            else:
                cur = point
                count += 1
        return count