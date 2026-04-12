# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i,j=head,head

        for _ in range(n):
            j=j.next
        
        if not j:
            return head.next

        while j.next:
            j=j.next
            i=i.next
        i.next=i.next.next

        return head