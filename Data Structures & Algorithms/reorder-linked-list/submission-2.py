# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        if count == 1:
            return
        idx = count // 2
        curr = head

        for i in range(idx):
            if curr:
                if i == idx - 1:
                    temp = curr
                    curr = curr.next
                    temp.next = None
                else:
                    curr = curr.next
        
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        l = head
        while l and prev:
            temp1 = l.next
            l.next = prev
            temp2 = prev.next
            if temp1:
                prev.next = temp1
            l = temp1
            prev = temp2
            

        