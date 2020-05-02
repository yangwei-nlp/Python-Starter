# 最长特殊序列：该序列为某字符串独有的最长子序列。
"""
- 注意题目中的独有两个字，
- s1 = 'ab',s2 = 'a',因为ab是s1独有，所以最长子序列为ab，
- s1 = 'ab', s2 = 'ab', 因为ab是两个串都有，ab排除，a也是两个串都有，排除，b也是两个串都有，排除。所以最长特殊序列不存在，返回-1
- 通过以上分析，我们可以得出结论，如果：两个串相等（不仅长度相等，内容也相等），那么他们的最长特殊序列不存在。返回-1
- 如果两个串长度不一样，那么长的串   永远也不可能是   短串的子序列，即len(s1) > len(s2),则最长特殊序列为s1,返回长度大的数
"""
class Solution:
    def findLUSlength(self, a, b):
        if a == b:
            return -1
        else:
            return max(len(a), len(b))


s = Solution()
print(s.findLUSlength('aba', 'cdc'))
