class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = lambda x: x[0] ** 2 + x[1] ** 2
        def partition(l: int, r: int) -> int:
            pivotIdx = r
            pivotDist = dist(points[pivotIdx])
            i = l
            for j in range(l, r):
                if dist(points[j]) < pivotDist:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            
            points[i], points[pivotIdx] = points[pivotIdx], points[i]
            return i
        
        L, R = 0, len(points) - 1
        pivot = len(points)

        while pivot != k:
            pivot = partition(L, R)
            if pivot < k:
                L = pivot + 1
            else:
                R = pivot - 1
        
        return points[:k]