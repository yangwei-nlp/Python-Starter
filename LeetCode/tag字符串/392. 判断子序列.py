class Solution:
    def isSubsequence(self, s, t):
        find_idx = -1
        for char in s:
            t = t[find_idx+1:]
            find_idx = t.find(char)
            if find_idx == -1:
                return False
        return True

    def isSubsequence2(self, s, t):
        # 方法二：使用两个指针来处理
        i, j = 0, 0
        while j < len(t):
            if i == len(s):
                return True
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i == len(s) and j == len(t):
            return True
        else:
            return False

    def isSubsequence3(self, s, t):
        if not s:
            return True
        if not t:
            return False
        if s == t:
            return True
        m = len(s)
        n = len(t)
        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if s[i] == t[j]:
                    res[i][j] = res[i-1][j-1] + 1
                else:
                    res[i][j] = max(res[i][j-1], res[i-1][j])
        return res[-1][-1] == m


s = "abc"
t = "ahbgdc"
sol = Solution()
print(sol.isSubsequence3(s, t))
