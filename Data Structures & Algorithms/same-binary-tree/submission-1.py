# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # queue -> FIFO

        # using bfs, going level by level comparing both of the trees
        queue = deque()
        if not p and q:
            return False
        if not q and p:
            return False
        if p == None and q == None:
            return True
        # p first
        queue.append(p)
        queue.append(q)

        while len(queue) > 0:
            p_curr = queue.popleft()
            q_curr = queue.popleft()

            if p_curr.val != q_curr.val:
                return False

            if p_curr.left and not q_curr.left:
                return False
            if not p_curr.left and q_curr.left:
                return False
            if p_curr.right and not q_curr.right:
                return False
            if not p_curr.right and q_curr.right:
                return False
            if p_curr.left and q_curr.left:
                queue.append(p_curr.left)
                queue.append(q_curr.left)
            if p_curr.right and q_curr.right:
                queue.append(p_curr.right)
                queue.append(q_curr.right)
        return True



        