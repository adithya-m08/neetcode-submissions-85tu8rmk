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
        def dfs(old):
            if not old:
                return None
            if old in m:
                return m[old]
            t=Node(old.val)
            m[old]=t
            for i in range(len(old.neighbors)):
                if old.neighbors[i]:
                    t.neighbors.append(dfs(old.neighbors[i]))
            return t

        return dfs(node)