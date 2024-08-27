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
**/

class Solution {
public:
    bool evaluateTree(TreeNode* root) {
        /**
         * Recursively evaluate a boolean binary tree. Leafs
         * nodes have 0 representing false and 1 representing
         * true, while non-leaf nodes have 2 representing OR
         * and 3 representing AND. Output will be a single
         * boolean value.
        **/

        // If a node is AND, we can return false early if either
        // branch evaluates to false, else return true. This may
        // save us evaluating half of the subsequent nodes.
        if (root->val == 3) {
            if (not evaluateTree(root->left)) return false;
            if (not evaluateTree(root->right)) return false;
            return true;
        }
        
        // If a node is OR, we can return true early if either
        // branch evaluates to true, else return false. This may
        // save us evaluating half of the subsequent nodes.
        if (root->val == 2) {
            if (evaluateTree(root->left)) return true;
            if (evaluateTree(root->right)) return true;
            return false;
        }

        // If node isn't OR or AND, we must be at a leaf so just
        // want to return the value of the node
        return root->val;
    }
};
