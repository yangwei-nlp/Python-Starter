# https://blog.csdn.net/qq_17550379/article/details/80512745
# 双指针的方法很容易实现   O(N)
class Solution:
    def twoSum(self, numbers: 'List[int]', target: 'int') -> 'List[int]':
        i, j = 0, len(numbers) - 1
        for _ in range(len(numbers) - 1):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1


# 暴力解法，这种很low的思路我居然还没想到，哈哈  O(N^2)
class Solution2:
    def twoSum2(self, numbers: 'List[int]', target: 'int') -> 'List[int]':
        # 循环遍历法
        for i in range(len(numbers)):
            if target - numbers[i] in numbers[i + 1:]:
                return i + 1, numbers.index(target - numbers[i], i + 1) + 1


# 双指针法，但是空间复杂度为O(N)
# 大概思路：创建字典，遍历每个数字，将target和每个数字的差存入字典，
# 如果遍历到某个元素的值等于字典里面的差，说明找到了，return即可
class Solution3:
    def twoSum3(self, numbers: 'List[int]', target: 'int') -> 'List[int]':
        dic = {}
        for i in range(len(numbers)):
            if target - numbers[i] in dic:
                return [dic[target - numbers[i]] + 1, i + 1]
            else:
                dic[numbers[i]] = i


# 二分查找法，复杂度O(nlogn)
# 大概思路：遍历每个元素，然后使用二分查找法 从该元素后的所有元素中
# 查找是否存在target-该元素值的大小
class Solution4:
    def twoSum4(self, numbers: 'List[int]', target: 'int') -> 'List[int]':
        for i in range(len(numbers)):
            j = self.binary_search(numbers, i+1, target-numbers[i])
            if j:
                return [i+1, j+1]

    def binary_search(self, numbers, i, find):
        j = len(numbers) - 1
        while i <= j:
            mid = (i + j) // 2
            if numbers[mid] == find:
                return mid
            elif numbers[mid] > find:
                j = mid - 1
            else:
                i = mid + 1
        return False