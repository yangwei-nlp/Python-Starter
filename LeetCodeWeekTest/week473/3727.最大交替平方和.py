from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        minus = len(nums) // 2
        nums_abs = [abs(num) for num in nums]
        nums_abs_sorted = sorted(nums_abs)

        ret = 0
        minus_threshold_idx = minus - 1
        for i in range(len(nums)):
            num = nums_abs_sorted[i]
            if i <= minus_threshold_idx:
                ret -= num**2
            else:
                ret += num**2
        return ret