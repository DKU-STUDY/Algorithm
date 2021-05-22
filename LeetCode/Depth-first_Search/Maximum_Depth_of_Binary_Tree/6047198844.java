/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int depth = 0;
    public int getMaxDepth(TreeNode root,int depth){
        if(root==null){
            return Math.max(this.depth,depth);
        }
        depth++;
        int res = depth;
        res = Math.max(getMaxDepth(root.left,depth),res);
        res = Math.max(getMaxDepth(root.right,depth),res);
        return res;
    }
    
    public int maxDepth(TreeNode root) {
        return getMaxDepth(root,0);
    }
}