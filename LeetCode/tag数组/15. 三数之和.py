class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res =[]
        i = 0
        for i in range(len(nums)):
            # 每次固定指针i，动态变化 l 和 r, 变化规则是可优化的地方
            if i == 0 or nums[i]>nums[i-1]:
                l = i+1
                r = len(nums)-1
                while l < r:
                    s = nums[i] + nums[l] +nums[r]
                    if s ==0:
                        # 如果等于0，则添加进去，肯定不会重复，因为重复的被移动走了，见下面的while循环
                        res.append([nums[i],nums[l],nums[r]])
                        l +=1
                        r -=1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while r > l and nums[r] == nums[r+1]:
                            r -= 1
                    elif s>0:
                        # 如果大于0，则说明右指针 r 数字过大，要往左移
                        r -=1
                    else :
                        # 如果小于0，则说明左指针 l 数字过大，要往右移
                        l +=1
        return res