class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        dp=dict()
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i==m:
                dp[(i,j)]=n-j
                return n-j
            if j==n:
                dp[(i,j)]=m-i
                return m-i

            if word1[i]==word2[j]:
                return dfs(i+1, j+1)

            res=min(dfs(i+1,j), dfs(i,j+1))
            res=min(dfs(i+1,j+1), res)
            dp[(i,j)]=res+1
            return res+1
        return dfs(0,0)