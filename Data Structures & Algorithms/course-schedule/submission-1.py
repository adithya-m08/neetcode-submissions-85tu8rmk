class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map={}
        map = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            map[c].append(p)
        cycle=set()

        def dfs(c):
            if c in cycle:
                return False
            
            if map[c] == []:
                return True
            
            cycle.add(c)
            for p in map[c]:
                if not dfs(p):
                    return False
            cycle.remove(c)
            map[c]=[]
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True