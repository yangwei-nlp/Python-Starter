class NumArray:
    def __init__(self, nums):
        self.array = nums
        if nums:
            self.dp = [None] * len(self.array)
            self.dp[0] = self.array[0]
            for k in range(1, len(self.dp)):
                self.dp[k] = self.dp[k-1] + self.array[k]

    def sumRange(self, i, j):
        if i == 0:
            return self.dp[j]
        else:
            return self.dp[j] - self.dp[i-1]

array = NumArray([-2,0,3,-5,2,-1])
print(array.sumRange(0, 2))
print(array.sumRange(2, 5))
print(array.sumRange(0, 5))


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)