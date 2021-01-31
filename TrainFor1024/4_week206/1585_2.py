# 思路借鉴：Huahua，https://www.bilibili.com/video/BV1a54y1m75Y
"""
要注意一个问题(难点)：题目虽然说到可以对连续子字符串排序(升序),以此得到目标字符串，但是我们实际上无需这样思考。
只需按照冒泡的思想进行两两换位即可,当然需要满足一个条件：该数比前面的数小才能互换位置。
利用冒泡的特点：
如84532，字符3位置前面没有他小的数，所以3可以移到第一位，而8452的相对顺序能够保持不变。

有了冒泡思路，遍历t中字符，看该字符在s中是否能挪到第一位，不行False，可以就将s中该字符删掉
最后遍历完毕就True


还有一个很妙的思想，查看s在位置i前是否有比char更小的数：
因为char取值范围0-9，而位置i前面的数可能很多很多，所以不能够一个个数判断是否小于char，而需要判断0-char的若干个数是否在位置i前面的字符串即可。
"""
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        # s_list = list(s)

        for i, char in enumerate(t):
            # 不存在该字符：False
            char_idx_in_s = s.find(char)
            if char_idx_in_s == -1:
                return False

            if self.front_exist_smaller(s, char_idx_in_s, char):
                return False
            else:
                s = s[:char_idx_in_s] + s[char_idx_in_s+1:]
        return True
    
    
    def front_exist_smaller(self, s, char_idx_in_s, char):
        # 查看s在位置i前是否有比char更小的数
        for smaller_num in range(int(char)):
            if str(smaller_num) in s[:char_idx_in_s]:
                return True
        return False


s = "12345"
t = "12435"
ss = Solution()
print(ss.isTransformable(s, t))
