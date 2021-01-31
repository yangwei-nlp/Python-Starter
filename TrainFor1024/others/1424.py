# 思路：Huahua
# 要点：每个对角线上的i+j是个定值，每行去遍历时，碰到i+j值时，添加进入list
# list中越往后的元素应该靠前输出

# 理解if i+j == len(rst):
#         rst.append([])
# 实质是i+j+1 == len(rst)+1

from typing import List
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        "使用dict存储"
        diagonal = {}
        for i, lst in enumerate(nums):
            for j, num in enumerate(lst):
                if i+j not in diagonal:
                    # 新对角线
                    diagonal[i+j] = []
                diagonal[i+j].append(num)

        rst = []
        for i in range(len(diagonal)):
            rst.extend(list(reversed(diagonal[i])))
        return rst

    def findDiagonalOrder_2(self, nums: List[List[int]]) -> List[int]:
        "使用list存储"
        rst = []
        for i, lst in enumerate(nums):
            for j, num in enumerate(lst):
                if i+j == len(rst):
                    rst.append([])
                rst[i+j].append(num)

        result = []
        for lst in rst:
            result.extend(lst[::-1])
        return result



nums = [[1,2,3],[4,5,6],[7,8,9]]
s = Solution()
# print(s.findDiagonalOrder(nums))
print(s.findDiagonalOrder_2(nums))
