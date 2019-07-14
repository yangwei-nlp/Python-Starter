# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
    # write code here
        if number == 1:
            return 1
        if number == 2:
            return 2
        if number >= 3:
            list_n = []
            list_n.append(1)
            list_n.append(2)
            for i in range(2, number):
                list_n.append(list_n[i-1] + list_n[i-2])
            return list_n[i]

s = Solution()
print(s.jumpFloor(5))