# 利用数学的思路就可以解决
class Solution:
    def complexNumberMultiply(self, a, b):
        a_1, a_2 = int(a.split('+')[0]), int(a.split('+')[1][:-1])
        b_1, b_2 = int(b.split('+')[0]), int(b.split('+')[1][:-1])
        ret_1 = a_1 * b_1 - a_2 * b_2
        ret_2 = a_1 * b_2 + a_2 * b_1
        return "{}+{}i".format(ret_1, ret_2)


s = Solution()
print(s.complexNumberMultiply("1+-1i", "1+-1i"))
