class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.val=val
        self.key=key
        self.prev=prev
        self.next=next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache={}
        self.left, self.right=Node(0,0), Node(0,0)
        self.left.next, self.right.prev=self.right, self.left
    
    def insert(self, node):
        prev=self.right.prev
        prev.next=node
        node.prev=prev
        self.right.prev=node
        node.next=self.right

    def delete(self, node):
        prev, next=node.prev, node.next
        prev.next=next
        next.prev=prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            self.delete(node)
            self.insert(node)
            return node.val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        if self.cap< len(self.cache):
            del self.cache[self.left.next.key]
            self.delete(self.left.next)
