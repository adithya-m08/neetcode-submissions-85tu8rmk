class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols=len(grid), len(grid[0])
        q=deque()
        time=0
        fresh=0
        direction=[[1,0], [-1,0], [0,1], [0,-1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                if grid[r][c]==1:
                    fresh+=1
        

        while q and fresh:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in direction:
                    if r+dr in range(rows) and c+dc in range(cols) and grid[r+dr][c+dc]==1 :
                        grid[r+dr][c+dc]=2
                        q.append((r+dr,c+dc))
                        fresh-=1
            time+=1
        
        return time if not fresh else -1
                    