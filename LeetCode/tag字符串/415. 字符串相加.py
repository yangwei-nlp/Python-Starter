class Solution:
    def addStrings(self, num1, num2):
        if len(num1) <= len(num2):
            short_num, long_num = num1, num2
        else:
            short_num, long_num = num2, num1

        sum_times = len(short_num)
        result = ''
        divisor = 0
        for i in range(-1, -(sum_times+1), -1):
            _sum = int(short_num[i]) + int(long_num[i]) + divisor

            divisor = _sum // 10
            remainder = _sum % 10

            result = str(remainder) + result

        # 另外，这里也可以直接在短的字符串前补零操作，对齐
        for i in range(-(sum_times+1), -(len(long_num)+1), -1):
            if divisor == 0:
                return long_num[:i+1] + result
            _sum = int(long_num[i]) + divisor

            divisor = _sum // 10
            remainder = _sum % 10

            result = str(remainder) + result
        if divisor != 0:
            result = str(divisor) + result
        return result


s = Solution()
print(s.addStrings('3824008', '92520'))
print(s.addStrings('1', '9'))

