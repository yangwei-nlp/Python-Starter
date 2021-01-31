from typing import List
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr = set(arr)
        all_arr = set(list(range(1, max(arr)+1)))
        return list(all_arr - arr)[k-1]


arr = [2,3,4,7,11]
k = 5
s = Solution()
print(s.findKthPositive(arr, k))
