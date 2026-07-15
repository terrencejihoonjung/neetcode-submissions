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

        print(head.val)
        print(prev.val)
        
        # reorder 
        while head or prev:
            if head:
                head_next = head.next
                head.next = prev
                head = head_next
            
            if prev:
                prev_next = prev.next
                prev.next = head
                prev = prev_next

        return None