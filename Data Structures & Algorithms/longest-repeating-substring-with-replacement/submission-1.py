class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        for c in set(s):
            i,j=0,0
            countc=0
            while j<len(s):
                if s[j]==c:
                    countc+=1
                if j-i+1-countc<=k:
                    res=max(res, j-i+1)
                else:
                    if s[i]==c:
                        countc-=1
                    i+=1
                j+=1    
        return res