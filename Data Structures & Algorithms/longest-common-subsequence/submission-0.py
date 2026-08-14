class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo: dict[tuple[int, int], int] = {}

        def dfs(i: int, j: int) -> int:
            if i > len(text1) - 1 or j > len(text2) - 1:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                res = 1 + dfs(i + 1, j + 1)
            else:
                res = max(dfs(i + 1, j), dfs(i, j + 1))

            memo[(i, j)] = res
            return res

        return dfs(0, 0)

