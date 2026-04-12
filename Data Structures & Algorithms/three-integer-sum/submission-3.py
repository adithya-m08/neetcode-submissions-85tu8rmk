class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sortedn=sorted(nums)
        res=[]
        for i, a in enumerate(sortedn):
            if a>0:
                break
            if i>0 and a == sortedn[i-1]:
                continue

            x,y= i+1, len(sortedn)-1

            while x<y:
                s=a+sortedn[x]+sortedn[y]
                if s>0:
                    y-=1
                elif s<0:
                    x+=1
                else:
                    res.append([a,sortedn[x],sortedn[y]])
                    x+=1
                    while sortedn[x]==sortedn[x-1] and x<y:
                        x+=1
        return res