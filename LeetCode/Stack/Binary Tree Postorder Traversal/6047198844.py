# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root:
            res += self.postorderTraversal(root.left)
            res += self.postorderTraversal(root.right)
            res.append(root.val)
        return res
        
        
        