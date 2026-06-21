class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols=len(board), len(board[0])
        visited=set()
        def dfs(i,j):
            if i not in range(rows) or j not in range(cols) or (i,j) in visited or board[i][j]=='X':
                return
            
            visited.add((i,j))

            board[i][j]='T'

            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            
        for i in range(rows):
            board[i][0]='T' if board[i][0]=='O' else board[i][0]
            board[i][cols-1]='T' if board[i][cols-1]=='O' else board[i][cols-1]
        for j in range(cols):
            board[0][j]='T' if board[0][j] =='O' else  board[0][j]
            board[rows-1][j]='T' if  board[rows-1][j] =='O' else  board[rows-1][j]
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='T':
                    dfs(r,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='T':
                    board[r][c]='O'
                elif board[r][c]=='O':
                    board[r][c]='X'