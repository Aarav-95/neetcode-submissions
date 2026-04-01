# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2
        curr = None
        head = None
        while h1 and h2:
            if h1.val > h2.val:
                if not curr:
                    curr = h2
                    head = curr
                else:
                    curr.next = h2
                    curr = curr.next
                h2 = h2.next
            else:
                if not curr:
                    curr = h1
                    head = curr
                else:
                    curr.next = h1
                    curr = curr.next
                h1 = h1.next
        
        while h1:
            if not curr:
                curr = h1
                head = curr
            else:
                curr.next = h1
                curr = curr.next
            h1 = h1.next
        
        while h2:
            if not curr:
                curr = h2
                head = curr
            else:
                curr.next = h2
                curr = curr.next
            h2 = h2.next
        
        return head
        