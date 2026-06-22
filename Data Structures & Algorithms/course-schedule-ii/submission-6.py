class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        premap=defaultdict(list)

        for u,v in prerequisites:
            premap[u].append(v)
        
        res=[]
        visited=set()
        completed=set()

        def dfs(i):
            if i in visited:
                return False
            if i in completed:
                return True
            
            visited.add(i)

            for course in premap[i]:
                if not dfs(course):
                    return False

            res.append(i)
            completed.add(i)
            visited.remove(i)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
                