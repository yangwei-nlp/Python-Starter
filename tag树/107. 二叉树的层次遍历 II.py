# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 这是方法一，觉得很牛皮
# class Solution:
#     def levelOrderBottom(self, root: 'TreeNode') -> 'List[List[int]]':
#         if not root:return []
#         queue = [root]
#         res = []
#         while queue:
#             temp_val = []
#             for _ in range(len(queue)):
#                 node = queue.pop(0)
#                 temp_val.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             res.insert(0, temp_val)
#         return res



class Solution:
    def levelOrderBottom(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root: return []
        stack = [root]
        res = []

        while len(stack) != 0:
            tmp = []
            res_each = []
            for i in stack:
                res_each.append(i.val)
                if i.left != None:
                    tmp.append(i.left)
                if i.right != None:
                    tmp.append(i.right)
            stack = tmp
            res.insert(0, res_each)

        return res