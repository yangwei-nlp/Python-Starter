# https://blog.csdn.net/qq_34364995/article/details/80718195

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        dic = {}

        for item in nums1:
            if item in dic:
                dic[item] += 1
            else:
                dic[item] = 1

        for item in nums2:
            if item in dic and dic[item] > 0:
                res.append(item)
                dic[item] -= 1

        return res

nums1 = [1,2,2,1]
nums2 = [2, 2]

s = Solution()
print(s.intersect(nums1, nums2))