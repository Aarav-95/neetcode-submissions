# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        cur = head
        count = 0
        while cur:
            cur = cur.next
            count += 1
        cur = head
        if count == n:
            return cur.next
        for i in range(count-n-1):
            cur = cur.next
        cur.next = cur.next.next
        return head