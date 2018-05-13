# coding=utf-8
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit

solver = Solution()
print solver.maxProfit([7,1,5,3,6,4])
print solver.maxProfit([1,2,3,4,5])
print solver.maxProfit([7,6,4,3,1])
