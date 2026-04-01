# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        if not head.next:
            return False
        fast = head.next
        while (slow.val != fast.val):
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return False
            if slow and fast and slow.val == fast.val:
                return True
            elif not fast:
                return False
            
        return True
        