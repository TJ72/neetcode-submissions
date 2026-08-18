class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, ones = 0, 0

        for num in nums:
            if num == 1:
                ones += 1
                res = max(res, ones)
            else:
                ones = 0
        
        return res
        