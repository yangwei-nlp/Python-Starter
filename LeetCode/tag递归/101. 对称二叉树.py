# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def isSymmetric(self, root: 'TreeNode') -> 'bool':
#         if not root:
#             return True
#         else:
#             return self.childTreeIsSymmetric(root.left, root.right)
#
#     def childTreeIsSymmetric(self, p, q):
#         # 递归结束条件：
#         # 1. 两个节点都为空
#         # 2. 一个为空，另一个非空
#         # 3. 都为非空，但是值不相等
#         # 4. 都为非空，但是值相等（再次进入递归）
#         if not p or not q:
#             # 条件12
#             return p == q
#             # 条件1返回True，条件2返回False
#         if p.val != q.val:
#             return False
#             # 条件3
#         return self.childTreeIsSymmetric(p.left, q.right) & self.childTreeIsSymmetric(p.right, q.left)
#
#         # 下面是自己原来的写法，主要问题就是结束条件没有想清楚
#         # if not p and not q:
#         #     return True
#         # elif (p.val != q.val) or (p.left and not q.right) or (not p.left and q.right) \
#         #         or (p.right and not q.left) or (not p.right and q.left):
#         # 这个问题主要是q.val，如果为空，那么没有val这个属性
#         #     # p q节点值不等或者pq子节点一个存在，对应另一个不存在
#         #     return False
#         # else:
#         #     return self.childTreeIsSymmetric(p.left, q.right) & self.childTreeIsSymmetric(p.right, q.left)


class Solution:
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True
        # 这里采用深度优先搜索的方法来逐一节点判断
        queue = [root.left, root.right]
        while queue:
            node1 = queue.pop(0)
            node2 = queue.pop(0)
            if not node1 and not node2:
                # 均为空
                continue
            if (node1 is None and node2) or (node1 and node2 is None):
                # 一空一非空
                return False
            if node1.val != node2.val:
                # 均为非空, 但值不等
                return False
            # 剩下：均为非空，但是值相等
            # 首先把左-右节点添加进来(关键就是要两两入队，两两出队)
            queue.append(node1.left)
            queue.append(node2.right)

            # 再记得把右-左节点添加进来
            queue.append(node1.right)
            queue.append(node2.left)
        return True