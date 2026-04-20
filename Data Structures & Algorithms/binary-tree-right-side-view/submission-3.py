# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []

        queue = collections.deque()
        queue.append(root)

        while queue:
            length = len(queue)
            level = []
            for i in range(length):
                top = queue.popleft()
                if top:
                    queue.append(top.left)
                    queue.append(top.right)
                    level.append(top.val)
            if level:
                res.append(level[-1])
        
        return res
