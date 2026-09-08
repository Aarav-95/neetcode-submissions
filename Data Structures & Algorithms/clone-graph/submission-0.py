"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            n = Node()
            n.val = node.val
            oldToNew[node] = n
            for neighbor in node.neighbors:
                n.neighbors.append(dfs(neighbor))
        
            return n
        return dfs(node) if node else None