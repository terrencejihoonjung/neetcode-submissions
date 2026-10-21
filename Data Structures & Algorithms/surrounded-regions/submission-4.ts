class Solution {
    static directions: number[][] = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    /**
     * @param {character[][]} board
     * @return {void} Do not return anything, modify board in-place instead.
     */
    solve(board: string[][]): void {
        const seen = new Set<string>();
        const n = board.length;
        const m = board[0].length; 
        for (let c = 0; c < m; c++) {
            if (!seen.has(`${0}-${c}`) && board[0][c] === "O") {
                this.dfs(0, c, seen, board);
            }
            
            if (!seen.has(`${n - 1}-${c}`) && board[n - 1][c] === "O") {
                this.dfs(n - 1, c, seen, board);
            }
        }

        for (let r = 1; r < n - 1; r++) {
            if (!seen.has(`${r}-${0}`) && board[r][0] === "O") {
                this.dfs(r, 0, seen, board);
            }

            if (!seen.has(`${r}-${m - 1}`) && board[r][m - 1] === "O") {
                this.dfs(r, m - 1, seen, board);
            }
        }

        for (let r = 1; r < n - 1; r++) {
            for (let c = 1; c < m - 1; c++) {
                if (board[r][c] === "O" && !seen.has(`${r}-${c}`)) {
                    board[r][c] = "X";
                }
            }
        }
    }

    dfs(r: number, c: number, seen: Set<string>, board: string[][]): void {
        seen.add(`${r}-${c}`);

        for (const direction of Solution.directions) {
            const newR = r + direction[0];
            const newC = c + direction[1];

            if (this.isValid(newR, newC, board) && board[newR][newC] === "O" && !seen.has(`${newR}-${newC}`)) {
                this.dfs(newR, newC, seen, board);
            }
        }
    }

    isValid(r: number, c: number, board: string[][]): boolean {
        return r >= 0 && c >= 0 && r < board.length && c < board[0].length;
    }
}

// any non-edge land cell needs to be captured 
// if we iterate the grid, and run dfs on regions, we won't know to capture until the very end of dfs worst case -> high complexity 

// why not find land that is untouchable first? Check edges of the grid, run dfs on those land cells and mark them as seen.

// then iterate through inner portion of grid
// if seen, skip, if not, capture

// time: O(mn), space: O(# of nodes in edges)