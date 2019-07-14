class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 不涉及什么算法，但是要对python的list、tuple、dict要熟
        ret = {}
        for string in strs:
            tmp_key = tuple(sorted(list(string)))
            if tmp_key in ret:
                ret[tmp_key].append(string)
            else:
                ret[tmp_key] = [string]
        return list(ret.values())