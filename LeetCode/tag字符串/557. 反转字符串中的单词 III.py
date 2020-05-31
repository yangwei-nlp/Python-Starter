# 方法一：比较常规的方法，朴素算法
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        result = ""
        for word in words:
            result += word[::-1]
            result += ' '
        return result.strip()


s = Solution()
# print(s.reverseWords("Let's take LeetCode contest"))


# 方法二：比较秀的方法
"""
这里利用的是字符串反转的规律
"""
class Solution2:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])[::-1]

s = Solution2()
print(s.reverseWords("Let's take LeetCode contest"))
