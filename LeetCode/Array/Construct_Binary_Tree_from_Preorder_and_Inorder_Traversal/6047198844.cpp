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
    TreeNode* build(int rootIdx, int inbegin, int inend, vector<int>& preorder, vector<int>& inorder) {
        TreeNode* root = NULL;
        if (inbegin <= inend&&rootIdx<preorder.size()) {
            int rootVal = preorder[rootIdx];
            int i = find(inorder.begin() + inbegin, inorder.begin() + inend, rootVal) - inorder.begin();
            
            root = new TreeNode(rootVal);
            root->left = build(rootIdx + 1, 
                               inbegin, i - 1, preorder, inorder);
            root->right = build(rootIdx + 1 + i - inbegin, 
                                i + 1, inend, preorder, inorder);
        }
        return root;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return build(0, 0, inorder.size() - 1, preorder, inorder);
    }
};