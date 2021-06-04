# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        Q = collections.deque([root])
        
        while Q:
            node = Q.popleft()
            
            if node:
                node.left, node.right = node.right, node.left
                Q.append(node.left)
                Q.append(node.right)
            
        return root