# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isEqual(root, subRoot):
            if not root and subRoot or root and not subRoot:
                return False
            if not root and not subRoot:
                return True
            if root and subRoot and root.val == subRoot.val:
                if not isEqual(root.left, subRoot.left):
                    return False
                if root.val != subRoot.val:
                    return False
                if not isEqual(root.right, subRoot.right):
                    return False
            if root.val != subRoot.val:
                return False
            return True

        if not root and subRoot or root and not subRoot:
            return False
        if root.val != subRoot.val:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        if root.val == subRoot.val:
            if isEqual(root, subRoot):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

            