# coding=utf-8
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        string = str.lstrip()
        if len(string) == 0:
            return 0
        if string[0] not in "+-0123456789":
            return 0
        if len(string) == 1:
            if string in "0123456789":
                return int(string)
            else:
                return 0
        if string[0] == '-':
            if string[1] not in "0123456789":
                return 0
            num = ""
            for i in range(1, len(string)):
                if string[i] in "0123456789":
                    num += string[i]
                else:
                    break
            flag = -int(num)
            if flag < -2147483648:
                return -2147483648
            else:
                return flag
        elif string[0] in "0123456789":
            num = ""
            for i in range(len(string)):
                if string[i] in "0123456789":
                    num += string[i]
                else:
                    break
            flag = int(num)
            if flag > 2147483648-1:
                return 2147483647
            else:
                return flag
        if string[0] == "+":
            if string[1] not in "0123456789":
                return 0
            num = ""
            for i in range(1, len(string)):
                if string[i] in "0123456789":
                    num += string[i]
                else:
                    break
            flag = int(num)
            if flag > 2147483647:
                return 2147483647
            else:
                return flag
        # 由于发现输入的都是每个单词后有个空格，所以方法二可以利用首先str.split()分隔

solver = Solution()
print solver.myAtoi("4193 with words")

print solver.myAtoi("words and 987")

print solver.myAtoi("-")

print solver.myAtoi("+1")
