# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder:
            root = TreeNode(preorder[0])
            #루트 인덱스 == 왼쪽 서브트리 개수
            root_idx = inorder.index(root.val)
            #preorder 왼쪽 서브트리 시작(1) ~ 왼쪽 서브트리 끝(1+왼쪽 서브트리 개수)
            #inorder 루트 기준 왼쪽(처음~루트인덱스(루트 제외))
            root.left = self.buildTree(preorder[1:1+root_idx], inorder[:root_idx])
            #preorder 오른쪽 서브트리 시작(root_idx+1) ~ 오른쪽 서브트리 끝
            #inorder 루트 기준 오른쪽(루트 오른쪽 ~ 끝)
            root.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:])
            return root