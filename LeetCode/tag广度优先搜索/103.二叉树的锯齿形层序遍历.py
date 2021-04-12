# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        all_nums = []

        queue = []
        queue.append(root)

        pos_flag = True
        floor_queue = []
        for i in range(len(queue)):
            # 控制该层多少个元素
            node = queue.pop(0)
            all_nums.append(node.val)
            if node.left:
                floor_queue.append(node.left)
            if node.right:
                floor_queue.append(node.right)
            
