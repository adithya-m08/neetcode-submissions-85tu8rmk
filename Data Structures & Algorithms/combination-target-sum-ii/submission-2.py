class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def dfs(i, curr, target):
            if target==0:
                res.append(curr.copy())
                return

            if target<0 or i>=len(candidates):
                return
            
            dfs(i+1, curr+[candidates[i]], target-candidates[i])

            while i<len(candidates)-1 and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1, curr, target)

        dfs(0,[],target)
        return res