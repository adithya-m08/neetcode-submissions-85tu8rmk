class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        for s in strs:
            res+=str(len(s))+'#'+s
        return res

    def decode(self, s: str) -> List[str]:
        i,j=0,0
        res=[]
        while i < len(s):
            if s[i] == '#':
                l = int(s[j:i])
                res.append(s[i+1:i+l+1])
                j=i=i+l+1
            i+=1
        return res