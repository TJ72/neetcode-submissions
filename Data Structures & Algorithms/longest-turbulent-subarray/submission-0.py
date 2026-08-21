class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1
        res, sign = 1, 0

        while r < len(arr):
            if arr[r - 1] > arr[r] and sign != -1:
                res = max(res, r - l + 1)
                r += 1
                sign = -1
            elif arr[r - 1] < arr[r] and sign != 1:
                res = max(res, r- l + 1)
                r += 1
                sign = 1
            else:
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                sign = 0

        return res