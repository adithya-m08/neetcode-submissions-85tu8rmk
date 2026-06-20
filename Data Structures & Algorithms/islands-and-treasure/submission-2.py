class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols=len(grid), len(grid[0])
        inf=2147483647

        q=deque()
        time=0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))
        
        directions=[[1,0],[-1,0],[0,1],[0,-1]]

        while q:
            time+=1
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    row, col=r+dr, c+dc
                    if row in range(rows) and col in range(cols) and grid[row][col]==inf:
                        grid[row][col]=time
                        q.append((row,col))


