class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 简单的二分查找算法，通过两个二分查找程序。时间复杂度为O(logM + logN)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        firstElem = [matrix[i][0] for i in range(len(matrix))]
        i = 0
        j = len(firstElem) - 1
        while i != j:
            if firstElem[i] == target or firstElem[j] == target:
                return True
            middle_index = (i + j) // 2
            if firstElem[middle_index] == target:
                return True
            elif firstElem[middle_index] > target:
                j = middle_index
            else:
                i = middle_index
            if j - i == 1:
                if firstElem[j] < target:
                    i = j
                break

        search_list = matrix[i]
        i = 0
        j = len(search_list) - 1
        if i == j:
            return search_list[i] == target
        while i != j:
            middle_index = (i + j) // 2
            if search_list[middle_index] == target:
                return True
            elif search_list[middle_index] > target:
                j = middle_index
            else:
                i = middle_index
            if j - i == 1:
                return search_list[i] == target or search_list[j] == target
        return False


s = Solution()
print(s.searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,50]], target=30))