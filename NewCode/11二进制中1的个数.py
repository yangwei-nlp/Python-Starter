# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n == 0:
            return 0
        temp = 1
        list_2 = []
        number = abs(n)
        while temp <= number:
            list_2.append(temp)
            temp *= 2
        bits = []  # 原码
        compare_n = 0
        for i in range(len(list_2)-1, -1, -1):
            if compare_n + list_2[i] <= number:
                compare_n += list_2[i]
                bits.append(1)
            else:
                bits.append(0)
        if compare_n == number:
            if n > 0:
                return sum(bits)
            else:
                print(bits)
                fanma = [1 if bit == 0 else 0 for bit in bits]  # 反码
                print(fanma)
                k = 0
                for i in range(len(fanma)-1, -1, -1):
                    if fanma[i] == 0:
                        break
                    k += 1
                print(k)
                return sum(fanma) - k + 1


s = Solution()
print(s.NumberOf1(-68))