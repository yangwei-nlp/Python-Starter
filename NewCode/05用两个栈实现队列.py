# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.num_pop = 0

    def push(self, item):
        self.stack1.append(item)

    def pop(self):
        self.stack2 = []
        for i in range(len(self.stack1) - 1, self.num_pop - 1, -1):
            self.stack2.append(self.stack1[i])
        self.num_pop += 1
        return self.stack2.pop()