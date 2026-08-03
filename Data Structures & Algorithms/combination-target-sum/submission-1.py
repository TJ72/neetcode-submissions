class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i: int, path: List[int], total: int) -> None:
            if total == target:
                res.append(path[:])
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                
                path.append(nums[j])
                dfs(j, path, total + nums[j])
                path.pop()
        
        dfs(0, [], 0)
        return res