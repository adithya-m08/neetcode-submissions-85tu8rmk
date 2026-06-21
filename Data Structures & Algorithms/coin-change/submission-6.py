class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res=float('inf')
        dp={}
        def dfs(i, amount):
            nonlocal res
            if (i, amount) in dp:
                return dp[(i,amount)]
            if amount==0:
                return 0 
            if amount<0 or i>=len(coins):
                return float('inf')
            take = 1+dfs(i, amount-coins[i])
            skip = dfs(i+1, amount)
            dp[(i,amount)]=min(take, skip)
            return dp[(i,amount)]
        res=dfs(0,amount)
        return -1 if res==float('inf') else res