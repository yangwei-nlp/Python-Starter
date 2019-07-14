# 我的思路：遍历每个坐标，然后分别判断是否可以流入太平洋和大西洋-这样很暴力法:(
# 能否流入太平洋和大西洋使用了BFS广度搜索(超出时间限制)（DFS深度搜索更加快速，因为我们只关心能否到达边界即可，
# 所以需要算法能够快速到达边界，显然DFS能够更快做到这一点）
# class Solution:
#     def pacificAtlantic(self, matrix: 'List[List[int]]') -> 'List[List[int]]':
#         res = []
#         if len(matrix) == 0:
#             return res
#         r, c = len(matrix), len(matrix[0])
#         for i in range(r):
#             for j in range(c):
#                 if self.toPacific(matrix, i, j, r, c) and self.toAtlantic(matrix, i, j, r, c):
#                     res.append([i, j])
#         return res
#
#     def toPacific(self, matrix, i, j, r, c):
#         queue = [(i, j)]
#         seen = [(i, j)]
#         dires = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 用于将当前点移动的增量
#         while queue:
#             i, j = queue.pop(0)
#             if i == 0 or j == 0:
#                 return True
#             for add_x, add_y in dires:
#                 x, y = i + add_x, j + add_y
#                 if 0 <= x < r and 0 <= y < c and matrix[i][j] >= matrix[x][y]\
#                         and (x, y) not in seen:
#                     queue.append((x, y))
#                     seen.append((x, y))
#         return False
#
#     def toAtlantic(self, matrix, i, j, r, c):
#         queue = [(i, j)]
#         seen = [(i, j)]
#         dires = [(0, 1), (0, -1), (-1, 0), (1, 0)]
#         while queue:
#             i, j = queue.pop(0)
#             if i == r - 1 or j == c - 1:
#                 return True
#             for add_x, add_y in dires:
#                 x, y = i + add_x, j + add_y
#                 if 0 <= x < r and 0 <= y <c and matrix[i][j] >= matrix[x][y]\
#                      and (x, y) not in seen:
#                     queue.append((x, y))
#                     seen.append((x, y))
#         return False


# 依然是遍历每个坐标，但是使用深度优先搜索来判断每个点是否能同时到达太平洋和大西洋(更快)
# class Solution:
#     def pacificAtlantic(self, matrix: 'List[List[int]]') -> 'List[List[int]]':
#         res = []
#         if len(matrix) == 0:
#             return res
#         r, c = len(matrix), len(matrix[0])
#         for i in range(r):
#             for j in range(c):
#                 if self.toPacific(matrix, i, j, r, c) and self.toAtlantic(matrix, i, j, r, c):
#                     res.append([i, j])
#         return res
#
#     def toPacific(self, matrix, i, j, r, c):
#         stack = [(i, j)]
#         seen = [(i, j)]
#         dires = [(0, 1), (0, -1), (-1, 0), (1, 0)]
#         while stack:
#             i, j = stack.pop()  # 深度优先搜索
#             if i == 0 or j == 0:
#                 return True
#             for add_x, add_y in dires:
#                 x, y = i + add_x, j + add_y
#                 if 0 <= x < r and 0 <= y < c and matrix[i][j] >= matrix[x][y]\
#                         and (x, y) not in seen:
#                     stack.append((x, y))
#                     seen.append((x, y))
#         return False
#
#     def toAtlantic(self, matrix, i, j, r, c):
#         stack = [(i, j)]
#         seen = [(i, j)]
#         dires = [(0, 1), (0, -1), (-1, 0), (1, 0)]
#         while stack:
#             i, j = stack.pop()
#             if i == r - 1 or j == c - 1:
#                 return True
#             for add_x, add_y in dires:
#                 x, y = i + add_x, j + add_y
#                 if 0 <= x < r and 0 <= y <c and matrix[i][j] >= matrix[x][y]\
#                      and (x, y) not in seen:
#                     stack.append((x, y))
#                     seen.append((x, y))
#         return False

# 法二，大神写的
# class Solution:
#     def pacificAtlantic(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         if not matrix or not matrix[0]: return []
#         m, n = len(matrix), len(matrix[0])
#         p_visited = [[False] * n for _ in range(m)]
#         a_visited = [[False] * n for _ in range(m)]
#
#         # 遍历每个初始符合的点
#         for i in range(m):
#             self.dfs(p_visited, matrix, m, n, i, 0)
#             self.dfs(a_visited, matrix, m, n, i, n - 1)
#         for j in range(n):
#             self.dfs(p_visited, matrix, m, n, 0, j)
#             self.dfs(a_visited, matrix, m, n, m - 1, j)
#
#         res = []
#         for i in range(m):
#             for j in range(n):
#                 if p_visited[i][j] and a_visited[i][j]:
#                     # 如果两个洋都可以到达，OK
#                     res.append([i, j])
#         return res
#
#     def dfs(self, visited, matrix, m, n, i, j):
#         # 深度优先搜索(以递归形式实现)
#         visited[i][j] = True  # 将符合条件的点设为True（表示能够抵达海洋）（初始点肯定满足条件）
#         directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
#         for dire in directions:
#             x, y = i + dire[0], j + dire[1]
#             if 0 <= x < m and 0 <= y < n and not visited[x][y] and matrix[x][y] >= matrix[i][j]:
#                 # 满足条件的点：首先不能越界，其次不能为已经判断过为True的
#                 self.dfs(visited, matrix, m, n, x, y)




# 纸上得来终觉浅，得知此事须躬行。理解了大神的思路再敲一遍代码
class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]: return []
        r, c = len(matrix), len(matrix[0])
        toPacific = [[False] * c for _ in range(r)]  # 为True表明能够到达Pacific
        toAtlantic = [[False] * c for _ in range(r)]
        # 将靠近太平洋的初始点送入dfs函数
        for i in range(r):
            self.dfs(matrix, toPacific, i, 0, r, c)
        for j in range(c):
            self.dfs(matrix, toPacific, 0, j, r, c)

        # 将靠近大西洋的初始点送入dfs函数
        for i in range(r):
            self.dfs(matrix, toAtlantic, i, c-1, r, c)
        for j in range(c):
            self.dfs(matrix, toAtlantic, r-1, j, r, c)

        # 两个矩阵融合
        res = []
        for i in range(r):
            for j in range(c):
                if toPacific[i][j] and toAtlantic[i][j]:
                    res.append([i, j])
        return res

    def dfs(self, matrix, toMatrix, i, j, r, c):
        toMatrix[i][j] = True
        dires = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in dires:
            x, y = i + dx, j + dy
            if 0 <= x < r and 0 <= y < c and not toMatrix[x][y] and matrix[x][y] >= matrix[i][j]:
                # 这里的递归就相当于是深度优先搜索
                self.dfs(matrix, toMatrix, x, y, r, c)



s = Solution()
print(s.pacificAtlantic([[1,1],[1,1],[1,1]]))





