class Solution {
    static directions: number[][] = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    maxAreaOfIsland(grid: number[][]): number {
        let maxArea = 0;
        for (let r = 0; r < grid.length; r++) {
            for (let c = 0; c < grid[0].length; c++) {
                if (grid[r][c] === 1) {
                    maxArea = Math.max(maxArea, this.dfs(r, c, grid));
                }
            }
        }

        return maxArea;
    }

    dfs(r: number, c: number, grid: number[][]): number {
        grid[r][c] = 0;

        let sum = 1;
        for (const direction of Solution.directions) {
            const newR = r + direction[0];
            const newC = c + direction[1];
            
            if (this.isValid(newR, newC, grid) && grid[newR][newC] === 1) {
                sum += this.dfs(newR, newC, grid);
            }
        }

        return sum;
    }

    isValid(r: number, c: number, grid: number[][]): boolean {
        return r >= 0 && c >= 0 && r < grid.length && c < grid[0].length;
    }
}

// iterate through grid, run DFS on each 1
// during dfs, modify 1s to 0s to mark them as visited 
// track global max, dfs returns area

// dfs(grid, r, c)
// - 1) modify 1 to 0, instantiate sum = 1
// - 2) for each direction, check if cell is land, in bounds, add dfs output to sum
// - 3) return sum