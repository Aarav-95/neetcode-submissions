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
    int height(TreeNode* root) {
        if (!root) return 0;
        return 1 + max(height(root->left), height(root->right));
    }
    bool isBalanced(TreeNode* root) {
        if (!root || (!root->right && !root->left)) return true;
        if (root->left && root->right) {
            if (isBalanced(root->left) && isBalanced(root->right)) {
                if (abs(height(root->left) - height(root->right)) <= 1) {
                    return true;
                }
                return false;
            }
        } 
        else if (root->left) {
            if (root->left->left || root->left->right) {
                return false;
            }
            else {return true;}
        }
        
        else if (root->right) {
            if (root->right->left || root->right->right) {
                return false;
            }
            else {return true;}
        }
    }
};
