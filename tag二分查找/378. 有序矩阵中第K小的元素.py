# 暴力法：每次移动一个位置然后将右边元素和下方元素添加入候选，再从中选择最小元素，超时
# class Solution:
#     def kthSmallest(self, matrix, k):
#         r, c = len(matrix), len(matrix[0])
#         move = [[0, 1], [1, 0]]
#         i, j = 0, 0
#         seen = ["0,0"]
#         temp = {}
#         while k > 0:
#             min_val = matrix[i][j]
#             for add_x, add_y in move:
#                 x, y = i + add_x, j + add_y
#                 cord = "{},{}".format(x, y)
#                 if x < r and y < c and cord not in seen:
#                     temp[cord] = matrix[x][y]
#                     seen.append(cord)
#             if temp:
#                 cord = min(temp, key=temp.get)
#                 temp.pop(cord)
#                 cord_split = cord.split(",")
#                 i, j = int(cord_split[0]), int(cord_split[1])
#             k -= 1
#         return min_val



# 使用优先级队列的方法（好像有点投机取巧的思想），并未用到任何算法
import queue
class Solution:
    def kthSmallest(self, matrix, k):
        r, c = len(matrix), len(matrix[0])
        pq = queue.PriorityQueue()
        for i in range(r):
            for j in range(c):
                pq.put(matrix[i][j])
        while k > 0:
            min_val = pq.get()
            k -= 1
        return min_val


s = Solution()
# print(s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))
print(s.kthSmallest([[-5]], 1))