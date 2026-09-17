# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        q = deque()
        q.append(root)
        while len(q) > 0:
            curr = q.popleft()
            left = curr.left
            right = curr.right
            curr.right = left
            curr.left = right
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return root

        '''
        if root == None:
            return
        
        left = root.left
        right = root.right
        root.left = right
        root.right = left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        '''
        

        