class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        memo = [[-1] * COLS for _ in range(ROWS)]

        def dfs(r: int, c: int) -> int:
            if r > ROWS - 1 or c > COLS - 1 or obstacleGrid[r][c] == 1:
                return 0
            if memo[r][c] != -1:
                return memo[r][c]
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            memo[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
            return memo[r][c]
        
        return dfs(0, 0)