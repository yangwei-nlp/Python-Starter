class Solution:
    def combine(self, n, k):
        res = []
        self.helper(range(1, n + 1), k, res, [])
        return res

    def helper(self, array, k, res, path):
        if k > len(array):
            # 就这个判断可以帮助节省大量运算，想想为什么！
            return
        if k == 0:
            res.append(path)
        else:
            for i in range(len(array)):
                self.helper(array[i + 1:], k - 1, res, path + [array[i]])
                # 这个递归函数的特点在于不需要返回值，只需要对res进行原地操作就可以

s = Solution()
print(s.combine(4, 3))
