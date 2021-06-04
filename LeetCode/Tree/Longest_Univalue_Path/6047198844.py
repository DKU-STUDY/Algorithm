# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest: int = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        #상태를 반환한다.
        #상태란 univalue를 가진 리프까지의 거리이다.
        def dfs(root):
            if not root:
                return -1
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            
            if root.left and root.left.val == root.val:
                left += 1
            else:
                left = 0
            
            if root.right and root.right.val == root.val:
                right += 1
            else:
                right = 0
                
            self.longest = max(self.longest, left + right)
            return max(left, right)
        
        dfs(root)
        return self.longest
            