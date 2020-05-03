class Solution:
    def detectCapitalUse(self, word):
        if word[0].isupper():
            # 首字母是大写
            if word.istitle() or word.isupper():
                return True
            else:
                return False
        else:
            # 首字母是小写
            if word.islower():
                return True
            else:
                return False
    
    def detectCapitalUse2(self, word):
        # 其实上面一句话就可以表达
        return word.islower() or word.isupper() or word.istitle()

s = Solution()
print(s.detectCapitalUse('Google'))