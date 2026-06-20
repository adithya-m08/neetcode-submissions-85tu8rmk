class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i, curr):
            if i>=len(nums) or sum(curr)>target:
                return
            if sum(curr)==target:
                res.append(curr.copy())
                return
            dfs(i, curr+[nums[i]])
            dfs(i+1, curr)
        dfs(0,[])
        return res

            