class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited=set()

        def dfs(i,j):
            if i>=rows or j>=cols or i<0 or j<0 or (i,j) in visited or grid[i][j]=='0':
                return
            
            visited.add((i,j))
            grid[i][j]='0'

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        res=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    dfs(i,j)
                    res+=1

        return res