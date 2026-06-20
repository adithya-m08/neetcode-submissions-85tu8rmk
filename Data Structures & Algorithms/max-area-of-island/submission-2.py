class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols=len(grid), len(grid[0])
        visited=set()

        def dfs(r,c):
            if not r in range(rows) or not c in range(cols) or (r,c) in visited or grid[r][c]==0:
                return 0
            
            visited.add((r,c))

            return 1+dfs(r+1, c)+dfs(r-1, c)+dfs(r, c+1)+dfs(r, c-1)
        
        res=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    area=dfs(r,c)
                    res=max(res, area)
        return res