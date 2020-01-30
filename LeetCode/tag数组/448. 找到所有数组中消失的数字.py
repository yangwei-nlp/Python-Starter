# -*- coding: utf-8 -*-
"""
Description :   
     Author :   Yang
       Date :   2020/1/30
"""


class Solution:
    def findDisappearedNumbers(self, nums):
        ret = list(range(len(nums)))

        for num in nums:
            ret[num - 1] = -1

        return [n + 1 for n in ret if n >= 0]


s = Solution()
print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))


# [4, 3, 2, 7, 8, 2, 3, 1]
# []
# 方法二：大神。time: o(N), space: o(1)
# 思路：每个数n代表数组第n个位置是存在数字的，而且总有一个数没有指向某个位置
class Solution2:
    def findDisappearedNumbers(self, nums):
        for num in nums:
            index = abs(num) - 1
            nums[index] = - abs(nums[index])  # 仍然保留这个位置数字的信息，不然就找不到了
        return [i + 1 for i, num in enumerate(nums) if num > 0]


s2 = Solution2()
print(s2.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
