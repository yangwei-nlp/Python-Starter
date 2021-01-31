class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        saved = []
        i = 0
        while i < len(s):
            j = 1
            while s[i: i+j] in saved:
                j += 1
            saved.append(s[i: i+j])
            i = i+j-1
            i += 1
        return len(saved)


ss = Solution()
s = "aba"
print(ss.maxUniqueSplit(s))


"""
www,z,f,v,e,d,w,fv,h,s,ww

"""