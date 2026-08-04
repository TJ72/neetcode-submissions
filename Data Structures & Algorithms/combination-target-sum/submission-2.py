class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i: int, path: List[int], total: int) -> None:
            if i >= len(nums) or total > target:
                return
            if total == target:
                res.append(path[:])
                return
            
            path.append(nums[i])
            dfs(i, path, total + nums[i])
            path.pop()
            dfs(i + 1, path, total)
        
        dfs(0, [], 0)
        return res
            