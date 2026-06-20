class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1=Counter(s1)

        need=len(c1)

        for i in range(len(s2)):
            c2, curr=defaultdict(int), 0

            for j in range(i, len(s2)):
                c2[s2[j]]+=1
                if c1[s2[j]]<c2[s2[j]]:
                    break
                if c1[s2[j]]==c2[s2[j]]:
                    curr+=1
                if curr==need:
                    return True
        return False