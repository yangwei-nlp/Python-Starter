class Solution:
    def removeKdigits(self, num, k):

        if k >= len(num):
            return "0"
        i = 0
        # 注意这是while循环而非for循环，因为需要动态改变num，然后删除元素
        while i < len(num) - 1 and k > 0:  # 开始搜索
            if (int(num[i]) > int(num[i + 1])):  # 如果有一位数字大于下一位，那么将这一位删除
                num = num[0:i] + num[i + 1:]
                if i > 0: i -= 1
                k -= 1
            else:
                i += 1
        num = num[:len(num) - k]
        return str(int(num))


s = Solution()
print(s.removeKdigits(num="1432219", k=3))
print(s.removeKdigits(num="1230", k=3))