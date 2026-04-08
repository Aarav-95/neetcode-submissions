# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge_lists(list1, list2):
            dummy = ListNode()
            res = dummy
            while list1 and list2:
                if list1.val > list2.val:
                    dummy.next = list2
                    list2 = list2.next
                else:
                    dummy.next = list1
                    list1 = list1.next
                dummy = dummy.next
              
            dummy.next = list1 or list2
            return res.next

        if len(lists) == 0:
            return None
        merged = lists[0]

        for i in range(1, len(lists)):
            temp = lists[i]
            merged = merge_lists(merged, temp)
        
        return merged
            