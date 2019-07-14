# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        num_space = 0
        # 总空格数
        for i in s:
            if i == ' ':
                num_space += 1

        new_length = len(s) + 2 * num_space  # 新字符串的长度
        index_origin = len(s) - 1  # 末尾字符的index
        index_new = new_length - 1  # 新字符串末尾字符的index
        new_string = [None for i in range(new_length)]

        while index_origin >= 0 & (index_new > index_origin):
            if s[index_origin] == ' ':
                new_string[index_new] = '0'
                index_new -= 1
                new_string[index_new] = '2'
                index_new -= 1
                new_string[index_new] = '%'
                index_new -= 1
            else:
                new_string[index_new] = s[index_origin]
                index_new -= 1
            index_origin -= 1
        return ''.join(new_string)


if __name__ == '__main__':
    a = Solution()
    print(a.replaceSpace('r y uu'))