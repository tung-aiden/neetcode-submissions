# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        # reverse the list
        # curr = head
        # prev = None
        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp

        # add the nodes to an array
        curr = head
        arr = []
        while curr:
            arr.append(curr)
            curr = curr.next
        index_to_remove = len(arr) - n
        # removing head
        if index_to_remove == 0:
            head = head.next
            return head
        # removing last node
        elif index_to_remove == len(arr) - 1:
            last_node = arr[index_to_remove - 1]
            last_node.next = None
            return head
        # removal in the middle
        else:
            dummy = arr[index_to_remove - 1]
            dummy.next = arr[index_to_remove + 1]
            return head

        

        


        
        