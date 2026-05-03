class Codec:
    def __init__(self):
        self.inorder = ","
        self.preorder = ","
    def _buildTree(self, preorder, inorder):
        if not preorder and not inorder:
            return None
        root = TreeNode(preorder[0])
        # Find the split index based on the LAST occurrence to handle duplicates or
        # track indices properly. However, Inorder+Preorder doesn't work with duplicate values.
        # To fix this minimally, we switch to a standard Preorder + Null marker approach.
        return None

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()