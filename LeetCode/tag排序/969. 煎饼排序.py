class Solution:
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # 思路来源：
        # https://blog.csdn.net/qq_17550379/article/details/85938407
        result = []
        for i in range(len(A)-1, 0, -1):
            max_index = self.findMaxIndex(A, i)
            if max_index < i:
                result.append(max_index+1)
                A[:max_index+1] = A[:max_index+1][::-1]
                result.append(i+1)
                A[:i+1] = A[:i+1][::-1]
        return result

    def findMaxIndex(self, A, i):
        """寻找前i个元素的最大值的索引"""
        max_index = 0
        for j in range(i+1):
            if A[j] > A[max_index]:
                max_index = j
        return max_index