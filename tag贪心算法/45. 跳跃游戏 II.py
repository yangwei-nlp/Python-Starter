class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 思路：当前步无论如何都是要跳的，应该选择哪种跳法最合适？贪心法则：
        # 应该跳到：在当前步内能跳的范围内，使得下一步能够达到最远距离的那一点
        # 这样每一步跳的都是当前能够够着的最远距离，那么总的来说贪心解就是最优解了
        if len(nums) == 1:
            return 0
        count = 0
        i = 0
        while i + nums[i] < len(nums) - 1:
            longest_index = i + nums[i]
            best_i = i
            for j in range(i+1, nums[i]+i+1):
                if nums[j] + j > longest_index:
                    longest_index = nums[j] + j
                    best_i = j
            i = best_i
            count += 1
        return count + 1

s = Solution()
print(s.jump([1,1,1,1]))