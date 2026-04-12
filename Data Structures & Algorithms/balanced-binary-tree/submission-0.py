# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 

        self.res=True

        def dfs(root) -> int:
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            self.res= self.res and (abs(left-right)<=1)
            return 1+max(left,right)
                
        dfs(root)
        return self.res
        