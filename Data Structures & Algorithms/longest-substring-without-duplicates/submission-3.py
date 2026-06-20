class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0
        res=0
        cs=set()
        while j<len(s):
            while s[j] in cs:
                cs.remove(s[i])
                i+=1
            res=max(res, j-i+1)
            cs.add(s[j])
            j+=1
        return res                