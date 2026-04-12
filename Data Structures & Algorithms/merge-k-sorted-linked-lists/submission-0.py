# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        res = ListNode(0)
        cur = res
        minHeap = []

        for lst in lists:
            if lst is not None:
                heapq.heappush(minHeap, (lst.val,id(lst), lst))

        while minHeap:
            node = heapq.heappop(minHeap)[2]
            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(minHeap, (node.next.val,id(node.next),node.next))

        return res.next