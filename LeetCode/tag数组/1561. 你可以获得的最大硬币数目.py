class Solution:
    def maxCoins(self, piles):
        piles.sort()
        ret = 0
        first_and_second = piles[len(piles) // 3: ]
        for i in range(0, len(first_and_second), 2):
            ret += first_and_second[i]
        return ret
    

s = Solution()
piles = [2,4,1,2,7,8]
print(s.maxCoins(piles))

# 122478
