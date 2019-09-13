"""
Description :   
     Author :   Yang
       Date :   2019/9/13
"""
# 思路一：
"""
观察例子得到一个思路，先排序，计算前三个元素和，再计算第2,3,4个元素之和，
再计算3,4,5个元素之和，这样可想而知漏掉很多种情况
"""

# 思路二：存在问题
"""
采用双指针的做法，固定住右端指针，左端指针和中间指针向右侧移动，但是出现
问题，因为右端指针固定住了，所以选的三个数字都包含数组中最大的那个数，显然
遗漏了很多情况，错误
"""
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        init_sum = nums[0] + nums[1] + nums[-1]
        init_diff = abs(init_sum - target)
        ret = init_sum
        r = len(nums) - 1
        for l in range(len(nums)-2):
            for mid in range(l+1, len(nums)-1):
                sum_all = nums[l] + nums[mid] + nums[-1]
                diff = abs(sum_all - target)
                if diff < init_diff:
                    ret = sum_all
        return ret


# s = Solution()
# print(s.threeSumClosest([-1, 2, 1, -4], 1))


# 思路三：https://blog.csdn.net/qq_17550379/article/details/83029688
"""
双指针做法，但是右端指针会根据条件来移动
先确定一个数 i，然后用两个指针 left 和 right 来滑动寻找另外两个数，
这种情况不会遗漏掉任何组合，另外注意每次确定 i时，注意right为len(nums)-1
每确定两个数，我们求出此三数之和，然后算和给定值的差的绝对值存在 
temp_diff 中，然后和 diff 比较并更新 diff 即可
"""
class Solution2:
    def threeSumClosest(self, nums, target):
        nums.sort()
        best_diff = float('inf')
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum_all = nums[i] + nums[l] + nums[r]
                temp_diff = abs(sum_all - target)
                if temp_diff < best_diff:
                    best_sum = sum_all
                    best_diff = temp_diff
                if sum_all > target:
                    r -= 1
                elif sum_all < target:
                    l += 1
                else:
                    return target
        return best_sum


s = Solution2()
print(s.threeSumClosest([-1, 2, 1, -4], 1))