# 方法一：蛮力法。
"""
先计算前面连续字符的长度，随后计算后面连续字符的长度
"""


class Solution:
    def countBinarySubstrings(self, s):
        result = 0
        for i in range(len(s)):
            first_length = 0
            second_length = 0
            j = i
            while j < len(s) and s[j] == s[i]:
                first_length += 1
                j += 1
            while j < len(s) and s[j] != s[i]:
                second_length += 1
                j += 1
                if first_length == second_length:
                    result += 1
                    break
        return result


# s = Solution()
# print(s.countBinarySubstrings('00001111'))


# 方法二：方法一其实还没用到问题背后的规律，本方法参考LeetCode他人评论
"""
先统计连续的0和1分别有多少个，如：111100011000，得到4323；在4323中的任意相邻两个数字，
取小的一个加起来，就是3+2+2 = 7.
"""


class Solution2:
    def countBinarySubstrings(self, s):
        candidate = []
        max_len = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                max_len += 1
            else:
                candidate.append(max_len)
                max_len = 1
        candidate.append(max_len)

        result = 0
        for j in range(len(candidate) - 1):
            result += min(candidate[j], candidate[j + 1])
        return result


s = Solution2()
print(s.countBinarySubstrings('111100011000'))
