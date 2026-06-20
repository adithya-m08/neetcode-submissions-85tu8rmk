class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count=Counter(hand)

        minH=list(count.keys())
        heapq.heapify(minH)

        while minH:
            start=minH[0]
            for i in range(groupSize):
                if i+start not in count:
                    return False
                count[i+start]-=1
                if count[i+start]==0:
                    if i+start!=minH[0]:
                        return False
                    heapq.heappop(minH)
        return True