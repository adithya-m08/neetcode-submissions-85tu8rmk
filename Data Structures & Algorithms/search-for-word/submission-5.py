class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols=len(board), len(board[0])
        visited=set()
        def dfs(r,c,i):
            if i==len(word):
                return True
            if not r in range(rows) or not c in range(cols) or (r,c) in visited or board[r][c]!=word[i]:
                return False
            visited.add((r,c))
            found=dfs(r+1, c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            visited.remove((r,c))
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c]==word[0]:
                    if dfs(r,c,0):
                        return True
        return False