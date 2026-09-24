class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = { i: [] for i in range(n) }
        for i, [u, v] in enumerate(edges):
            prob = succProb[i]
            adj[u].append([v, prob])
            adj[v].append([u, prob])
        
        pq = [[-1, start_node]]
        visit = set()
        while pq:
            prob, curr = heapq.heappop(pq)
            visit.add(curr)

            if curr == end_node:
                return -prob
            
            for nei, edgeProb in adj[curr]:
                if nei not in visit:
                    heapq.heappush(pq, [prob * edgeProb, nei])
        
        return 0.0
