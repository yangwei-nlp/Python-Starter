# class Solution:
#     def kClosest(self, points, K):
#         """
#         :type points: List[List[int]]
#         :type K: int
#         :rtype: List[List[int]]
#         """
#         return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:K]


points = [[1,3],[-2,2]]
K = 1


class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if K == len(points):
            return points
        distance = [point[0]**2 + point[1]**2 for point in points]
        for i in range(K):
            min_val_index = i
            for j in range(i+1, len(distance)):
                if distance[j] < distance[min_val_index]:
                    min_val_index = j
            distance[i], distance[min_val_index] = distance[min_val_index], distance[i]
            points[i], points[min_val_index] = points[min_val_index], points[i]
        return points[:K]
    # 该方法是自己想的，可行，但是超过时间限制