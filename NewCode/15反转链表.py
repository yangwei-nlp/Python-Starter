# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pre = pHead
        if pre == None:
            return pre
        cur = pHead.next
        if cur == None:
            return pre

        # 对待pre为初节点情况
        temp = cur.next
        cur.next = pre
        pre.next = None
        pre = cur
        cur = temp

        while cur != None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre