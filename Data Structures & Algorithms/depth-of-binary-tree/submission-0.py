# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(curr):

            if not curr:
                return 0
            if curr.left:
                left = dfs(curr.left)
            else:
                left = 0
            if curr.right:
                right = dfs(curr.right)
            else:
                right = 0
            return 1 + max(left,right)
            
        return dfs(root)
        