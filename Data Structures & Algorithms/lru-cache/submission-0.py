class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.cache = {}
        # keeping two dummy nodes to keep track of the LRU and MRU
        # left node (next) is the LRU
        # right node (prev) is the MRU
        self.left = Node(0,0)
        self.right = Node(0,0)
        # we will insert nodes in between the two dummy nodes
        self.left.next = self.right
        self.right.prev = self.left
    
    # remove node from the linked list
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    # insert at the MRU place
    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        self.right.prev = node
        node.next = self.right
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove the node from linkedlist
            self.remove(self.cache[key])
            # add it again to the MRU
            self.insert(self.cache[key])
            # return the value
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove the old key value from linkedlist
            self.remove(self.cache[key])
        # update the cache
        self.cache[key] = Node(key, value)
        # insert into MRU
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove from linked_list and delete from cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



        
