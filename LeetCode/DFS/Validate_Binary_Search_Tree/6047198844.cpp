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

/*
이진 탐색 트리 문제
*/
class Solution {
private: vector<int> arr_;
    
public:
    void dfs(TreeNode* root){
        if(root==NULL)
            return;
        dfs(root->left);
        arr_.push_back(root->val);
        dfs(root->right);
    }
    
    
    bool isValidBST(TreeNode* root) {
        dfs(root);
        int arrSize = arr_.size();
        for(int i = 1; i < arrSize; i++)
            if(arr_[i-1]>=arr_[i])
                return false;
        return true;
    }
};