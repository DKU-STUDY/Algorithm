#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import urllib.request
from functools import lru_cache


@lru_cache(None)
def max_binary(root: TreeNode, check: bool) -> int:  # 이전에 안뽑았으면 True, 뽑았으면 False
    if not root:
        return 0

    pick = 0
    not_pick = 0

    not_pick = max_binary(root.left, True) + max_binary(root.right, True)

    if check:
        pick = root.val + max_binary(root.left, False) + max_binary(root.right, False)

    return max(pick, not_pick)


class Solution:
    def rob(self, root: TreeNode) -> int:
        return max_binary(root, True)