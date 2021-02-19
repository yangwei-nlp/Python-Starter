"""
首先要认识到，最终的有效字符串就是消除多余的括号，由此，目标就转换为了消除多余的括号，
一个朴素的思路：
在匹配时消掉最近的括号，然后剩下的括号就是需要最终保留的
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indices = []
        brackets = []
        for idx, char in enumerate(s):
            if char in ["(", ")"]:
                indices.append(idx)
                brackets.append(char)
        
        for i, (idx, brac) in enumerate(zip(indices[1:], brackets[1:])):
            i += 1
            if brackets[i-1] == '(' and brac == ')':
                del indices[i]
                del brackets[i]
                del indices[i-1]
                del brackets[i-1]
        print(indices)



s = Solution()
print(s.minRemoveToMakeValid("lee(t(c)o)de)"))

