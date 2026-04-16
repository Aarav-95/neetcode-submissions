# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(root, subRoot):
            if not root and not subRoot:
                return True
            if not root and subRoot or not subRoot and root or root.val != subRoot.val:
                return False
            return isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)

        if root:
            a = self.isSubtree(root.left, subRoot)
            if a:
                return True
            if isSameTree(root, subRoot):
                return True
            b = self.isSubtree(root.right, subRoot)
            if b:
                return True
        return False