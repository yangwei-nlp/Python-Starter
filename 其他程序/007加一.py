# coding=utf-8
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits == [9]*len(digits):
            digits = [0]*len(digits)
            digits.insert(0, 1)
            return digits
        else:
            for i in range(len(digits)-1,-1,-1):
                if digits[i] != 9:
                    digits[i] += 1
                    if digits[i+1:] != []:
                        digits[i+1:] = [0]*(len(digits)-1-i)
                    break
            return digits

solver = Solution()
print solver.plusOne([1,2,3])
print solver.plusOne([4,3,9,1])
print solver.plusOne([9,9,9,9])
