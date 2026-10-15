class Solution {
    static directions: number[][] = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    orangesRotting(grid: number[][]): number {
        const queue: number[][] = [];
        let numFreshFruit = 0;
        for (let r = 0; r < grid.length; r++) {
            for (let c = 0; c < grid[0].length; c++) {
                const fruit = grid[r][c];

                // rotten fruit 
                if (fruit === 2) {
                    queue.push([r, c]);
                }

                // fresh fruit 
                else if (fruit === 1) {
                    numFreshFruit++;
                }
            }
        }

        if (numFreshFruit > 0 && queue.length === 0) return -1;
        if (numFreshFruit === 0) return 0;

        // BFS
        let minutes = 0;
        while (queue.length > 0) {
            const level = queue.length;

            for (let i = 0; i < level; i++) {
                const [r, c] = queue.shift();

                for (const direction of Solution.directions) {
                    const newR = r + direction[0];
                    const newC = c + direction[1];
                    
                    if (this.isValid(grid, newR, newC) && grid[newR][newC] === 1) {
                        grid[newR][newC] = 2;
                        numFreshFruit--;
                        queue.push([newR, newC]);
                    }
                }
            }

            if (queue.length > 0) minutes++;
        }

        if (numFreshFruit !== 0) return -1;
        return minutes;
    }

    isValid(grid: number[][], r: number, c: number) {
        return r >= 0 && r < grid.length && c >= 0 && c < grid[0].length;
    }
}

// Find locations of rotten fruits first. 
// - If no rotten fruits or no fresh fruit-> return 0
// - track how many fresh fruits there are 

// Perform BFS on all those rotten fruits. For each level iteration, we count a minute
// - will have use the shift() method to deque an elemnet -> O(n) time 
// - when do we know to stop BFS? -> once there are no more rotten fruits in the queue
// - IMPORTANT -> decrement # of fresh fruits each time we rot a fruit. At the end,
//                we can check # of fresh fruit === 0 to ensure all fruits became rotten. 

// Don't need a set to track seen fruits -> directly modify elements in the grid 