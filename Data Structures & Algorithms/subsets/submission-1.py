class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(nums,s):
            if not len(nums):
                res.append(s)
                return
            s.append(nums[0])
            backtrack(nums[1:],s.copy())
            s.remove(nums[0])
            backtrack(nums[1:],s)

        backtrack(nums,[])
        return res