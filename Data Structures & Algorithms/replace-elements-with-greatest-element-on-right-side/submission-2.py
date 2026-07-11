class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0] * n
        right_max = -1
        for i in range(n - 1, -1, -1):
            res[i] = right_max
            right_max = max(arr[i], right_max)
        return res