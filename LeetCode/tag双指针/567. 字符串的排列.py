# 这个解法的算法错误，反例：
# "hello"
# "ooolleoooleh"
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
        # continuous_len = 0
        # i = 0
        # while continuous_len <= len(s1) and i <= len(s2)-1:
        #     if continuous_len == len(s1):
        #         return True
        #     char = s2[i]
        #     s1 = s1[:i]
        #     i += 1
        #     if char not in s1:
        #         continuous_len = 0
        #     else:
        #         continuous_len += 1
        # if continuous_len == len(s1):
        #     return True
        # return False


# 使用滑动窗口的方法
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         dict1, dict2 = {}, {}
#         for char in s1:
#             if char in dict1:
#                 dict1[char] += 1
#             else:
#                 dict1[char] = 1
#         i, j = 0, len(s1)
#         # 这是第一个窗口
#         for char in s2[i: j]:
#             if char in dict2:
#                 dict2[char] += 1
#             else:
#                 dict2[char] = 1
#
#         while j < len(s2):
#             if self.check(dict1, dict2):
#                 return True
#             dict2[s2[i]] -= 1
#             if s2[j] in dict2:
#                 dict2[s2[j]] += 1
#             else:
#                 dict2[s2[j]] = 1
#             i += 1
#             j += 1
#         if self.check(dict1, dict2):
#             return True
#         return False
#
#     def check(self, dict1, dict2):
#         for char in dict1:
#             if char not in dict2:
#                 return False
#             if dict1[char] != dict2[char]:
#                 return False
#         return True

# 参考下大神写的简洁版本
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def check12(d1,d2):    #判断d1,d2里的字频是否相同
            for x in d1.keys():
                if x not in d2:return False
                if d1[x]!=d2[x]:return False
            return True


        if len(s2)<len(s1):return False
        d1,d2={},{}
        for x in s1:
            d1[x]=d1.get(x,0)+1

        i,j=0,len(s1)
        for x in s2[i:j]:
            d2[x]=d2.get(x,0)+1
        if check12(d1,d2):return True

        while j<len(s2):
            d2[s2[i]]-=1
            i+=1
            j+=1
            d2[s2[j-1]]=d2.get(s2[j-1],0)+1
            if check12(d1,d2):return True
        return False

s = Solution()
# print(s.checkInclusion("hello", "ooolleoooleh"))
# print(s.checkInclusion("rokx", "otrxvfszxroxrzdsltg"))
print(s.checkInclusion("adc", "dcda"))
