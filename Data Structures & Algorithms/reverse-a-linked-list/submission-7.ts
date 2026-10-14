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
     * @param {ListNode} head
     * @return {ListNode}
     */
    reverseList(head: ListNode | null): ListNode {
        if (!head) return null;

        let prev = null;
        while (head) {
            const next = head.next;
            head.next = prev;
            prev = head;
            head = next;
        }

        return prev;
    }
}
