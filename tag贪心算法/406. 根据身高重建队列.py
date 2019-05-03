# 这个算法有错
# class Solution:
#     def reconstructQueue(self, people: 'List[List[int]]') -> 'List[List[int]]':
#         if not people: return []
#         res = [people[0]]
#         for i in range(1, len(people)):
#             bigger_num = 0
#             temp = people[i]
#             for j in range(len(res)):
#                 if temp[1] == 0:
#                     if temp[0] < res[j][0]:
#                         res.insert(0, temp)
#                         break
#                 if res[j][0] >= temp[0]:
#                     bigger_num += 1
#                 if bigger_num == temp[1]:
#                     res.insert(j+1, temp)
#                     break
#             if bigger_num < temp[1]:
#                 res.insert(j + 1, temp)
#         return res


# class Solution(object):
#     def reconstructQueue(self, people):
#         if len(people) <= 1:
#             return people
#         res = []
#         # 先按照身高降序排列，当身高相等时在按照比其大的人数升序排列
#         people = sorted(people, key=lambda x: (x[0], -x[1]), reverse=True)
#         res.append(people[0])
#         # 然后逐个插入，若比当前人高的人有i个，则把该人插入队列的第i位
#         for i in range(1, len(people)):
#             j = people[i][1]
#             if j == 0:
#                 res = [people[i]] + res
#             else:
#                 res = res[:j] + [people[i]] + res[j:]
#         return res


# 方法：大的元素用来确定相对顺序，小的元素来最终定序
# class Solution(object):
#     def reconstructQueue(self, people):
#         if not people: return []
#         people.sort(key=lambda li: (li[0], -li[1]), reverse=True)
#         res = [people[0]]
#         for i in range(1, len(people)):
#             temp_li = people[i]
#             bigger_num = 0
#             for j in range(len(res)):
#                 if temp_li[1] == 0 and temp_li[0] < res[0][0]:
#                     res.insert(0, temp_li)
#                     break
#                 if res[j][0] >= temp_li[0]:
#                     bigger_num += 1
#                 if bigger_num == temp_li[1]:
#                     res.insert(j+1, temp_li)
#                     break
#         return res
# 中间的循环还是表明自己没有懂这个问题的关键


# 对上面解法的优化
class Solution(object):
    def reconstructQueue(self, people):
        if not people: return []
        people.sort(key=lambda li: (li[0], -li[1]), reverse=True)
        res = [people[0]]
        for i in range(1, len(people)):
            temp_li = people[i]
            if temp_li[1] == 0:
                res.insert(0, temp_li)
            else:
                res.insert(temp_li[1], temp_li)
        return res


s = Solution()
print(s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
