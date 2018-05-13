# coding=utf-8
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = "0" + "12113"
        list_str = []
        for i in range(len(string)):
            _str = string[i]
            if string[i] != string[i-1]:
                list_str.append(_str)
            else:
                _str += string[i]
                # list_str.append(_str)
        # if string[-1] != string[-2]:
        #     list_str.append(string[-1])
