# 方法一，用到了栈的思想，先分割数字，然后判断标点符号，再去实现数学计算。
# 其中的正则表达式分割，可以自己实现。
import re
class Solution:
    def calculate(self, s: str) -> int:
        char_list = re.split(r"([+|\-|*|/])", s.replace(" ", ""))
        char_list.insert(0, "+")
        t_sum = 0
        eles = []
        for i, char in enumerate(char_list):
            if char.isdigit():
                if char_list[i-1] == "+":
                    eles.append(int(char))
                elif char_list[i-1] == "-":
                    eles.append(-int(char))
                elif char_list[i-1] == "*":
                    eles.append(int(eles.pop())*int(char))
                elif char_list[i-1] == "/":
                    last_int = int(eles.pop())
                    eles.append(int(last_int/int(char)))
        return sum(eles)


# s = Solution()
# string = "14-3/2"
# print(s.calculate(string))



from collections import deque
class Solution2:
    def calculate(self, s: str) -> int:
        n = len(s)
        s = deque(s)
        num = 0
        sign = "+"
        res = []
        for i in range(n):
            char = s.popleft()
            if char.isdigit():
                num = num * 10 + int(char)
            if char == "(":
                num = self.calculate(s)
            if (not char.isdigit() and char != " ") or not s:
                if sign == "+":
                    res.append(num)
                if sign == "-":
                    res.append(-num)
                if sign == "*":
                    res.append(res.pop() * num)
                if sign == "/":
                    res.append(int(res.pop() / num))
                num = 0
                sign = char
            if char == ")":
                break
        return sum(res)


# s2 = Solution2()
# string = "14-3/2"
# print(s2.calculate(string))


# my own version
class Solution3:
    def calculate(self, s: str) -> int:
        tmp_num = 0
        nums = [0]
        flag = '+'
        for i, char in enumerate(s):
            if char.isdigit():
                # 获取当前数字：如果是遇到数字就一直加
                tmp_num = tmp_num*10 + int(char)

            if char in ['+', '-', '*', '/'] or i==len(s)-1:
                # 遇到其他符号就停止，然后将当前数字加入list
                if flag == '+':
                    nums.append(tmp_num)
                elif flag == '-':
                    nums.append(-tmp_num)
                elif flag == '*':
                    nums.append(nums.pop()*tmp_num)
                elif flag == '/':
                    nums.append(int(nums.pop()/tmp_num))

                if flag == ' ':
                    continue
                else:
                    flag = char
                tmp_num = 0
        return sum(nums)


s2 = Solution3()
string = "14-3/2"
print(s2.calculate(string))
