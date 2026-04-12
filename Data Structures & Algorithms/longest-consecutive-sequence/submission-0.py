class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setn = set(nums)

        res=0

        for num in setn:
            if(num-1) not in setn:
                l=1
                while(num+l) in setn:
                    l+=1
                res=max(res,l)
        return res