class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pset, aset=set(), set()
        rows, cols= len(heights), len(heights[0])
        res=[]
        def dfs(i,j,visit,height):
            if not i in range(rows) or not j in range(cols) or (i,j) in visit or height>heights[i][j]:
                return
            visit.add((i,j))
            dfs(i+1, j, visit, heights[i][j])
            dfs(i-1,j, visit, heights[i][j])
            dfs(i, j+1, visit,heights[i][j])
            dfs(i, j-1, visit, heights[i][j])

        for r in range(rows):
            dfs(r, 0, pset, -1)
            dfs(r, cols-1, aset, -1)
        
        for c in range(cols):
            dfs(0, c, pset, -1)
            dfs(rows-1, c, aset,-1)
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pset and (r,c) in aset:
                    res.append([r,c])
        return res