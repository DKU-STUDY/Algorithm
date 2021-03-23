/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private: int acc = 0;
public:
    void Traversal(TreeNode* root) {
        if(root == NULL)
            return;
        
        Traversal(root->right);
        root->val += acc;
        acc = root->val;
        Traversal(root->left);
    }
    
    
    TreeNode* convertBST(TreeNode* root) {
        Traversal(root);
        return root;
    }
};