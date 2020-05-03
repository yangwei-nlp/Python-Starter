from collections import Counter
class Solution:
    def findLUSlength(self, strs):
        s = dict(Counter(strs))
        string_to_count = sorted([*zip(s.keys(), s.values())], key=lambda x: len(x[0]), reverse=True)
        prev = set()
        # 一定注意遍历顺序：先取出最长的字符串
        for string, count in string_to_count:
            if count == 1:
                for tmp in prev:
                    if self.isSubsequence(string, tmp):
                        break
                else:
                    return len(string)
            else:
                prev.add(string)
        return -1


    def isSubsequence(self, s, t):
        # 详见 #LeetCode 392
        find_idx = -1
        for char in s:
            t = t[find_idx+1:]
            find_idx = t.find(char)
            if find_idx == -1:
                return False
        return True


s = Solution()
print(s.findLUSlength(["aabbcc", "aabbcc","c","e","aabbcd"]))