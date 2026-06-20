class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited=set()
        
        def dfs(node):
            if node is None or node in visited:
                return
            
            visited.add(node)

            for nei in adj[node]:
                dfs(nei)
        
        res=0
        for node in range(n):
            if not node in visited:
                dfs(node)
                res+=1
        return res