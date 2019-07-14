class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # 思路不是很懂
        # 注意，双重for循环的思路可行，但是超时
        if sum(gas)<sum(cost):
            # 如果总油量少于总消耗量，当然无论如何都跑不完一圈
            return -1
        # 如果总油量多于
        res = 0
        station = 0
        for i in range(len(gas)):
            if res+gas[i]-cost[i]<0:
                station = i+1
                res = 0
            else:
                res = res+gas[i]-cost[i]
        return station

s = Solution()
print(s.canCompleteCircuit([1,2,3,4,3,2,4,1,5,3,2,4],
                           [1,1,1,3,2,4,3,6,7,4,3,1]))


