# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here

        first_num = pre[0]
        root = TreeNode(first_num)
        root_index = tin.index(first_num)
        pre.pop(0)
        if len(pre) == 1:
            if tin.index(pre[0]) > tin.index(first_num):
                root.right = TreeNode(pre[0])
            else:
                root.left = TreeNode(pre[0])
            return
        root.left = self.reConstructBinaryTree(pre[1:root_index+1], tin[:root_index])
        root.right = self.reConstructBinaryTree(pre[root_index+1:], tin[root_index+1:])
