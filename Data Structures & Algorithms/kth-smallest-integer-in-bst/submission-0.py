# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        def inOrder(root):
            if root:
                inOrder(root.left)
                nodes.append(root.val)
                inOrder(root.right)
        
        inOrder(root)
        return nodes[k-1]