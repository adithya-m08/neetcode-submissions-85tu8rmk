# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res=list3=ListNode()

        while list1 and list2:
            if list1.val<=list2.val:
                temp=ListNode()
                temp.val=list1.val
                list3.next=temp
                list1=list1.next
                list3=list3.next
            else:
                temp=ListNode()
                temp.val=list2.val
                list3.next=temp
                list2=list2.next
                list3=list3.next
        
        if list1:
            list3.next=list1
        
        elif list2:
            list3.next=list2
        
        return res.next