# https://blog.csdn.net/qq_20141867/article/details/81065793

# 法一(剑指offer思路)
def hasPath(self, matrix, rows, cols, path):
    # 参数校验
    if len(matrix) == 0 or len(matrix) != rows * cols or len(path) == 0:
        return False
    visited = [False] * len(matrix)
    pathlength = [0]
    for i in range(rows):
        for j in range(cols):
            # 以矩阵中每一个位置作为起点进行搜索
            if self.haspath(matrix, rows, cols, path, j, i, visited, pathlength):
                return True
    return False


# 判断矩阵位置（x,y）的字符能否加入已找到的路径中
def haspath(self, matrix, rows, cols, path, x, y, visited, pathlength):
    '''
    :param matrix:字符矩阵
    :param rows:矩阵的行数
    :param cols:矩阵的列数
    :param path:需要寻找的路径
    :param x:当前位置的横坐标(对应列数)
    :param y:当前位置的纵坐标(对应行数)
    :param visited:访问标志数组
    :param pathlength:已经找到的路径长度
    :return:是否存在路径
    '''
    if pathlength[0] == len(path):
        return True
    curhaspath = False
    # 参数校验：1、位置坐标不超过行列数 2、当前位置字符等于路径中对应位置的字符 3、当前位置未存在于当前已找到的路径中
    if 0 <= x < cols and 0 <= y < rows \
            and matrix[y * cols + x] == path[pathlength[0]] \
            and not visited[y * cols + x]:

        visited[y * cols + x] = True
        pathlength[0] += 1
        # 分别向左，向右，向上，向下移动一个格子，任一方向能够继续往下走均可
        curhaspath = self.haspath(matrix, rows, cols, path, x - 1, y, visited, pathlength) \
                     or self.haspath(matrix, rows, cols, path, x, y - 1, visited, pathlength) \
                     or self.haspath(matrix, rows, cols, path, x + 1, y, visited, pathlength) \
                     or self.haspath(matrix, rows, cols, path, x, y + 1, visited, pathlength)
        # 如果不能再走下一步，需要回退到上一状态
        if not curhaspath:
            pathlength[0] -= 1
            visited[y * cols + x] = False
    return curhaspath


# 法二
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        assistMatrix = [True] * rows * cols  # True表示下一步可以走
        # 两个for循环控制起点位置
        for i in range(rows):
            for j in range(cols):
                if (self.hasPathAtAStartPoint(matrix, rows, cols, i, j, path, assistMatrix)):
                    return True
        return False

    def hasPathAtAStartPoint(self, matrix, rows, cols, i, j, path, assistMatrix):
        if not path:
            return True
        index = i * cols + j  # 表示在matrix列表中是第几个元素
        if i < 0 or i >= rows or j < 0 or j >= cols or matrix[index] != path[0] or assistMatrix[index] == False:
            # 无路可走的时候就说明不会有路径，返回False
            return False
        assistMatrix[index] = False  # 程序如果能到这一行说明上一步(step-1步)走的是对的(暂时)
        # 接下来再看下一步(step步)怎么走
        if (self.hasPathAtAStartPoint(matrix, rows, cols, i + 1, j, path[1:], assistMatrix)
            or self.hasPathAtAStartPoint(matrix, rows, cols, i - 1, j, path[1:], assistMatrix)
            or self.hasPathAtAStartPoint(matrix, rows, cols, i, j - 1, path[1:], assistMatrix)
            or self.hasPathAtAStartPoint(matrix, rows, cols, i, j + 1, path[1:], assistMatrix)):
            return True
        # 如果上面四种走法全是False，那么step-1步是错的，不应该到这里来，返回False，但是这不妨碍别的路径经过此点
        # 所以改为True
        assistMatrix[index] = True
        return False


a = Solution()

print(a.hasPath([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 3, 4, [1, 2, 3, 4, 5]))
