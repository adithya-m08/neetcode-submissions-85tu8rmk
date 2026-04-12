class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(i,n, s):
            if s==target:
                res.append(n.copy())
                return
            elif i>=len(nums) or s>target:
                return

            n.append(nums[i])
            backtrack(i,n,s+nums[i])
            n.pop()
            backtrack(i+1,n,s)
        backtrack(0, [], 0)
        return res