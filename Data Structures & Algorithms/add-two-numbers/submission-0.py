# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # given two non-empty linkedlists
        # each one represents a non negative integer
        # digits are stored in reverse order
        # 123 is stored as
        # 3 -> 2 -> 1 ->
        # each node has a single digit
        # no leading zeros, except 0 itself
        # return the sum

        # initial thoughts:
        # go through each list, check if there is a val at current node, add the twovals together
        # check if it is above 10, if it is %10, and carry over the 1 to the next value

        # instantiating a dummy node to return later
        dummy = ListNode()
        # temp var to trtack current node, we will add our sum to this node
        current = dummy
        # insantiaite carry var -> should always be either 0 or 1
        carry = 0

        # go while we still need to add numbers
        while l1 or l2 or carry:
            # check for a l1 #, if none, 0
            if l1:
                list1_val = l1.val
                l1 = l1.next
            else:
                list1_val = 0
            # check for a l2 #, if none, 0
            if l2:
                list2_val = l2.val
                l2 = l2.next
            else:
                list2_val = 0
            
            curr_sum = list1_val + list2_val + carry
            if curr_sum < 10:
                current.next = ListNode(curr_sum)
                carry = 0
                current = current.next
            # >= 10, we need to carry to other side
            else:
                carry = 1
                curr_sum = curr_sum % 10
                current.next = ListNode(curr_sum)
                current = current.next
        return dummy.next

            


        