class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i, num in enumerate(nums):
            if num != val:
                nums[k] = nums[i]
                k += 1
        
        return k