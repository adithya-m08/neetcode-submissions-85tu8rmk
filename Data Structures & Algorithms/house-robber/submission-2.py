class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n

        def dfs(i):
            if i>=len(nums):
                return 0
            if dp[i]!=-1:
                return dp[i]
            res= max(dfs(i+1), dfs(i+2)+nums[i])
            dp[i]=res
            return res
        return dfs(0)