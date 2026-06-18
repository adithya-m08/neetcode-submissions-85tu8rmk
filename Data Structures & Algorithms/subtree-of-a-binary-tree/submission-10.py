# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root==None and subRoot!=None:
            return False
        def isSameTree(a, b):
            if a==None and b==None:
                return True
            if (a!=None and b==None) or (a==None and b!=None):
                return False
            if a!=None and b!=None and a.val!=b.val:
                return False
            return isSameTree(a.left, b.left) and isSameTree(a.right, b.right)
        
        if root.val==subRoot.val:
            if isSameTree(root,subRoot):
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)