class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROW, COL = len(image), len(image[0])
        original = image[sr][sc]
        if original == color:
            return image

        def dfs(r: int, c: int) -> None:
            if min(r, c) < 0 or r >= ROW or c >= COL or image[r][c] != original:
                return

            image[r][c] = color
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        
        dfs(sr, sc)
        return image