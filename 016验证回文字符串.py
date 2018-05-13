# coding=utf-8
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = [char.lower() for char in s if char.isalnum()]
        flag = True
        for i in range(len(string)/2):
            if string[i] != string[len(string)-1-i]:
                flag = False
                break
        return flag

solver = Solution()
print solver.isPalindrome("race a car")

print solver.isPalindrome("A man, a plan, a canal: Panama")
