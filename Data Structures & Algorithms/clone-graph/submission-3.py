"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        m={}
        if not node:
            return
        def dfs(old):
            if old in m:
                return m[old]

            temp=Node(old.val)
            m[old]=temp

            new_nei=[]

            for nei in old.neighbors:
                new_nei.append(dfs(nei))

            m[old].neighbors=new_nei

            return m[old]

        dfs(node)
        return m[node]