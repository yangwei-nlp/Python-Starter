# 错误法：没有注意到题目中的"连续子数组"字眼，我以为是任意位置的组合呢
class Solution2:
    def minSubArrayLen(self, s, nums):
        nums.sort(reverse=True)
        count = 0  # 使用的元素个数
        total_sum = 0  # 总和
        for num in nums:
            count += 1
            total_sum += num
            if total_sum >= s:
                return count
        return 0


# 法二：基本思想就是，初始化一个最小的窗口，然后不断的右移，右移过程中如果temp_sum超过s，
# 就将左指针右移，直到temp_sum小于s。如果temp_sum小于s，则右移右指针。在这个移动过程中
# 记录下元素个数
class Solution:
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0

        n = len(nums)
        total_sum = 0
        min_gap = n + 1
        l, r = 0, 0
        while r < n:  # 注意到右指针会一直在左指针的右边
            total_sum += nums[r]
            while total_sum >= s:
                total_sum -= nums[l]
                min_gap = min(min_gap, r - l + 1)
                l += 1
            r += 1
        return 0 if min_gap == n + 1 else min_gap

s = 7
nums = [2, 3, 1, 2, 4, 3]


sl = Solution()
print(sl.minSubArrayLen(s, nums))
