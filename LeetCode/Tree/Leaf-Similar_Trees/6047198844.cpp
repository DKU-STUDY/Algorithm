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
public:
    void leaf(TreeNode* root,vector<int>&res){
        if(root==NULL)
            return;
        if(root->left==NULL&&root->right==NULL){
            res.push_back(root->val);
            return;
        }
        
        leaf(root->left,res);
        leaf(root->right,res);
    }
    
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> left;
        vector<int> right;
        leaf(root1,left);
        leaf(root2,right);
        
        if(left.size()!=right.size())
            return false;
        return equal(left.begin(),left.end(),right.begin());
    }
};
