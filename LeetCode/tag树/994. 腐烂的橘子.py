# 方法一，写不下去了，感觉思路复杂
# class Solution:
#     def orangesRotting(self, grid: 'List[List[int]]') -> 'int':
#         if not self.isThereRottedOrange(grid):
#             # 没有烂橘子，grid永远不可能全部烂掉
#             return -1
#
#         while not self.isAllRot(grid):
#             # 不是所有橘子都烂掉的话进来
#
#
#     def isAllRot(self, grid):
#         # 判断橘子是否全部烂掉了
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 1:
#                     return False
#         return True
#
#     def isThereRottedOrange(self, grid):
#         # 判断是否存在烂橘子
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 2:
#                     return True
#         return False

# 这个方法，这个写法，真是让人顶礼膜拜啊
class Solution:
    def orangesRotting(self, grid: 'List[List[int]]') -> 'int':
        r, c = len(grid), len(grid[0])
        rot = list()
        # rot用来存储腐烂了的橘子
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    rot.append((i, j, 0))  # 0表示需要0分钟
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 四个方向上的对应坐标增量
        # d用来移动点（i, j），当然是在grid内移动
        res = 0  # 保证其变为全局变量
        while rot:
            # 如果存在腐烂的橘子就说明需要继续弹出该橘子，然后检查其邻居是否为新鲜橘子
            i, j, res = rot.pop(0)  # 注意，我们需要使用广度优先搜索，
            # 这样才能找到最后剩下的那个橘子和最开始的橘子是第几层关系，
            # 第几层关系就表示了需要几分钟感染到那里---《算法图解》第六章
            for xd, yd in d:
                x = i + xd
                y = j + yd
                if 0 <= x < r and 0 <= y < c and grid[x][y] == 1:
                    grid[x][y] = 2
                    rot.append((x, y, res + 1))  # 注意，都在一个for循环内将res增加1，
                # 表示这一层关系的点都需要res+1分钟
        # 结束循环表明没有烂橘子加入。有两种可能：1.所有新鲜橘子都被感染。2.烂橘子的附近没有新鲜橘子，
        # 无法继续感染新鲜橘子了（也即还存在新鲜橘子）
        if any(1 in row for row in grid):
            # 表明还存在新鲜橘子，属于第二种情况
            return -1
        return res


s = Solution()
print(s.orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
