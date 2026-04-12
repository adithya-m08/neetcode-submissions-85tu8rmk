# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root, subRoot):
            if root and subRoot and root.val==subRoot.val:
                return isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)
            elif root ==None and subRoot==None:
                return True
            else:
                return False
        if not root:
            return False

        if root.val==subRoot.val:
            return isSameTree(root,subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)