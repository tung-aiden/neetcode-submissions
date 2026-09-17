# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        result = []
        i = 0
        curr = head
        while curr:
            result.append(curr)
            curr = curr.next
        j = len(result) - 1

        while i < j:
            result[i].next = result[j]
            i += 1
            result[j].next = result[i]
            j-= 1
        
        result[i].next = None
        



        
        