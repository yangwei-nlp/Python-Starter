# 规律：如果是快乐数，那么数字的平方和一定不会循环出现，反之，非快乐数，那么数字的平方和一定会重复，循环
class Solution:
    def isHappy(self, n: 'int') -> 'bool':
        num_string = str(n)
        sum_set = set()
        while True:
            temp_sum = 0
            for i in range(len(num_string)):
                temp_sum += int(num_string[i])**2
            if temp_sum == 1:
                return True
            elif temp_sum not in sum_set:
                sum_set.add(temp_sum)
            else:
                return False
            num_string = str(temp_sum)


# 其中在求平方和的时候没有用到普遍的算法，而是比较low的先转为字符串再求和
def sum_square(n):
    temp_sum = 0
    while n != 0:
        remainder = n % 10
        temp_sum += remainder**2
        n = n // 10
    return temp_sum

sum_square(19)