# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseKNodes(head: Optional[ListNode], k: int):
            curr = head
            prev = None
            nextHead = None
            for i in range(k):
                if i == k - 1:
                    nextHead = curr.next
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return [prev, nextHead] 
        
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        cycles = n // k
        extra = n % k
        curr = head
        new_head = None
        nextPoint = None
        for i in range(cycles):
            reverse = reverseKNodes(curr, k)
            prev = reverse[0]
            nextHead = reverse[1]
            if i == 0:
                new_head = prev
            if nextPoint:
                nextPoint.next = prev
            nextPoint = curr
            curr = nextHead

        if extra:
            nextPoint.next = curr
        return new_head

            
            
