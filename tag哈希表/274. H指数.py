# 我的这种思路本质上是一种排序方法，但是超时
# 说实话，这道题题意并不是很理解
from itertools import compress

# class Solution:
#     def hIndex(self, citations: list) -> int:
#         if citations == [0]: return 0
#         h = len(citations)
#         tf_seq = list(map(lambda item: item>=h, citations))
#         bigger_num = sum(tf_seq)
#         ft_seq = list(map(lambda item: item<h, citations))
#         citations = list(compress(citations, ft_seq))
#         # while h != bigger_num:
#         while h > bigger_num:
#             h -= 1
#             tf_seq = list(map(lambda item: item >= h, citations))
#             bigger_num += sum(tf_seq)
#             ft_seq = list(map(lambda item: item < h, citations))
#             citations = list(compress(citations, ft_seq))
#         return h


# 思路，将数组排序后，数组的元素和其索引构成某种联系，接下来可以用这个联系来解题
# 注意本题的一个坑：
# 英文题目像在说，请找到数组中满足这样的H：数组有H个元素大于等于H
# 但实际上中文题目是正确的，请找到数组中最大的这样的数：n篇论文中被引用次数至少为H的。。（编不下去了）
class Solution:
    def hIndex(self, citations: list) -> int:
        citations.sort(reverse=True)
        h = 0
        while h < len(citations) and citations[h] >= h+1:
            h += 1
        return h

s = Solution()
print(s.hIndex([0,0]))