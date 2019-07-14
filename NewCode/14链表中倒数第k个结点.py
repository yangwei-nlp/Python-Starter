# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def FindKthToTail(self, head, k):
#         # write code here
#         if head == None:
#             return None
#
#         cur = head
#         length = 1
#         while cur.next != None:
#             length += 1
#             cur = cur.next
#
#         target = length - k + 1
#         if target > length or k > length:
#             return None
#
#         cur = head
#         count = 1
#         while count != target:
#             cur = cur.next
#             count += 1
#         return cur


class Solution:
    def FindKthToTail(self, head, k):
        # write code here

        if head == None:
            return None
        one = head
        two = head
        count = 1
        while count != k:
            one = one.next
            if one == None:
                return None
            count += 1
        while one.next != None:
            one = one.next
            two = two.next
        return two