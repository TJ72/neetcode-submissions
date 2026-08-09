class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def dfs(r: int, c: int) -> None:
            if min(r, c) < 0 or r > ROWS - 1 or c > COLS - 1 or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)
        
        return res