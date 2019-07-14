# 被这道题坑死了，题目说的是最小的连续子数组，我没有看到连续二字，
# 导致我毫无思路，并且看别人的代码废了九牛二虎之力，当然还是没懂，
# 蓦然回首，题目竟是连续子数组，额，真想搬起石头砸自己的脚

# 方法：滑动窗口的方法
# 既然是连续子区间，那么用两个指针分别表示左边界和右边界，满足条件的就
# 获取区间长度，保存最小的区间长度即可
class Solution:
    def minSubArrayLen(self, s, nums) -> int:
        i, j = 0, 0
        temp_sum = 0
        min_gap = len(nums) + 1
        while j < len(nums):
            while j < len(nums) and temp_sum < s:
                temp_sum += nums[j]
                j += 1
            while temp_sum >= s:
                min_gap = min(j-i, min_gap)  # 注意这里是j-i，而非j-1-i
                temp_sum -= nums[i]
                i += 1
        if min_gap == len(nums) + 1:
            return 0
        else:
            return min_gap