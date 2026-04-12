class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedn=sorted(nums)
        res=[]
        for i,num in enumerate(sortedn):
            a=num
            if a>0:
                break
            if i>0 and a == sortedn[i-1]:
                continue

            l,r = i+1, len(sortedn)-1
            while l<r:
                if((sortedn[l]+sortedn[r]+a)>0):
                    r-=1
                elif((sortedn[l]+sortedn[r]+a)<0):
                    l+=1
                else:
                    res.append([a,sortedn[l],sortedn[r]])
                    l+=1
                    while sortedn[l]==sortedn[l-1] and l<r:
                        l+=1
        
        return res