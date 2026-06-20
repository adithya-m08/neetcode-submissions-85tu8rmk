class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(openn, closen, curr):
            if openn==closen==n:
                res.append(curr)
                return
            if openn<n:
                dfs(openn+1, closen, curr+'(')
            if closen<openn:
                dfs(openn, closen+1, curr+')')
        dfs(0,0,'')
        return res
