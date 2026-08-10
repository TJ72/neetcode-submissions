class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] == 1 or grid[N - 1][N - 1] == 1:
            return -1
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1],
                      [-1, -1], [-1, 1], [1, -1], [1, 1]]
        queue = deque()
        queue.append((0, 0))
        grid[0][0] = 1
        res = 1

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == N - 1 and c == N - 1:
                    return res

                for dr, dc in directions:
                    if min(r + dr, c + dc) < 0 or r + dr > N - 1 or c + dc > N - 1 or grid[r + dr][c + dc] == 1:
                        continue
                    
                    queue.append((r + dr, c + dc))
                    grid[r + dr][c + dc] = 1

            res += 1
        
        return -1