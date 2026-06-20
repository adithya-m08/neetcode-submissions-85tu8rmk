from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dfs(i, j):
            if not i in range(m) or not j in range(n):
                return 0
            if (i,j)==(m-1,n-1):
                return 1
            return dfs(i+1,j)+dfs(i, j+1)

        return dfs(0,0)