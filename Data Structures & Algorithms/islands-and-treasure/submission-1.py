class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        q=deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))
        direc=[[1,0], [-1,0], [0,1], [0,-1]]
        dist=0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                grid[r][c]=dist
                for dr, dc in direc:
                    rn, cn=r+dr, c+dc
                    if rn>=0 and cn>=0 and rn<rows and cn<cols and grid[rn][cn]==2147483647:
                        grid[rn][cn]=dist+1
                        q.append((rn,cn))
            dist+=1

                