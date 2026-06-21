class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i=0
        n=len(nums)
        res=[]
        while i<n:
            a=nums[i]
            if a>0:
                break
            
            j,k=i+1,n-1
            while j<k:
                sum=a+nums[j]+nums[k]
                if sum>0:
                    k-=1
                elif sum<0:
                    j+=1
                else:
                    res.append([a, nums[j], nums[k]])
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i+=1
            while i<n and nums[i]==nums[i-1]:
                i+=1
        return res


