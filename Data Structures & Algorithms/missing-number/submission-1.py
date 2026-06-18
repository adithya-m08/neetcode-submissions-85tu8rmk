class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumn=0
        for n in nums:
            sumn+=n
        target=(len(nums)*(len(nums)+1))/2
        return int(target-sumn)