# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        val = [p.val, q.val]

        def contained(p, num):
            if not p:
                return False
            if p.val == num:
                return True
            else:
                return contained(p.left, num) or contained(p.right, num)

        if root.val in val:
            return root
        
        elif root.right.val in val:
            if root.right.val == p.val:
                if contained(root.right, q.val):
                    return p
                return root
            else:
                if contained(root.right, p.val):
                    return q
                return root
        elif root.left.val in val:
            if root.left.val == p.val:
                if contained(root.left, q.val):
                    return p
                return root
            else:
                if contained(root.left, p.val):
                    return q
                return root
        if contained(root.left, p.val):
            if contained(root.right, q.val):
                return root
            else:
                return self.lowestCommonAncestor(root.left, p, q)
        elif contained(root.right, p.val):
            if contained(root.left, q.val):
                return root
            else:
                return self.lowestCommonAncestor(root.right, p, q)
        


