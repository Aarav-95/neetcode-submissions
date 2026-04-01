# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        if length - n == 0:
            if head:
                return head.next
            return None
        
        curr = head
        for i in range(length-n-1):
            if curr:
                curr = curr.next
        
        if not curr or not curr.next:
            return None

        curr.next = curr.next.next
        return head