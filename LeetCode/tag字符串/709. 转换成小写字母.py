# 方法一：使用内置函数
class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()


s = Solution()
print(s.toLowerCase('Hello, World!'))


# 方法二：使用编码转换
"""
'A' - 'Z' 对应的 ascii值 是 65 - 90；
'a' - 'z' 对应的 ascii值 是 97 - 122；
大小字母转换相差32，解题只要记住ord(),chr()函数即可：
ord()函数就是用来返回单个字符的ascii值（0-255）或者unicode数值
chr()函数是输入一个整数【0，255】返回其对应的ascii符号
"""
class Solution2:
    def toLowerCase(self, str: str) -> str:
        ret = ''
        for s in str:
            if 65 <= ord(s) <= 90:
                ret += chr(ord(s) + 32)
            else:
                ret += s
        return ret


s2 = Solution2()
print(s2.toLowerCase('Hello, World!'))
