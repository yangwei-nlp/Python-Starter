# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # 广度优先遍历
        nodes = [(root, 1)]
        i = 0
        while i < len(nodes):
            node, v = nodes[i]
            if node:
                nodes.append((node.left, 2*v))
                nodes.append((node.right, 2*v+1))
            i += 1
        return nodes[-1][1] == len(nodes)


s = Solution()
s.isCompleteTree()

