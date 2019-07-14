# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        visited = [False] * rows * cols
        self.moveControl(threshold, 0, 0, rows, cols, visited)
        visited[0] = True  # 代表已经访问过
        return sum(visited)

    def moveControl(self, threshold, i, j, rows, cols, visited):
        locInVisited = i * cols + j
        if i < 0 or j < 0 or visited[locInVisited] is True \
                or i >= rows or j >= cols:
            return

        string = str(i) + str(j)
        count = 0
        for i in range(len(string)):
            count += int(string[i])

        if count > threshold:
            return
        else:
            visited[locInVisited] = True

        self.moveControl(threshold, i + 1, j, rows, cols, visited)
        self.moveControl(threshold, i - 1, j, rows, cols, visited)
        self.moveControl(threshold, i, j + 1, rows, cols, visited)
        self.moveControl(threshold, i, j - 1, rows, cols, visited)
