# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 法一：递归的方法，由于对递归仍然不是很熟练，所以写的磕磕盼盼
# class Solution:
#     def hasPathSum(self, root: 'TreeNode', sum: 'int') -> 'bool':
#         if not root:
#             # 如果当前节点为空，说明这条路径不满足，返回False
#             return False
#         if root.left is None and root.right is None:
#             # 表明当前判断的节点是叶子节点
#             if sum == root.val:  # 注意判断的条件
#                 return True
#             else:
#                 return False
#         # 不是叶子节点就需要继续递归
#         return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

# 法二：迭代的方法也是可行的，使用 深度优先搜索 + 栈
class Solution:
    def hasPathSum(self, root: 'TreeNode', sum: 'int') -> 'bool':
        stack = [(root, sum)]
        while stack:
            node, sum = stack.pop()

            if not node:
                return False

            if node.left is None and node.right is None:
                if sum == node.val:
                    return True
                return False

            stack.append((node.left, sum - node.val))
            stack.append((node.right, sum - node.val))


class Solution:
    def hasPathSum(self, root: 'TreeNode', sum: 'int') -> 'bool':
        if not root:
            return False
        stack = [(root, sum)]
        while stack:
            node, sum = stack.pop()
            if node.left is None and node.right is None:
                # 如果是叶子节点
                if sum == node.val:
                    return True
                continue  # 不满足条件的叶子节点，下面的程序无需执行了
            if node.left:
                stack.append((node.left, sum - node.val))
            if node.right:
                stack.append((node.right, sum - node.val))
        return False