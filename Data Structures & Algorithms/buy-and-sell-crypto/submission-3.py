class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                c=prices[j]-prices[i]
                p=max(c,p)
        
        return p
                    