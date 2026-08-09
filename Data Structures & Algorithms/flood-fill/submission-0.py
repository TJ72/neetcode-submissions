class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROW, COL = len(image), len(image[0])
        original = image[sr][sc]

        def dfs(r: int, c: int, visit: set) -> None:
            if min(r, c) < 0 or r >= ROW or c >= COL or image[r][c] != original:
                return
            if (r, c) in visit:
                return

            visit.add((r, c))
            image[r][c] = color

            dfs(r - 1, c, visit)
            dfs(r + 1, c, visit)
            dfs(r, c - 1, visit)
            dfs(r, c + 1, visit)
        
        dfs(sr, sc, set())
        return image