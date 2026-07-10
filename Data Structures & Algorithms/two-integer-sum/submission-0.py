class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, num in enumerate(nums):
            if num in lookup:
                return [lookup[num], i]

            lookup[target - num] = i