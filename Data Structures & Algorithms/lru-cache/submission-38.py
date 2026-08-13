class Node:
    def __init__(self, key: int = -1, val: int = -1, next: Optional["Node"] = None, prev: Optional["Node"] = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.pairs = {} 

        self.head = Node()
        self.tail = Node() 

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove_at_node(self, node: Node) -> None:
        next = node.next 
        prev = node.prev
        prev.next = next
        next.prev = prev
    
    def add_to_head(self, node: Node) -> None:
        next = self.head.next
        self.head.next = node 
        next.prev = node 

        node.prev = self.head 
        node.next = next

    def get(self, key: int) -> int:
        if key not in self.pairs: return -1 

        node = self.pairs[key]

        # remove from list 
        self.remove_at_node(node)

        # add new node to head 
        self.add_to_head(node)

        # return value 
        return node.val


    def put(self, key: int, value: int) -> None:
        # remove if node exists in list 
        if key in self.pairs:
            node = self.pairs[key]
            self.remove_at_node(node)
            del self.pairs[node.key]
        
        # if we are at capacity, we should remove the least recently used key 
        if len(self.pairs) >= self.capacity:
            node_to_remove = self.tail.prev
            self.remove_at_node(node_to_remove)
            del self.pairs[node_to_remove.key]

        # add new node to head 
        new_node = Node(key, value)
        self.add_to_head(new_node)

        # update key-value pair in map 
        self.pairs[key] = new_node

        
# storing unique key-value pairs in cache (map in this case)
# how do we track the LRU key-value pair?

# we'll need logic to update pairs that get "used" 
# we'll need logic to remove LRU pairs 

# we can use a doubly linked list to move nodes (pairs) around as needed

# get: update the node as recently used (remove node, add node to front), return the pair's value

# put: 
#   - if key not in map, we just add to front
#   - if key in map, we update node as recently used, update map's key-value 

# we need removeAtNode, addToHead methods 
# keep track of a tail and head node 
# keep track of a map that maps keys to nodes
# nodes should contain key, value, next, prev 