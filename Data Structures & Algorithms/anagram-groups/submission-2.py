class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for s in strs:
            key=tuple(sorted(s))
            if(key in d.keys()):
                d[key].append(s)
            else:
                d[key] = [s]
        return list(d.values())