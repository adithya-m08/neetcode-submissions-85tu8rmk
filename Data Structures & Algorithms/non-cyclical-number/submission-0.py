class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast= n, self.sumofsquare(n)
        while slow!=fast:
            fast=self.sumofsquare(fast)
            fast=self.sumofsquare(fast)
            slow=self.sumofsquare(slow)
        return fast==1 

    def sumofsquare(self, n: int):
        res=0
        while n:
            digit=n%10
            digit=digit**2
            res+=digit
            n=n//10
        return res
        