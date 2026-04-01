# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def trav(self, root: TreeNode, m: int) -> int:
        if not root:
            return 0
        elif root.val >= m:
            m = root.val
            return 1 + self.trav(root.left, m) + self.trav(root.right, m)
        return self.trav(root.left, m) + self.trav(root.right, m)


    def goodNodes(self, root: TreeNode) -> int:
        return 1 + self.trav(root.left, root.val) + self.trav(root.right, root.val)