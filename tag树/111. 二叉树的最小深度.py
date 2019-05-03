# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 法一，我也不懂为什么bug不断
# class Solution:
#     def minDepth(self, root: 'TreeNode') -> 'int':
#         if not root:
#             return 0
#         queue = [root]
#         depth = 1
#         while queue:
#             node = queue.pop(0)  # 广度优先搜索
#             for child in [node.left, node.right]:
#                 if child:
#                     if not (child.left or child.right):
#                         return depth + 1
#                     queue.append(child)
#             if node.left or node.right:
#                 depth += 1
#         return depth


# 大神之作
class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            if root.left and root.right:
                return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
            elif root.left:
                return 1 + self.minDepth(root.left)
            elif root.right:
                return 1 + self.minDepth(root.right)
            else:
                return 1
        else:
            return 0


root = TreeNode(0)
s = Solution()
print(s.minDepth(root))
