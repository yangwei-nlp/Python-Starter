# -*- coding: utf-8 -*-
"""
Description :   
     Author :   Yang
       Date :   2020/1/15
"""


class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0

        max_list = []
        for idx, p in enumerate(prices[:-1]):
            tmp_income = 0
            tmp_list = prices[idx + 1:]
            for sold_p in tmp_list:
                if sold_p - p > tmp_income:
                    tmp_income = sold_p - p
            max_list.append(tmp_income)
        return max(max_list)


# 双重遍历，复杂度为n*(n-1)/2
s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))


# 一次遍历，复杂度n，维护一个最大利润和最低价格，
# 因为在遍历，所以会找到更大的卖出价格的点，只要不断更新最低买入价格和最大利润即可
class Solution2:
    def maxProfit(self, prices):
        best_buy_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < best_buy_price:
                best_buy_price = price
            elif price - best_buy_price > max_profit:
                max_profit = price - best_buy_price
        return max_profit
