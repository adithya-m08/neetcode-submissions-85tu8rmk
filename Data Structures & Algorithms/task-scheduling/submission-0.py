class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks=list(Counter(tasks).values())
        tasks=[-t for t in tasks]
        heapq.heapify(tasks)
        q=deque()
        time=0
        while tasks or q:
            time+=1

            if not tasks:
                time=q[0][1]

            else:
                count=1+heapq.heappop(tasks)
                if count<0:
                    q.append([count, time+n])
            if q and time==q[0][1]:
                heapq.heappush(tasks, q.popleft()[0])
            
        return time