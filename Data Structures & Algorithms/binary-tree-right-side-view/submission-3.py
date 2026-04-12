# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        q=deque()
        q.append(root)
        while q:
            rightn=None
            for i in range(len(q)):
                
                n=q.popleft()
                if n:
                    rightn=n
                    q.append(n.left)
                    q.append(n.right)
            if rightn:
                res.append(rightn.val)
        return res