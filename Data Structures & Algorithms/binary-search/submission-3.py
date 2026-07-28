class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)

        while lo < hi:
            m = (lo + hi) // 2

            if nums[m] >= target:
                hi = m
            else:
                lo = m + 1

        return lo if lo < len(nums) and nums[lo] == target else -1
