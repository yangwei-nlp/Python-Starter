# 参考：https://www.youtube.com/watch?v=uD1Cw1JbD8E
# 方法一：利用位运算相关知识，通过对被除数进行更新来达到目的
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_VALUE = 2 ** 31 - 1
        MIN_VALUE = - 2 ** 31
        if dividend == 0:
            return 0
        if divisor == 0:
            return MAX_VALUE

        if dividend == MIN_VALUE:
            if divisor == -1:
                return MAX_VALUE
            elif divisor == 1:
                return MIN_VALUE

        sign = 1
        if dividend < 0:
            sign = -sign
            dividend = -dividend
        if divisor < 0:
            sign = -sign
            divisor = -divisor

        res = 0
        while dividend >= divisor:
            shift = 0
            while dividend >= (divisor << shift):
                shift += 1
            res += 1 << (shift - 1)
            dividend -= (divisor << (shift -1))

        return sign * res


# s = Solution()
# print(s.divide(10, 3))


# 方法二：利用原始思想：被除数不断减去除数（前提是将除数和被除数全部化为正数），并且计数减的次数，
# 直到被除数被减至比除数还要小就停止，返回计数即可得到商
# 这里如果不使用二分查找的思想，那么复杂度为O(dividend/divisor)，反之则为O(log(dividend/divisor))
# 二分查找思想：第一次dividend减去divisor，如果dividend还是大于divisor，那么dividend减去
# 2*divisor（即divisor+divisor），这样依次类推，到了小于divisor的时候将差作为新的dividend
# 重复刚才过程，最后计数即可得到商
class Solution2:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_VALUE = 2 ** 31 - 1
        MIN_VALUE = - 2 ** 31
        if dividend == 0:
            return 0
        if divisor == 0:
            return MAX_VALUE

        if dividend == MIN_VALUE:
            if divisor == -1:
                return MAX_VALUE
            elif divisor == 1:
                return MIN_VALUE

        sign = 1
        if dividend < 0:
            sign = -sign
            dividend = -dividend
        if divisor < 0:
            sign = -sign
            divisor = -divisor

        saved_divisor = divisor
        res = 0
        while dividend >= divisor:
            count = 1
            while dividend >= (divisor + divisor):
                count += 1
                divisor += divisor
            res += (2 ** (count - 1))
            dividend -= divisor
            divisor = saved_divisor
        # return res * sign
        # 这里的乘法改进：
        return res if sign > 0 else 0 - res


s = Solution2()
print(s.divide(10, 3))
