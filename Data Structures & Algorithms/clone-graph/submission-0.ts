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

        const seen = new Set<number>();
        const nodes = new Map<Node, Node>();
        const newNode = new Node(node.val);
        nodes.set(node, newNode);

        this.dfs(node, newNode, seen, nodes);
        return newNode;
    }

    dfs(node: Node, newNode: Node, seen: Set<number>, nodes: Map<Node, Node>): void {
        if (seen.has(node.val)) return;

        seen.add(node.val);

        const neighbors = node.neighbors;
        for (const neighbor of neighbors) {
            let nodeToAdd = null;
            if (!nodes.has(neighbor)) {
                nodeToAdd = new Node(neighbor.val);
                nodes.set(neighbor, nodeToAdd);
            } else nodeToAdd = nodes.get(neighbor);

            newNode.neighbors.push(nodeToAdd);
            this.dfs(neighbor, nodeToAdd, seen, nodes);
        }
    }
}

// create a map from old node to new node
// traverse through the graph using DFS while marking nodes visited
