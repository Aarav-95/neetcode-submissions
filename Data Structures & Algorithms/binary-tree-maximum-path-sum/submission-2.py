# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        m = float("-inf")

        def dfs(root):
            nonlocal m
            if root:
                max_left = dfs(root.left)
                max_right = dfs(root.right)
                temp = max(root.val, root.val+max_left, root.val+max_left+max_right, root.val+max_right)
                max_val = max(root.val, root.val+max_left, root.val+max_right)
                if temp > m:
                    m = temp
                return max_val
            return 0
        
        dfs(root)
        return m