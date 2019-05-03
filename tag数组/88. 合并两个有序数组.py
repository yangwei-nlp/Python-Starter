# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: void Do not return anything, modify nums1 in-place instead.
#         """
#         if n == 0:
#             return
#         i = 0
#         j = 0
#         while i < j + m and j < n:
#             if nums1[i] > nums2[j]:
#                 nums1[i + 1:m] = nums1[i:m-1]
#                 nums1[i] = nums2[j]
#                 j += 1
#             else:
#                 i += 1
#         if j != n:
#             nums1[i:] = nums2[j:]
# s = Solution()
# nums1 = [1,2,4,5,6,0]
# nums2 = [3]
# s.merge(nums1,5,nums2,1)
# print(nums1)
# print(nums2)


# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: void Do not return anything, modify nums1 in-place instead.
#         """
#         # 万般尝试皆bug，无奈只能用sort
#         nums1[m:] = nums2[::]
#         nums1.sort()
#         # 思路，先将两个数组融合，然后将nums1进行排序
#         # 当然，这种做法毫无算法可言


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # https://blog.csdn.net/weixin_31866177/article/details/82947561
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if m == 0:
            nums1[:n] = nums2[:n]
        # 最终根据网上的思路，自己手写实现，还是比较有成就感的
