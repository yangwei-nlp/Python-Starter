# 解题思路：
# 能凑成回文：最多只有一个字母是奇数次数，其它都是偶数
class Solution:
    def canPermutePalindrome(self, s):
        from collections import Counter
        single_num = 0  # 落单的字符数目
        for char, count in Counter(s).items():
            if count % 2 == 1:
                single_num += 1
                if single_num > 1:
                    return False
        return True

s = Solution()
print(s.canPermutePalindrome('taafvahs'))