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
    ArrayList<Integer> left = new ArrayList<Integer>();
    ArrayList<Integer> right = new ArrayList<Integer>();
    
    public void inOrderLeft(TreeNode root){
        //nothing
        if(root==null){
            left.add(null); 
            return;    
        }
        //root
        left.add(root.val); 
        //left
        inOrderLeft(root.left);
        //right
        inOrderLeft(root.right);
    }
    
    public void inOrderRight(TreeNode root){
        //nothing
        if(root==null){
            right.add(null);
            return;    
        }
        //root
        right.add(root.val);
        //right
        inOrderRight(root.right);
        //left
        inOrderRight(root.left);
    }
    
    public boolean isSymmetric(TreeNode root) {
        inOrderLeft(root);
        inOrderRight(root);
        return left.equals(right);
    }
}
