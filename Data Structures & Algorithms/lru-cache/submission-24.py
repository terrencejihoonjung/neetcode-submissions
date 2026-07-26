class Node():
    def __init__(self, key=-1, val=-1, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev= prev

class LRUCache:

    def __init__(self, capacity: int):
        self.pairs = {}
        self.size = capacity

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: Node) -> None:
        next = node.next
        prev = node.prev 

        next.prev = prev
        prev.next = next
    
    def addToHead(self, node: Node) -> None:
        next = self.head.next
        prev = self.head

        node.next = next
        node.prev = prev
        next.prev = node
        prev.next = node

    def get(self, key: int) -> int:
        if key not in self.pairs: return -1

        node = self.pairs[key]
        self.remove(node)
        self.addToHead(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.pairs: 
            self.remove(self.pairs[key])

        new_node = Node(key, value)
        self.addToHead(new_node)
        self.pairs[key] = new_node

        if self.size < len(self.pairs.keys()):
            lru = self.tail.prev

            print(self.pairs.keys(), lru.key)
            print(lru.key in self.pairs)

            del self.pairs[lru.key]
            self.remove(lru)

        
# use a doubly linked list to have access to head and tail 
# this allows us to add/remove from the front and back, 
#   having full control over least/most recently used elements

# track capacity limit via the count of the map's keys. 

# init
# - set limit, head, tail, and map (key -> node)

# remove(node): removes a node at any position 

# get
# - if key not in map, return -1
# - if key in map, 
#   - remove node 
#   - add node to head 
#   - return node's value 