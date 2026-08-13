class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        rows = len(grid)
        cols = len(grid[0])

        seen = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in seen:
                    ans += 1
                    self.dfs(r, c, grid, seen)
        
        return ans


    def dfs(self, r, c, grid, seen) -> None:
        rows, cols = len(grid), len(grid[0])
        stack = [(r, c)]
        seen.add((r, c))

        while stack:
            r, c = stack.pop()

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc

                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == "1" and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    stack.append((nr, nc))
        
# For an iterative DFS in python
# - set up stack and seen with initial node 
# - while stack is valid, add directional nodes IF they are in-bounds and not seen 

# For this problem:
# - every time we run DFS on an unseen node, that counts as a single island 
# - just count the # of islands for the whole grid 