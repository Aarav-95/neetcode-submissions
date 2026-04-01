"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldNew = {}
        curr = head
        flag = 0
        res = None
        while curr:
            temp = Node(curr.val)
            if not flag:
                res = temp
                flag = 1
            oldNew[curr] = temp
            curr = curr.next

        for old in oldNew:
            if old.random:
                oldNew[old].random = oldNew[old.random]
            if old.next:
                oldNew[old].next = oldNew[old.next]
        
        return res
        