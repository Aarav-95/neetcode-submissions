# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        # 1 2 3 4
        i, l = 0, len(nodes) - 1
        while i < l:
            nodes[i].next = nodes[l]
            i += 1
            if i >= l:
                break
            nodes[l].next = nodes[i]
            l -= 1
        nodes[i].next = None
        
        