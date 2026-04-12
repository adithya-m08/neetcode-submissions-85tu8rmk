class Solution:
    def numDecodings(self, s: str) -> int:
        valid=set(range(1, 27))

        def dfs(i):
            if i >= len(s):
                return 1
            if s[i]=='0':
                return 0

            res=dfs(i+1)
            if i<len(s)-1 and int(s[i:i+2]) in valid:
                res+=dfs(i+2)
            
            return res
        
        return dfs(0)