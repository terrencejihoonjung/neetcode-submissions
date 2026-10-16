class ListNode {
    key: number;
    val: number;
    next: ListNode | null;
    prev: ListNode | null;

    constructor(key: number = -1, val: number = -1, next: ListNode | null = null, prev: ListNode | null = null) {
        this.key = key;
        this.val = val;
        this.next = next;
        this.prev = prev;
    }
}

class LRUCache {
    capacity: number;
    head: ListNode | null;
    tail: ListNode | null;
    nodes: Map<number, ListNode>; // key -> Node
    
    /**
     * @param {number} capacity
     */
    constructor(capacity: number) {
        this.capacity = capacity;

        this.head = new ListNode();
        this.tail = new ListNode();
        this.tail.prev = this.head;
        this.head.next = this.tail;

        this.nodes = new Map<number, ListNode>();
    }

    remove(node: ListNode): void {
        const prev = node.prev;
        const next = node.next;
        prev.next = next;
        next.prev = prev;
    }

    addToTail(node: ListNode): void {
        const prev = this.tail.prev;
        prev.next = node;
        this.tail.prev = node;

        node.prev = prev;
        node.next = this.tail;
    }

    /**
     * @param {number} key
     * @return {number}
     */
    get(key: number): number {
        if (!this.nodes.has(key)) return -1;

        // mark as used 
        const node = this.nodes.get(key);
        this.remove(node);
        this.addToTail(node);

        return node.val;
    }

    /**
     * @param {number} key
     * @param {number} value
     * @return {void}
     */
    put(key: number, value: number): void {
        // update if exists
        if (this.nodes.has(key)) {
            const node = this.nodes.get(key);
            this.remove(node);
            this.addToTail(node);
            node.val = value;
            return;
        }

        // check capcity
        if (this.capacity === this.nodes.size) {
            const nodeToRemove = this.head.next;
            this.remove(nodeToRemove);
            this.nodes.delete(nodeToRemove.key);
        }

        // add node 
        const newNode = new ListNode(key, value);
        this.addToTail(newNode)
        this.nodes.set(key, newNode);
    }
}

// need a way to mark pairs as used in the context of time 
// - remove node from doubly linked list and move it to head

// need a way to remove least recently used key in O(1) while also 
// - use map to track key-Node pairs and use a O(1) remove method

// maintian doubly linked list where we can 
// - remove a node at any position 
// - add to the tail

// get method should:
// - mark pair as used (remove + add to head)
// - return value

// put method should:
// - update if exists 
// - check capacity is full -> remove node from list AND map
// - add node to tail + map
