class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax, globalMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for num in nums:
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)
            globalMax = max(globalMax, curMax)
            globalMin = min(globalMin, curMin)

            total += num
        
        return max(globalMax, total - globalMin)if globalMax > 0 else globalMax