class ListNode {
    key: number;
    val: number;
    prev: ListNode | null;
    next: ListNode | null;

    constructor(key: number = -1, val: number = -1, prev: ListNode | null = null, next: ListNode | null = null) {
        this.key = key;
        this.val = val;
        this.prev = prev;
        this.next = next;
    }
}

class LRUCache {
    capacity: number;
    head: ListNode;
    tail: ListNode;
    nodes: Map<number, ListNode>;


    /**
     * @param {number} capacity
     */
    constructor(capacity: number) {
        this.capacity = capacity;
        this.nodes = new Map<number, ListNode>();

        this.head = new ListNode();
        this.tail = new ListNode();
        this.tail.prev = this.head;
        this.head.next = this.tail;
    }

    remove(node: ListNode) {
        const prev = node.prev;
        const next = node.next;
        prev.next = next;
        next.prev = prev;
    }

    addToTail(node: ListNode) {
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
        if (this.nodes.has(key)) {
            const node = this.nodes.get(key);
            node.val = value;
            this.remove(node);
            this.addToTail(node);
            return;
        }

        if (this.nodes.size === this.capacity) {
            const nodeToRemove = this.head.next;
            this.remove(nodeToRemove);
            this.nodes.delete(nodeToRemove.key);
        }

        const newNode = new ListNode(key, value);
        this.addToTail(newNode);
        this.nodes.set(key, newNode);
    }
}

// need to way to consider usage on a get or put 
// - then we can remove the least recently used pair when capacity is full
// - need a data structure that can remove elements and add them to the back
// - add fresh elements to the front 
// - need a doubly linked list (deque)

// implement remove method given node 
// implement addToTail method given node 

// implement doubly linked list using head and tail node 
// track nodes using map<key, node>

// get:
// - check if node exists 
// - mark node as used: remove, add to tail 
// - return value 

// put:
// - check for existing node -> update, mark as used, and early return 
// - check capacity. If full, remove lru node from deque and map
// - add new node to tail