class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit=set()
        def dfs(node, parent):
            if node in visit:
                return False
            visit.add(node)
            for n in adj[node]:
                if n==parent:
                    continue
                if not dfs(n, node):
                    return False
            return True
        return dfs(0,-1) and len(visit)==n

