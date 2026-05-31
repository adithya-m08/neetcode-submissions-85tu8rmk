class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * 2*n
        for a in range(n):
            ans[a] = ans[a+n]=nums[a]

        return ans