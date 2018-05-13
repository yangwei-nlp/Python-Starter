# coding=utf-8
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        out = list(set(nums1).intersection(set(nums2)))
        output = []
        for i in range(len(out)):
            num = out[i]
            # 计算out中的元素在nums1中出现次数
            n1 = 0
            for j in range(nums1.index(num), len(nums1)):
                if nums1[j] == num:
                    n1 += 1
                else:
                    break
            # 计算out中的元素在nums2中出现次数
            n2 = 0
            for k in range(nums2.index(num), len(nums2)):
                if nums2[k] == num:
                    n2 += 1
                else:
                    break
            length = n1 if n1 <= n2 else n2
            output += [out[i]]*length
        return output

solver = Solution()
print solver.intersect([1,2,2,1], [2,2])