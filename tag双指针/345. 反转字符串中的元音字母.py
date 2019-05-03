# 偷懒了，将互换字符和指针移动一起实现，但是bug满天飞，水平差了一丢丢
# class Solution:
#     def reverseVowels(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         if len(s) == 0:
#             return ""
#         char_list = ['a'] * len(s)
#         vowel_list = ['a', 'e', 'i', 'o', 'u']
#         i = 0
#         j = len(s) - 1
#         while i < j:
#             if s[i] not in vowel_list:
#                 char_list[i] = s[i]
#                 i += 1
#             if s[j] not in vowel_list:
#                 char_list[j] = s[j]
#                 j -= 1
#             if s[i] in vowel_list and s[j] in vowel_list:
#                 char_list[i], char_list[j] = s[j], s[i]
#                 i += 1
#                 j -= 1
#             if j - i == 1:
#                 char_list[i], char_list[j] = s[i], s[j]
#         char_list[i] = s[i]
#         result = ""
#         for char in char_list:
#             result += char
#         return result


class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_list = list(s)
        vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] not in vowel_list:
                i += 1
            elif s[j] not in vowel_list:
                j -= 1
            else:
                char_list[i], char_list[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(char_list)
        # 将互换字符和指针移动分开就简单了