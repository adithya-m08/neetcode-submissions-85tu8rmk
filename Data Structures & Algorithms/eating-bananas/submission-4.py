class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i,j=1,max(piles)
        res=0
        while i<=j:
            k=(i+j)//2
            totaltime=0
            for p in piles:
                totaltime+=math.ceil(p/k)
            if totaltime<=h:
                res=k
                j=k-1
            else:
                i=k+1
            
        return res