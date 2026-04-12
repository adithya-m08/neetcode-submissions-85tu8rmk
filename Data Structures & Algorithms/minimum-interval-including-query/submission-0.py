class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res=[]
        intervals.sort(key=lambda x:x[0])
        for q in queries:
            op=float('inf')
            for i in intervals:
                if i[0]<=q<=i[1]:
                    op=min(op, i[1]-i[0]+1)
            res.append(op if op!=float('inf') else -1)
        return res