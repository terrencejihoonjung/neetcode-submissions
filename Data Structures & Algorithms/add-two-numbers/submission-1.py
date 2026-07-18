# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        ret = curr
        
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0 
            sum = val1 + val2 + carry 

            if sum < 10: 
                curr.next = ListNode(sum)
                carry = 0
            elif sum >= 10:
                remainder = sum % 10
                carry = 1
                curr.next = ListNode(remainder)

            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if carry == 1: curr.next = ListNode(carry)
        
        return ret.next

# go through both lists:
# - if sum < 10, create new node(sum)
# - if sum >= 10:
#   - calculate sum % 10 (e.g., 18 % 10 = 8)
#   - create new node(remainder)
#   - carry over to next sum calculated
# - at the end, if carry over exists, just add one more node to the end of the list