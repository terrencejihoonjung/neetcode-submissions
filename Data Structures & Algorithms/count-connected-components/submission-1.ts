class Solution {
    /**
     * @param {number} n
     * @param {number[][]} edges
     * @returns {number}
     */
    countComponents(n: number, edges: number[][]): number {
        if (n === 1) return 1;

        let ret = 0;
        const seen = new Set<number>();
        const graph = new Map<number, number[]>();
        for (const [n1, n2] of edges) {
            if (!graph.has(n1)) graph.set(n1, []);
            if (!graph.has(n2)) graph.set(n2, []);
            graph.get(n1).push(n2);
            graph.get(n2).push(n1);
        }

        for (let i = 0; i < n; i++) {
            if (!seen.has(i)) {
                this.dfs(i, seen, graph);
                ret++;
            }
        }
        
        return ret;
    }

    dfs(n: number, seen: Set<number>, graph: Map<number, number[]>): void {
        seen.add(n);

        const neighbors = graph.get(n) ?? [];
        for (const neighbor of neighbors) {
            if (!seen.has(neighbor)) {
                this.dfs(neighbor, seen, graph);
            }
        }
    }
}

// map each node to their connected nodes in an adjacency list as a map
// for each node, run dfs and track a seen set and increment to count. If seen, skip node.

// dfs: 
// 1) mark as seen
// 2) for each neighbor, only run dfs if it is not seen 