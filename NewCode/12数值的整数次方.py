# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        ret = 1
        if exponent == 0:
            return 1
        expo = abs(exponent)
        for i in range(expo):
            ret *= base
        if exponent > 0:
            return ret
        else:
            return 1/ret

s = Solution()
print(s.Power(2, -1))
