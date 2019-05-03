# import queue
#
#
# class Solution:
#     def reorganizeString(self, S):
#         """
#         :type S: str
#         :rtype: str
#         """
#         res = ""
#         n = len(S)
#         a = [0 for i in range(26)]
#         for i in range(n):
#             a[ord(S[i]) - ord('a')] += 1
#             # chr(n)函数，将ASCII值转换为字符
#             # 而ord(char)函数，将字符char转换为ASCII值
#         for i in range(26):
#             if a[i] > (n + 1) // 2:
#                 # 如果某个字符出现次数占比超过一半，那么就不能满足条件，为啥呢？
#                 return res
#         que = queue.PriorityQueue()
#         for i in range(26):
#             if (a[i] > 0):
#                 # 注意，数字越小的表示优先级越高（负数也是一样），所以需要把正数转为负数
#                 que.put([-a[i], chr(i + ord('a'))])
#         while que.qsize() > 1:
#             # 每次都拿频数最多的那两个字符出来
#             s1 = que.get()
#             # 最小的负数，也即字母数最多的那个
#             s2 = que.get()
#             # 字母数第二多的那个
#             res += s1[1]
#             res += s2[1]
#             if s1[0] < -1:
#                 # 只有一次出现的字符就不用再次加入到优先队列里面了
#                 s1[0] += 1
#                 que.put(s1)
#             if s2[0] < -1:
#                 s2[0] += 1
#                 que.put(s2)
#         if que.qsize() > 0:
#             res += que.get()[1]
#         return res




import queue

# 代码还是自己实实在在的写一遍好啊
class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        # 首先需要将各个字母及其出现频数构建成为优先级队列
        a = [0 for _ in range(26)]
        for i in range(len(S)):
            a[ord(S[i]) - ord('a')] += 1
            # 这样做能降低空间复杂度（个人感觉不会的话不用弄这种奇淫技巧，踏踏实实用dict也可以）
        for i in range(26):
            # 如果某个字符出现频数高于总长度一半，那么必定无解
            if a[i] > (len(S) + 1) // 2:
                return ""
        que = queue.PriorityQueue()
        for i in range(26):
            if a[i] > 0:
                que.put([-a[i], chr(ord('a') + i)])
        res = ""
        while que.qsize() > 1:
            # 思路：每次拿出最频繁的两个字母，然后组合起来，这样就会得到一个解
            temp1 = que.get()
            res += temp1[1]
            temp2 = que.get()
            res += temp2[1]
            if temp1[0] < -1:
                temp1[0] += 1
                que.put(temp1)
            if temp2[0] < -1:
                temp2[0] += 1
                que.put(temp2)
        if que.qsize() > 0:
            res += que.get()[1]
        return res