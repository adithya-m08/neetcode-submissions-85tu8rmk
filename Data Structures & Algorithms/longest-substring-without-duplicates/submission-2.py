class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setc=set()
        res=0
        i,j=0,0
        while j<len(s):
            while s[j] in setc:
                setc.remove(s[i])
                i+=1
            setc.add(s[j])
            res=max(j-i+1,res)

            j+=1
        return res