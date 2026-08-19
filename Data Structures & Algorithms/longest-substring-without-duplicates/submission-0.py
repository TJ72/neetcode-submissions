class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, res = 0, 0
        contain = set()

        for r in range(len(s)):
            while s[r] in contain:
                contain.remove(s[l])
                l += 1
            
            contain.add(s[r])
            res = max(res, r - l + 1)
        
        return res