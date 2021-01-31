# 思路：Huahua，https://www.bilibili.com/video/BV1a54y1m75Y
"""
思路完全是花花的，在此1:1复现. 用dict形式存储

s_idx[int(char)].popleft()和if s_idx[k] and...
这样保证了，遍历t时，已经能够正确挪位的字符不会在下次判断中被重复考虑

"""
from collections import defaultdict, deque
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        s_idx = defaultdict(deque)
        for i, char in enumerate(s):
            s_idx[int(char)].append(i)
        
        for j, char in enumerate(t):
            if not s_idx[int(char)]:
                return False
            for k in range(int(char)):
                if s_idx[k] and s_idx[k][0] < s_idx[int(char)][0]:
                    return False
            s_idx[int(char)].popleft()  # 这句话异常关键啊!
        return True


s = "84532"
t = "34852"
ss = Solution()
print(ss.isTransformable(s, t))
