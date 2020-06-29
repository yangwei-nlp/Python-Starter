# 调用库函数
# 其他方法当然可以，但是需要手写排序算法，然后记录到第k个大的数即return
class Solution:
    def findKthLargest(self, nums, k):
        nums.sort(reverse=True)
        return nums[k-1]


nums = [3, 2, 1, 5, 6, 4]
k = 2

s = Solution()
print(s.findKthLargest())