# 法一，时间复杂度倒是很低为O(N)，但是发现空间复杂度也为O(N)，不符合题目要求
# class Solution:
#     def findDuplicate(self, nums: 'List[int]') -> 'int':
#         sorted_nums = sorted(nums)
#         for i in range(len(sorted_nums)-1):
#             if sorted_nums[i] == sorted_nums[i+1]:
#                 return sorted_nums[i]


# 法二，二分查找，应用到了鸽笼原理
# class Solution:
#     def findDuplicate(self, nums: 'List[int]') -> 'int':
#         i = 0
#         j = len(nums)-1-1
#         while j - i > 1:
#             mid = (i + j) // 2
#             cnt = 0  # nums中在1-n序列中mid索引左侧的数字的个数
#             for num in nums:
#                 if num <= mid+1 and num >= i+1:
#                     cnt += 1
#             if cnt > (mid - i) + 1:
#                 j = mid
#             else:
#                 i = mid + 1
#         cnt_i = 0
#         for num in nums:
#             if num == i+1:
#                 cnt_i += 1
#         if cnt_i > 1:
#             return i + 1
#         else:
#             return j + 1


# 关于总数计算边界的优化
# class Solution:
#     def findDuplicate(self, nums: 'List[int]') -> 'int':
#         i = 1
#         j = len(nums)-1
#         while j - i > 1:
#             mid = (i + j) // 2
#             cnt = 0  # nums中在1-n序列中mid左侧数字的总数
#             for num in nums:
#                 if num <= mid:
#                     cnt += 1
#             if cnt > mid:
#                 j = mid
#             else:
#                 i = mid + 1
#         cnt_i = 0
#         for num in nums:
#             if num <= i:
#                 cnt_i += 1
#         return i if cnt_i > i else j



class Solution:
    def findDuplicate(self, nums: 'List[int]') -> 'int':
        i = 1
        j = len(nums)-1
        while j > i:  # 巧妙设置i=mid +1,就可以这样，法二那样多麻烦啊
            mid = (i + j) // 2
            cnt = 0  # nums中在1-n序列中mid左侧数字的总数
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt > mid:
                j = mid
            else:
                i = mid + 1  # 优秀
        return i


s = Solution()
print(s.findDuplicate([1,3,4,2,2]))
