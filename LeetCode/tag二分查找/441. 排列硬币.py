# class Solution:
#     def arrangeCoins(self, n: 'int') -> 'int':
#         if n == 1:
#             return 1
#         if n == 0:
#             return 0
#         temp_sum = 0
#         for i in range(1, n+1):
#             if n >= temp_sum and n < temp_sum + i:
#                 return i - 1
#             else:
#                 temp_sum += i


# 同一思想，但是程序妙不可言
# class Solution:
#     def arrangeCoins(self, n: 'int') -> 'int':
#         i = 1
#         while n >= i:
#             n -= i
#             i += 1
#         return i - 1



# 使用二分查找法来降低复杂度至O(logN)
class Solution:
    def arrangeCoins(self, n: 'int') -> 'int':
        if n == 0:
            return 0
        i = 1
        j = n
        while j - i > 1:
            mid_val = (i + j) // 2
            if n < mid_val*(mid_val+1) / 2:
                j = mid_val
            elif n > mid_val*(mid_val+1) / 2:
                i = mid_val
            else:
                return mid_val
        return i

s = Solution()
print(s.arrangeCoins(5))