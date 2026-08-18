class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, ones = 0, 0

        for num in nums:
            if num == 1:
                ones += 1
            else:
                res = max(res, ones)
                ones = 0
        
        return max(res, ones)
        