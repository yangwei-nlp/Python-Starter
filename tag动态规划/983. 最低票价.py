# class Solution:
#     def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
#         dp = [0] * (len(days) + 1)
#         for i in range(1, len(days)+1):
#             if days[i-1] - 7 <= 0:
#                 dp[i] = min(costs[1], dp[i-1] + costs[0])
#                 continue
#             elif days[i - 1] - 30 <= 0:
#                 dp[i] = min(costs[2], costs[1], dp[i - 1] + costs[0])
#                 continue
#             for j in range(i, -1, -1):
#                 if days[j-1] < days[i-1] - 7:
#                     temp_cost = min(dp[j+1] + costs[1], dp[i-1] + costs[0])
#                 elif days[j-1] < days[i-1] - 30:
#                     dp[i] = min(dp[j+1] + costs[2], temp_cost)
#                     break
#                 else:
#                     dp[i] = dp[i-1] + costs[0]
#         return dp[-1]
# 上面这种方法思路是完全正确的，但是如何用程序找到7天前的那天，这是很麻烦的一件事情，不如下面这种方法，
# 虽然耗了内存，但是程序简单了很多

# class Solution:
#     def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
#         n = len(days)
#         dp = [0] * 366
#         go = set(days)
#         for i in range(1, 366):
#             if i in go:
#                 dp[i] = min(dp[i-1] + costs[0], dp[max(i-7, 0)] + costs[1], dp[max(i-30, 0)] + costs[2])
#             else:
#                 dp[i] = dp[i-1]
#         return dp[days[-1]]

class Solution:
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
        n = len(days)
        dp = [0] * 366  # 因为365天，再加上一个0，共366个dp值
        go = set(days)
        for i in range(1, 366):
            if i in go:
                dp[i] = min(dp[i-1] + costs[0], dp[max(i-7, 0)] + costs[1], dp[max(i-30, 0)] + costs[2])
            else:
                dp[i] = dp[i-1]  # 主要为了把空缺的天数填满，以便后续返回查找
        return dp[days[-1]]

# class Solution:
#     def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
#         dp, weeks, months = [0] * (len(days) + 1), 0, 0
#         for i in range(len(days)):
#             while days[weeks] < days[i] - 6:
#                 weeks += 1
#             while days[months] < days[i] - 29:
#                 months += 1
#             dp[i + 1] = min((dp[i] + costs[0], dp[weeks] + costs[1], dp[months] + costs[2]))
#         return dp[-1]
s = Solution()
print(s.mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]))
