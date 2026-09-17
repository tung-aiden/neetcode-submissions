# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # determine if a tree is balanced or not
        # balanced -> left and right subtrees differ in height by no more than 1

        def dfs(curr):

            if not curr:
                return [True, 0]
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            hl = left[1]
            hr = right[1]
            balanced = abs(hl - hr) <= 1 and left[0] and right[0]

            return ([balanced, 1 + max(hl, hr)])
        
        res = dfs(root)
        return res[0]
            

            