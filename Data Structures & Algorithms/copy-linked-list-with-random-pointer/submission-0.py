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
        if not head: return None

        node_dict = {}
        node_dict[None] = None
        curr = head
        while curr: 
            if curr not in node_dict:
                node_dict[curr] = Node(curr.val)
            curr = curr.next
        
        print(node_dict)
        curr = head 
        while curr:
            new_node = node_dict[curr]
            new_node.next = node_dict[curr.next]
            new_node.random = node_dict[curr.random]
            curr = curr.next
        
        return node_dict[head]
        
# traverse through list and map out nodes (old -> new)
#   - e.g., old_0 -> new_0, old_1, new_1

# then iterate through list again
# this time we can fill out next and random slots for new nodes 
