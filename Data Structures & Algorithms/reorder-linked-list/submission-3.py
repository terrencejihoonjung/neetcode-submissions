# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next: return None

        # use slow fast pointer to get a ref to the middle node
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse 2nd half of list
        next = slow.next
        slow.next = None 
        slow = next

        prev = None
        curr = slow
        while curr: 
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # reorder 
        while prev:
            tmp1, tmp2 = head.next, prev.next
            head.next = prev
            prev.next = tmp1 

            head = tmp1 
            prev = tmp2
