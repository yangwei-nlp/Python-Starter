# 题目理解错了，以为是不能两两相邻，然后移除后的空位就搁在那里

class Solution:
    def minCost(self, s, cost):
        if len(s) == 1:
            return 0
        delete_cost = cost[0]
        remain_cost = 0
        total_cost = 0
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                total_cost += min(remain_cost, delete_cost)
                remain_cost = 0
                delete_cost = cost[i]
            else:
                remain_cost, delete_cost = delete_cost, cost[i] + remain_cost
        if s[i] == s[i-1]:
            total_cost += min(remain_cost, delete_cost)
        return total_cost


s = "bbbaaa"
cost = [4,9,3,8,8,9]
ss = Solution()
print(ss.minCost(s, cost))
