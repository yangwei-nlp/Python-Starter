# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        elif number >= 3:
            N = []
            N.append(1)
            N.append(2)
            for i in range(2, number):
                N.append(N[i-1]+N[i-2])
            return N[-1]
        else:
            return 0