"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # intuition -> i can create a dictionary to store each Nodes next and random

        cur = head
        # initializing with None: None -> node might be None
        lookup = {None:None}

        curr = head
        # mapping a copy of current nodes to a new copy
        # this new copy does not have the next and random pointers yet
        while curr:
            new = Node(curr.val)
            lookup[curr] = new
            curr = curr.next
        
        curr = head
        while curr:
            temp = lookup[curr]
            temp.next = lookup[curr.next]
            temp.random = lookup[curr.random]
            curr = curr.next
        return lookup[head]




        
        