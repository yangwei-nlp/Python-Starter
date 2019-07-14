# class Solution:
#     def minCostClimbingStairs(self, cost):
#         """
#         :type cost: List[int]
#         :rtype: int
#         """
#         dp = [0] * len(cost)
#         if len(cost) == 1:
#             return cost[0]
#         elif len(cost) == 2:
#             return min(cost)
#         for i in range(2, len(cost)-1):
#             dp[i] = min(dp[i-2], dp[i-1]) + cost[i]
#         dp[-1] = min(dp[-2], dp[-3] + cost[-1])
#         return dp[-1]
#         # 此代码有问题
#         # 原理：每一步跳跃会选择最节省跳跃开支的跳跃方法，
#         # 而且、每次跳跃的新开支会记录下来，这样到最后就得到总的最少开支


# 法二：节省了内存占用，比较好的方法
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        l1, l2 = cost[0], cost[1]
        i = 2
        while i < len(cost):
            tmp = l2
            l2 = min(l2, l1) + cost[i]
            l1 = tmp
            i += 1
        return min(l1, l2)


s = Solution()
print(s.minCostClimbingStairs([0, 0, 0, 1]))
