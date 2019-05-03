# class Solution:
# 法一，问题多多，处理特殊情况很麻烦
#     def findRadius(self, houses: 'List[int]', heaters: 'List[int]') -> 'int':
#         min_r = [0] * len(heaters)
#         for i in range(len(heaters)):
#             if heaters[i] > houses[-1] or heaters[i] < houses[0]:
#                 min_r[i] = 0
#             else:
#                 if i == 0:
#                     if len(heaters) == 1:
#                         min_r[i] = max(heaters[i] - houses[0], houses[-1] - heaters[i])
#                     else:
#                         min_r[i] = max(heaters[i]-houses[0], (heaters[i+1]-heaters[i])//2)
#                 elif i == len(heaters) - 1:
#                     min_r[i] = (heaters[i]-heaters[i-1])//2
#                 else:
#                     min_r[i] = max((heaters[i+1]-heaters[i])//2, (heaters[i]-heaters[i-1])//2)
#         return max(min_r)


# 法二，换一种思路：
# 计算每个房屋所需的最小半径，然后再对所有房屋的最小半径求最大值，即得到答案
# 这里所需最小半径的计算就用到了二分方法
class Solution:
    def findRadius(self, houses: 'List[int]', heaters: 'List[int]') -> 'int':
        min_radius = 0
        heaters.sort()  # 艹，居然要排序，我特么的无语
        for loc in houses:
            min_radius = max(min_radius, self.binary_search(heaters, loc))
        return min_radius

    def binary_search(self, heaters, loc):
        i = 0
        j = len(heaters) - 1
        if loc <= heaters[0]:
            return abs(heaters[0] - loc)
        elif loc >= heaters[-1]:
            return abs(heaters[-1] - loc)
        while j - i > 1:
            mid_index = (i + j) // 2
            if heaters[mid_index] >= loc and heaters[mid_index-1] <= loc:
                return min(abs(heaters[mid_index]-loc), abs(loc-heaters[mid_index-1]))
            elif heaters[mid_index] > loc and heaters[mid_index-1] > loc:
                j = mid_index
            elif heaters[mid_index] < loc and heaters[mid_index-1] < loc:
                i = mid_index
        return min(abs(heaters[-1]-loc), abs(loc-heaters[0]))


s = Solution()
print(s.binary_search([1,5], [2]))