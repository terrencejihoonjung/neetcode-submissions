class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.': continue

                elif f"r_{board[i][j]}_{i}" in seen or f"c_{board[i][j]}_{j}" in seen or f"box_{board[i][j]}_{i//3}_{j//3}" in seen:
                    return False
                else:
                    seen.add(f"r_{board[i][j]}_{i}")
                    seen.add(f"c_{board[i][j]}_{j}")
                    seen.add(f"box_{board[i][j]}_{i//3}_{j//3}")
        
        return True
    # row -> "r_0-8"
    # col -> "c_0-8"
    # box -> "box_0_1, box_0_2"