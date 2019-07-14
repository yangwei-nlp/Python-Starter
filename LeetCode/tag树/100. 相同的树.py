# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路倒是很简单，但是beats 0.94%，扎心
# class Solution:
#     def isSameTree(self, p: 'TreeNode', q: 'TreeNode') -> 'bool':
#         if (not p and q) or (p and not q):
#             # 两个一个为空，一个非空
#             return False
#         if not p and not q:
#             return True
#         p_queue = [p]
#         q_queue = [q]
#         while p_queue and q_queue:
#             node_p = p_queue.pop(0)
#             node_q = q_queue.pop(0)
#             if node_p.val != node_q.val:
#                 return False
#             if node_p.left:
#                 if node_q.left:
#                     if node_p.val == node_q.val:
#                         p_queue.append(node_p.left)
#                         q_queue.append(node_q.left)
#                     else:
#                         return False
#                 else:
#                     return False
#             elif node_q.left:
#                 return False
#             if node_p.right:
#                 if node_q.right:
#                     if node_p.val == node_q.val:
#                         p_queue.append(node_p.right)
#                         q_queue.append(node_q.right)
#                     else:
#                         return False
#                 else:
#                     return False
#             elif node_q.right:
#                 return False
#         return True


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 用递归(DFS)的方法来判断，而非上面使用队列+广搜的方式
class Solution:
    def isSameTree(self, p: 'TreeNode', q: 'TreeNode') -> 'bool':
        if not p and not q:
            # 终止条件：pq两个子节点均为空节点
            return True
        elif p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False