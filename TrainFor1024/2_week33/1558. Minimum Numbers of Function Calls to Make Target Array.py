class Solution:
    def minOperations(self, nums):
        odd_num = 0
        even_num = 0
        
        for num in nums:
            if num % 2 == 1:
                odd_num += 1
        max_num = max(nums)

        op_1_num = max_num // 2
        if max_num % 2 == 0:
            return op_1_num + odd_num + len(nums)
        else:
            return op_1_num + odd_num + len(nums)
        print(2333)


nums = [1,5]
s = Solution()
s.minOperations(nums)
