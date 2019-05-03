# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 方法一，这里要注意中间的for循环，功能相当于pop(0)，感觉很巧妙（trick）
# class Solution:
#     def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
#         if not root: return []
#         queue = [root]
#         res = []
#         while queue:
#             temp_queue = []
#             temp_val = []
#             for node in queue:
#                 temp_val.append(node.val)
#                 if node.left:
#                     temp_queue.append(node.left)
#                 if node.right:
#                     temp_queue.append(node.right)
#             res.append(temp_val)
#             queue = temp_queue
#         return res


# 方法二，试一试递归大法
class Solution:
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root: return []
        res = []
        queue = [root]
        self.BFS(queue, res)
        return res

# 这里递归的主要思想就是需要按照层来递归，每一层所有元素加入队列，
# 然后再将元素的左儿子右儿子添加，并递归
    def BFS(self, queue, res):
        temp_val = []
        new_queue = []
        while queue:
            node = queue.pop(0)
            temp_val.append(node.val)
            if node.left:
                new_queue.append(node.left)
            if node.right:
                new_queue.append(node.right)
        if temp_val:
            # 为空表示到底了不用再递归了
            res.append(temp_val)
            self.BFS(new_queue, res)