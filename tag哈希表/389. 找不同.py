# O(2N)的复杂度
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import defaultdict
        s_dict = defaultdict(int)
        for char in s:
            s_dict[char] += 1

        for char in t:
            if char not in s_dict:
                # 字典查找是O(1)复杂度
                return char
            else:
                if s_dict[char] == 0:
                    return char
                else:
                    s_dict[char] -= 1


# 大神解法，利用字符的ASCII码来计算
class Solution2:
    def findTheDifference(self, s, t):
        a1 = sum([ord(x) for x in s])
        a2 = sum([ord(x) for x in t])
        return chr(a2-a1)