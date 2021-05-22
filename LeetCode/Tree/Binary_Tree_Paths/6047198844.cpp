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
    vector<string> res;
public:
    void TreePaths(TreeNode* root, string &paths){
        if(root==NULL)
            return;

        string temp = paths;  
        if(root->left==NULL&&root->right==NULL){
            paths += to_string(root->val);
            res.push_back(paths);
            paths = temp;
            return;
        }
        paths += to_string(root->val)+"->";
        TreePaths(root->left, paths);
        TreePaths(root->right, paths);
        paths = temp;
    }
    
    vector<string> binaryTreePaths(TreeNode* root) {
        string paths = "";
        TreePaths(root,paths);
        return res;
    }
};
