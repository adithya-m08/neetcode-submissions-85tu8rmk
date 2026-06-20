class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        time=0
        l,r=1,max(piles)
        res=0
        while l<=r:
            k=(l+r)//2
            time=0
            for p in piles:
                time+=math.ceil(p/k)
            if time>h:
                l=k+1
            else:
                res=k
                r=k-1
        return res