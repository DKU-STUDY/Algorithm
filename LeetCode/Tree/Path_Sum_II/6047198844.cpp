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
    vector<vector<int>> res;
    
public:
    void pSum(TreeNode*root, int targetSum,vector<int>&temp){
        if(root==NULL)
            return;
        
        temp.push_back(root->val);        

        if(root->left==NULL&&root->right==NULL&&targetSum==root->val)
            res.push_back(temp);

        pSum(root->left,targetSum-root->val,temp);
        pSum(root->right,targetSum-root->val,temp);
        
        temp.pop_back();
    }
    
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<int> temp;
        pSum(root, targetSum, temp);
        return res;
    }
};