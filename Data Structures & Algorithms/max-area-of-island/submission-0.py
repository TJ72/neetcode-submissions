class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def dfs(r: int, c: int) -> int:
            if min(r, c) < 0 or r > ROWS - 1 or c > COLS - 1 or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c  + 1) + dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        
        return res