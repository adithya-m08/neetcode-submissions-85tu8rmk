class Solution:
    def isHappy(self, n: int) -> bool:
        def sumofsquares(num):
            res=0
            while num:
                d=num%10
                res+=d*d
                num=num//10
            return res
        
        visit=set()

        while n not in visit:
            visit.add(n)
            n=sumofsquares(n)
            if n==1:
                return True
        
        return False
