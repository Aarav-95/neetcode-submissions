# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.m = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            temp = 0
            a = 0
            b = 0
            if root.left:
                temp += 1
                a += 1
            if root.right:
                temp += 1
                b += 1
            l = dfs(root.left)
            r = dfs(root.right)
            temp += l + r
            self.m = temp if temp > self.m else self.m # m = 1
            return max(a+l, b+r)
        
        res = dfs(root)
        return self.m