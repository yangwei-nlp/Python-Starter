class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 用二分查找法搜索这个整数，另外还可以用别的方法，如牛顿迭代法
        if x == 1:
            return 1
        l = 0
        r = x
        while r - l > 1:
            middle = (l + r) // 2
            if middle**2 > x:
                r = middle
            elif middle**2 == x:
                return middle
            else:
                l = middle
        return l