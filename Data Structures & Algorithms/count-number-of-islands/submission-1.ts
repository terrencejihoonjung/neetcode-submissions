class Solution {
    directions: number[][] = [[0, 1], [0, -1], [1, 0], [-1, 0]];

    /**
     * @param {character[][]} grid
     * @return {number}
     */
    numIslands(grid: string[][]): number {
        const seen = new Set<string>();
        let res = 0;

        for (let r = 0; r < grid.length; r++) {
            for (let c = 0; c < grid[0].length; c++) {
                if (!seen.has(`${r}-${c}`) && grid[r][c] === "1") {
                    res++;
                    this.dfs(grid, r, c, seen);
                }
            }
        }

        return res;
    }

    dfs(grid: string[][], r: number, c: number, seen: Set<string>): void {
        seen.add(`${r}-${c}`);

        for (const direction of this.directions) {
            const newR = r + direction[0];
            const newC = c + direction[1];

            if (newR >= 0 && newR < grid.length && newC >= 0 && newC < grid[0].length && grid[newR][newC] === "1" && !seen.has(`${newR}-${newC}`)) {
                this.dfs(grid, newR, newC, seen);
            }
        }
    }
}

// For each land we encounter, perform DFS until we cover the entire island 
// Track each land we land on so that in the iteration, we avoid performing DFS on it
// Each DFS run is an increment to the total # of islands 

// DFS
// - mark land as seen 
// - for each direction:
//   - if it is land, within bounds, and not seen, recursively call dfs on it 

// time: O(nm), space: O(nm)