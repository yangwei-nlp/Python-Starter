# 暴力解法，没有用到任何算法思想，并且超出时间限制。
# class Solution:
#     def maxArea(self, height: 'List[int]') -> 'int':
#         volume = [0] * len(height)
#         for i in range(1, len(height)):
#             temp_vol = 0
#             for j in range(i-1, -1, -1):
#                 temp_vol = max((i-j)*min(height[i], height[j]), temp_vol)
#             volume[i] = temp_vol
#         return max(volume)


# 使用双指针方法
class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':
        max_area = 0
        i = 0
        j = len(height) - 1
        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            if height[i] <= height[j]:
                # 如果左边木板更短，则左指针右移才可能使总容量更大（容量取决于更短的木板）
                # 反之右指针左移的话，容量只会更小或不变，而不会增加
                i += 1
            else:
                j -= 1
        return max_area