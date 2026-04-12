# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root and root.left and root.right:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        elif root and root.right:
            root.left = root.right
            root.right = None
            self.invertTree(root.left)
        elif root and root.left:
            root.right = root.left
            root.left = None
            self.invertTree(root.right)

        return root
        