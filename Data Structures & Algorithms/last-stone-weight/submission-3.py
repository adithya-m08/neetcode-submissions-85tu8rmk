class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[-s for s in stones]

        heapq.heapify(heap)

        while len(heap)>1:
            a=heapq.heappop(heap)
            b=heapq.heappop(heap)

            n=abs(a-b)

            if n>0:
                heapq.heappush(heap, -n)
            
        return -heap[0] if heap else 0