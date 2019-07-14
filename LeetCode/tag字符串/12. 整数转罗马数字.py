class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_dict = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        divisor = [1000, 500, 100, 50, 10, 5, 1]
        ret = ""
        for div in divisor:
            if num // div != 0:
                ret += num_dict[div] * (num // div)
                num = num % div
            if num == 4:
                ret += "IV"
                num -= 4
            elif num == 9:
                ret += "IX"
                num -= 9
            elif num // 10 == 4:
                ret += "XL"
                num -= 40
            elif num // 10 == 9:
                ret += "XC"
                num -= 90
            elif num // 100 == 4:
                ret += "CD"
                num -= 400
            elif num // 100 == 9:
                ret += "CM"
                num -= 900

        return ret

s = Solution()
print(s.intToRoman(94))