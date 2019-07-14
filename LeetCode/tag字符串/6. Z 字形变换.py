class Solution:
    def convert(self, s: 'str', numRows: 'int') -> 'str':
        if not s or len(s) == 1 or numRows == 1: return s
        length = len(s)
        column_gap = 2 * numRows - 2
        res = ""
        for i in range(numRows):
            # 遍历每行的字符，将每行的字符一次性相加
            for j in range(i, length, column_gap):
                # j代表在s中是第j个字符
                res += s[j]
                if i != 0 and i != numRows - 1 and j + column_gap - 2 * i < length:
                    res += s[j + column_gap - 2 * i]
        return res


s = Solution()
print(s.convert("PAYPALISHIRING", 3))
