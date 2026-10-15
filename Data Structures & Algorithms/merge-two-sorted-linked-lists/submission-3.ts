/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */
    mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode {
        if (!list1) return list2;
        if (!list2) return list1; 

        let p1 = list1;
        let p2 = list2;
        const dummy = new ListNode();
        let curr = dummy;

        while (p1 && p2) {
            if (p1.val <= p2.val) {
                curr.next = p1;
                p1 = p1.next;
            } else {
                curr.next = p2;
                p2 = p2.next;
            }
            curr = curr.next;
        }

        if (!p1) curr.next = p2;
        if (!p2) curr.next = p1;

        return dummy.next;
    }
}

// Iterate through lists in parallel using 2 pointers 
// If we exhaust either list, add the rest of the other list
// Each iteration, add whichever element is <= than the other. Then move the corresponding pointer
// 2n iterations in total -> time: O(n), space: O(n)