# 不需要想，直接按照要求实现，easy题，O(nlogn)
class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import defaultdict
        s_dict = defaultdict(int)
        for char in s:
            s_dict[char] += 1
        ret = sorted(s_dict.items(), key=lambda item: item[1], reverse=True)
        return "".join([item[0]*item[1] for item in ret])


# 关于字典的另外一种骚操作
class Solution2:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_map = {}
        for i in s:
            str_map[i] = str_map.get(i, 0) + 1  # 牛批

        tmp = sorted(str_map.items(), key=lambda d:d[1], reverse=True)
        return ''.join([key*val for key, val in tmp])