class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        min_len = min([len(string) for string in strs])
        count = 1
        while count <= min_len:
            for i in range(len(strs)-1):
                if strs[i][:count] != strs[i+1][:count]:
                    return strs[0][:count - 1]
            count += 1
        return strs[0][:count-1]
s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["a","b"]))
print(s.longestCommonPrefix(["aa","a"]))
# class Solution:
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if not strs:
#             return ""
#         if len(strs) == 1:
#             return strs[0]
#         minl = min([len(x) for x in strs])
#         end = 0
#         while end < minl:
#             for i in range(1,len(strs)):
#                 if strs[i][end]!= strs[i-1][end]:
#                     return strs[0][:end]
#             end += 1
#         return strs[0][:end]