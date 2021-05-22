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
    vector <int> _arr;
public:
    void inorder(TreeNode* root){
        if(root==NULL) return;
        inorder(root->left);
        _arr.push_back(root->val);
        inorder(root->right);
    }
    
    void recover(TreeNode* root,int&idx){
        if(root==NULL) return;
        recover(root->left,idx);
        root->val = _arr[idx++];
        recover(root->right,idx);
    }
    
    void recoverTree(TreeNode* root) {
        inorder(root);
        sort(_arr.begin(),_arr.end());
        int idx = 0;
        recover(root,idx);
    }
};