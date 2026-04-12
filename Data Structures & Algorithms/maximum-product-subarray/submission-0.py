class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[0]*n for _ in range(n)]
        res=nums[0]
        for i in range(len(nums)):
            prod=nums[i]
            res=max(res,prod)
            for j in range(i+1,len(nums)):
                prod*=nums[j]
                res=max(res, prod)

        return res