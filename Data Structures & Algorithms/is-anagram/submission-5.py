class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds=defaultdict(int)
        dt=defaultdict(int)

        if len(s)!=len(t):
            return False
        
        for i in range(len(s)):
            ds[s[i]]+=1
            dt[t[i]]+=1

        return ds==dt