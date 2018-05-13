# coding=utf-8
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        string = str(x)
        if string[0] == '-':
            string = '-' + string[-1:0:-1]
        else:
            string = string[::-1]
        if string[-1] == '0':
            string = string[:-1]
        number = int(string)
        if  number >= -2147483648L and number <= 2147483647:
            return number
        else:
            return 0

solver = Solution()
print solver.reverse(2247483647)