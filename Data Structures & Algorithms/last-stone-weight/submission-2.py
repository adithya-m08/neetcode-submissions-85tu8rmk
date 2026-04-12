class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[-x for x in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            a=heapq.heappop(heap)
            b=heapq.heappop(heap)
            if abs(a-b)>0:
                heapq.heappush(heap, -abs(a-b))
        
        return -heap[0] if len(heap)==1 else 0