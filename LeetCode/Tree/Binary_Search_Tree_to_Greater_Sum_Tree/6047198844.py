# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    acc: int = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        #현재노드의 부모와 부모오른쪽의 합, 현재노드
        if root:
            self.bstToGst(root.right)
            self.acc += root.val
            root.val = self.acc
            self.bstToGst(root.left)
        return root