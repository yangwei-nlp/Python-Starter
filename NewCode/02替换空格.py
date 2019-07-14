# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        # s.replace(" ", "%20")
        string = ""
        for item in s:
            if item == " ":
                string += "%20"
            else:
                string += item
        return string

sol = Solution()
sol.replaceSpace("hello world")