# 方法一：re正则表达式工具包
"""
re.split的特点是可以按照自定义的模式去split，这里我们按照一个或多个空格split
re.sub('\s+', ' ', s), 表示将s中一个或多个空格替换为一个空格
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        import re
        words = re.split('\s+', s.strip())
        return ' '.join(words[::-1])


s = Solution()
# print(s.reverseWords('a good    example!'))
# print(s.reverseWords("  hello    world!  "))



# 方法二：python内置的split()方法就可以实现上述操作
class Solution2:
    def reverseWords(sel, s: str) -> str:
        words_iterator = s.split()  # 分割好的单词列表
        # reversed(words_iterator) 生成一个反转的迭代器对象
        return ' '.join(reversed(words_iterator))

s2 = Solution2()
print(s2.reverseWords("  hello    world!  "))
