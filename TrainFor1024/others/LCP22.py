# 思路：先确定有多少行，再确定有多少列
# 难点 判断一下k==0和k==n*n的两种特殊情况
import math
class Solution:
    def paintingPlan(self, n: int, k: int) -> int:
        if k in [0, n*n]:
            # k==n*n时下面公式会多算很多种
            return 1

        def combinations(a):
            return math.factorial(n) // (math.factorial(a) * math.factorial(n-a))

        def total_combs(row, col):
            return combinations(row)*combinations(col)

        cnt = 0
        for row in range(n+1):
            for col in range(n+1):
                if row*n+(n-row)*col == k:
                    cnt += total_combs(row, col)
                    # print(row, col, total_combs(row, col))

        return cnt

s = Solution()
print(s.paintingPlan(2, 4))

