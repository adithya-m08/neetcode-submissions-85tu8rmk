class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols=len(board), len(board[0])

        dr, dc, dsq= defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(rows):
            for c in range(cols):
                if(board[r][c]=='.'):
                    continue
                if((board[r][c] in dr[r]) or (board[r][c] in dc[c]) or 
                (board[r][c] in dsq[(r//3,c//3)])):
                    return False
                
                dr[r].add(board[r][c])
                dc[c].add(board[r][c])
                dsq[(r//3,c//3)].add(board[r][c])
        return True
                