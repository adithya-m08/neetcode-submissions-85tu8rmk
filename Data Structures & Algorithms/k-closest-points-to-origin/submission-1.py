class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for p in points:
            heap.append((math.sqrt(p[0]*p[0]+p[1]*p[1]), p[0], p[1]))
        heapq.heapify(heap)

        res=[]
        for _ in range(k):
            p=heapq.heappop(heap)
            res.append([p[1], p[2]])
        return res
        