from collections import defaultdict


class Solution:
    def wordPattern(self, pattern, str):
        wordList = str.split(" ")
        patternDict = defaultdict(list)
        for i, char in enumerate(pattern):
            patternDict[char].append(i)
        if len(patternDict) > len(wordList) or len(pattern) < len(wordList):
            return False
        words_pattern = []
        for tmp, index_list in patternDict.items():
            char = wordList[patternDict[tmp][0]]
            if char not in words_pattern:
                words_pattern.append(char)
            else:
                return False
            for index in index_list:
                if wordList[index] != char:
                    return False
        return True


s = Solution()
print(s.wordPattern("abba", "dog cat cat dog"))