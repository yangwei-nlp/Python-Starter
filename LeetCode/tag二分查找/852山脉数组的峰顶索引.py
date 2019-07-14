class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        first = 0
        last = len(A) - 1

        while last - first > 1:
            mid = (first + last) // 2
            if A[mid + 1] > A[mid]:  # 条件1
                first = mid
            elif A[mid + 1] < A[mid]:  # 条件2
                last = mid
        return last  # 最后一次循环肯定是条件2满足，所以返回last
