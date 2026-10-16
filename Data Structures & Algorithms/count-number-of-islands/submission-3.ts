class Solution {
    static directions: number[][] = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    /**
     * @param {character[][]} grid
     * @return {number}
     */
    numIslands(grid: string[][]): number {
        let ret = 0;
        const seen = new Set<string>(); 
        const rows = grid.length; 
        const cols = grid[0].length; 

        for (let r = 0; r < rows; r++) {
            for (let c = 0; c < cols; c++) {
                if (grid[r][c] === "1" && !seen.has(`${r}-${c}`)) {
                    this.dfs(r, c, grid, seen);
                    ret++;
                }
            }
        }

        return ret;
    }

    dfs(r: number, c: number, grid: string[][], seen: Set<string>): void {
        seen.add(`${r}-${c}`);

        for (const direction of Solution.directions) {
            const newR = r + direction[0];
            const newC = c + direction[1];

            if (this.isValid(newR, newC, grid) && !seen.has(`${newR}-${newC}`)) {
                this.dfs(newR, newC, grid, seen);
            }
        }
    }

    isValid(r: number, c: number, grid: string[][]): boolean {
        return r >= 0 && r < grid.length && c >= 0 && c < grid[0].length && grid[r][c] === "1"; 
    }
}

// iterate through every element 
// - 0: skip 
// - 1: run DFS on 1 IF we haven't seen it yet (mark seen nodes in dfs). After dfs, we increment the num of islands 

// dfs(seen, r,  c, grid): void 
// - mark as seen
// - for each adjacent direction check bounds, not seen, and is land -> recursive dfs call 