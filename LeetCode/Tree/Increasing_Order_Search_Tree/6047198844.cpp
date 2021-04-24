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
private:
    vector<int> res;
public:
    void makeTree(TreeNode* root){
        if(root==NULL)
            return;
        
        makeTree(root->left);
        
        res.push_back(root->val);
        
        makeTree(root->right);
        
        return;
    }
    
    TreeNode* increasingBST(TreeNode* root) {
        makeTree(root);
        
        TreeNode* r = new TreeNode(res[0]);
        TreeNode* temp = r;
        for(int i = 1 ; i < res.size(); i++){
            temp->right = new TreeNode(res[i]);
            temp = temp->right;
        }
        return r;
    }
};