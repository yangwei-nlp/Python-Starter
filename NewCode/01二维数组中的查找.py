# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if array == [[]]:
            return False
        if target < array[0][0]:
            return False
        row = len(array)
        column = len(array[0])
        for i in range(row):
            if target > array[i][-1]:
                continue
            else:
                for j in range(column):
                    if target > array[-1][j]:
                        continue
                    if array[i][j] == target:
                        return True
        return False