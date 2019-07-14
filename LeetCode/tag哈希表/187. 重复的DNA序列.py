# 字典真是强大啊，这么牛批的方法，O(N)的时间和空间复杂度
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        series_dict = {}
        for i in range(len(s)-9):
            if s[i: i+10] in series_dict:
                series_dict[s[i: i+10]] += 1
            else:
                series_dict[s[i: i+10]] = 1
        return [key for key, value in series_dict.items() if value > 1]


# 这个collections.defaultdict感觉很好用，不错
import collections
class Solution2:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        series_dict = collections.defaultdict(int)
        for i in range(len(s)-9):
            series_dict[s[i: i+10]] += 1
        return [key for key, value in series_dict.items() if value > 1]


