# 方法居然这么慢，beat 5.7%
class Solution:
    def findLongestWord(self, s, d):
        if not d:
            return ""
        self.s = s
        max_len = 0
        min_long_str = ""
        for word in d:
            if len(word) > max_len:
                if self.help(word):
                    min_long_str = word
                    max_len = len(word)
            if len(word) == max_len:
                if word < min_long_str:
                    if self.help(word):
                        min_long_str = word
        return min_long_str

    def help(self, word):
        i, j = 0, 0
        while i < len(word) and j < len(self.s):
            if word[i] == self.s[j]:
                i += 1
                j += 1
            else:
                j += 1
        return True if i == len(word) else False


s = Solution()
print(s.findLongestWord("apple", ["zxc","vbn"]))