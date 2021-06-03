# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest: int = 0
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        #상태를 반환한다. 상태란 현재노드에서 리프노드까지의 거리이다.
        #거리는 간선의 개수를 뜻한다.
        def dfs(root):
            #이 부분이 매우 중요하다. 리프노드의 경우 상태로 0. 거리로 0을 가져야한다.
            if not root:
                return -1
            
            #left의 상태와 right의 상태를 얻는다.
            left = dfs(root.left)
            right = dfs(root.right)
            
            self.longest = max(self.longest, 2 + left + right)
            
            return 1 + max(left, right)
        
        dfs(root)
        return self.longest