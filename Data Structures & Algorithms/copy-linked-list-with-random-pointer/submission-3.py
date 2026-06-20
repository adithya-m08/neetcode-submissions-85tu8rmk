"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        m=dict()
        curr=head
        if not head:
            return None
        
        while curr:
            temp=Node(curr.val)
            temp.next=curr.next
            m[curr]=temp
            curr=curr.next
        
        curr=head
        while curr:
            m[curr].next=m[curr.next] if curr.next else None
            m[curr].random=m[curr.random] if curr.random else None
            curr=curr.next
        
        return m[head]