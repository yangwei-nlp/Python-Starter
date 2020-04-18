# 方法一：方法比较naive，直接暴力判断，没有使用到任何规律
class Solution:
    def canConstruct(self, ransomNote, magazine):
        remain_str = magazine
        for char in ransomNote:
            if char not in remain_str:
                return False
            else:
                remain_str = remain_str[:remain_str.index(char)] + \
                             remain_str[remain_str.index(char)+1:]
        return True


s = Solution()
print(s.canConstruct('aa', 'ab'))


# 方法二：如果ransomNote可以由magazine组成，那么ransomNote中
# 每个unique字符的出现次数是小于或等于该字符在magazine中出现次数的
class Solution2:
    def canConstruct(self, ransomNote, magazine):
        # 一一对应
        uniques = set(ransomNote)
        for char in uniques:
            if ransomNote.count(char) > magazine.count(char):
                return False
        return True


s = Solution2()
print(s.canConstruct('aa', 'ab'))