class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns= set(nums)
        res=0
        for n in nums:
            if(n-1 in ns):
                continue
            l=1
            while(n+1 in ns):
                l+=1
                n+=1
            res=max(res, l)

        return res