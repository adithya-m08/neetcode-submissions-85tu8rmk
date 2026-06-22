# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res=ListNode(0)
        minh=[]
        curr=res

        for node in lists:
            if node is not None:
                heapq.heappush(minh, (node.val, id(node), node))
        
        while minh:
            node=heapq.heappop(minh)[2]
            curr.next=node
            curr=curr.next

            if node.next:
                heapq.heappush(minh, (node.next.val, id(node.next), node.next))
        return res.next