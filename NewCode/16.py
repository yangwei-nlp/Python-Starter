# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1

        if pHead1.val <= pHead2.val:
            Head = pHead1
            cur = pHead1
        else:
            Head = pHead2
            cur = pHead2

        while pHead1 != None & pHead2 != None:
            if pHead1.val <= pHead2.val:
                pHead1 = pHead1.next
                cur.next = pHead2
                cur = pHead2
            else:
                pHead2 = pHead2.next
                cur.next = pHead1
                cur = pHead1
            