class Solution:
    def rob(self, nums: List[int]) -> int:
        dp={}
        if len(nums)==1:
            return nums[0]
        def dfs(i, first):
            if i>=len(nums) or (i==len(nums)-1 and first):
                return 0
            if (i, first) in dp:
                return dp[(i, first)]
            
            dp[(i, first)]=max(dfs(i+1, first), nums[i]+ dfs(i+2, first or i==0))
            return dp[(i, first)]

        return max(dfs(0, True), dfs(1, False))