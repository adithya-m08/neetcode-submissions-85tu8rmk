class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh=0
        rows, cols=len(grid), len(grid[0])
        q=deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append((r,c))
        res=0
        direc=[[1,0], [0,1], [-1,0], [0,-1]]

        while fresh and q:
            for _ in range(len(q)):
                r,c=q.popleft()
                
                for dr, dc in direc:
                    nr, nc=r+dr, c+dc

                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        fresh-=1
                        grid[nr][nc]=2
                        q.append((nr,nc))    

            res+=1
        
        return res if not fresh else -1