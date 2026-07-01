# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None: return list2
        if list2 == None: return list1
        
        head1 = list1
        head2 = list2

        curr = head1 if head1.val <= head2.val else head2
        dummy = curr

        if head1.val <= head2.val: head1 = head1.next
        else: head2 = head2.next

        while (head1 and head2):
            if head1.val <= head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next

            curr = curr.next
        
        if head1 == None: curr.next = head2
        if head2 == None: curr.next = head1
        return dummy


# iterate list1 and list2 in parallel
# append to a list depending on which list's elem is smaller
# if we exhaust either one, add the rest of the other 

