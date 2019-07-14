# -*- coding:utf-8 -*-
# class Solution:
#     def minNumberInRotateArray(self, rotateArray):
#         # write code here
#         if not rotateArray:
#             return 0
#
#         for i in range(len(rotateArray)-1):
#             if rotateArray[i+1] >= rotateArray[i]:
#                 continue
#             else:
#                 i += 1
#                 break
#         # 由于题目中说明了输入是一个非减排序的数组的一个旋转，故最小值一定在第一个元素以后
#         # return rotateArray[0]
#         return rotateArray[i]


class Solution:
    # 二分查找法
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        n = len(rotateArray)

        if n == 0:
            return 0

        first = 0
        last = n - 1
        mid = (first + last) // 2

        while last - first > 1:
            mid = (first + last) // 2
            # mid对应值要么大于等于first的值，要么小于等于last对应的值
            if rotateArray[mid] >= rotateArray[first]:
                # 因为是非减序列，所以大于等于
                first = mid
                # mid = (first + last) // 2
            elif rotateArray[mid] <= rotateArray[last]:
                # 因为是非减序列，所以小于等于
                last = mid
                # mid = (first + last) // 2
        return rotateArray[last]





s = Solution()
print(s.minNumberInRotateArray([1,1,1,1,1]))
