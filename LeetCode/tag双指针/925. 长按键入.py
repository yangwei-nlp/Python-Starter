# 法一，有bug
# class Solution:
#     def isLongPressedName(self, name: str, typed: str) -> bool:
#         i = 0
#         j = 0
#         while i <= len(name) - 1 and j <= len(typed) - 1:
#             if name[i] != typed[j]:
#                 return False
#             while i <= len(name) - 1 and j <= len(typed) - 1 and name[i] == typed[j]:
#                 j += 1
#             i += 1
#         return True

# 法二，思路无比简单，但是bug无比多，崩溃，耗时2小时整
# class Solution:
#     def isLongPressedName(self, name: str, typed: str) -> bool:
#         i = 0
#         j = 0
#         while i <= len(name) - 1 and j <= len(typed) - 1:
#             temp_i = name[i]
#             temp_j = typed[j]
#             cnt_i = 1
#             while i < len(name) - 1 and j <= len(typed) - 1 and name[i] == name[i+1]:
#                 cnt_i += 1
#                 i += 1
#             cnt_j = 1
#             while i <= len(name) - 1 and j < len(typed) - 1 and typed[j] == typed[j+1]:
#                 cnt_j += 1
#                 j += 1
#             if temp_i == temp_j and cnt_j >= cnt_i:
#                 i += 1
#                 j += 1
#                 cnt_i = 1
#                 cnt_j = 1
#             else:
#                 return False
#         if i != len(name):
#             return False
#         return True


# 别人的思路，更简洁
class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if name[0] != typed[0] or name[-1] != typed[-1]:
            return False
        i, j, len_n, len_t = 0, 0, len(name), len(typed)
        while i < len_n and j < len_t:
            if name[i] == typed[j]:
                i, j = i + 1, j + 1
            elif name[i - 1] == typed[j]:
                j += 1
            else:
                return False
        return True if i == len_n else False


s = Solution()
print(s.isLongPressedName(name = "leelee", typed = "lleeelee"))
print(s.isLongPressedName(name = "plpkoh", typed = "plppkkh"))