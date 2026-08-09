class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue, visit = deque(), set()
        queue.append((0, 0))
        visit.add((0, 0))
        res = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return res
                
                for dr, dc in directions:
                    if min(r + dr, c + dc) < 0 or r + dr > ROWS - 1 or c + dc > COLS - 1 or (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1:
                        continue
                    
                    visit.add((r + dr, c + dc))
                    queue.append((r + dr, c + dc))
                
            res += 1
        
        return -1
            