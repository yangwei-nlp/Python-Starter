# -*- coding:utf-8 -*-
import time
# class Solution:
# 递归方法
#     def Fibonacci(self, n):
#         # write code here
#         if n == 0:
#             return 0
#         if n < 3:
#             return 1
#         return self.Fibonacci(n-1) + self.Fibonacci(n-2)
#
# start = time.time()
# s = Solution()
# print(s.Fibonacci(39))
# end = time.time()
# print(end-start)

# -*- coding:utf-8 -*-
# 迭代方法
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        last = 0
        temp = 1
        if n == 1:
            return temp
        for i in range(n-1):
            temp, last = last + temp, temp
        return temp
start = time.time()
s = Solution()
print(s.Fibonacci(100))
end = time.time()
print(end-start)

# -*- coding:utf-8 -*-
# 这是动态规划的例子
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n >= 3:
            s = []*n
            s.append(1)
            s.append(1)
            for i in range(2,n):
                s.append(s[i-1]+s[i-2])
            return s[n-1]
#
# start = time.time()
# s = Solution()
# print(s.Fibonacci(100))
# end = time.time()
# print(end-start)