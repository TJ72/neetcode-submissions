class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if count >> num & 1:
                return num
            
            count |= (1 << num)