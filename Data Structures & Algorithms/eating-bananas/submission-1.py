class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        res = hi

        while lo <= hi:
            k = (lo + hi) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            
            if hours <= h:
                res = min(res, k)
                hi = k - 1
            else:
                lo = k + 1
            
        return res