"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        queue = [(root, 1)]
        while queue:
            node, res = queue.pop(0)
            for child in node.children:
                queue.append((child, res+1))
        return res