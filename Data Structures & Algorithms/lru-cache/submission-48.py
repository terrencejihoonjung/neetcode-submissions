class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.limit = capacity
        self.nodes = {} 

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def addToHead(self, node: Node) -> None:
        next = self.head.next

        self.head.next = node
        next.prev = node

        node.next = next
        node.prev = self.head

    def addToTail(self, node: Node) -> None:
        prev = self.tail.prev

        self.tail.prev.next = node
        self.tail.prev = node

        node.next = self.tail
        node.prev = prev
        
    def remove(self, node: Node) -> None:
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key not in self.nodes: return -1

        node = self.nodes[key]

        self.remove(node)
        self.addToHead(node)
        
        return node.val
        
    def put(self, key: int, value: int) -> None:
        # if capacity is reached, remove from tail and map 
        if len(self.nodes) == self.limit and key not in self.nodes:
            del self.nodes[self.tail.prev.key]
            self.remove(self.tail.prev)

        
        # update map and update doubly linked list
        if key not in self.nodes:
            self.nodes[key] = Node(key, value)
        else:
            node = self.nodes[key]
            node.val = value
            self.remove(node)
        
        self.addToHead(self.nodes[key])



        
# how to track recency of a node?
#   - doubly linked list (deque)
#   - removing a node from a deque -> O(1)
#   - adding a node to head or tail -> O(1) 

# we can add a node to head or tail in O(1) time 
# to remove a node anywhere, we need the reference to the node
#   - create a mapping of key to node for O(1) access
#   - the map's size helps us gauge whether we are at capacity or not 

# need remove, addToHead, addToTail methods 
#   - remove: remove from list 
#   - add: add to list