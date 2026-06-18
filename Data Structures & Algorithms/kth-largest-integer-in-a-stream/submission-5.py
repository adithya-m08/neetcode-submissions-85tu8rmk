class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap=nums
        self.size=k
        heapq.heapify(nums)
        while len(nums)-k > 0:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap)-self.size> 0:
            heapq.heappop(self.heap)
        return self.heap[0]
