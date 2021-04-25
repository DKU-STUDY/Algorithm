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
    int findBottomLeftValue(TreeNode* root) {
        
        int leftmost;

        //Queue에 넣는다. BFS        
        queue <TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            TreeNode* temp = q.front(); q.pop();
            leftmost = temp->val;
            if(temp->right)
                q.push(temp->right);
            if(temp->left)
                q.push(temp->left);
        }
        return leftmost;
    }
};

//10000