class ListNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key=key
        self.val=val
        self.prev=prev
        self.next=next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.capacity=capacity
        self.lru, self.mru=ListNode(0,0),ListNode(0,0)
        self.lru.next, self.mru.prev=self.mru, self.lru
    
    def insert(self, node: ListNode):
        self.mru.prev.next=node
        node.prev=self.mru.prev
        node.next=self.mru
        self.mru.prev=node
    
    def delete(self, node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def get(self, key: int) -> int:
        if key not in self.cache.keys():
            return -1
        node=self.cache[key]
        self.delete(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.delete(self.cache[key])
            del self.cache[key]
        self.cache[key]=ListNode(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru_node = self.lru.next
            self.delete(lru_node)
            del self.cache[lru_node.key]
        
