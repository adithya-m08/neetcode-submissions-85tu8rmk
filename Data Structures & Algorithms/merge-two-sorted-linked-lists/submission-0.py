# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode()
        head=res
        while(list1 and list2):
            if(list1.val<=list2.val):
                temp=ListNode(list1.val,None)
                head.next=temp
                head=temp
                list1=list1.next
            elif(list2.val<list1.val):
                temp=ListNode(list2.val,None)
                head.next=temp
                head=temp
                list2=list2.next
        if list1:
            head.next=list1
        elif list2:
            head.next=list2
        return res.next