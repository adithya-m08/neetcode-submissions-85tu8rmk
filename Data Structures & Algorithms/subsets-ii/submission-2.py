class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]

        def dfs(i, curr):
            if i==len(nums):
                res.append(curr.copy())
                return
            
            dfs(i+1, curr+[nums[i]])

            while i<len(nums)-1 and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1, curr)
        dfs(0,[])
        return res