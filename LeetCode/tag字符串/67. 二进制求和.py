# -*- coding: utf-8 -*-
"""
Description :   
     Author :   Yang
       Date :   2020/4/6
"""
# 方法一：采用内置函数
class Solution1:
    def addBinary(self, a, b):
        # int(xxx, 2) 将二进制字符串转换为十进制
        # bin(xxx) 将十进制数转换为二进制。0b开头
        num = int(a, 2) + int(b, 2)
        return bin(num)[2:]


# 方法二：一个naive的思想，就是算术的算法
class Solution:
    def addBinary(self, a, b):
        if len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b
        else:
            a = '0' * (len(b) - len(a)) + a
        result = ''
        next = 0
        for i in range(len(a)-1, -1, -1):
            tmp = int(a[i]) + int(b[i])
            if tmp == 0:
                if next == 1:
                    result = '1' + result
                else:
                    result = '0' + result
                next = 0
            elif tmp == 1:
                if next == 1:
                    result = '0' + result
                    next = 1
                else:
                    result = '1' + result
                    next = 0
            else:
                if next == 1:
                    result = '1' + result
                    next = 1
                else:
                    result = '0' + result
                    next = 1
        if next == 1:
            return '1' + result
        else:
            return result

s = Solution()
print(s.addBinary('10', '1'))
