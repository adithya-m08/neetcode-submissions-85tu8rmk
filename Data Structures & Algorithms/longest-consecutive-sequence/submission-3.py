class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        res=0

        for n in nums:
            if n-1 in s:
                continue
            a=n
            c=1
            while a+1 in s:
                c+=1
                a+=1
            res=max(res,c)
        return res