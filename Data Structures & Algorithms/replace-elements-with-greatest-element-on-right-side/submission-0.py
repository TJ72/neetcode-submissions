class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        res = [0] * length
        curr_max = arr[length - 1]

        for i in reversed(range(length)):
            if i == length - 1:
                res[i] = -1
            else:
                res[i] = curr_max
            
            curr_max = max(arr[i], curr_max)
            
        return res