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
    TreeNode* build (int postIdx, int inBeginIdx, int inEndIdx, vector<int>& inorder, vector<int>& postorder){
        TreeNode* root = NULL; 
        if(inBeginIdx < inEndIdx){
            int rootValue = postorder[postIdx];
            root = new TreeNode(rootValue);
            
            int i = find(inorder.begin()+inBeginIdx, inorder.begin()+inEndIdx, rootValue) - inorder.begin();
            
            int leftNum = i - inBeginIdx;
            int rightNum = inEndIdx - inBeginIdx - leftNum - 1;
            
            root->left = build (postIdx-1-rightNum, 
                                inBeginIdx, 
                                i, 
                                inorder, postorder);
            
            root->right = build (postIdx-1, 
                                 i+1, 
                                 inEndIdx, 
                                inorder, postorder);
        }
        return root;
    }
    
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        return build (postorder.size()-1, 0, inorder.size(), inorder, postorder);
    }
};