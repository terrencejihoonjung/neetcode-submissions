/**
 * // Definition for a Node.
 * class Node {
 *     constructor(val = 0, neighbors = []) {
 *       this.val = val;
 *       this.neighbors = neighbors;
 *     }
 * }
 */

class Solution {
    /**
     * @param {Node} node
     * @return {Node}
     */
    cloneGraph(node: Node | null): Node {
        if (!node) return null;

        const nodes = new Map<Node, Node>();
        const newNode = new Node(node.val);
        nodes.set(node, newNode);

        this.dfs(node, newNode, nodes);
        return newNode;
    }

    dfs(node: Node, newNode: Node, nodes: Map<Node, Node>): void {
        const neighbors = node.neighbors;
        for (const neighbor of neighbors) {
            if (!nodes.has(neighbor)) {
                nodes.set(neighbor, new Node(neighbor.val));
                newNode.neighbors.push(nodes.get(neighbor));
                this.dfs(neighbor, nodes.get(neighbor), nodes);
            } else {
                newNode.neighbors.push(nodes.get(neighbor));
            }
        }
    }
}

// create a map from old node to new node
// traverse through the graph using DFS while marking nodes visited
