class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = { i: [] for i in range(n) }
        for u, v, w in edges:
            adj[u].append([v, w])
            adj[v].append([u, w])
        
        visit = set()
        minHeap = [[0, 0]]
        res = 0
        while minHeap and len(visit) < n:
            weight, v = heapq.heappop(minHeap)
            if v in visit:
                continue
            
            res += weight
            visit.add(v)
            for neighbor, weight in adj[v]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, [weight, neighbor])
        
        return res if len(visit) == n else -1