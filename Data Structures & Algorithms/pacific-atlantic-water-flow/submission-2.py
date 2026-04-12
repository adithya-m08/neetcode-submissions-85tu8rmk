class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic=set(), set()
        rows, cols = len(heights), len(heights[0])
        direc=[[0,1],[1,0], [-1,0], [0,-1]]

        def dfs(i,j, visited, prev):
            if 0<=i<rows and 0<=j<cols and heights[i][j]>=prev and (i,j) not in visited:
                visited.add((i,j))
                for dr, dc in direc:
                    nr, nc=i+dr, j+dc
                    dfs(nr, nc, visited, heights[i][j])
            
        for r in range(rows):
            dfs(r, cols-1, atlantic, -1)
            dfs(r, 0, pacific, -1)
        
        for c in range(cols):
            dfs(rows-1, c, atlantic, -1)
            dfs(0, c, pacific, -1)

        print(pacific)
        res=[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])

        return res