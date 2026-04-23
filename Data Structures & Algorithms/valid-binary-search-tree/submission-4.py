# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, left, right):
            if root:
                if left < root.val and right > root.val:
                    return isValid(root.left, left, root.val) and isValid(root.right, root.val, right)   
                return False
            return True
        return isValid(root, -1001, 1001)