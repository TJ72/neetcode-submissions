class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold
        currSum = sum(arr[:k])
        res = 1 if currSum >= target else 0

        for r in range(k, len(arr)):
            currSum += arr[r] - arr[r - k]
            if currSum >= target:
                res += 1
        
        return res