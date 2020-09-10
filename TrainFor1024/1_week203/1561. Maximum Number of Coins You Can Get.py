# 2020-8-28
# 脑袋犹如静止，思维停滞
class Solution:
    def maxCoins(self, piles):
        piles.sort()
        ret = 0
        first_and_second = piles[len(piles) // 3: ]
        for i in range(0, len(first_and_second), 2):
            ret += first_and_second[i]
        return ret
    

# s = Solution()
# piles = [2,4,1,2,7,8]
# print(s.maxCoins(piles))

# 122478


# 2020-9-10
class Solution2:
    def maxCoins(self, piles):
        piles.sort()
        ret = 0
        for i in range(len(piles)//3, len(piles), 2):
            ret += piles[i]
        return ret

piles = [2,4,1,2,7,8]
s = Solution2()
s.maxCoins(piles)
