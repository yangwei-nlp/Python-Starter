class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # global ret
        start = "1"
        if n == 1:
            return start
        for i in range(n-1):
            ret = ""

            pattern = start[0]
            cnt = 1

            for s in start[1:]:
                if s == pattern:
                    cnt += 1
                else:
                    ret = ret + str(cnt) + pattern
                    pattern = s
                    cnt = 1
            ret = ret + str(cnt) + pattern

            start = ret

        return ret

solver = Solution()
print(solver.countAndSay(1))