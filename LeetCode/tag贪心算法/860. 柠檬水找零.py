class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        wallet = {5: 0, 10: 0}
        # 20美元的对于找零没用，所以不考虑
        for bill in bills:
            if bill == 5:
                wallet[5] += 1
            elif bill == 10:
                if wallet[5] == 0:
                    return False
                else:
                    wallet[5] -= 1
                    wallet[10] += 1
            else:
                if wallet[5] >= 1 and wallet[10] >= 1:
                    wallet[10] -= 1
                    wallet[5] -= 1
                elif wallet[5] >= 3:
                    wallet[5] -= 3
                else:
                    return False
        return True

s = Solution()
print(s.lemonadeChange([5,5,10,10,20]))
