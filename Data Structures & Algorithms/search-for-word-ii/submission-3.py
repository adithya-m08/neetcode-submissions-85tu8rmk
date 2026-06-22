class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows,cols=len(board), len(board[0])
        root=TrieNode()
        res=[]
        visited=set()

        for word in words:
            curr=root
            for char in word:
                if not char in curr.children:
                    curr.children[char]=TrieNode()
                curr=curr.children[char]
            curr.end=True

        def dfs(r,c,root,word):
            if r not in range(rows) or c not in range(cols) or (r,c) in visited or board[r][c] not in root.children:
                return
    
            visited.add((r,c))
            root=root.children[board[r][c]]
            word+=board[r][c]

            if root.end:
                res.append(word)
                root.end=False

            dfs(r+1,c,root,word)
            dfs(r,c+1,root,word)
            dfs(r-1,c,root,word)
            dfs(r,c-1,root,word)

            visited.remove((r,c))


        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")

        return res
                
