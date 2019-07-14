# -*- coding:utf-8 -*-
# class Solution:
#     def reOrderArray(self, array):
#         # write code here
#         odd = []
#         even = []
#         for item in array:
#             if item&1 == 1:
#                 odd.append(item)
#             else:
#                 even.append(item)
#         return odd + even

class Solution:
    def reOrderArray(self, array):
        # write code here
        for i in range(len(array)):
            if array[i]&1 == 0:
                temp = array[i]
                for j in range(i,len(array)-1):
                    array[j] = array[j+1]
                array[-1] = temp
        return array
s = Solution()
print(s.reOrderArray([3,10,4,2,15,4,6,8,5,4,10]))


language = ["c", "java", "c++", "php", "c", "python", "c"]
for i in range(len(language) - 1, -1, -1):
    if language[i]=="c":
        del language[i]
print(language)

a = 0
for name in language:
    print(name)
    if name == "c":
        del language[a]
    else:
        print(language[a])
        a = a + 1
