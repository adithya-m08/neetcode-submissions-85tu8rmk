from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dfs(i, rob):
            nonlocal nums
            if i>=len(nums):
                return rob
            rob+=nums[i]
            a=dfs(i+2, rob)

            rob-=nums[i]
            b=dfs(i+1, rob)

            return max(a,b)
        return dfs(0,0)