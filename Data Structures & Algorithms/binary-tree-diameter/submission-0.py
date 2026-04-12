# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestPath(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.longestPath(root.left),self.longestPath(root.right)) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        diameter = self.longestPath(root.left) + self.longestPath(root.right)
        
        return max(diameter, max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)))