# class Solution:
#     def search(self, nums: 'List[int]', target: 'int') -> 'int':
#         i = 0
#         j = len(nums) - 1
#         if nums[i] == target:
#             return i
#         elif nums[j] == target:
#             return j
#         while j - i > 1:
#             mid_index = (i + j) // 2
#             if nums[mid_index] == target:
#                 return mid_index
#             elif nums[mid_index] < target:
#                 i = mid_index
#             else:
#                 j = mid_index
#         if nums[i] == target:
#             return i
#         else:
#             return -1


# 上述方法还是略复杂，主要是因为循环终止条件过于复杂
class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        i = 0
        j = len(nums) - 1
        while j - i > 1:
            mid_index = (i + j) // 2
            if nums[mid_index] == target:
                return mid_index
            elif nums[mid_index] > target:
                j = mid_index
            else:
                i = mid_index
        if nums[i] == target:
            return i
        elif nums[j] == target:
            return j
        else:
            return -1


s = Solution()
print(s.search([-1,0,3,5,9,12], 2))