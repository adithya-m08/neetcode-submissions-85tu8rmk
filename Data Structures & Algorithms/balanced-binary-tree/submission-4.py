# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res=True
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            
            l=dfs(root.left)
            r=dfs(root.right)

            diff=abs(l-r)
            res = res and True if diff<=1 else False
            return 1+max(l, r)
        dfs(root)
        return res

