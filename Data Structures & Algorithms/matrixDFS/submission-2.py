class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> int:
            if min(r, c) < 0 or r > ROWS - 1 or c > COLS - 1 or grid[r][c] == 1:
                return 0
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            grid[r][c] = 1
            count = 0
            count += dfs(r - 1, c)
            count += dfs(r + 1, c)
            count += dfs(r, c - 1)
            count += dfs(r, c + 1)
            grid[r][c] = 0
            return count
        
        return dfs(0, 0)