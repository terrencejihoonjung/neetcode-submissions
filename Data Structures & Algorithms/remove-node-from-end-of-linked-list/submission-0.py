# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get length of list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        idx = length - n
        if idx == 0: return head.next

        curr = head
        for i in range(idx - 1):
            curr = curr.next
            prev = curr
        
        prev = curr 
        curr = curr.next
        next = curr.next
        prev.next = next

        return head


# find length of list
# use length - n to get the ith node to remove 
# iterate to the node right before the ith node and modify the pointer 
#   - if the ith node is the first node, just return the next node. 

