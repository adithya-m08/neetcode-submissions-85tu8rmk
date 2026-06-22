class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap=defaultdict(list)
        for u,v in prerequisites:
            premap[u].append(v)
        visited=set()
        def dfs(i):
            if i in visited:
                return False
            if i not in premap:
                return True
            
            visited.add(i)

            for course in premap[i]:
                if not dfs(course):
                    return False
            
            visited.remove(i)
            del premap[i]
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True