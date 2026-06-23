class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)

        if n==0:
            return 0
        
        leftm=[0]*n
        rightm=[0]*n

        leftm[0]=height[0]
        for i in range(1,n):
            leftm[i]=max(height[i], leftm[i-1])
        
        rightm[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            rightm[i]=max(height[i], rightm[i+1])
        
        res=0
        for i in range(n):
            res+=min(leftm[i], rightm[i])-height[i]
        
        return res